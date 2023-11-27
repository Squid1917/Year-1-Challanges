# Define a function 'sort_dict_by_value' that takes a dictionary 'd' and an optional 'reverse' flag.
# It returns the dictionary sorted by values in ascending or descending order, based on the 'reverse' flag.
def sort_dict_by_value(d, reverse = False):
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

# Print a message indicating the start of the code section.
print("Original dictionary elements:")

# Create a dictionary 'colors' with key-value pairs.
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

# Print the original dictionary 'colors'.
print(colors)

# Print a message indicating the start of the sorting process in ascending order.
print("\nSort (ascending) the said dictionary elements by value:")

# Call the 'sort_dict_by_value' function to sort the 'colors' dictionary by value in ascending order.
# Print the result.
print(sort_dict_by_value(colors))

# Print a message indicating the start of the sorting process in descending order.
print("\nSort (descending) the said dictionary elements by value:")

# Call the 'sort_dict_by_value' function with 'reverse=True' to sort the 'colors' dictionary by value in descending order.
# Print the result.
print(sort_dict_by_value(colors, True)) 