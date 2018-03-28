def mat_txt_to_hist(filename):
    import os
    import matplotlib.pyplot as plt
    import numpy
 
    if(filename[0]=="/"):
        filename = filename
    else:
        filename = os.getcwd() + "/" + filename   # get the path included filename
    loca=len(filename)
    for i in range (1,len(filename)+1):       # find the "/" location
        if(filename[-i] == "/"):
            loca = i-1
            break

    FILENAME = filename.replace(filename[:-loca],"")   # this is the shorten filename
#    print(FILENAME, "******")    
#    print(filename,FILENAME)   
   # fileroot = filename.replace(".txt","_F.root")
   # fileroot = fileroot.replace("//","/")
    f = open(filename,"r")
    xs = []
    xw = []
    yv = []
    
    for line in f:
        _,num1,num2,num3=line.split()
        xs.append((float(num1)+float(num2))/2) #x position of each bars
        xw.append(float(num2)-float(num1))  # width of each bars
        yv.append(float(num3))   # y value

    def Zvalue(a): #normalization
        xz=[]
        for i in a:
            xz.append((i-numpy.mean(a))/numpy.std(a))
        return xz

    def probability(b): # make pdf 
        yp=[]
        for i in b:
            yp.append(i/numpy.sum(b))
        return yp

    def upper_pro(c): #find the probabilty's upper bound, is the max value + the half of max value
        max_pro = c[0]
        for i in c:
            if max_pro<i:
                max_pro = i
        if max_pro >= 0.6:
            return 1
        else:
            return max_pro+(max_pro/2)

    def abs_max(d): #return the max_absolute value
        max_ab=d[0]
        for i in d:
            if numpy.fabs(max_ab)<numpy.fabs(i):
                max_ab = i
        return max_ab
         
                
    plt.bar(Zvalue(xs),probability(yv),Zvalue(xs)[0]-Zvalue(xs)[1])

    plt.axis([-abs_max(Zvalue(xs))-0.2,abs_max(Zvalue(xs))+0.2,0,upper_pro(probability(yv))])
    plt.xlabel("Z")
    plt.ylabel("Probability")
    plt.title(FILENAME+"_hist")
    plt.show()


mat_txt_to_hist("/home/manggny/Desktop/Group_study/TESTs/project_180324/lecture_readfile/root2_project.txt")
