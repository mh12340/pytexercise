while True:
    num = input("Enter 1st segment to convert(or 'q' to stop program): ")

    if num == 'q':
        print("Program closed.")
        break

    num2 = input("Enter 2nd segment to convert: ")
    num3 = input("Enter 3rd segment to convert: ")
    num4 = input("Enter 4th segment to convert:")

    base = int(input("Enter base of number you entered(2 = binary, 8 = octal, 10 = decimal, 16 = hexadecimal): "))

    # converts input numbers to decimal using num and the base entered
    dec = int(num, base)
    dec2 = int(num2, base)
    dec3 = int(num3, base)
    dec4 = int(num4, base)


    # converts the dec numbers to bin, oct and hexa, stripping them of the first 2 characters
    binary = bin(dec)[2:]
    binary2 = bin(dec2)[2:]
    binary3 = bin(dec3)[2:]
    binary4 = bin(dec4)[2:]
    octal = oct(dec)[2:]
    octal2 = oct(dec2)[2:]
    octal3 = oct(dec3)[2:]
    octal4 = oct(dec4)[2:]
    hexa = hex(dec)[2:]
    hexa2 = hex(dec2)[2:]
    hexa3 = hex(dec3)[2:]
    hexa4 = hex(dec4)[2:]

    # prints all the converted ip's
    print("Entered Ip4 = " + num + "." + num2 + "." + num3 + "." + num4)
    print(f"Decimal: {dec}.{dec2}.{dec3}.{dec4}")
    print("Binary: " + binary + "." + binary2 + "." + binary3 + "." + binary4)
    print("Octal: " + octal + "." + octal2 +"." + octal3 + "." + octal4)
    print("Hexadecimal: " + hexa + "." + hexa2 + "." + hexa3 + "." + hexa4)
