print("This is only a postive number converter \n")

def ConvertToBinary(num):

    if num > 1:
        ConvertToBinary(num // 2)
        print(num % 2, end="")
    elif num == 0:
        print(0, end="")
    else:
        print(1, end="")

number = int(input("Enter any number: "))

ConvertToBinary(number)