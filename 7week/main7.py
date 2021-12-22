import pandas as pd

stud = pd.read_csv("StudentsPerformance.CSV")

a = stud[stud.loc['writing score'] & stud.loc['writing score'] > 0]

print((stud.loc[:6]).shape)  #
print((stud.iloc[:7]).shape)  #
print((stud.tail(7)).shape)  #
print((stud.iloc[0:7]).shape)
print((stud.loc[:7]).shape)  # yhih
print((stud.head(7)).shape)  #
