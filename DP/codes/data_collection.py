import os
import pandas as pd
import pulp as pl
import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
output = {"Innings 1":[0,0,0,0,0,0,0,0],"Innings 2":[0,0,0,0,0,0,0,0]}
def update_output(row):
    if(row[1]=='1'):
        # inning 1
        output['Innings 1'][0]+=1
        if(row[15]!=""):
            output['Innings 1'][7]+=1
        else:
            if(row[7]=='1'):
                output['Innings 1'][1]+=1
            elif(row[7]=='2'):
                output['Innings 1'][2]+=1
            elif(row[7]=='3'):
                output['Innings 1'][3]+=1
            elif(row[7]=='4'):
                output['Innings 1'][4]+=1
            elif(row[7]=='5'):
                output['Innings 1'][5]+=1
            elif(row[7]=='6'):
                output['Innings 1'][6]+=1
    elif(row[1]=='2'):
        # inning 2
        output['Innings 2'][0]+=1
        if(row[15]!=""):
            output['Innings 2'][7]+=1
        else:
            if(row[7]=='1'):
                output['Innings 2'][1]+=1
            elif(row[7]=='2'):
                output['Innings 2'][2]+=1
            elif(row[7]=='3'):
                output['Innings 2'][3]+=1
            elif(row[7]=='4'):
                output['Innings 2'][4]+=1
            elif(row[7]=='5'):
                output['Innings 2'][5]+=1
            elif(row[7]=='6'):
                output['Innings 2'][6]+=1


if __name__ == '__main__':
    print(bcolors.OKCYAN + "\t\t Welcome to Calculate data" + bcolors.ENDC)
    win_by_wic =0
    win_by_run =0
    super_over =0
    for file_number in range(1216492,1216548,1):
        file_location = "../match_data/"
        file_location += str(file_number)
        file_location += ".csv"
        with open(file_location, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            i=1
            for row in csvreader:
                # row contains the ith row of csv file
                if(row[0]=="info" and i==21):
                    if(row[1]=="winner_runs"):
                        win_by_run+=1
                    elif(row[1]=="winner_wickets"):
                        win_by_wic+=1
                    else:
                        super_over+=1
                if(row[0] == "ball"):
                    if(row[8] == '0'):
                        update_output(row)
                i+=1
    print(bcolors.UNDERLINE + "The detailed report of the season 2020" + bcolors.ENDC)
    print(output)
    print(bcolors.UNDERLINE + "Batting First " + str(win_by_run) + " Batting Second " + str(win_by_wic) + " Tied decided by superover " + str(super_over) + bcolors.ENDC)
    print(bcolors.OKGREEN + "First Innings" + bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of wicket {}".format(output['Innings 1'][7]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of dot ball {}".format((output['Innings 1'][0] - (output['Innings 1'][7]+output['Innings 1'][1]+output['Innings 1'][2]+output['Innings 1'][3]+output['Innings 1'][4]+output['Innings 1'][5]+output['Innings 1'][6]))/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of one run {}".format(output['Innings 1'][1]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of two runs {}".format(output['Innings 1'][2]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of three runs {}".format(output['Innings 1'][3]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of four runs {}".format(output['Innings 1'][4]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of five runs {}".format(output['Innings 1'][5]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKBLUE + "Probability of six runs {}".format(output['Innings 1'][6]/output['Innings 1'][0])+ bcolors.ENDC)
    print(bcolors.OKGREEN + "Second Innings" + bcolors.ENDC)
    print(bcolors.WARNING + "Probability of wicket {}".format(output['Innings 2'][7]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of dot ball {}".format((output['Innings 2'][0] -(output['Innings 2'][7]+output['Innings 2'][1]+output['Innings 2'][2]+output['Innings 2'][3]+output['Innings 2'][4]+output['Innings 2'][5]+output['Innings 2'][6]))/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of one run {}".format(output['Innings 2'][1]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of two runs {}".format(output['Innings 2'][2]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of three runs {}".format(output['Innings 2'][3]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of four runs {}".format(output['Innings 2'][4]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of five runs {}".format(output['Innings 2'][5]/output['Innings 2'][0])+ bcolors.ENDC)
    print(bcolors.WARNING + "Probability of six runs {}".format(output['Innings 2'][6]/output['Innings 2'][0])+ bcolors.ENDC)