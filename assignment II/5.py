# itemgetter is faster than lambda function
from operator import itemgetter

# tuple
first_name, last_name, age = (
    "Aju",
    "Tamang",
    19
)

# list
people = []

# append your tuple
people.append((first_name,last_name,age))

firstname, lastname, age = ("Mahesh", "Regmi", 20)
people.append((firstname, lastname, age))

firstname, lastname, age = ("Dhiren", "Rai", 19)
people.append((firstname, lastname, age))
print("ORIGINAL LIST: ", people)


# sort the list with firstname
# sorted_list = sorted(people, key=lambda x: x[0])
sorted_list = sorted(people, key=itemgetter(0))
print("FIRSTNAME: ", sorted_list)


# sort the list with lastname
sorted_list = sorted(people, key=itemgetter(1))
print("LASTNAME: ", sorted_list)

# sort the list with age
sorted_list = sorted(people, key=itemgetter(2))
print("AGE: ", sorted_list)