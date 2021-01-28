def twoSum(num,target):
	for i in range(len(num)):
		for j in range(len(num)):
			if num[i]+num[j]==target:
				return i,j
     
                
                
                
num=[1,6,5,4,3]
target=10
print(twoSum(num,target))