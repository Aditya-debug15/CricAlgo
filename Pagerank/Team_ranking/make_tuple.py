import os
import pandas as pd
import pulp as pl
import csv
dict_playerid = {}
dict_playerid["Delhi Capitals"] = 0
dict_playerid["Mumbai Indians"] = 1
dict_playerid["Sunrisers Hyderabad"] = 2
dict_playerid["Royal Challengers Bangalore"] = 3
dict_playerid["Chennai Super Kings"] = 4
dict_playerid["Kings XI Punjab"] = 5
dict_playerid["Kolkata Knight Riders"] = 6
dict_playerid["Rajasthan Royals"] = 7
rows, cols = (8, 8)
winners = [[0 for i in range(cols)] for j in range(rows)]
List_of_tuple = []
def get_key(val):
    for key, value in dict_playerid.items():
         if val == value:
             return key 
    return "key doesn't exist"
def get_tuple():
    for file_number in range(1216492,1216548,1):
        file_location = "match_data/"
        file_location += str(file_number)
        file_location += ".csv"
        with open(file_location, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            i=1
            for row in csvreader:
                # row contains the ith row of csv file
                if(i==3):
                    key_1 =row[2]
                elif(i==4):
                    key_2 = row[2]
                elif(i==20 and row[2]!="tie"):
                    key_3 = row[2]
                    if(key_3 == key_1):
                        winners[dict_playerid[key_3]][dict_playerid[key_2]]+=1
                    else:
                        winners[dict_playerid[key_3]][dict_playerid[key_1]]+=1
                i+=1
    for i in range(0,8):
        for j in range(0,8):
            if(winners[i][j] != 0):
                edge_from = get_key(j)
                edge_to = get_key(i)
                List_of_tuple.append((edge_from,edge_to,winners[i][j]))
    return List_of_tuple
