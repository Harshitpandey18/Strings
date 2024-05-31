from tabulate import tabulate #tabulate module is imported
def printTable():
    #input validation
    while True:
        try:
            n=int(input("Enter the number of lists: "))
        except:
            print("Enter an integer")
            continue 
        try:
            l=int(input("Enter the length of each list: "))
        except:
            print("Enter an integer")
            continue
        break #breaks the loop
    List=[] #empty list 
    for i in range(n): 
        Lists=[] #empty list 
        print("Enter the values of List",i+1)
        for j in range(l): #loop will run
            #input validation
            while True:
                try:
                    val=str(input())
                except ValueError:
                    print("Enter a string")
                    continue
                break
            Lists.append(val) 
        List.append(Lists) #list is appended
    print(tabulate(List,stralign="right")) #table is created
printTable()
