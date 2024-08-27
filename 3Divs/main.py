while True:
    try:
        op = input("Please choose a division operator(/, // or %) or (q) to close program: ").lower()

        if op == 'q':
            print("Program closed.")
            break

        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        result = None

        if num2 == 0:
            print("Cant divide by 0. Enter valid number.")
            continue

        if op == '/':
            result = num1 / num2
            print("Result: ", result)
        elif op == '//':
            result = num1 / num2
            print("Result: ", result)
        elif op == '%':
            result = num1 % num2
            print("Result: ", result)

    except ValueError:
        print("Invalid Input.")