
sum=0
lim=1000
for i in range(1,1000):
    if 3*i < lim:
        print "{} ,".format(3*i)
        sum = sum + 3*i
    if 5*i < lim and  ((5*i)%3 != 0):
        print "{} ,".format(5*i)
        sum = sum + 5*i


print sum

