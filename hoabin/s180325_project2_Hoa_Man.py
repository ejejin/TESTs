import matplotlib.pyplot as plt
import numpy

f = open("../project_180324/lecture_readfile/root2_project.txt","r")

xs=[]
xw=[]
yv=[]


for line in f:
    _,num1,num2,num3=line.split()
    xs.append((float(num1)+float(num2))/2)
    xw.append(float(num2)-float(num1))
    yv.append(float(num3))

def Zvalue(a):
    xz=[]
    for i in a:
        xz.append((i-numpy.mean(a))/numpy.std(a))
    return xz

def probability(b):
    yp=[]
    for i in b:
        yp.append(i/numpy.sum(b))
    return yp

plt.bar(Zvalue(xs),probability(yv),Zvalue(xs)[0]-Zvalue(xs)[1])

plt.axis([-2,2,0,0.05])
plt.xlabel("Z")
plt.ylabel("Probability")
plt.title("Project2")



Mean=numpy.mean(yv)
Standard=numpy.std(yv)
TotalNumber=len(yv)
text = "mean = "+str(int(Mean))+" ,std = "+str(int(Standard))

plt.annotate(text,xy=(-0.5,0.04))

plt.text(Mean,Standard,TotalNumber)

plt.show()



