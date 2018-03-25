
f = open("n1.txt",'r')

for line in f:
    num1, num2 = line.split()
    print(num1, end=' ')
    print(num2)

print(type(num1))

f.close()
