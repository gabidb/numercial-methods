from integration import *
from differentiation import *
from math import *
def f(x): return x**2
def main():
    i = Simpsons(1,5)
    v = CompositeSimpsons(1,4,100)
    #v.integrate(f)
    #u = v.integrate(f)
    #print(u)
    s = "Centered4"
    d = eval(s)(f, 0.25)
    print(d(0.5))
    # t = Trapezoidal(0,1,4)
    # print(t.integrate(f))
    return

if __name__ == '__main__':
    main()
