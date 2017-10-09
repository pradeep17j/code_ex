

## Find the largest sum of consecutive nums in a give array
##

import pprint

l1=[1,2,-1,0,4,-3,4,0,-6,10]


#
# solution 1
#
# create a list of list
# add pos[0]+ pos[1] and save in the d1[0][0]
# add pos[0]+post[1]+pos[2] and save in d1[0][1]
# ........ add pos[1]+pos[2] and save in d1[1][0] .. and go on

d1=list()
sum1=0

pp = pprint.PrettyPrinter(indent=4)

for i in range(len(l1)):
    if i+1 < len(l1):
        d1.append(list())
    for j in range(i+1,len(l1)):
        d1[i].append(sum(l1[i:j+1]))

pp.pprint(d1)


#
# solution 2
# optimized here
# add pos[0]+pos[1] and save in d1[0][0]
# add d1[0][0] + pos[2] and save in d1[0][1]
# add d1[0][1] + pos[3] and save in d1[0][2]
# then when d1[0] is fully done, exit this loop

d1=list()
d1.append(list())
for i in range(1,len(l1)):
    if len(d1[-1]) > 0:
        d1[-1].append(d1[-1][-1]+l1[i])
    else:
        d1[-1].append(l1[0]+l1[i])


#  d1[1][0] = d1[0][1] - l1[0]
#  d1[1][1] = d1[0][2] - l1[0] .. until d1[1] is done
#
# d1[2][0] = d1[1][1] - l1[1]  ....etc

for j in l1:
    #get the last index
    index = len(d1)-1
    for k in d1[index][1:]:
        if index == len(d1)-1:
            d1.append(list())
        d1[-1].append(k-j)


pp.pprint(d1)
