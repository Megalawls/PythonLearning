import pandas as pd
# import numpy as np

titanicPassengers = pd.read_csv("titanic.csv")
df = pd.DataFrame(data=titanicPassengers, columns=["Name", "Age", "Cabin"])

#Count the numver of missing values in each column
countNaN = titanicPassengers.isnull().sum()

#Replace NaN
nonNA = df.fillna(0)

#Split the 'name' column into 3 columns - first name, surname and title
dfsplit = pd.DataFrame(df.Name.str.replace(".", ",").str.split(",", 2).tolist()
                            , columns=["SurName", "Title", "Other Names"]) #Need to format this to have it ordered Title, Name, Other Names

print(dfsplit)
