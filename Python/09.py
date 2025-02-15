
x = int(input("Enter the number you want to Search for -> "))
tuple = (1,4,9,16,25,36,49,64,81,100)
i=1
while i<len(tuple):
    if(tuple[i]==x):
        print("Index of x is ", i)
        break
    if(i==len(tuple)-1 and tuple[i]!=x):
        print("Number Not Found")
    i = i+1
