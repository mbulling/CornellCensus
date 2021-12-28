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
colleges = ['College of Engineering', 'College of Arts and Sciences', 'Dyson School of Business', 'College of Agriculture and Life Sciences', 'College of Human Ecology']
ratingAvgCOE = 0.0


def getcollege():
    """
    returns college list
    """
    data = filter()
    colleges = []
    rating = [6, 2, 3, 4, 5]
    for college in data:
        colleges.append(college)
    for college in colleges:
        rating.append(data[college])
    #return colleges
    return ['Engine', 'Art']

def getrating():
    """
    returns rating list
    """
    #data = mason()
    colleges = []
    rating = [6, 2, 3, 4, 5]
    
    return [6, 2, 4, 5, 6]

def getyear():
    rawdata = sheet.get_all_values()
    years = [0, 0, 0, 0]
    for u in rawdata:
        if u[2] == 'Freshman':
            years[0] = years[0] + 1
        if u[2] == 'Sophomore':
            years[1] = years[1] + 1
        if u[2] == 'Junior':
            years[2] = years[2] + 1
        if u[2] == 'Senior':
            years[3] = years[3] + 1
    return years

def getmajor():
    return ["Computer Science", "Mechanical Engineering"]





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
    rating = [6, 2, 3, 4, 5]

    # for x in rawdata:
    #     college.append(x[0])
    #     rating.append(x[1])
    # college.pop(0)
    # rating.pop(0)

    # for index in range(len(college)):
    #     if not college[index] in dict:
    #         dict[college[index]] = []
    #     dict[college[index]].append(rating[index])

    # for college in dict:
    #     data = dict[college]
    #     sum = 0
    #     avg = 0
    #     for index in range(len(data)):
    #         sum += int(data[index])
    #     if len(data) == 0:
    #         avg = 0
    #     else:
    #         avg = sum / len(data)
    #     dict[college] = round(avg, 1)

    return dict

def mason():
    rawdata = sheet.get_all_values()
    dict = {}
    college = []
    rating = [6, 2, 3, 4, 5]
    ratCOE = 0.0
    numCOE = 0

    for x in rawdata:
        if x[0] == colleges[0]:
            #ratCOE += int(x[1])
            numCOE += 1
        
    
    college.append(colleges[0])
    rating.append(ratCOE/numCOE)

    #dict[colleges[0]] = rating[0]

    # for index in range(len(college)):
    #     if not college[index] in dict:
    #         dict[college[index]] = []
    #     dict[college[index]].append(rating[index])

    # for college in dict:
    #     data = dict[college]
    #     sum = 0
    #     avg = 0
    #     for index in range(len(data)):
    #         sum += int(data[index])
    #     if len(data) == 0:
    #         avg = 0
    #     else:
    #         avg = sum / len(data)
    #     dict[college] = round(avg, 1)

    return dict
