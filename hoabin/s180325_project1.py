import matplotlib.pyplot as plt
import numpy

f = open("../project_180324/lecture_readfile/root1_project.txt","r")
xs = []
xw = []
#xw2 = []
yv = []

for line in f:
    _,num1,num2,num3 = line.split()
    yv.append(float(num3))
    xs.append((float(num1)+float(num2))/2)
    xw.append(float(num2)-float(num1))

def Zvalue(c):
    xz=[]
    for i in c:
        Z=(i-numpy.mean(c))/numpy.std(c)
        xz.append(Z)
    return xz




def probability(d):
    E=[]
    for i in d:
        xo=(i/numpy.sum(d))
        E.append(xo)
    return E

plt.bar(Zvalue(xs),probability(yv),Zvalue(xs)[0]-Zvalue(xs)[1])

print(sum(probability(yv)))
plt.axis([-2,2,0,0.05])
plt.xlabel("Z(X)")
plt.ylabel("Probability")
plt.title("Project1")


print(numpy.mean(probability(yv)),numpy.std(yv),numpy.sum(yv))

plt.show()

'''
def mean(a):
    sum=0
    for i in a:
        sum=sum+i
    return sum/len(a)

def de_mean(b):
    x_bar = mean(b)
    return []
'''