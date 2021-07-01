# Question 1: Write a lambda expression which takes an argument x as a parameter and simply returns x.
# Assign this expression to a variable named my_lambda_func.
## Write your code below, 1 line
my_lambda_func = lambda x: x 
## End question 1

# Question 2: Print the type of my_lambda_func. Hint: did you accidentally call the function?
## Write your code below, 1 line
# R: No
print(type(my_lambda_func))
## End question 2

# Question 3: Write a lambda expression which returns the cosine of an argument x and assign it
# to a variable named my_cos. Hint: math module
## Write your code below, 2 lines
import math
my_cos = lambda x: math.cos(x)
## End question 3

# Question 4: Write a lambda expression which models this equation f(x) = x^3 + 3x^2 + 200.
# Asssign it to a variable my_eq1
## Write your code below, 1 line
my_eq1 = lambda x: x**3 + 3*x**2 + 200
print(my_eq1(2))
## End question 4

# Question 5: Write a lambda expression which models this equation f(x,y,z) = x^3 + 3y^2 + z
# where z is optional. If no value for z is provided use the default value of 100.
# Assign this expression to a variable my_eq2
## Write your code below, 1 line
my_eq = lambda x, y, z=100: x**3 + 3*y**2 + z
## End question 5
