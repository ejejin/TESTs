from matplotlib import pyplot as plt

f = open("../n1.txt","r")

XAXIS = []; YAXIS = []

for line in f:
    xaxis, yaxis = line.split()
    XAXIS.append(xaxis);  YAXIS.append(int(yaxis))
print(XAXIS);print(YAXIS)

xs = [i+0.1 for i ,_ in enumerate(XAXIS)]
plt.bar(xs, YAXIS); plt.ylabel(" Counted number ");      plt.title("tutorial of reading in data and plotting")
plt.xticks([i+0.5 for i,_ in enumerate(XAXIS)], XAXIS);  plt.show()

