import time

import requests
from bs4 import BeautifulSoup
import csv
import os
import datetime


def all_menu(url, headers):
    site = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(site.text, 'lxml')
    amount_pages = int(soup.find_all('a', class_='page-numbers')[-2].text)

    if not os.path.exists('data'):
        os.mkdir('data')

    if not os.path.exists('data/all_menu'):
        os.mkdir('data/all_menu')

    with open('data/all_menu/all_menu.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Название',
                'Состав',
                'Цена',
                'Ссылка на товар'
            )
        )

    for page in range(1, amount_pages + 1):
        url = f'https://sushidom.by/shop/page/{page}'
        site = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(site.text, 'lxml')
        products = soup.find_all('div', class_='shop-cards')
        for product in products:
            try:
                title = product.find('h5').text
            except Exception:
                title = 'Нет названия'

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

            with open('data/all_menu/all_menu.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        title.strip(),
                        compounds.strip(),
                        price.strip(),
                        url.strip(),
                    )
                )

        print(f'\033[32m[+] page {page}/{amount_pages} DONE!')


def main():
    start_time = time.time()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'accept': '*/*'
    }
    url = 'https://sushidom.by/shop/'
    all_menu(url, headers)
    end_time = time.time()
    print(f'[INFO] TIME WORK PROGRAMM: {(end_time - start_time):.2f} SECONDS')


if __name__ == '__main__':
    main()
