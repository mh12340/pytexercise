
while True:
    num = input("Enter number to convert(or 'q' to stop program): ")

    if num == 'q':
        print("Program closed.")
        break

    base = int(input("Enter base of number you entered(2 = binary, 8 = octal, 10 = decimal, 16 = hexadecimal): "))

    #converts input number to decimal using num and the base entered
    dec = int(num, base)

    #converts the dec number to bin, oct and hexa, stripping them of the first 2 characters
    binary = bin(dec)[2:]
    octal = oct(dec)[2:]
    hexa = hex(dec)[2:]

    #prints all the converted numbers
    print("Entered number = ",num , " (Base = ",base , "): ")
    print("Decimal: ", dec)
    print("Binary: ", binary)
    print("Octal: ", octal)
    print("Hexadecimal: ", hexa)