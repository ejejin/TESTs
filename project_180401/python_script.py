import sys
sys.path.append("../functions")
from c1_basic_statistic import c1_total_ENTRY, c1_mean 

Infile = "project1_10K.txt"
MEAN = c1_mean(Infile)
print(MEAN)

#from c2_basic_histo_plotting import Basic_histo
#Basic_histo(Infile)






