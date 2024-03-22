import random
import string


def complex_pass(length):
    char1 = string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    password = ''.join(random.choice(char1) for _ in range(length))
    return password


def mod_pass(length):
    char1 = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char1) for _ in range(length))
    return password


def simple_pass(length):
    char1 = string.ascii_letters + string.digits
    password = ''.join(random.choice(char1) for _ in range(length))
    return password


def main():
    while True:
        length = int(input("Enter the length of password you want: "))
        if length <= 0:
            print("Please enter valid length")
        else:
            break
    complexity = input("Enter the complexity of password (complex/moderate/simple): ")
    if complexity == "complex":
        print("Your password is : ", complex_pass(length))
    elif complexity == "moderate":
        print("Your password is : ", mod_pass(length))
    elif complexity == "simple":
        print("Your password is : ", simple_pass(length))
    else:
        print("Invalid Option")


if __name__ == "__main__":
    main()
