import sys
import numpy as np
sys.path.append("../functions")

Project1 = "project1_1M.txt"

'''
from c2_basic_histo_plotting import Basic_histo
Basic_histo(Project1)

from c3_Fit_Gaus_histo_plotting import Fit_Gaus_histo
Fit_Gaus_histo(Project1,"a")
'''

from c3_statistics_man import *
print(n_frequent_bin(Project1,0.5))

filename = "project1_1M.txt"
infile=open("project1_1M.txt")
list_file=[]
for line in infile:
    binN, ibin, fbin, entry = line.split()
    list_file.append([int(binN), float(ibin), float(fbin), float(entry)])

l=[x[0] for x in list_file]
entry=[x[3] for x in list_file]
p1 = 0.025
p2=0.975
total_entry = sum(entry)
print(total_entry)
s_entry = 0
for i in l:
    s_entry+=entry[i-1]
    if s_entry >= (p1*total_entry):
        point_binN = i
        low_bar = s_entry - entry[i-1]
        break

s_entry2 = 0
for i in l:
    s_entry2+=entry[i-1]
    if s_entry2 >= (p2*total_entry):
        point_binN2 = i
        low_bar2 = s_entry2 - entry[i-1]
        break
p_entry = p1*total_entry

p2_entry = p2*total_entry

print(point_binN)
x_p1 = list_file[point_binN-2][2]+(list_file[point_binN-1][2]-list_file[point_binN-1][1])*(p_entry-low_bar)/(s_entry-low_bar)
x_p2 = list_file[point_binN2-2][2]+(list_file[point_binN2-1][2]-list_file[point_binN2-1][1])*(p2_entry-low_bar2)/(s_entry2-low_bar2)
             # n% point = fbin of lower bound + width of bar*((n% entry-lower bar entry)/(upper bar entry-lower bar entry))
print(x_p1,x_p2)

for i in range(point_binN-1):
    list_file[i]=[list_file[i][0],list_file[i][1],list_file[i][2],0]

for i in range(point_binN2,len(l)):
    list_file[i] = [list_file[i][0], list_file[i][1], list_file[i][2], 0]

f_p05=open('project1_1M_p05.txt','w')
for i in range(int(binN)):
    f_p05.write(str(list_file[i][0])+" "+str(list_file[i][1])+" "+str(list_file[i][2])+" "+str(list_file[i][3])+'\n')

f_p05.close()

from c2_basic_histo_plotting import Basic_histo
project_xp05='project1_1M_p05.txt'
Basic_histo(project_xp05)


'''
from c1_basic_statistic import c1_mean,c1_standard_deviation

print((x_p05-c1_mean(filename))/c1_standard_deviation(filename))
'''
'''
for line in infile:
    binN, ibin, fbin, entry = line.split()
    list_file.append([int(binN), float(ibin), float(fbin), float(entry)])
'''












