# Multiple_Equation_Tools
This is a toolkit containing two tools to calculate solutions of multi-variable functions. Both the two tools in this project deal with
equations containing arbitrary number of variables; the difference is that in equation_calculator.py, you are allowed to put in a number
of equations, and you receive the exact value of each variable as long as the number of equations equal to the number of variables, and a
kind reminder is that here the exact value are fractions, rather than float numbers. While in the un_fixed_equations, you are allowed to 
put in one indefinite equation with arbitrary number of variables, and it finally returns you the non-negative integer solutions.

# Here is the clear explainations and guides on how you use the two tools

# equation_calculator.py
In this ducument, all numbers are fractions. The way you express a fraction a/b is to type a respective list [a,b] where a is numerator and
b is denominator. For solving equations, you are encouraged to call function print_results(s) to print the result, s is a list of lists, where 
each list in s is a list of all coefficients of a equation. 
eg.
the original equation is:

	m+2n+p-3q+5r+10=0
	2m+3n+4p+6q+5r-18=0
	m+3n+5p+2q+7r-9=0
	2m+5n-3p-8q+6r-24=0
	4m+2n-3p+5q+10r=0
Be remind that you should make sure that the constant is removed to LHS,leaving RHS to be 0
Then you can type coefficients and constant in each equation; To get the final solutions printed, you can call function print_results():

	>>>s1=[[1,1],[2,1],[1,1],[-3,1],[5,1],[10,1]]
	>>>s2=[[2,1],[3,1],[4,1],[6,1],[5,1],[-18,1]]
	>>>s3=[[1,1],[3,1],[5,1],[2,1],[7,1],[-9,1]]
	>>>s4=[[2,1],[5,1],[-3,1],[-8,1],[6,1],[-24,1]]
	>>>s5=[[4,1],[2,1],[-3,1],[5,1],[10,1],[-32,1]]
	>>>print_result([s1,s2,s3,s4,s5])
	x 1 = -4169 / 156
	x 2 = 2735 / 156
	x 3 = -1711 / 156
	x 4 = 405 / 52
	x 5 = 499 / 156
# un_fixed_equations.py
In this document, you may try calling 2 different functions to deal with 2 different type of indefinite equations.
The first function is unfix_solution_printer(n,c), where n is number of variables and c is the constant in right hand
side of the equation (be reminded that this is different from what you may do in equation_calculator.py). And here all
coefficient of variables are 1
eg. equation: x+y+z=1 

	>>>unfix_soultion_printer(3,1)
	solution 1
	x 1 	 0
	x 2 	 0
	x 3 	 1
	solution 2
	x 1 	 0
	x 2 	 1
	x 3 	 0
	solution 3
	x 1 	 1
	x 2 	 0
	x 3 	 0
Another more powerful function is geunfix_printer(s,c),which allow the variables in equations to be arbitrary non-negative
integer. here s is a list containing all coefficients, while c is the constant in right hand side of the equation.
eg. equation :2x+3y+z=3

	>>>geunfix_printer([2,3,1],3)
	number of solutions: 3
	solution 1
	x 1 	 0
	x 2 	 0
	x 3 	 3
	solution 2
	x 1 	 0
	x 2 	 1
	x 3 	 0
	solution 3
	x 1 	 1
	x 2 	 0
	x 3 	 1
