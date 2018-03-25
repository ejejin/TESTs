
f = open("n1.txt",'r')
LL1 = [] 
LL2 = []
for line in f:
    num1, num2 = line.split()
    print(num1, end=' ')
    print(num2)
    LL1.append(num1)
    LL2.append(num2)
print(LL1);print(LL2)
f.close()
