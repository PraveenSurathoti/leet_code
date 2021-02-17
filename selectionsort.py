#list1 = [56,3,2,78,6,0]
#print(list1)
'''
list []
num = int(input("how many numbers you want to enter:"))
print("enter values:")
for j in range(num):
	list1.append(int(input()))'''

def SelectionSort(list1):
    for i in range(len(list1)):
        min_val = min(list1[i:])
        min_ind = list1.index(min_val)
#print(min_ind)
        list1[i],list1[min_ind] = list1[min_ind],list1[i]
    
list1= []
num = int(input("How many elements you want in the list:"))
list1 = [int(input())for i in range(num)]
SelectionSort(list1)
print(list1)
	
#print(list1)