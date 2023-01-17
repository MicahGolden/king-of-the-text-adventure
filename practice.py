import pandas as pd

example_dictionary = {
'name': ["Rich", "Ash", "Ben", "Steph"], 
"age": [35,26,37,26], 
"designation":["Head", "Head of US", "Instructor", "a.Instructor"]
}

df = pd.DataFrame(example_dictionary)

print(df)
#df.to_csv('example_csv')
df.to_json('example_json')