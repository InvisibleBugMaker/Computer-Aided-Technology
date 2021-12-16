def add(v,u):
    '''addition,copy from HW5'''
    v = list(v)
    u = list(u)
    for i in range(len(v)):
        v[i] = v[i] + u[i]
    return v

def norm(v):
    '''normal,copy from HW5'''
    length = 0
    for i in range(len(v)):
        length += v[i]**2
    norm = tuple(i/length**0.5 for i in v)
    return norm

def cross(v,u):
    '''cross, copy from HW5'''
    a = v[1]*u[2]-v[2]*u[1]
    b = v[0]*u[2]-v[2]*u[0]
    c = v[0]*u[1]-v[1]*u[0]
    cross = (a,b,c)
    return cross

def invert(v):
    '''invert,copy from HW5'''
    invert = [i*-1 for i in v]
    return invert

def dot(v,u):
    '''dot product,copy from HW5'''
    dot_product = 0
    for i in range(len(v)):
        dot_product += v[i]*u[i]
    return dot_product


if __name__ == '__main__':
    import sys
    terms = [float(x) for x in sys.argv[2:]]
    a = terms[0:3]
    b = terms[3:6]
    if sys.argv[1] == 'dot':
        print(tuple(dot(a,b)))
    if sys.argv[1] == 'add':
        print(tuple(add(a,b)))
    if sys.argv[1] == 'norm':
        print(tuple(norm(a)))
    if sys.argv[1] == 'cross':
        print(tuple(cross(a,b)))
    if sys.argv[1] == 'invert':
        print(tuple(invert(a)))