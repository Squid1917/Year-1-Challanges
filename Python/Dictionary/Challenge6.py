# Prompt the user to input a number and store it in the variable 'n'.
n = int(input("Input a number "))

# Create an empty dictionary 'd' to store the square of numbers.
d = dict()

# Iterate through numbers from 1 to 'n' (inclusive).
for x in range(1, n + 1):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x * x

# Print the dictionary 'd' containing the squares of numbers from 1 to 'n'.
print(d) 
