class Link:
    empty = ()
    def __init__(self, first, rest=empty):
    # isinstance(a, A): whether "a" is one of instances of A
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'
    def __getitem__(self,i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest) # len(()) -> 0
    @property
    def second(self):
        return self.rest.first
    @second.setter
    def second(self, value):
        self.rest.first = value

def sum_lnk(lnk: Link, g):
    if lnk is Link.empty:
        return 0
    else:
        return g(lnk.first) + sum_lnk(lnk.rest, g)

def main():
    sqr = lambda x: x * x
    dbl = lambda y: 2 * y

    lnk1 = Link(1, Link(2, Link(3, Link(4, Link.empty))))
    print(sum_lnk(lnk1, sqr))  
    print(sum_lnk(lnk1, dbl)) 
    lnk2 = Link(3, Link(5, Link(4, Link(6, Link.empty))))
    print(sum_lnk(lnk2, dbl))  

main()
