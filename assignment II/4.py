friends =[]
print(id(friends))

friends.append("Mahesh")
friends.append("Abishek")
friends.append("Kiran")
friends.append("Ayush")

print(id(friends))

# No id hasn't change id of list but the id of each list elements has changed.

print("Before sorting: ",friends)

friends.sort() # O(nlogn)

print("After sorting: ",friends)
print("First item on list: ",friends[0])
print("Second item on list: ",friends[1])