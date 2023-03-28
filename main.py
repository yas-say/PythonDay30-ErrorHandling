# try:
#     f = open("abc.txt")
# except FileNotFoundError as error_message:
#     print(f"{error_message}: No such file")
#     f = open("abc.txt", "w")
# else:
#     print(f.readlines())
# finally:
#     content = f.close()
#     print(f"{content} file closed")

#User raised error


# height = float(input("Enter your height in meter: "))
# weight = int(input("Enter your weight in pounds: "))
#
# if height > 3:
#     raise ValueError("Human cant have height greater than 3")
#
# bmi = weight / height ** 2
# print(bmi)




fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(1)