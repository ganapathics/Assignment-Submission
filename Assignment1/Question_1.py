a = input("Enter a low interval  : ")
b = input("Enter a High interval : ")
a = int(a)
b = int(b)
for x in range(a,b,1):
    if x>1:
        for y in range(2,x):
            if (x%y) == 0:
                break
            else:
                print(x)

x = input("Enter lower interval: ")  
y = input("Enter upper interval: ")  
x = int(x)
y = int(y)
for a in range(x,y,1):  
   if a > 1:  
       for i in range(2,a,1):  
           if (a % i) == 0:  
               break  
       else:  
           print(a)  
    