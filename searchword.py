fh  = open("pravee.txt", "r")
word=input("enter word to search:")
s=" "
count=1
L=fh.readlines()

for i in L:
    L2=i.split()
    if word in L2:
        print("Line number",count,":",i)
    count+=1