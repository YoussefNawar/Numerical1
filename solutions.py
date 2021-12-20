import math
from math import sin, cos, tan, log, exp
from sympy import var
from sympy import symbols
import timeit
from sympy import sympify
import sympy as sy
from sympy.utilities.lambdify import lambdify

import sympy as sym


def f(equation, value):
    equation = equation.replace('ln', 'log')

    equation = equation.replace('e', 'math.e')
    equation = equation.replace('^', '**')
    x = value
    return eval(equation)


def g(equation, value):
    equation = equation.replace('ln', 'log')
    equation = equation.replace('^', '**')
    equation = equation.replace('e', 'math.e')
    x = value
    return eval(equation)

def differentiation(equation, value):
    equation = equation.replace('ln', 'sy.log')
    equation = equation.replace('sin', 'sy.sin')
    equation = equation.replace('cos', 'sy.cos')
    equation = equation.replace('tan', 'sy.tan')
    equation = equation.replace('exp', 'sy.exp')
    equation = equation.replace('^', '**')
    x = symbols('x')
    differ = eval(equation).diff(x)
    return differ.evalf(subs={x: value})


def bisection(equation, xu, xl, epsilon=0.00001, max_iterations=50):
    t1 = timeit.default_timer()


    if f(equation, xu) * f(equation, xl) >= 0:
        output = ("error in range")
        stringnothing = ("")
        return output,stringnothing
    else:
        xr = (xu + xl) / 2
        approximate_error = 0
        iterationlist = []
        iterationlist.append('%d \t xl = %.16f \t xu = %.15f\t\t xr = %.15f\t\t f(xr) =  %.15f\t\t\t\t-\n' % (0, xl, xu, xr, f(equation, xr)))

        for i in range(1, max_iterations + 1):

            # iterationlist.append("%d, xr = %.16f, f(xr) = %.16f and the precision = .%16f " %(i,xr,f(equation,xr),approximate_error))
            if f(equation, xr) * f(equation, xl) < 0:
                xu = xr
            elif f(equation, xr) * f(equation, xl) > 0:
                xl = xr
            prev = xr
            xr = (xu + xl) / 2
            try:
                approximate_error = abs((xr - prev) / xr) * 100
            except ZeroDivisionError:
                print("zero division error")
                break
            iterationlist.append("%d, xr = %.16f, f(xr) = %.16f and the precision = .%16f " % (
                i, xr, f(equation, xr), approximate_error))

            if approximate_error < epsilon:
                break
    t2 = timeit.default_timer()
    iterationss = ""
    for iteration in iterationlist:
        print(iteration)
        iterationss += iteration + '\n'
    answer = "Root = ", xr, "Precision: ", approximate_error, "\nnumber of iterations = ", iteration, "\nRuntime: ",(t2 - t1)
    print(answer)
    return iterationss,answer


bisection('x^2 + 4',4,3)


def falsi(equation, xu, xl, epsilon=0.00001, max_iterations=50):
    t1 = timeit.default_timer()
    approximate_error = 0

    if f(equation, xu) * f(equation, xl) >= 0:
        print("error in range")
        exit()
    else:
        xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))
        iterationlist = []
        iterationlist.append('%d \t xl = %.16f \t xu = %.15f\t\t xr = %.15f\t\t f(xr) =  %.15f\t\t\t\t-\n' % (
        0, xl, xu, xr, f(equation, xr)))
        if f(equation, xr) == 0:
            print("xr = %d" % (xr))
            exit()
        for i in range(1, max_iterations):

            if f(equation, xr) < 0:
                xl = xr
            elif f(equation, xr) > 0:
                xu = xr
            prev = xr
            xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))
            try:
                approximate_error = abs((xr - prev) / xr) * 100
            except ZeroDivisionError:
                print("zero division error")
                break
            iterationlist.append("%d, xr = %.16f, f(xr) = %.16f and the precision = .%16f " % (
                i, xr, f(equation, xr), approximate_error))

            if approximate_error < epsilon:
                break

    t2 = timeit.default_timer()
    iterationss = ""
    for iteration in iterationlist:
        print(iteration)
        iterationss += iteration + '\n'
    answer = "Root = ", xr, "Precision: ", approximate_error, "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1)
    return iterationss, answer


#falsi("x**3-5*x-9",3,2)

def Newton(equation, x0, epsilon=0.00001, max_iterations=50):
    t1 = timeit.default_timer()


    x = x0
    approximate_error = 0
    iterationlist = []
    iterationlist.append('%d \t xi = %.16f \t\t\t f(xi) =  %.15f\t\t\t\t-\n' % (
    0, x,  f(equation, x)))
    for i in range(1, max_iterations):
        prev = x

        try:
            x = x - (f(equation, x) / differentiation(equation, x))
        except ZeroDivisionError:
            print("Division by zero error")
            break

        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
                i, x, f(equation, x), approximate_error))
        approximate_error = approximate_error = abs((x - prev) / x) * 100
        if approximate_error < epsilon:
            break
    t2 = timeit.default_timer()
    iterationss = ""
    for iteration in iterationlist:
        print(iteration)
        iterationss += iteration + '\n'
    answer = "Root = ", x, "Precision: ", approximate_error, "\n # of iterations = ", iteration, "\nRuntime: ", (
                t2 - t1)
    print(answer)
    return iterationss, answer

#Newton("x**3 - 5*x - 9",2)
def fixed(equation1, equation2, x0, epsilon=0.00001, max_iterations=50):
    t1 = timeit.default_timer()

    x = x0

    iterationlist = []
    iterationlist.append('%d \t xi = %.16f \t\t\t f(xi) =  %.15f\t\t\t\t-\n' % (
        0, x, f(equation1, x)))
    for i in range(1, max_iterations):

        prev = x
        x = g(equation2, x)
        approximate_error = abs((x - prev) / x) * 100
        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
                i, x, f(equation1, x), approximate_error))

        if approximate_error < epsilon:
            break
    t2 = timeit.default_timer()
    iterationss = ""
    for iteration in iterationlist:
        print(iteration)
        iterationss += iteration + '\n'
    answer = "Root = ", x, "Precision: ", approximate_error, "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1)
    print(answer)
    return iterationss, float(answer)

#fixed("x*x*x + x*x -1","1/((x+1)**0.5)",2)

def secant(equation, x0, x1, epsilon=0.00001, max_iterations=50):
    t1 = timeit.default_timer()


    iterationlist = []
    iterationlist.append('%d \t x0 = %.16f \t x1 = %.15f' % (
        0, x0, x1))

    for i in range(1, max_iterations):

        x2 = x0 - (x1 - x0) * f(equation, x0) / (f(equation, x1) - f(equation, x0))
        approximate_error = abs(f(equation, x2))*100
        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
                i, x2, f(equation, x2), approximate_error))
        x0 = x1
        x1 = x2

        if approximate_error < epsilon:
            break
    t2 = timeit.default_timer()
    iterationss = ""
    for iteration in iterationlist:
        print(iteration)
        iterationss += iteration + '\n'
    answer = "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1)
    print(answer)
    return iterationss, answer

#secant("x**3 - 5*x - 9",2,3)
