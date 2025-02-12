#To check whether a list contain a Palindrome of elements
list1 = [1,2,3,2,1]
list2 = [1,"abc","abc",1]
list22 = list2[::-1]
list11 = list1[::-1]
print("Palindrome = ",list1==list11)
print("Palindrome = ",list2==list22)
