# Question 1: Write the minimum possible code necessary to create a class Company.
# I will test this class by writing code such as below:
# company_a = Company()
# company_a.name = "School of Python"
# print(company_a.name)
## Write your code below, 2 lines ##


## End question 1

# Question 2: Write a class Travel which is a subclass of Company (Travel inherits
# from Company). The Travel class should have the following features:
# a) It should have an __init__() method which take a name as argument. 
# b) The default (if no name is provided) for name should be "Generic". So if 
# anyone created a Travel object with no name, it should automatically
# be set to Generic.
## Write your code below, variable lines ##


## End question 2

# Question 3: Add a dunder str method to the Travel class (make sure it's tabbed in). 
# If we print an object of the class whose name is 'Adrenaline Junkies', it will
# print "Company name: Adrenaline Junkies" to the screen. Use the .format() method.
## Write your code below, 2 lines ##


##

# Question 4: Write a repr() method for the Travel class (make sure it's tabbed in), 
# so if we write the following code:
# bever = Travel('bever')
# print(repr(bever))
# 
# The output will be like below:
# Travel('bever')
# Use the .format() method.
## Write your code below, 2 lines


##

# Question 5: Write a set_name() method for the Travel class (make sure it's tabbed in).
# This method accepts a new_name argument as a parameter and sets the name attribute
# of the object to this new_name string. If we wrote the code below:
# bever = Travel('bever')
# print(bever)
# bever.set_name('beverly hills')
# print(bever)
#
# It would result in the following output
# Company name: bever
# Company name: beverly hills
## Write your code below, 2 lines


##