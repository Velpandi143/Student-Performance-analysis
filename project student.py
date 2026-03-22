import pandas as pd

std = pd.read_csv("students.csv")
std['Total'] = std["Maths"] + std['Science'] + std['English']
std['Average'] = std["Total"] / 3
m = std.sort_values('Total', ascending=False)
print(m,'\n')
print('this student was the first mark : ',std.loc[std['Average'].idxmax(),'Name'])
print('this student was the last mark : ' ,std.loc[std['Average'].idxmin(),'Name'])
print('class average is the : ',std['Average'].mean())
print('Average:\n',std[['Maths','Science','English']].mean())

