
import random
import pprint

pp = pprint.PrettyPrinter(indent=1, width=180 )

num_floors=100
fatal_floor=random.randint(1,100)
safe_floor=None

print "fatal {}".format(fatal_floor)

class egg(object):
    def __init__(self, state='safe'):
        self.state=state

    def change_state(self, state):
        self.state=state

num_tries=dict()

eggs=list()

num_eggs=2

for e1 in range(num_eggs):
    eggs.append(egg())

def prn_result(num_tries):
    for i in num_tries.keys():
        print "iter {} tries {}".format(i, num_tries[i])



for i in range(1,num_floors):
    j=i
    if i > fatal_floor:
        break
    print "iter {}".format(i)
    num_tries[i]=list()
    while (j<num_floors):
        if j < fatal_floor:
            #print "less"
            num_tries[i].append(j)
            j = j + i
        elif j >= fatal_floor:
            #print "more"
            num_tries[i].append(j)

            if len(eggs) > 1:
                e1= eggs.pop()
                e1.change_state('break')
                if (num_tries[i].index(j-1)):
                    safe_floor=j-1
                    print "safe {}".format(safe_floor)
                    break
                if len(eggs) > 1:
                    j=j+i
                    continue
            else:
                for k in xrange((j-i)+1, j):
                    num_tries[i].append(k)
                    if k == fatal_floor:
                        safe_floor=k-1
                        print "safe {}".format(safe_floor)
                        #pp.pprint(num_tries)
                        #prn_result(num_tries)
                        break
                    else:
                        continue
                break





#pp.pprint(num_tries)
prn_result(num_tries)

