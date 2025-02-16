print("write a program to find factorial of number")
num = int(input("Enter any number you want to find the factorial of no: "))
res = 1

while(num>0):
   res = res*num
   num = num-1
print(res)