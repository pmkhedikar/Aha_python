# n1 = int(input('Enter first no :'))
# n2 = int(input('Enter second no:'))
# n3 = int(input('Enter third no :'))
#
# # Using List
#
# numbers = [n1, n2, n3]
# print(numbers)
# numbers.sort()
# print(len(numbers))
# print(numbers[len(numbers)-1])





lst = []
n = int(input("Please enter no: "))

for i in range(0 , n):
    numbers = int(input())
    lst.append(numbers)
print(lst)
lst.sort()
print(lst[n-1])