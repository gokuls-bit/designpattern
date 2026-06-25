num = int(input("enter the number"))
a,b = 0,1
print("fibonacci series ,")
for i in range(num):
    print(a,end = "")
    a,b = b,a+b