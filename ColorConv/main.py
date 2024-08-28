
rgb_input = input("Please enter the RGB color code like this '100,100,100': ")

valid_input = False

# loop until valid input
while not valid_input:
    #splits into 3 parts
    parts = rgb_input.split(",")

    # checks for 3 parts
    if len(parts) == 3:
        try:
            #converts parts to int
            r = int(parts[0])
            g = int(parts[1])
            b = int(parts[2])

            #checks values if 0-255
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                valid_input = True
            else:
                print("Each number must be between 0 and 255.")
                rgb_input = input("Please enter the RGB color code like this(Max 3 Digits) '100,100,100': ")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            rgb_input = input("Please enter the RGB color code like this(Max 3 Digits) '100,100,100': ")
    else:
        print("Invalid input. Please enter exactly three numbers separated by commas.")
        rgb_input = input("Please enter the RGB color code like this(Max 3 Digits) '100,100,100': ")

# rgb to hexadec
hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)

#rgb to cmy
c = 1 - r / 255
m = 1 - g / 255
y = 1 - b / 255

#cmy to %
c = round(c * 100)
m = round(m * 100)
y = round(y * 100)


print("Hexcode:", hex_code)
print("CMY:", (c, m, y))
