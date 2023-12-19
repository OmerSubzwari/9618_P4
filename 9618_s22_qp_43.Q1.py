def PrintArray(DataArray): # Define procedure PrintArray with parameter of defined array
    outputvalue = ""
    for i in range(0, len(DataArray)): # Loop that will repeat until EOF
        outputvalue = outputvalue + str((DataArray[i])) + " " # Set output value as the next value in array with a space after
    print(outputvalue)

def LinearSearch(DataArray,Search): # Define function for searching a value in array
    count = 0 # Set count for how many times the value has been found to 0
    for j in range(0, len(DataArray)):
        if(DataArray[j] == Search):
            count +=1 # Increment count for everytime the value has been found
    return count

DataArray = [] # Array for 25 elements

file = open("Data.txt", "r") # Open the file in read mode
for Line in file:
    DataArray.append(int(Line)) # Add each element read from data file into the array
file.close()

PrintArray(DataArray) # Call the procedure to print the elements of the array

Search = int(input("Input a number you want to find: ")) # Take input of value to search
while Search < 0 or Search > 100: # Run loop for values within and inclusive of 0 and 100
    Search = int(input("Input a number you want to find: "))
Repeat = LinearSearch(DataArray, Search) # Call LinearSearch function
print(f"The number {Search} is found {Repeat} times.") # Print the value and how many times it has repeated
