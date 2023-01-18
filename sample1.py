number = int(input("Enter the number : "))
lst = []
if number > 9:
    for i in range(number):
        lst.append(i)
    print("The given range of number is : ",lst)
else:
    print("The number is less than 9")