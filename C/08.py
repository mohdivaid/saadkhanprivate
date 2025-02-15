print("Program to add data to list")
list =[]
n = int(input("Enter the number up to which you want the squares -> "))
i = 1
while i <= n: 
    list.append(i*i)
    i += 1 
print("The list of items is \n", list)
