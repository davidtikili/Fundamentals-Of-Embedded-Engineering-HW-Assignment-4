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


def prnt_lnk(s):
    output = "<"
    for i in range(len(s)):
        if i == (len(s) - 1):
            output += f"{s[i]}"
        else:
            output += f"{s[i]} "

    output += ">"
    return output
   

def main():
    print(prnt_lnk(Link(1, Link(2, Link(3, Link(4))))))

main()