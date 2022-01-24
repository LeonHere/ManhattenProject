# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:24:12 2022

@author: Leon Stegmann acer
"""

#----------------------------------------
#           Project 01
#----------------------------------------


#path to Data
path = r'C:\Users\fruitninja\Dropbox\UiA\ENE_418\project_1\Project1_data'   #Without the r, backslashes are treated as escape

#Library for read ...
import pandas as pd
#Library for 
import numpy as np

#Read Data
data=[]
data = pd.read_csv(path + r'\1-2013.dat',sep= ';')

month = np.arange(1,13)
year = np.arange(2013,2018)
"""
for y in year:
    for m in month:
        new = pd.read_csv(path + '\\' + str(m) + '-' + str(y) + '.dat' , sep = ';')
        if m==1 :
            data = new
        else:
            data=data.append(new,ignore_index=True)        
        
        print('addedData:' + str(m) + '.' + str(y))
"""

#1. Calculate the monthly production for string 3 for all months in the data set. Indicate if there 
#       are missing data for some months. Display the result graphically.

units = data.iloc[0][0:31]
print(units)

# ---------------------------
# Total Power calc

VAC = 'Inv3_UAC_V_Avg'
IAC = 'Inv3_IAC_A_Avg'
counter = np.arange(0,len(data))
P_tot  = 0
for i in counter:
    P_tot = P_tot + data[VAC][i]*data[IAC][i]    

print( P_tot)    


#---------------------
# check Data for missing Data

def schaltjahr(y):
    if y!=0:
        if (y % 400) == 0 :
            return 1
        elif (y % 100) == 0 :
            return 1            
        elif (y % 4) == 0 :
            return 1            
        else :
            return 0
            
            
#check MINUTE

def check_MINUTE(date):
    if data['MINUTE'][i] != date['m']: #if newMnute==oldMinute+1
        print('missing date' + str(date))           
    
def check_HOUR(date):
    date['h']=date['h']%24
    if data['HOUR'][i] != date['h']:
        print('missing date' + str(date))
    date['h']=date['h']+1

def  Time_upcounter(date):
    date['m']=date['m']+1
    if date['m'] == 60 :
        date['m'] = date['m']%60
        date['h'] =date['h']+1
    if date['h'] == 24 :
        date['h'] = date['h']%24
        date['dd'] =date['d']+1
    if date['mm'] == 2 and date['dd']>28:
        if schaltjahr(date['yyyy']):
             date['dd']=date['dd'] %30 +1                 
        else:
            date['dd']=date['dd'] %29 +1
    elif date['mm'] in [1,3,5,7,8,10,12] and date['dd'] == 32:
        date['dd'] = date['dd']%31
        date['mm']=date['mm']+1
    elif date['mm'] in [4,6,9,11] and date['dd'] == 32:
        date['dd'] = date['dd']%30
        date['mm'] = date['mm']+1
        


#check time continuity
i = 0
start_year = year[0]
date = {'yyyy':start_year,'mm':1,'dd':1,'h':0,'m':0} # year, Month, hour, minute
"""
while i < 100: #len(data):
    check_MINUTE(date)
    if date['m']==1:
        check_HOUR(date)
    Time_upcounter(date)    
    print(date)
    i = i+1
"""

for i in np.arange(0,100):
    print(Time_upcounter(date))
    Time_upcounter(date)





