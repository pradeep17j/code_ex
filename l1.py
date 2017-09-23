
for i in num_floors:
    j=i
    num_tries[i]=list()
    while (j<num_floors):
        if j < fatal_floor:
            num_tries[i].append(j)
            j = j + i
        elif j >= fatal_floor:
            num_tries[i].append(j)
            e1= eggs.pop()
            e1.change_state('break')
            for k in xrange(i+1, j):
                num_tries[i].append(j)
                if k == fatal_floor:
                    safe_floor=k-1
                else:
                    continue

