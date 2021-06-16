import pandas as pd
from datetime import date
import os


def exist_result(file: str):
    '''
    Check if file with results exists,
    if not, create this file
    :param file: (str) path of file to check
    '''
    if not os.path.exists(file):
        folders = os.path.split(file)[0]
        os.makedirs(folders, exist_ok=True)
        with open(file, "w") as result:
            result.write("points,date,user")


def writing(file: str, score: str, date: str, user: str, num: int):
    """
    Write results to csv file
    :param file: (str) name of file
    :param score: (str) number of achieved score
    :param date: (str) date of achieved score
    :param user: (str) user name
    :param num: (int) number of maximum amount of statistics
    """
    exist_result(file)
    df = pd.read_csv(file)
    sorted = df.sort_values(["points"], ascending=False)
    if sorted.empty:
        sorted.loc[0] = [score, date, user]
    elif sorted.index[-1] < num - 1:
        sorted.loc[sorted.index[-1] + 1] = [score, date, user]
    elif sorted["points"].iloc[-1] < score:
        sorted.loc[sorted.index[-1]] = [score, date, user]
    new_table = sorted.sort_values(["points"], ascending=False)
    new_table.to_csv(file, index=False)


def today_points_write(file: str, score: str, user: str, num: int =10):
    '''
    Write achieved score with today date
    :param file: (str) name of file
    :param score: (str) number of achieved score
    :param user: (str) user name
    :param num: (int) number of maximum amount of statistics
    '''
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    writing(file, score, d1, user, num)
