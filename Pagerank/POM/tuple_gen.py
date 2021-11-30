import csv

dict_playerid = {}
dict_playerid["DA Warner"] = 0
dict_playerid["MS Harris"] = 1
dict_playerid["M Labuschagne"] = 2
dict_playerid["SPD Smith"] = 3
dict_playerid["MS Wade"] = 4
dict_playerid["C Green"] = 5
dict_playerid["TD Paine"] = 6
dict_playerid["PJ Cummins"] = 7
dict_playerid["MA Starc"] = 8
dict_playerid["NM Lyon"] = 9
dict_playerid["JR Hazlewood"] = 10
dict_playerid["RG Sharma"] = 11
dict_playerid["Shubman Gill"] = 12
dict_playerid["CA Pujara"] = 13
dict_playerid["AM Rahane"] = 14
dict_playerid["MA Agarwal"] = 15
dict_playerid["RR Pant"] = 16
dict_playerid["Washington Sundar"] = 17
dict_playerid["SN Thakur"] = 18
dict_playerid["NA Saini"] = 19
dict_playerid["Mohammed Siraj"] = 20
dict_playerid["T Natarajan"] = 21
rows, cols = (11, 11)
aus_score = [[0 for i in range(cols)] for j in range(rows)]
ind_score = [[0 for i in range(cols)] for j in range(rows)]
List_of_tuple = []
file_location = "gabba_test.csv"

def get_key(val):
    for key, value in dict_playerid.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def update_aus(row):
    if(row[15] != ""):
        # wicket taken need to add 15 to bowler
        key_bowler = dict_playerid[row[6]] - 11
        key_batsman = dict_playerid[row[4]]
        ind_score[key_bowler][key_batsman] += 15
    else:
        key_bowler = dict_playerid[row[6]] - 11
        key_batsman = dict_playerid[row[4]]
        aus_score[key_batsman][key_bowler] += int(row[7])


def update_ind(row):
    if(row[15] != ""):
        # wicket taken need to add 15 to bowler
        key_bowler = dict_playerid[row[6]] 
        key_batsman = dict_playerid[row[4]] - 11
        aus_score[key_bowler][key_batsman] += 15
    else:
        key_bowler = dict_playerid[row[6]]
        key_batsman = dict_playerid[row[4]] - 11
        ind_score[key_batsman][key_bowler]+= int(row[7])

def get_tuple():
    with open(file_location, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            # row contains the ith row of csv file
            if(row[0] == "ball" and (row[1] == "1" or row[1]=="3")):
                if(row[8] == '0'):
                    update_aus(row)
            if(row[0] == "ball" and (row[1] == "2" or row[1]=="4")):
                if(row[8] == '0'):
                    update_ind(row)
    for i in range(0,11):
        for j in range(0,11):
            if(aus_score[i][j] != 0):
                edge_from = get_key(j+11)
                edge_to = get_key(i)
                List_of_tuple.append((edge_from,edge_to,aus_score[i][j]))
            if(ind_score[i][j]!=0):
                edge_from = get_key(j)
                edge_to = get_key(i+11)
                List_of_tuple.append((edge_from,edge_to,ind_score[i][j]))
    return List_of_tuple