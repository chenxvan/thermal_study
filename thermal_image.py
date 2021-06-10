import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import matplotlib
import sys

#prepare a list of sorted files
dir_input = sys.argv[1]
file_list = os.listdir(dir_input)
thermal_files = []
for i in file_list:
    if i[-4:] == ".csv":
        if i!= "dataset.csv":
            thermal_files.append(i)

thermal_files_sorted = sorted(thermal_files)

def tempvis(csv_file, tmax, tmin, cmap, dirname):

    csv = np.genfromtxt(csv_file, delimiter=',')
    croppedcsv = csv[0:170,150:320]
    fig, ax = plt.subplots()
#    ax.matshow(csv, interpolation='none', vmin=tmin, vmax=tmax, cmap=cmap) #use this one for full image
    ax.matshow(croppedcsv, interpolation='none', vmin=tmin, vmax=tmax, cmap=cmap) 
    norm = mpl.colors.Normalize(vmin=tmin,vmax=tmax)
    sm = plt.cm.ScalarMappable(cmap="rainbow", norm=norm)
    sm.set_array([])
    plt.colorbar(sm, boundaries=np.arange(tmin,tmax,.1))

    file_name = csv_file.split('/')[5][:-4]
    ax.set(xlabel='\ndistance in pixels',ylabel='distance in pixels')
    saveas = dir_input+file_name+'.png'
    plt.savefig(saveas,format='png')
    plt.close() # only innovation; should stop the error

#Set temp range
t_max = int(sys.argv[2])
t_min =	int(sys.argv[3])

for i in thermal_files_sorted:
    input_file = dir_input+i
    tempvis(input_file, t_max, t_min, "rainbow", dir_input)
