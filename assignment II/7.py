details =[]

first_name, last_name,age = "Mahesh", "Regmi",20
details.append((first_name,last_name,age))

first_name, last_name,age = "Abhisek", "Acharya",19
details.append((first_name,last_name,age))

first_name, last_name,age = "Kiran" ,"Ghimire",21
details.append((first_name,last_name,age))

print(details)

sum = 0
total_entry = int(len(details))

for _ in details:
    if _[2] is not None:
        sum =sum+_[2]
    average = sum/total_entry

print("Average age is: ",average)

for value in details:
    if value[2] is not None:
        if value[2] > average:
            print("Name: {}[{}] is older than average age[{}]".format(value[0],value[2],average))
        elif value[2] < average:
            print("Name: {}[{}] is younger than average age[{}]".format(value[0],value[2],average))
        else:
            print("Name: {}[{}] is equal to average age[{}]".format(value[0],value[2],average))