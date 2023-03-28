try:
    f = open("abc.txt")
except FileNotFoundError as error_message:
    print(f"{error_message}: No such file")
    f = open("abc.txt", "w")
else:
    print(f.readlines())
finally:
    f.close()
    print("file closed")
