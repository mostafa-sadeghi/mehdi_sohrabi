# course = "python"
# print(len(course))

# print(course[0])
# print(course[1])
# print(course[5])
# print(course[-1])
# print(course[len(course)-1])

# name = input('enter a name: ')
# course = input('enter your course: ')

# message = "%s Welcome to %s class"%(name,course)
# print(message)

# message = f'{name}, welcome to {course} class'
# print(message)

# message = name + ", " + "Welcome to " + course + " class"
# print(message)

# print('*' * 10)

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0])
# print(numbers[:3])
# print(numbers[::2])
# print(numbers[1::2])

# numbers.append("something else")
# print(numbers)

# numbers.remove("something else")
# print(numbers)

# del numbers[3]
# print(numbers)


# list1 = [1,2,3,4,5]
# list2 = [6,7,8]

# output = list1 + list2

# print(output)

# print(output*3)
# list1.extend([10,20,30])
# list1.append([10,20,30])
# print(list1)


# numbers = (1,2,3,4,5,6)
# print(type(numbers))

# tuple object is immutable
# numbers = (1, 2, 3, 4)
# numbers[0] = 100
# print(numbers)

# import math
# import statistics
# numbers = (1, 2, 3, 4)

# print(statistics.mean(numbers))
# print(statistics.variance(numbers))
# print(max(numbers))
# print(min(numbers))
# print(math.sqrt(9))

# dictionary
# product = {}
# print(type(product))

# product = {
#     'id': 1,
#     'product_name': 'bag',
#     'price': 1000,
#     'release_year': 2023
# }

# product['price'] = 2000
# print(product['price'])
# all_products = [{'name': 'p1', 'price': 1.0}, {
#     'name': 'p2', 'price': 2.0}, {'name': 'p3', 'price': 3.0}]
# for i in range(3):
#     product_name = input('enter product name: ')
#     product_price = float(input('enter product price: '))

#     product = {}
#     product['name'] = product_name
#     product['price'] = product_price

#     all_products.append(product)

# print(all_products)

# for product in all_products:
#     if product['price'] > 2:
#         all_products.remove(product)

# for product in all_products:
#     if product['price'] > 2:
#         all_products.remove(product)

# print(all_products)


# numbers = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# print(numbers[0][2])

numbers = [10, 3, 7, 1, 9]
# numbers.sort()
# print(numbers)