import random
import time
import requests
from bs4 import BeautifulSoup
import csv
import os
from art import *
from fake_useragent import UserAgent

HEADERS = {
    'user-agent': UserAgent().random,
    'accept': '*/*'
}

LANGUAGES = {
    'EN': {
        'start_program': 'Welcome to my program!'
                         ' She can take the site menu and write it to a csv file.\nThere are two ways to write a menu:'
                         ' the entire menu at once into one file, or each category into a separate file.',
        'change_language': 'Do you want to change language?[+/-]: ',
        'language_was_change': 'The language has been changed to',
        'parser_choice': 'Choose how you want to take the menu from the sushihouse website: 1 if the entire menu is'
                         ' written to one file, 2 if each category is written to a separate file: ',
        'unknown_parser': 'Unknown choice! Try again :)',
        'start_process': 'Start of process:',
        'process_finished': 'The process is over! The file has been generated :)',
        'info_about_process': 'Information about the work of the program:'
    },
    'RU': {
        'start_program': 'Добро пожаловать в мою программу!'
                         ' Она умеет брать меню сайта и записывать его в csv файл.\nЕсть два способа'
                         ' записи меню: сразу всё меню в один файл или каждая категория в отдельный файл. ',
        'change_language': 'Вы хотите сменить язык?[+/-]: ',
        'language_was_change': 'Язык был изменен на',
        'parser_choice': 'Выберите как вы хотите взять меню с сайта сушидома: 1 если всё меню записать в один файл, '
                         '2 если каждая категория записывается в отдельный файл: ',
        'unknown_parser': 'Неизвестный выбор! Попробуйте еще раз :)',
        'start_process': 'Начало процесса:',
        'process_finished': 'Процесс закончен! Файл сформирован :)',
        'info_about_process': 'Информация о работе программы:'

    }
}


def create_dir(type_parser):
    if not os.path.exists('data'):
        os.mkdir('data')

    if not os.path.exists(f'data/{type_parser}'):
        os.mkdir(f'data/{type_parser}')


def update_csv_file_new_dishes(url, amount_pages, type_parser, title):
    for page in range(1, amount_pages + 1):
        url = f'{url}page/{page}'
        site = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(site.text, 'lxml')
        products = soup.find_all('div', class_='shop-cards')
        for product in products:
            try:
                name = product.find('h5').text
            except Exception:
                name = 'Нет названия'

            try:
                url = product.find('h5').find('a').get('href')
            except Exception:
                url = 'Нет url'

            try:
                compounds = ''
                all_compound = product.find('div', class_='shop-cards__desc-p__desc').find_all('p')
                for compround in all_compound:
                    compounds = compounds.replace('\u25ba', '')
                    compounds += compround.text + '\n'
                if compounds:
                    compounds = compounds.strip()
                else:
                    compounds = 'Нет состава'
            except Exception:
                compounds = 'Нет состава'

            try:
                price = product.find('span', class_='woocommerce-Price-amount amount').text
            except Exception:
                price = 'Всё зависит от количества'

            with open(f'data/{type_parser}/{title}.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        name.strip(),
                        compounds.strip(),
                        price.strip(),
                        url.strip(),
                    )
                )
        time.sleep(random.randint(2, 4))
        print(f'\033[32m[+] page {page}/{amount_pages} DONE!')


def info(func):
    def inner(*args, **kwargs):
        print(f'\033[35m{LANGUAGES[lang]["start_process"]}')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'\033[35m{LANGUAGES[lang]["process_finished"]}')
        print(f'\033[35m{LANGUAGES[lang]["info_about_process"]}')
        print(f'\033[35mTIME WORK PROGRAM: {(end_time - start_time):.2f} SECONDS')
        print('\033[35m-' * 50)

    return inner


@info
def menu_by_category(url, type_parser):
    create_dir(type_parser)

    site = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(site.text, 'lxml')
    for category in soup.find_all('div', class_='col-xl-2 col-md-3 col-6'):
        url = category.find('a', class_='home-menu-items').get('href')
        title = url.split('/')[-2]
        print(f'\033[35m{title}:')

        with open(f'data/{type_parser}/{title}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    'Название',
                    'Состав',
                    'Цена',
                    'Ссылка на товар'
                )
            )

        site_category = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(site_category.text, 'lxml')
        try:
            amount_pages = int(soup.find_all('a', class_='page-numbers')[-2].text)
        except IndexError:
            amount_pages = 1

        update_csv_file_new_dishes(url, amount_pages, type_parser, title)


@info
def all_menu(url, type_parser):
    create_dir(type_parser)

    site = requests.get(url=url, headers=HEADERS)
    soup = BeautifulSoup(site.text, 'lxml')
    amount_pages = int(soup.find_all('a', class_='page-numbers')[-2].text)

    with open(f'data/{type_parser}/{type_parser}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Название',
                'Состав',
                'Цена',
                'Ссылка на товар'
            )
        )

    update_csv_file_new_dishes(url, amount_pages, type_parser, type_parser)


def interface():
    global lang
    lang = 'EN'
    print(f'\033[35m{text2art("MENU   SITE")}')
    print(f'\033[35m{LANGUAGES[lang]["start_program"]}')
    change_language = input(f'\033[35m{LANGUAGES[lang]["change_language"]}').strip()
    if change_language == '+':
        lang = 'RU' if lang == 'EN' else 'EN'
        print(f'\033[35m{LANGUAGES[lang]["language_was_change"]} {lang}.')
    while True:
        choose_parser = input(f'\033[35m{LANGUAGES[lang]["parser_choice"]}').strip()
        if choose_parser == '1':
            url = 'https://sushidom.by/shop/'
            type_parser = 'all_menu'
            all_menu(url, type_parser)
            break
        elif choose_parser == '2':
            url = 'https://sushidom.by/'
            type_parser = 'menu_by_category'
            menu_by_category(url, type_parser)
            break
        else:
            print(f'\033[35m{LANGUAGES[lang]["unknown_parser"]}')


if __name__ == '__main__':
    interface()
