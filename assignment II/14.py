import csv


with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    list_of_dict = []
    for row in reader:
        list_of_dict.append(dict(row))
    print(list_of_dict)

  
