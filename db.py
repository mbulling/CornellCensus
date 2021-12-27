import gspread
from oauth2client.service_account import ServiceAccountCredentials
# import pandas as pd
# import matplotlib.pyplot as plt
# import mpld3
#
# import base64
# from io import BytesIO

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]



# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("db").sheet1
colleges = ['engineering', 'arts and science', 'dyson', 'cals', 'humec']

def getcollege():
    """
    returns college list
    """
    data = filter()
    colleges = []
    rating = []
    for college in data:
        colleges.append(college)
    for college in colleges:
        rating.append(data[college])
    return colleges

def getrating():
    """
    returns rating list
    """
    data = filter()
    colleges = []
    rating = []
    for college in data:
        colleges.append(college)
    for college in colleges:
        rating.append(data[college])
    return rating



def nindex():
    """
    return next index on google sheet
    """
    rawdata = sheet.get_all_records()
    return len(rawdata) + 2

def filter():
    """
    cleans raw data from the google sheet csv file
    """
    rawdata = sheet.get_all_values()
    dict = {}
    college = []
    rating = []

    for x in rawdata:
        college.append(x[0])
        rating.append(x[1])
    college.pop(0)
    rating.pop(0)

    for index in range(len(college)):
        if not college[index] in dict:
            dict[college[index]] = []
        dict[college[index]].append(rating[index])

    for college in dict:
        data = dict[college]
        sum = 0
        avg = 0
        for index in range(len(data)):
            sum += int(data[index])
        if len(data) == 0:
            avg = 0
        else:
            avg = sum / len(data)
        dict[college] = round(avg, 1)

    return dict
