import pytest

#unsorted=[1,2,3,9,7,6,5]
unsorted=[1]
#unsorted=[]

# The Merge Sort function
# Takes in the unsorted array as parameter

def msort(unsorted):

    # If no elements or only 1 element
    # return since nothing to sort
    if len(unsorted) == 1 or len(unsorted) == 0:
        return unsorted

    # Get Array Length
    arry_len = len(unsorted)

    # Split it into half
    # Dont worry , if odd number of elements
    # You cannot split into exact half

    # First half
    left_half = unsorted[0:int(arry_len/2)]

    # second half
    right_half = unsorted[int(arry_len/2):]

    # Recursive call to sort left half
    r1 = msort(left_half)

    # Recursive call to sort right half
    r2 = msort(right_half)

    # A temp array to merge r1 and r2 arrays returned
    # by the recursive calls. r1 and r2 are already sorted
    new_arry = list()

    # Have 2 variable i and j to index through r1 an r2
    # The while loop below does the following
    # it indexes through both r1 and r2 which are sorted
    # and find the lowest value at a give index and insert it into
    # new_array

    i = j = 0
    while (i < len(r1) and j < len(r2)):

        if r1[i] < r2[j]:
            new_arry.append(r1[i])
            i = i + 1
        elif r2[j] < r1[i]:
            new_arry.append(r2[j])
            j = j + 1
        else:
            new_arry.append(r2[j])
            new_arry.append(r1[i])
            i = i + 1
            j = j + 1

    # This condition is take care of condition where
    # r1 and r2 arrays are not of same length
    # so , when the while condition terminates above
    # the array which is longer is not traversed completely
    # we need to add the untraversed elements of the longer of the r1 and r2
    # into new_array at the end to complete the merge

    if (i < len(r1)):
        new_arry = new_arry + r1[i:]
    elif (j < len(r2)):
        new_arry = new_arry + r2[j:]

    return new_arry


print msort(unsorted)

# Test code in pytest
# To test, run as below
# pytest -v -s msort.py

import random

@pytest.mark.parametrize('val,val1',[(0,210), (11,2010), (20,6000)])

def test_msort(val, val1):

    count=0
    t_array = list()

    clast = random.randint(val,val1)

    while(count < clast):
        t_array.append(random.randint(val,val1))
        count = count + 1

    #print t_array
    m_array = msort(t_array)

    t_array.sort()
    #print m_array
    assert cmp(m_array, t_array) == 0



