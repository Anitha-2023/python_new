lst = range(1,11)
even_list = []
odd_list = []
print(list(lst))
for i in lst:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even List is : ",even_list)
print("Odd List is : ",odd_list)