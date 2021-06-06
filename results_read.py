import pandas as pd
from datetime import date
import os

def exist_result(file):
    if not os.path.exists(file):
        with open(file, "w") as result:
            result.write("points,date")

def writing(file, score, date, num):
    exist_result(file)
    df = pd.read_csv(file)
    sorted = df.sort_values(["points"], ascending=False)
    if sorted.empty:
        sorted.loc[0] = [score, date]
    elif sorted.index[-1] < num-1:
        sorted.loc[sorted.index[-1]+1] = [score, date]
    elif sorted["points"].iloc[-1] < score:
        sorted.loc[sorted.index[-1]] = [score, date]
    new_table = sorted.sort_values(["points"], ascending=False)
    new_table.to_csv(file, index=False)

def today_points_write(file, score, num=10):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    writing(file, score, d1, num)

#def reading(file):
#    df = pd.read_csv(file)
#    points = df['points'].tolist()
#    data = df["date"].tolist()
#    return zip(points, data)