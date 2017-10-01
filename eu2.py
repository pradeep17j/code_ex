
fib_list=[1,2]
end=40
while len(fib_list) < end:
    new_term = fib_list[-1]+fib_list[-2]
    if new_term < 4000000:
        fib_list.append(new_term)
    else:
        print len(fib_list)
        break

sum=0
#for i in range(0,len(fib_list),2):
for v in fib_list:
    if v%2 == 0:
        sum = sum + v

print fib_list
print sum

