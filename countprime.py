limit=int(input("enter the range:"))


def prime_count(n):
    lst=[]
    for num in range(n+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
                lst.append(num)
    return len(lst)
print("The primes nums are",prime_count(limit))
    