myList = [1,2,4,5,6,8,9]
list_range  = myList[1:3]
myList[1:3] = [12, 13]
all_after = myList[2:]
all_before = myList[:-1]
ordered_list = [1,2,3,4,5,6,7,8,9]
#list methods add data in an index  on the list
myList.insert(2,6)
#add to the  end of the list
myList.append(89)
#remove an item from the list
#myList.remove(4) 
ordered_list.reverse()
print(ordered_list)