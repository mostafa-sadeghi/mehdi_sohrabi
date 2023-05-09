# s = "abc"
# print(len(s))
# print(s[0])
# print(s[1])
# print(s[2])

# s = "abcdefgh"
# print(s[::-1])
# print(s[3:6])
# print(s[0])
# print(s[-1])

# s= "hello"
# s[0] = "y" # error

# s = "abcdefgh"
# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")


# course = input('enter course name: ')
# for i in range(len(course)):
#     print(course[i], end=" ")


# Functions

# def is_even(number):
#     return number % 2 == 0

# print(is_even(4))

# scope

# def f(x):
#     x = x + 1
#     print('in f(x) : x =',x)
#     return x

# x = 3
# z = f(x)
# print('x outside',x)


x = 0


def f(x):
    x = x + 1
    print(x)


f(x)
print(x)
