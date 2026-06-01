data=[[1,2],[2,3],[3,4] ,[5,6],[6,7],[7,8]]
target=[0,0,0,1,1,1]
find=[4,4]
dist=[]
for i in range(len(data)):
    d=0
    for j in range(len(data[i])):
        d+=(data[i][j]-find[j])**2
    dist.append((d,target[i]))
dist.sort()
print(dist)
k=4
count0=0
count1=0
for i in range(k):
    if dist[1]==0:
        count0+=1
    else:
        count1+=1
if(count0>count1):
    print("new assign is ",0)
else:
    print("new assign is ",1) 