from pymongo import MongoClient
import pprint
import config

cluster = MongoClient(config.MongoURI)#config.py содержит только монго токен
db = cluster["test"] #DB name
collection = db["test"] #Cluster name
InputFlag = True

choose = int(input("Введите 0 если хотите ввести содержимое файла NameList .txt\nВведите 1 если хотете добавить по одному\nВведите 2 для удаления\nВведите 3 для просмотра содержимого коллекции\n\n"))
if choose == 0:
    i = int(input("С какой UserID начинать вставку\n"))
    t = open('NameList .txt', 'r', encoding="UTF-8")
    for line in t:
        line = line[0:-1]
        collection.insert_one({'UserID': i, 'Username': line, 'Flag': 'false'})
        i += 1


elif choose == 1:
    while InputFlag:
        i = int(input('В какую позицию?\n'))
        EnteredName = input("Введите имя\n")
        collection.delete_one({'UserID': i})
        collection.insert_one({'UserID': i, 'Username': EnteredName, 'Flag': 'false'})
        i += 1
        InputFlag = bool(input("Eще?\nДа - 1\nНет - 0\n"))


elif choose == 2:
    collection.delete_many({})


elif choose == 3:
    count = 0
    while count < collection.estimated_document_count():
        pprint.pprint(db.test.find_one({}))
        count = count + 1

print("Сделано\n")

