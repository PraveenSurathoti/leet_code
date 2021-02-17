def InsertionSort(my_list):
	for index in range(1,len(my_list)):
		current_element = my_list[index]
		pos = index
		while current_element<my_list[pos-1] and pos>0:
			my_list[pos] = my_list[pos-1]
			pos = pos-1
		my_list[pos] = current_element

'''t1 = []
num = int(input("how many numbers you want to enter:"))
print("enter values:")
for j in range(num):
	list1.append(int(input()))
print(list1)'''


'''list1 = [2,4,3,5,1]
InsertionSort(list1)
print(list1)'''

list1= []
num = int(input("How many elements you want in the list:"))
list1 = [int(input())for i in range(num)]
InsertionSort(list1)
print(list1)