import math
import sympy as sym
def f(x):
    function = lambda x: input()
    return function


def bisection(xu, xl):
    iteration = 1
    Condition = True
    if f(xu) * f(xl) >= 0:
        print("error in range")
        exit()
    else:
        while Condition:
            xr = (xu + xl) / 2
            print(' In iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (iteration, xr, f(xr)))
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr

            iteration = iteration + 1
            if iteration > 50:
                break

            Condition = abs(f(xr)) > 0.00001
    print('\n the required root is %0.6f ' % xr)


def falsi(xu,xl):
    iteration = 1
    condition = True
    if f(xu) * f(xl) >= 0:
        print("error in range")
        exit()
    else:
        while condition:
            xr = ((xl*f(xu))-(xu*f(xl)))/(f(xu)-f(xl))
            print('In iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (iteration, xr, f(xr)))
            if f(xr) < 0:
                xl = xr
            else:
                xu = xr
            iteration = iteration + 1
            if iteration > 50:
                break
            condition = abs(f(xr)) > 0.00001

    print('\n the required root is %0.6f ' % xr)
def Newton(x0):

    iteration = 1
    flag = 1
    condition = True
    while condition:
        f1 = sym.diff(f(x0))
        if f1 ==0.0:
            print('Divide by zero error!')
            break
        x1 = x0 - f(x0) / f1
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (iteration, x1, f(x1)))
        x0 = x1
        iteration = iteration + 1

        if iteration > 50:
            flag = 0
            break

        condition = abs(f(x1)) > 0.00001

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


