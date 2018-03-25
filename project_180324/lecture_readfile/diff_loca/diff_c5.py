f = open("../n1.txt","r")
LL = []
for line in f:
    print(line, end = '')
    LL.append(line)

print(LL)
f.close()

