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

def insrt(l: Link, elm, ind):
   
    if ind == 0:
        return Link(elm, l)
    elif l is Link.empty:
        return Link(elm, Link.empty)
    else:
        return Link(l.first, insrt(l.rest, elm, ind - 1))

def main():
    l = Link(11, Link(12, Link(13, Link.empty)))
    n = insrt(l, 2021, 1)
    print(n)  

    m = insrt(n, 2022, 20)
    print(m)
main()
