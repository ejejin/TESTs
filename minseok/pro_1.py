import matplotlib.pyplot as plt

f = open("../project_180324/lecture_readfile/root1_project.txt",'r')
xaxis = []
yaxis = []
xmax = []

for line in f:
    _,Xmin,Xmax,ht = line.split()
    xaxis.append(float(Xmin))
    yaxis.append(float(ht))
    xmax.append(float(Xmax))

xs = [i+0.1 for i, _ in enumerate(xaxis)]
#plt.bar(xs, yaxis)
#plt.ylabel("entry")
#plt.xlabel("Bins")
#plt.title("Project_1")
#plt.xticks([i+0.5 for i, _ in enumerate(xaxis)],xaxis)
#plt.show()

total_ent = 0
ratio = []

for i in yaxis:
    total_ent = total_ent + i

for k in yaxis:
    mediation = k/total_ent
    ratio.append(float(mediation))

plt.bar(xs,ratio)
plt.ylabel("ratio")
plt.xlabel("Bins")
plt.title("Project_2")

plt.text(-3,0.037, 'Standard deviation = 10.95')
plt.text(-3,0.035, 'Variation = 120.00')
plt.text(-3,0.033, 'Mean = 0.24')
plt.show()

mean = 0
mean_l = []
mean_t = 0

for q in range(len(xaxis)):
    i = xaxis[q] 
    j = yaxis[q]
    k = xmax[q]
    mean = abs((i+k)*j/2)
    mean_l.append(float(mean))
for w in mean_l:
    mean_t = mean_t + w
mean_t = mean_t/total_ent

sd_sum = 0
index = 0

for a in yaxis:
    sd_sum = sd_sum + pow((a - mean_t),2)
    #print(pow((a - mean_t),2))

#print(sd)
print(sd_sum/total_ent-1)
print(pow((sd_sum/total_ent-1),1/2))
print(mean_t)


