import math
import Vectors as ve

def rod(v, k, theta):
    '''use the function from Vectors to calculate the result'''
    cos = math.cos(theta/180*math.pi)
    sin = math.sin(theta/180*math.pi)

    a = [i * cos for i in v]
    b = [i * sin for i in ve.cross(k, v)]
    c = [i * ve.dot(k, v) * (1 - cos) for i in k]
    v_rot = ve.add(ve.add(a, b), c)
    return v_rot

if __name__ == '__main__':
    import sys
    terms = [float(x) for x in sys.argv[1:]]
    v = terms[0:3]
    k = terms[3:6]
    theta = terms[6]
    print(rod(v, k, theta))

else:
    print('Not run directly')
