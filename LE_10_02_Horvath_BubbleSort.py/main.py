#bubble sort function with an option to reverse order.
def bubble_sort(arr, reverse=False):
    amount = len(arr)  #get length of array
    #outer loop to control number of passes over list
    for i in range(amount):
        #inner loop to compare elements and swap if needed
        for j in range(0, amount-1-i):
            if reverse:  #if reverse is true -> descending order
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  #swap if current element is smaller
            else:  #if reverse is false -> ascending order
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  #swap if current element is greater
    return arr

#function to read file
def read_file(filename):
    #open and read file
    with open(filename, 'r') as file:
        return [int(line) for line in file]  #return list of integers

#asks user for filename
filename = input("Enter the filename to read values from: ")

#error handling + read file
try:
    values = read_file(filename)  #read file
except FileNotFoundError:  #file not found error
    print(f"Error: File '{filename}' not found.")
    exit()
except ValueError:  #value error
    print("Error: File contains non-numeric values.")
    exit()

#prints original list
print("\nOriginal list:")
print(values)

#loops until order is chosen
while True:
    #asks user for sorting order
    order = input("\nChoose sorting order (1 for ascending, 2 for descending): ")
    if order in ['1', '2']:  #check if input is 1 or 2
        break  #exit loop if true
    print("Invalid input. Please enter '1' or '2'.")  #stay in loop asking for new input

#sets reverse to true if descending order was chosen
reverse = (order == '2')

#sorts values using bubble_sort function
sorted_values = bubble_sort(values, reverse)

# Print the sorted list
print("\nSorted list:")
print(sorted_values)
