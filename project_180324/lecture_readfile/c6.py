
f = open("root0_project.txt",'r')
LL = [] 
for line in f:
    _, _, _ , num = line.split()
    LL.append(num)
print(LL)
f.close()
