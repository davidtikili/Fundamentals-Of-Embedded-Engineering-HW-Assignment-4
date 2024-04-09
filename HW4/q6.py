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

def change(lnk: Link, u, v):
    
    if lnk is Link.empty:
        return lnk
    elif lnk.first == u:
        return Link(v, change(lnk.rest, u, v))
    else:
        return Link(lnk.first, change(lnk.rest, u, v))

def main():
    l = Link(1, Link(2, Link(3, Link.empty)))
    n = change(l, 3, 1)
    print(n)  

    m = change(n, 1, 2)
    print(m)  

    result = change(m, 5, 1)
    print(result)  

main()
