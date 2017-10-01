
# Problem

#The prime factors of 13195 are
#What is the largest prime factor of the number 


import math as m1

num=600851475143
start = 2
div_fact=400000
# Slice the range of check to avoid memory over run.
end=num/div_fact

divs= list()

while div_fact > 2:

    for i in range(start,end):
        # Skip evens , since div by 2 is alreay tried
        if i > 2 and i%2 == 0:
            continue
        if num % i == 0:
            divs.append(i)

    # move to next slice
    start=end
    div_fact=div_fact-10000
    #print "div_fact {}".format(div_fact)
    if div_fact > 0:
        end=num/div_fact
    else:
        end=num

#print divs

# Among all the factors, find the primes as per wiki article

for i in divs:
    div=False
    for j in range(2,int(m1.sqrt(i))):
        if j > 2 and j%2 == 0:
            continue
        if i%j==0:
            div=True
            print "{} is div by {}".format(i,j)
            continue

    if div is False:
        print "{} is prime".format(i)

