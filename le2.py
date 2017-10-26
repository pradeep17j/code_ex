
s1='aabichhdef'


l1=list(s1)
d2=dict()
index=0

while(l1):

    v0=l1.pop(0)
    if l1[0] != v0:
        if index not in d2:
            d2[index]=list()
        if v0 not in d2[index]:
            d2[index].append(v0)
            d2[index].append(l1.pop(0))
        else:
            index=index+1
            if index not in d2:
                d2[index]=list()
                d2[index].append(v0)
                d2[index].append(l1.pop(0))

    else:
        if index in d2:
            if v0 not in d2[index]:
                d2[index].append(v0)

        index=index+1

    if len(l1) == 1:
        break


print s1
print d2

