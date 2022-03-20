"""
import csv
data=[]
with open ("car.csv",'r')as csvfile:
    fdata=csv.reader(csvfile)
    for x in fdata:
        data.append(x)
        #print(x,'\n')

numOfAttribute=len(data[0])-1
specificHypothesis=['0']*numOfAttribute
generalHypothesis=['?']*numOfAttribute

print()
print(specificHypothesis,'\n')
print(generalHypothesis,'\n')
temp=[]
flag=False
for i in range (len(data)):

    if data[i][numOfAttribute]== 'Yes' :
        if flag:
            for j in range(numOfAttribute):
                if specificHypothesis[j]!=data[i][j]:
                    specificHypothesis[j]='?'
        else :
            for j in range(numOfAttribute):
                specificHypothesis[j]=data[i][j]
            flag=True
        for j in range(numOfAttribute):
            delcount=0
            for k in range(len(temp)):
                #print(temp,k)
                if temp[k-delcount][j]!=specificHypothesis[j] and temp[k-delcount][j] !='?':
                    delcount+=1
                    del temp[k-delcount]
    else:
        for j in range(numOfAttribute):
            if data[i][j]!=specificHypothesis[j] and specificHypothesis !='?':
                generalHypothesis[j]=specificHypothesis[j]
                temp.append(generalHypothesis)
                generalHypothesis=['?']*numOfAttribute
    print('\n\n',specificHypothesis,'\n\n')
    if (len(temp))==0:
        print('general Hypothesis',generalHypothesis)
    else:
        print('general Hypothesis', temp)
    

generalHypothesis=[]
for i in g:
    for j in i:
        if j !='?':
            generalHypothesis.append(i)
            break
print(generalHypothesis)
"""
import csv
with open("car.csv","r") as csvfile:
    a=[tuple(x) for x in csv.reader(csvfile)]

num_att=len(a[0])-1

S=['0']*num_att
G=['?']*num_att
i=0
print("S[{0}]: ".format(i),S)
print("G[{0}]: ".format(i),G)
temp=[]

for i in range(len(a)):
    if a[i][-1]=='Yes':
        for j in range(num_att):
            S[j]=a[i][j]
        break
print("-----------")


for i in range(1,len(a)):
    if a[i][num_att]=='Yes':
        for j in range(num_att):
            if S[j]!=a[i][j]:
                S[j]='?'
        for j in range(num_att):
            for k in range(len(temp)-1):
                if temp[k][j]!=S[j] and temp[k][j]!='?':
                    del temp[k]
    
    else:
        if len(temp)==0:
            for j in range(num_att):
                if a[i][j]!=S[j] and S[j]!='?':
                    G[j]=S[j]
                    temp.append(G)
                    G=['?']*num_att
        else:
            for h in range(len(temp)):
                c=0
                for j in range(num_att):
                    if temp[h][j]!=a[i][j]:
                        c+=1
                        if temp[h][j]!='?':
                            v=temp[h][j]

                if c<num_att:
                    #print(temp[h])
                    G=temp[h].copy()
                    hypo=temp[h].copy()
                    del temp[h]
                    for j in range(num_att):
                        if a[i][j]!=S[j] and S[j]!='?' and S[j]!=v:
                            G[j]=S[j]
                            #print(G)
                            temp.append(G)
                            G=hypo.copy()


    print("S[{0}]: ".format(i),S)

    if len(temp)==0:
        print("G[{0}]: ".format(i),G)
    else:
        print("G[{0}]: ".format(i),temp)
    print("-----------")
