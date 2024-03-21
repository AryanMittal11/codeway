def add_nums(num1, num2):
    return f"{num1} + {num2} = {num1+num2}"


def sub_nums(num1, num2):
    return f"{num1} - {num2} = {num1-num2}"


def mult_nums(num1, num2):
    return f"{num1} * {num2} = {num1*num2}"


def div_nums(num1, num2):
    if num2 == 0:
        return "Invalid output"
    else:
        return f"{num1} / {num2} = {num1/num2}"


def main():
    while True:
        chk = input("You want to do calculation (y/n): ")
        if chk == "y":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter the operation you want to perform: ")

            if op == "+":
                print(add_nums(num1, num2))
            elif op == "-":
                print(sub_nums(num1, num2))
            elif op == "*":
                print(mult_nums(num1, num2))
            elif op == "/":
                print(div_nums(num1, num2))
            else:
                print("Please Enter valid operator")
        elif chk == "n":
            print("Exiting Program")
            break
        else:
            print("Please Enter valid option")


if __name__ == "__main__":
    main()
