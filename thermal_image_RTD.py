import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import os
from datetime import datetime
import time
import matplotlib
import csv
import sys
#from ROOT import *
#gStyle.SetOptStat(0)


#calculate average temp for an area
def temp_avg(input_file, xmin, xmax, ymin, ymax):
    df=pd.read_csv(input_file, sep=',',header=None)
    points = []
    i = xmin

    while i < xmax:
        j = ymin
        while j < ymax:
            points.append(df.values[i][j])
            j +=1
        i += 1
    avg_temp = sum(points)/len(points)
    return avg_temp

#create a list for input
def sorted_list(dir_input):
    file_list = os.listdir(dir_input)
    thermal_files = []
    for i in file_list:

        if i[-4:] == ".csv": 
            if i!= "dataset.csv":
                thermal_files.append(i)

    thermal_files_sorted = sorted(thermal_files)
    return thermal_files_sorted

#create a list for run time
def time_list(input_list):
    #Get run time in min
    t_ini = input_list[0].split('.')[0][:-1]
    t_ini_sec = time.mktime(time.strptime(t_ini,"%m-%d-%Y-%H-%M-%S"))
    run_time = []
    
    for i in input_list:
        t = i.split('.')[0][:-1]
        seconds = time.mktime(time.strptime(t,"%m-%d-%Y-%H-%M-%S"))
        runtime_min = int((seconds-t_ini_sec)/60)
        run_time.append(runtime_min)

    return run_time

def RTD(input_file):
    RTD_value = [] 
    df=pd.read_csv(input_file, sep=',',header=None)
    for i in df.values:
        RTD_value.append(i[1])
    return RTD_value
    
dir_input = sys.argv[1]


file_list = sorted_list(dir_input)
temp_list1 = []
temp_list2 = []
temp_list3 = []
temp_list4 = []


#Get the temp values
for i in range(len(file_list)):
    temp_list1.append(temp_avg(dir_input+file_list[i], 60, 63, 207, 210))
    temp_list2.append(temp_avg(dir_input+file_list[i], 100, 103, 207, 210))
    temp_list3.append(temp_avg(dir_input+file_list[i], 60, 63, 237, 240))
    temp_list4.append(temp_avg(dir_input+file_list[i], 100, 103, 237, 240))



RTD_therm = []

for i in range(len(temp_list1)):
    RTD_value = []
    RTD_value.append(temp_list1[i]) 
    RTD_value.append(temp_list1[i])
    RTD_value.append(temp_list1[i])
    RTD_value.append(temp_list1[i])
    RTD_therm.append(sum(RTD_value)/len(RTD_value))


RTD_real = RTD(dir_input+"dataset.csv")    
#Get time info
run_time = time_list(file_list)

#define plot
fig, ax = plt.subplots()

ax.plot(run_time, RTD_real, color='blue', label='Measurements from RTD')
ax.plot(run_time, RTD_therm, color='red', label='Measurements from Thermal Image')


ax.legend()
ax.set(xlabel='Run Time (m)', ylabel='Temperature (C)',
       title='Thermal Image Measurement')

pic_name = dir_input.split('/')[4]+'RTD.png'
plt.savefig(pic_name,format='png')
plt.show()
