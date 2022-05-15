# Scraping site sushidom

<a id='anchor'></a>
Language:

* [RU](#ru_doc)
* [EN](#en_doc)

<a id='ru_doc'></a>

### Документация

***

Перед вами представлен парсер сайта sushidom.
В качестве интерфейса используется консоль.
При запуске программы перед вами появляется вводная информация. В начале стоит выбор: изменить язык на
русский или оставить английский,
так как по умолчанию он является основным языком.

![interface](images/readme/scrap_interface.png)

Следующий выбор касается способа парсинга. Есть два способа: спарсить всё меню в
один файл или каждую категорию в отдельный файл.

![lang_ru](images/readme/scrap_ru.png)

В процессе парсинга показываются выполненные стадии парсинга страницы.

![process_parsing](images/readme/scrap_process.png)

Сформированные файлы сохраняются
в папку data, а внутри папки data в папку соответствующую выбраному парсеру.

![data](images/readme/scrap_data.png)
![data_choose](images/readme/scrap_data_choose.png)
![data_pr_all](images/readme/scrap_data_pr_all.png)
![data_pr_category](images/readme/scrap_data_pr_by_category.png)

В конце парсинга программа выводит информацию, что всё успешно спарсилось
и также показывает время за которое спарсился сайт.

![end_program](images/readme/scrap_finish_ru.png)

Используемые библиотеки:

* requests;
* BeautifulSoup;
* csv;
* os;
* art;
* fake_useragent;
* time.

__Спасибо за внимание!__

### Documentation

***

Here is a site parser. The console is used as an interface.
When you start the program, introductory information appears
in front of you. At the beginning, you are faced with a choice:
change the language to Russian or leave English, since it is the
main language by default.

![interface](images/readme/scrap_interface.png)

The next choice concerns the parsing method .
There are two ways: parse the entire menu into one file or each category
into a separate file.

<a id='en_doc'></a>

![lang_ru](images/readme/scrap_ru.png)

During the parsing process, the completed stages of parsing the page are
shown.

![process_parsing](images/readme/scrap_process.png)

The generated files are saved in a folder, and inside the folder
in a folder corresponding to the selected parser.

![data](images/readme/scrap_data.png)
![data_choose](images/readme/scrap_data_choose.png)
![data_pr_all](images/readme/scrap_data_pr_all.png)
![data_pr_category](images/readme/scrap_data_pr_by_category.png)

At the end of parsing,
the program displays information that everything was successfully parsed
and also shows the time for which the site was parsed.

![end_program](images/readme/scrap_finish_ru.png)

Libraries used:

* requests;
* BeautifulSoup;
* csv;
* os;
* art;
* fake_useragent;
* time.

__Thank you for your attention!__

[Up | Вверх](#anchor)