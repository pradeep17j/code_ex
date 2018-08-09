
import pytest

class Solution(object):

    # function to find
    # Length of Longest substring with non repeating chars
    #

    def nonRepeatingSubStrLen(self, s1):

        # Starting index into string
        i = 0

        # We are find an instance of substring which is non repeating
        # This variable start is here to record the start of  current
        # substring that is being worked on
        start = 0

        # f1 and f2 are the start and end positions or index of the longest
        # non-repeating substring that has been found

        f1 = f2 = 0

        # a dictionary used to find the non-repeating string.
        # Keys for this dict are chars in the string
        # if we have an hash collision, that means we have found a repeating char
        td = dict()

        # The latest non-repeating substring is in lstr.
        lstr = ''

        if len(s1) == 0 or len(s1) == 1:
            return len(s1)

        # loop through until end of string

        while( i < len(s1) ):

            # If this character s1[i] is already found in dict td

            if(s1[i] in td):

                # If the current substring longer than the
                # one already found, remember the new longer substring in lstr
                if(len(lstr) < len(s1[start:i])):
                    lstr = s1[start:i]
                    #print "{}\n".format(lstr)

                    # Record the start and end of longest substr found until now
                    f1 = start
                    f2 = i - 1

                # Whether this was the longest substr or not, when there is hash collision
                # set the start to position which is new non-repeat char
                # Reset the td to empty dict
                # The first char into this reinitialized dict is the char pointed to by start
                # i should be index to next char

                start = td[s1[i]] + 1
                td = dict()
                td[s1[start]] = start
                i = start + 1
            else:
                # Incase there was no hash collision, keep adding chars to hash

                td[s1[i]] = i
                i = i + 1


        # This if else clause is for specific condition
        # Take for example , all chars in string are unique
        # then lstr will not be set to anything in above loop.
        # All the hash keys in td are unique. So length of hash is same as
        # longest string with non-repeat chars. This condition is take care in else part
        #
        # Another interesting case is when the longest substr is found at the end of the string
        # In this case, the while loop terminates after inserting a char into td.
        # In this case lstr will contain some non-repeating substr which is not the longest or nothing
        # at all. For this case we will have to see , who is longest here and print the length of
        # longest.

        if len(lstr) >= len(td):
            print "Longest non repeating str is {}".format(lstr)
            print "Position is {} {}".format(f1,f2)
            return len(lstr)
        else:
            print "Longest non repeating str is {}".format(td.keys())
            print "Position is {} {}".format(f1,f2)
            return len(td)


SObj = Solution()
print SObj.nonRepeatingSubStrLen("aab")

#@pytest.mark.parametrize('val,val1',[(0,210), (11,2010), (20,6000)])

def test_solution():

    SObj = Solution()
    nr = {'ac':2,
          'abc':3,
          'abcd':4,
          'abcdeeee':5,
          'abcdeeeee':5,
          'eeeeabcde':5,
          'eeeeeabcde':5,
          'eaeeabeeabcde':5,
          'abcdeeabeee':5,
          }

    for nrs,nrsl in nr.items():
        print "---------------\n"
        print "test str {} ".format(nrs)
        assert SObj.nonRepeatingSubStrLen(nrs) == nrsl
        print "---------------\n"






