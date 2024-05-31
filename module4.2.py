#input validation
while True:
    try:
        string=str(input("Enter a string "))
    except:
        print("Enter a string value")
        continue
    break #loop breaks
Str="" #empty string
for i in string.split(): #splits the string
    if i.isnumeric(): #checks if the string is a numeric value
        Str +=i+' ' 
    elif i[0] in ['a','e','i','o','u','y','A','E','I','O','U','Y']: #checks if value is in list
        Str+= i+ 'yay' + ' '
    elif i[0] and i[1] not in ['a','e','i','o','u','y','A','E','I','O','U','Y']: #checks if value is not present in list
        Str+= i[2:]+i[0:2]+'ay'+' '
    else:
        Str+= i[1:]+i[0]+'ay'+' ' 
print(Str) 
        
        
