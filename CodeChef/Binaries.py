# Link (https://www.codewars.com/kata/5d98b6b38b0f6c001a461198)

"""
def code(s):
    return ''.join( f'{"0"*(d.bit_length()-1)}1{d:b}' for d in map(int,s))
    
def decode(s):
    it, n, out = iter(s), 1, []
    for c in it:
        if c=='0':
            n += 1
        else:
            out.append( int(''.join(next(it) for _ in range(n)), 2) )
            n = 1
    return ''.join(map(str, out))

print(decode(code("46")))
"""

