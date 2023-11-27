# Create the first dictionary 'd1' with key-value pairs.
d1 = {'a': 100, 'b': 200}

# Create the second dictionary 'd2' with key-value pairs.
d2 = {'x': 300, 'y': 200}

# Create a new dictionary 'd' and initialize it as a copy of 'd1'.
d = d1.copy()

# Update the dictionary 'd' by adding key-value pairs from 'd2'.
d.update(d2)

# Print the dictionary 'd' after combining the key-value pairs from 'd1' and 'd2.
print(d) 
