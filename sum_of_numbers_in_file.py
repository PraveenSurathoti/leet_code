def main():
    numbersFile = open("pravee.txt", "r")
    numbersFile.split(" ")
    
    count = 0

    for line in numbersFile:
        count = count + int(line)
        
    print("The numbers in the file sum up to", count)

    numbersFile.close()
main()