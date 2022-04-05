from bs4 import BeautifulSoup
import sqlite3
import requests


with sqlite3.connect("C:\\Users\edgar777\Documents\GitHub\sit-catalog\SI-Catalog\sicatalog\db.sqlite3") as db:
    counter = 0
    cur = db.cursor()
    asiq = requests.get('https://www.citilink.ru/catalog/pylesosy/')
    parser = BeautifulSoup(asiq.text,'html.parser')
    Cost_List = parser.findAll('span',class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
    Name_List = parser.findAll('a',class_='ProductCardHorizontal__title Link js--Link Link_type_default')
    for x in range(len(Name_List)):
        qw = cur.execute('SELECT title FROM parsers_sitdatabase')
        if not Name_List[x].text in qw:
            cur.execute('INSERT INTO parsers_sitdatabase VALUES (?,?,?,?)',
            (Name_List[x].text, Cost_List[x].text, 'пылеотсос', 'https://www.citilink.ru/catalog/pylesosy/'))

    db.commit()

    with sqlite3.connect("C:\\Users\edgar777\Documents\GitHub\sit-catalog\SI-Catalog\sicatalog\db.sqlite3") as db:
        counter = 0
        cur = db.cursor()
        asiq = requests.get('https://www.citilink.ru/catalog/pylesosy/')
        parser = BeautifulSoup(asiq.text, 'html.parser')
        Cost_List = parser.findAll('span',
                                   class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
        Name_List = parser.findAll('a', class_='ProductCardHorizontal__title Link js--Link Link_type_default')
        for x in range(len(Name_List)):
            qw = cur.execute('SELECT title FROM parsers_sitdatabase')
            if not Name_List[x].text in qw:
                cur.execute('INSERT INTO parsers_sitdatabase VALUES (?,?,?,?)',
                            (Name_List[x].text, Cost_List[x].text, 'пылеотсос',
                             'https://www.citilink.ru/catalog/pylesosy/'))

        db.commit()

        with sqlite3.connect("C:\\Users\edgar777\Documents\GitHub\sit-catalog\SI-Catalog\sicatalog\db.sqlite3") as db:
            counter = 0
            cur = db.cursor()
            asiq = requests.get('https://www.citilink.ru/catalog/pylesosy/')
            parser = BeautifulSoup(asiq.text, 'html.parser')
            Cost_List = parser.findAll('span',
                                       class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
            Name_List = parser.findAll('a', class_='ProductCardHorizontal__title Link js--Link Link_type_default')
            for x in range(len(Name_List)):
                qw = cur.execute('SELECT title FROM parsers_sitdatabase')
                if not Name_List[x].text in qw:
                    cur.execute('INSERT INTO parsers_sitdatabase VALUES (?,?,?,?)',
                                (Name_List[x].text, Cost_List[x].text, 'пылеотсос',
                                 'https://www.citilink.ru/catalog/pylesosy/'))

            db.commit()

            with sqlite3.connect(
                    "C:\\Users\edgar777\Documents\GitHub\sit-catalog\SI-Catalog\sicatalog\db.sqlite3") as db:
                counter = 0
                cur = db.cursor()
                asiq = requests.get('https://www.citilink.ru/catalog/pylesosy/')
                parser = BeautifulSoup(asiq.text, 'html.parser')
                Cost_List = parser.findAll('span',
                                           class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
                Name_List = parser.findAll('a', class_='ProductCardHorizontal__title Link js--Link Link_type_default')
                for x in range(len(Name_List)):
                    qw = cur.execute('SELECT title FROM parsers_sitdatabase')
                    if not Name_List[x].text in qw:
                        cur.execute('INSERT INTO parsers_sitdatabase VALUES (?,?,?,?)',
                                    (Name_List[x].text, Cost_List[x].text, 'пылеотсос',
                                     'https://www.citilink.ru/catalog/pylesosy/'))

                db.commit()

                with sqlite3.connect(
                        "C:\\Users\edgar777\Documents\GitHub\sit-catalog\SI-Catalog\sicatalog\db.sqlite3") as db:
                    counter = 0
                    cur = db.cursor()
                    asiq = requests.get('https://www.citilink.ru/catalog/pylesosy/')
                    parser = BeautifulSoup(asiq.text, 'html.parser')
                    Cost_List = parser.findAll('span',
                                               class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
                    Name_List = parser.findAll('a',
                                               class_='ProductCardHorizontal__title Link js--Link Link_type_default')
                    for x in range(len(Name_List)):
                        qw = cur.execute('SELECT title FROM parsers_sitdatabase')
                        if not Name_List[x].text in qw:
                            cur.execute('INSERT INTO parsers_sitdatabase VALUES (?,?,?,?)',
                                        (Name_List[x].text, Cost_List[x].text, 'пылеотсос',
                                         'https://www.citilink.ru/catalog/pylesosy/'))

                    db.commit()