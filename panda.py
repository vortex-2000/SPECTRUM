import matplotlib.pyplot as plt

import pandas as pd


def convertion(cell):
    if cell=="no":
        return 0
    if cell=="yes":
        return 1
    return cell

df = pd.read_csv("student-math.csv", sep=';',
                 converters={
                     "schoolsup":convertion,
                     "famsup":convertion,
                     "paid":convertion,
                     "activities":convertion,
                     "nursery":convertion,
                     "higher":convertion,
                     "internet":convertion,
                     "romantic":convertion
                     })



col=df["G1"]+df["G2"]+df["G3"]

df["final grade"]=col

del df['G1']
del df['G2']
del df['G3']



plt.scatter(df['studytime'], df['final grade'])
plt.xlabel("hours")
plt.ylabel("marks")


data=[df.studytime,df["final grade"]]

fig, ax = plt.subplots()

ax.boxplot(data)



df.to_csv("new.csv")


