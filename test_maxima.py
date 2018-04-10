import numpy as np
from maxima import find_maxima
x1 = [0, 1, 2, 1, 2, 1, 0]
x2 = [-i**2 for i in range(-3, 4)]
x3 = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
x4 = [4, 2, 1, 3, 1]

def test_maxima():
    test1=find_maxima(x1)
    if test1==[2,4]:
        print("test_1 passed")
    else:
        print("test_1 failed")

    test2=find_maxima(x2)
    if test2==[3]:
        print("test_2 passed")
    else:
        print("test_2 failed")

    test3=find_maxima(x3)
    if test3==[16,78]:
        print("test_3 passed")
    else:
        print("test_3 failed")

    test4=find_maxima(x4)
    if test4==[0]:
        print("test_4 passed")
    else:
        print("test_4 failed")

test_maxima()
