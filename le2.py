
import pytest

s1='aabichhdefkkkweryoll'
s1='bbbb'





class find_long1(object):

    def __init__(self):
        self.o_index=0
        self.i_index=1
        self.d1=str()
        self.max_size=0

    def find1(self,s1):

        l1=list(s1)

        if (len(s1) == 0 or len(s1)) == 1:
            return len(s1)

        #v=l1[0]
        v=s1[0]
        self.d1 = self.d1+v
        full=len(s1)

        while(self.i_index < full):
            #v1=l1[self.i_index]
            v1=s1[self.i_index]

            if v1 in self.d1:
                if len(self.d1) > self.max_size:
                    self.max_size=len(self.d1)
                self.d1=self.d1.rsplit(v1)[1]
            self.d1 = self.d1+v1

            self.i_index = self.i_index + 1

        if len(self.d1) > self.max_size:
            self.max_size=len(self.d1)

        return self.max_size




@pytest.mark.parametrize("test_input,expected", [
        ("jbpnbwwd", 4),
        ("aabcadef", 6),
        ("", 0),
        ("c", 1),
        ("pwwkew",3),
        ("dvdf", 3),
        ("bbbbb", 1),
        ("bbbbbi", 2),
        ("aaaabca",3),
        ("bbbabca",3),
        ("cccabca",3),
        ("aaaabcb",3),
        ("bbbabcb",3),
        ("cccabcb",3),
        ("aaaabcc",3),
        ("bbbabcc",3),
        ("cccabcc",3),

        ("aaaabcia",4),
        ("bbbabcia",4),
        ("cccabcia",4),
        ("aaaabcib",4),
        ("bbbabcib",4),
        ("cccabcib",4),
        ("aaaabcic",4),
        ("bbbabcic",4),
        ("cccabcic",4),

        ('ahssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssshlkxsjj;;lkdddddddddddddddddddddddddddddddddddddddddddddddddbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456', 68),





        ])

def test_find(test_input,expected):

    obj=find_long1()
    assert obj.find1(test_input) == expected


