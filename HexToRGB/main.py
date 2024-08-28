while True:
    user_input = input("Please enter Hex to convert to RGB(or 'q' to stop program): ")

    if user_input == 'q':
        print("Program closed.")
        break

    #gets rid of the #
    user_input = user_input[1:]

    #assigns first 2 characters to r and converts it to decimal
    r = int(user_input[0:2], 16)
    g = int(user_input[2:4], 16)
    b = int(user_input[4:6], 16)

    print("RGB = ",r , " ",g , " ",b )