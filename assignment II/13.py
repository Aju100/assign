
import csv

csv_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('csvfile.csv', 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(["Name", "Address", "Age"])
    for data in csv_list:
        writer.writerow(data)

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ', escapechar=' ', quoting = csv.QUOTE_NONE)
    for data in reader:
        print(data)
    