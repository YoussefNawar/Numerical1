from math import sin, cos, tan, log, exp
from sympy import var
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
    x = var('x')
    expr = sympify(equation)
    res = expr.subs(x, value)
    return res

def differentiation(equation,value):
    equation = equation.replace('ln', 'sym.log')
    equation = equation.replace('sin', 'sym.sin')
    equation = equation.replace('cos', 'sym.cos')
    equation = equation.replace('tan', 'sym.tan')
    equation = equation.replace('exp', 'sym.exp')
    equation = equation.replace('^', '**')
    x = symbols('x')
    differ = eval(equation).diff(x)
    return differ.evalf(subs={x: value})
def bisection(equation,xu,xl):
    max_iterations = 50
    epsilon = 0.0001

    if f(equation,xu) * f(equation,xl) >= 0:
        print("error in range")
        exit()
    else:
        xr = (xu + xl)/2
        iterations = 1

        for i in range(1, max_iterations):
            if f(equation, xr) * f(equation, xl) < 0:
                xu = xr
            elif f(equation, xr) * f(equation, xl) > 0:
                xl = xr
            prev = xr
            xr = (xl + xu) / 2
            approximate_error = abs((xr - prev) / xr)
            iterations = iterations + 1
            if approximate_error < epsilon:
                break
    output = 'xr = : ' + str(xr) + ' , number of iterations = ' + str(iterations)
    return (output)




def falsi(equation,xu,xl):

    max_iterations = 50
    epsilon = 0.0001

    if f(equation,xu) * f(equation,xl) >= 0:
        print("error in range")
        exit()
    else:
        iteration = 1
        xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))
        for i in range(1, max_iterations):



            if f(equation,xr) < 0:
                xl = xr
            elif  f(equation,xr) > 0:
                xu = xr
            iteration = iteration + 1
            prev = xr
            xr = ((xl * f(equation, xu)) - (xu * f(equation, xl))) / (f(equation, xu) - f(equation, xl))
            approximate_error = abs((xr - prev) / xr)
            if approximate_error < epsilon:
                break
            else:
                break
    output = 'xr = : ' + str(xr) + ' , number of iterations = ' + str(iteration)
    return output

def Newton(equation,x0):
    iterations = 0
    max_iteration = 50
    epsilon = 0.0001
    x = x0

    for i in range(max_iteration):
        iterations += 1
        fx = f(equation,x)

        xn = x
        x = x - (fx / differentiation(equation,x))
        ea = abs((x - xn) / x)

        if ea < epsilon:
            break
    output = 'root = : ' + str(x) + ' , number of iterations = ' + str(iterations)
    return output

def fixed(equation1,equation2,x0):
    max_iteration = 50
    epsilon = 0.00001
    x = x0
    iterations = 0
    for i in range(max_iteration):
        iterations = iterations + 1
        xf = x
        x = g(equation2,x)
        ea = abs((x - xf) / x)
        if ea < epsilon:
            break
    output = 'root = : ' + str(x) + ' , number of iterations = ' + str(iterations)
    return output
def secant(equation,x0,x1):
    max_iteration = 50
    epsilon = 0.00001
    iteration = 0
    for i in range (max_iteration):
        iteration = iteration + 1
        x2 = x0 - (x1 - x0) * f(equation,x0) / (f(equation,x1) - f(equation,x0))
        x0 = x1
        x1 = x2
        ea = abs((x2-x0)/x2)
        if ea < epsilon:
            break
    output = 'root = : ' + str(x2) + ' , number of iterations = ' + str(iteration)
    return output



