"""
    File contains the starting point of the program.
    It manages user input/output processes.
"""
from integration import Integration, Simpsons,\
    CompositeSimpsons, CompositeTrapezoidal
from differentiation import Derivative, Forward,\
    Forward2, Centered, Centered4, Backward, Backward2
from math import pi, cos, sin, tan
import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, lambdify
import csv
from tabulate import tabulate

__all__ = ["Simpsons", "CompositeSimpsons", "CompositeTrapezoidal",
           "Forward", "Forward2", "Centered",
           "Centered4", "Backward", "Backward2",
           "pi", "cos", "sin", "tan"]


def plot(func, v, dx, h, methods):
    """
        Displays the plot of derivatives of the passed methods
    """
    f = lambdify(Symbol('x'), func)
    plt.figure(figsize=(12, 8))
    num = 0
    for method in methods:
        pattern = ['-.', '--', '.', '_', '+', 'o', '>']
        fcn = eval(method)(f, h)
        plt.plot(v, list(map(fcn, v)), pattern[num],
                 label=f'{method} difference approximation')
        num += 1
    plt.plot(v, list(map(dx, v)),
             label='Exact difference approximation')
    plt.legend()
    plt.title(f'Approximations of d/dx({func})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    """
        Starting point

        Reads user input and outputs appropriate information
        
        If user chooses differentiation,
        the program reads the function from the file,
        it finds the exact derivative and plots
        the graphs of the methods specified in the file
        + the exact derivative for comparison

        If user chooses integration,
        the program computes the integral of the function
        in the file using the method in the file for different
        values of N i.e. it splits the interval in different number
        of chunks to improve the approximation
        Finally, it outputs a table with the approximations
        for different values of N and the respective error
        error = exact value - approximation
    """

    while True:
        print("""
            ************* MENU **************

            (1) Differentiate
            (2) Integrate
        """)

        choice = input("Enter your preferance (1/2): ")

        while choice not in ['1', '2']:
            choice = input("Enter a valid option (1/2): ")

        file_name = input("Enter absolute path to file: ")

        try:
            with open(file_name) as file:
                reader = csv.reader(file)
                if choice == '1':
                    for row in reader:
                        v = np.arange(float(eval(row[1])), float(eval(row[2])),
                                      float(row[3]))
                        dx = lambdify(Symbol('x'), Derivative(row[0]).get_exact_value())
                        plot(row[0], v, dx, float(row[3]), row[4].split(':'))
                elif choice == '2':
                    for row in reader:
                        f = lambdify(Symbol('x'), row[0])
                        lower_limit = float(eval(row[1]))
                        upper_limit = float(eval(row[2]))
                        method = eval(row[4])(lower_limit, upper_limit, f)
                        list = []
                        for i in range(1, int(row[3])):
                            approx = method.integrate(2**i)
                            list.append([2**i, approx, 
                            Integration(lower_limit, upper_limit, row[0]).get_error(approx)])
                        print(row[4], '\n')
                        print(tabulate(list, headers=['N', 'Approximation',
                              "Error"], tablefmt='orgtbl'), '\n')
        except FileNotFoundError:
            print(f"File with name {file_name} could not be found.")

        return


if __name__ == '__main__':
    main()
