import math
from math import sin, cos, tan, log, exp
from sympy import var
import timeit
from sympy import sympify
from sympy.utilities.lambdify import lambdify
from sympy import symbols
import sympy as sym
def f(equation,value):
    equation = equation.replace('ln', 'sym.log')
    equation = equation.replace('sin', 'sym.sin')
    equation = equation.replace('cos', 'sym.cos')
    equation = equation.replace('tan', 'sym.tan')
    equation = equation.replace('exp', 'sym.exp')
    equation = equation.replace('^', '**')
    x = var('x')
    expr = sympify(equation)
    res = expr.subs(x, value)
    return res
def g(equation,value):
    equation = equation.replace('ln', 'sym.log')
    equation = equation.replace('sin', 'sym.sin')
    equation = equation.replace('cos', 'sym.cos')
    equation = equation.replace('tan', 'sym.tan')
    equation = equation.replace('exp', 'sym.exp')
    equation = equation.replace('^', '**')
    equation = equation.replace('exp', '2.7182818284590452353602874713527')
    x = var('x')
    expr = sympify(equation)
    res = expr.subs(x, value)
    return res

def differentiation(equation,value):
    #equation = equation.replace('ln', 'sym.log')
    equation = equation.replace('sin', 'sym.sin')
    equation = equation.replace('cos', 'sym.cos')
    equation = equation.replace('tan', 'sym.tan')
    equation = equation.replace('exp', 'sym.exp')
    equation = equation.replace('^', '**')
    x = symbols('x')
    differ = eval(equation).diff(x)
    return differ.evalf(subs={x: value})
def bisection(equation,xu,xl):
    t1 = timeit.default_timer()
    max_iterations = 50
    epsilon = 0.0001


    if f(equation,xu) * f(equation,xl) >= 0:
        print("error in range")
        return
    else:
        xr = (xu + xl)/2
        iteration = 0
        approximate_error = 0
        iterationlist = []
        for i in range(1, max_iterations):
            iteration = iteration + 1

            iterationlist.append("iteration number %d, xr = %.16f, f(xr) = %.16f and the precision = .%16f " %(iteration,xr,f(equation,xr),approximate_error))
            if f(equation, xr) * f(equation, xl) < 0:
                xu = xr
            elif f(equation, xr) * f(equation, xl) > 0:
                xl = xr
            prev = xr
            xr = (xl + xu) / 2
            approximate_error = abs((xr - prev) / xr)


            if approximate_error < epsilon:
                break
    t2 = timeit.default_timer()
    for iteration in iterationlist:
        print(iteration)
    print("Root = ", xr, "Precision: ", approximate_error, "\nnumber of iterations = ", iteration, "\nRuntime: ", (t2 - t1))
    return xr, approximate_error, iteration, iterationlist, (t2 - t1)





def falsi(equation,xu,xl):
    t1 = timeit.default_timer()
    max_iterations = 50
    epsilon = 0.00001
    approximate_error = 0
    prev = 0
    if f(equation,xu) * f(equation,xl) >= 0:
        print("error in range")
        exit()
    else:
        iteration = 0
        xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))
        iterationlist = []
        if f(equation,xr) == 0:
            print("xr = %d"%(xr))
            exit()
        for i in range(1,max_iterations):
            iteration += 1

            approximate_error = abs((xr - prev) / xr)

            if approximate_error < epsilon or f(equation,xr) == 0:
                break
            prev = xr
            if f(equation,xr) < 0:
                xl = xr
            elif  f(equation,xr) > 0:
                xu = xr

            iterationlist.append(
                "Iteration number %d, xr = %.16f, f(xr) = %.16f and precision: %.16f " % (iteration, xr, f(equation,xr),approximate_error))


            xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))




    t2 =  timeit.default_timer()
    for iteration in iterationlist:
        print(iteration)
    print("Root = ", xr, "Precision: ", approximate_error, "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1))
    return xr, approximate_error, iteration, iterationlist, (t2 - t1)


def Newton(equation,x0):
    t1 = timeit.default_timer()
    iterations = 0
    max_iteration = 50
    epsilon = 0.00001
    x = x0
    approximate_error = 0
    iterationlist = []

    for i in range(max_iteration):
        iterations += 1
        fx = f(equation,x)
        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
            iterations, x, f(equation, x), approximate_error))
        xn = x
        x = x - (fx / differentiation(equation,x))
        approximate_error = abs((x - xn) / x)

        if approximate_error < epsilon:
            break
    t2 = timeit.default_timer()
    for iteration in iterationlist:
        print(iteration)
    print("Root = ", x, "Precision: ", approximate_error, "\n# of iterations = ", iterations, "\nRuntime: ", (t2 - t1))
    return x, approximate_error, iterations, iterationlist, (t2 - t1)

def fixed(equation1,equation2,x0):
    t1 = timeit.default_timer()
    max_iteration = 50
    epsilon = 0.00001
    x = x0
    iterations = 0
    iterationlist = []
    ea = 0
    for i in range(max_iteration):
        iterations = iterations + 1
        xf = x
        x = g(equation2,x)
        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
                iterations, x, f(equation1, x), ea))
        ea = abs((x - xf) / x)
        if ea < epsilon:
            break
    t2 = timeit.default_timer()
    for iteration in iterationlist:
        print(iteration)
    print("Root = ", x, "Precision: ", ea, "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1))
    return x, ea, iteration, iterationlist, (t2 - t1)
#fixed("x*x*x + x*x -1","1/((x+1)**0.5)",2)

def secant(equation,x0,x1):
    t1 = timeit.default_timer()
    max_iteration = 50
    epsilon = 0.00001
    iteration = 0
    iterationlist = []
    ea = 0

    for i in range (max_iteration):
        iteration = iteration + 1
        x2 = x0 - ((x1 - x0) * f(equation,x0) / (f(equation,x1) - f(equation,x0)))
        iterationlist.append(
            "Iteration #%d, x = %.16f, f(x) = %.16f and precision: %.16f " % (
                iteration, x2, f(equation, x2), ea))
        x0 = x1
        x1 = x2

        ea = abs((x2-x0)/x2)
        if ea < epsilon:
            break
    t2 = timeit.default_timer()
    for iteration in iterationlist:
        print(iteration)
    print( "\n# of iterations = ", iteration, "\nRuntime: ", (t2 - t1))
    return x2, ea, iteration, iterationlist, (t2 - t1)





