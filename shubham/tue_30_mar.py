# from datetime import datetime, timedelta, time, date

# today = date.today()
# print(today)
# nyd = date(today.year, 1, 1)

# if nyd < today:
#     print((today - nyd).days)


# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# thislist.sort()
# thislist.reverse()

# print(thislist)

# for item in thislist:
# 	print(item)

# number = input("Enter the number: ")
# x = int(number)%2
# if x == 0:
#     print(number, "is even number")
# else:
#     print(number, "is odd number")

# count = int(input("Enter the count of numbers: "))
# i = 0
# sum = 0
# for i in range(count):
#     x = int(input("Enter an integer: "))
#     sum = sum + x
# avg = sum/count
# print(" The average is: ", avg)

number = int(input("Enter the number: "))
if (number % 7 == 0 and number % 5 == 0):
    print(number, "is multiple of both 5 and 7")
