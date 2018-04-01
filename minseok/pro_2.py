import matplotlib.pyplot as plt

f = open("../project_180324/lecture_readfile/root2_project.txt",'r')

xaxis = []
yaxis = []

for line in f:
    _,x,_,y = line.split()
    xaxis.append(float(x))
    yaxis.append(float(y))

xs = [i+0.1 for i, _ in enumerate(xaxis)]

#plt.bar(xs,yaxis)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Figure_2")
#plt.show()

total_ent = 0
mediation = 0
md = 0
ratio = []
for i in yaxis:
    total_ent = total_ent + i
    print(total_ent)
for j in yaxis:
    mediation = j/total_ent
    #md = md + mediation
    ratio.append(mediation)
    
plt.bar(xs,ratio)
plt.show()

#print(ratio)
#print(total_ent)
