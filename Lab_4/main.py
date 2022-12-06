import csv
import random
FILENAME : str = "dataSet.csv"
OUTPUTFILE : str = "newDataSet.csv"

#Переопределение map
def OverrideMap(func, initial_list : list)->list:
    result_list = list()
    for item in initial_list:
        result_list.append(func(item))
    return result_list

#Переопределение reduce
def OverrideReduce(func, initial_list : list):
    index = 2
    length = len(initial_list)
    result = func(initial_list[0], initial_list[1])
    while(index < length):
        result = func(result, initial_list[index])
        index += 1
    return result

#Генерация списка списков для .csv файла
def CreateDataSet()->list:
    item_type : list = ["Клинок", "Посох", "Свиток", "Щит", "Кристалл"]
    item_quality : list = ["Легендарный", "Обыкновенный", "Редкий", "Ультра-редкий", "Реликтовый"]
    item_property : list = ["Неразрушимый", "Огненный", "Ледяной", "Зачарованный", "Проклятый", "Идеальный"]
    items = list()
    i = 0
    amount = 30
    items.append(["Предмет", "Стоимость предмета"])
    while i < amount:
        random_item = item_quality[random.randint(0, len(item_quality)) - 1] + ' ' + item_property[random.randint(0, len(item_property) - 1)] + ' ' + item_type[random.randint(0, len(item_type) - 1)]
        items.append([random_item, random.randint(1, 9001) * 100])
        i += 1
    return items

#Запись данных в .csv файл
def WriteCSV(dataSet : list, file_name):
    with open(file_name, "w", newline = "") as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerows(dataSet)

def WriteInCSVFromListDict(dataSet : list, fileName : str):
    with open(fileName, "w", newline = "") as file:
        columns = list(dataSet[0].keys());
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader();   
        writer.writerows(dataSet);

#Чтение из .csv файла
def ReadCSV(file_name)->list:
    with open(file_name, "r", newline = "") as file:
        reader = csv.DictReader(file)
        result_list = list()
        for dict in reader:
            result_list.append(dict)
    return result_list

#Разбиение записи с ключом названия предмета на 3 части
def SplitItemName(initial_list : dict)->dict:
    result_list = dict()
    lines = initial_list["Предмет"].split(' ')
    result_list["Качество предмета"] = lines[0]
    result_list["Свойство предмета"] = lines[1]
    result_list["Тип предмета"] = lines[2]
    result_list["Стоимость предмета"] = initial_list["Стоимость предмета"]
    return result_list

#Подсчет общей стоимости всех предметов
def SumCostAllItems(initial_list_one: dict, initial_list_two : dict)->list:
    result_list = dict()
    result_list["Стоимость предмета"] = int(initial_list_one["Стоимость предмета"]) + int(initial_list_two["Стоимость предмета"])
    return result_list

WriteCSV(CreateDataSet(), FILENAME)
dataSet : list = ReadCSV(FILENAME)
new_DataSet : list = OverrideMap(SplitItemName, dataSet)
WriteCSV(new_DataSet, OUTPUTFILE)
all_item_cost = OverrideReduce(SumCostAllItems, dataSet)["Стоимость предмета"]
print("Стоимость всех предметов в файле: " + str(all_item_cost))
