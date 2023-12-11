import pandas as pd

'''
data = { #Sets the values
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}

df = pd.DataFrame(data, index =["day1","day2","day3"] ) #Creates a DataFrame

print(df) # Prints Out the data frame in a nice format
'''

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
