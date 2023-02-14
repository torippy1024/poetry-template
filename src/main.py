def addition(num1: float, num2: float):
    return num1 + num2


if __name__ == "__main__":
    print("Please enter two numbers.")

    try:
        num1 = float(input("num1: "))
        num2 = float(input("num2: "))
    except ValueError:
        print("Invalid input. Please enter number.")
        exit()

    result = addition(num1, num2)
    print(f"{num1} + {num2} = {result}")
