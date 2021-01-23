str1 = input("enter the string : ")
ch = input("enter Character to find : ")
for i in range(len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)