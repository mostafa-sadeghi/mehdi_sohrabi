# temp = 35
# if temp > 30:
#     print("ok")
# elif temp > 20:
#     print("temp is greater than 20")
# else:
#     print("something else")


# age = 22
# if age >= 18:
#     message = "adult"
# else:
#     message = "not adult"

# print(message)

# ternery operator
# age = 12
# message = "adult" if age >= 18 else "not adult"
# print(message)

# age = 25
# if age >= 20 and age <= 30:
# print("ok")
# if 20 <= age <= 30:
#     print("ok")

# for i in range(6):
#     print("one")

#     print("two")

# print("outside")

# for i in range(6):
#     print(i,end=" ")

# for x in 'python':
#     print(x, end=" ")

# for x in [1, 2, 3, 4, 5]:
#     print(x, end=" ")

# successful = False
# for number in range(3):
#     print("Attempt")
#     user_name = input('enter user name: ')
#     if user_name == "admin":
#         successful = True
#     if successful:
#         print("login success")
#         break


# number = int(float(input('enter a number: ')))
# if number == 1:
#     print(f"you entered {number}")


# print(type('1'))
# print(type(1))
# x = '1'
# y = 1
# if x == y:
#     print(f"{x} = {y}")
# else:
#     print(f"{x} != {y}, because their types is not the same")


# x = input('enter a number: ')
# y = input('enter a number: ')

# if x == y:
#     print(f"{x} = {y}")
# else:
#     print(f"{x} != {y}")

# x = 1
# y = input('enter a number: ')
# if x == y:
#     print(f"{x} = {y}")
# else:
#     print(f"{x} != {y}")

# success = False

# for number in range(3):
#     print("Attempt")
#     if success:
#         print("success")
#         break

# else:
#     print("Attempted 3 times and failed.")

x = [
    [1, 2, 3],
    [4, 2, 6]
]

total = 0
for row in x:
    for col in row:
        # total = total + col # total += col
        if col == 2:
            total += 1

    #     print(col,end=" ")
    # print()

print(total)
