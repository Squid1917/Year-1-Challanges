# Create a dictionary 'd' with key-value pairs.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define a function 'is_key_present' that takes an argument 'x'.
def is_key_present(x):
    # Check if 'x' is a key in the dictionary 'd'.
    if x in d:
        # If 'x' is present in 'd', print a message indicating that the key is present.
        print('Key is present in the dictionary')
    else:
        # If 'x' is not present in 'd', print a message indicating that the key is not present.
        print('Key is not present in the dictionary')

# Call the 'is_key_present' function with the argument 5 to check if 5 is a key in the dictionary.
is_key_present(5)

# Call the 'is_key_present' function with the argument 9 to check if 9 is a key in the dictionary.
is_key_present(9) 
