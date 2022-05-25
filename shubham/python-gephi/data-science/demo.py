# def counter(limit=10):
#     for i in range(1, limit+1):
#         yield i


# x = counter(6)

# print(next(x))
# print("====================")
# print("====================")
# print("====================")
# print("====================")
# print("====================")
# print("====================")
# print("====================")
# print("====================")
# print(next(x))

l =[1,2,3,4]
# print(dir(l))

s = "i aM coDer"
s1 = "i am pythö~n!"
s = 'ß'
# s1 = 'ß'
s = s.capitalize()
# print(s)
# s = s.title()
# s1 = s1.casefold()
# s = s.lower()
s1 = s1.center(14)
# print(s1)
# s1 = s1.center(15, '^')
# s1 = s1.encode(encoding='UTF-8',errors='strict')
# print(s1)
message = 'python is popular programming language, python is popular programming language, \
python is popular programming language'
substr = 'py'
# print(message.count(substr, 10, 22))
# c = l.count(3)
# print(c)

string = 'pythön! ß'
# s = string.encode('ascii', 'replace')
# s = string.encode('ascii', 'ignore')
# s = string.encode('ascii', 'strict')
# s = 'ß'.encode('ascii')
# s = s1.encode('ascii', 'xmlcharrefreplace')
# s = string.encode('ascii', 'backslashreplace')
# s = string.encode('ascii', 'namereplace')
# message = 'Python is fun'
# s = message.endswith('fun')
# s = message.endswith('fun', 20)
# l = ['the', 'teacher', 'author']
# s = l[1].endswith('r',5,7)
# string = 'xyz\t12345\tabc'
# print(string)
# s = string.expandtabs(2)

string = 'python developer'
s=string.find('o')
s=string.find('o', 5, 9)
print(s)


# print('the number is: {}'.format(12))
# print(f'the number is {122}')

# s=string.index('e', -10+2, -2)
# string = 'pyt54645hon '

# s=string.isalnum()
# print(s)

l = [1, 4, 5, 2, 6]
for i in range(1, 7):
	if i not in l:
		print(i)
		