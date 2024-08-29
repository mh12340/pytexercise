#ask for userinput
start_num = int(input("Enter start value: "))
end_num = int(input("Enter end value: "))
steps = int(input("Enter the number of steps: "))

#calculate step size
step_size = (end_num - start_num) / steps

#generate sequence
sequence = []
for i in range(steps + 1):      #steps + 1 makes sure the end_num gets printed aswell
    sequence.append(int(start_num + i * step_size))

print("Generated Sequence: ", sequence)

