
#Coding Tasks Group 1
#Source: Exercises from Coursera's "Coding the Matrix: Linear Algebra through Computer Science Applications"
#course by Dr.Philip Klein
#URL: https://www.coursera.org/course/matrix

#Note: You are allowed to modify only the right hand side
#of those expressions which are marked `None'

#Task 1
#Assign 10 to variable `base'
#Assign set {0,1,2,3,4,5,6,7,8,9} to variable `digits'
#Now, write an expression which will generate a set of ALL two digit 
#numbers belonging to `base'.
#For example, for the above values of base and digits, you should get
#the set {0,1,2,3,4,5,6,7,8,9,10,11,12......99}
#If base = 2 and digits = {0,1}, you should get: {0,1,2,3}
#Your expression should work for any value of base and digits

#Hint1: If `a' and `b' are two digits belonging to `base', how
#do you compute the value of the number formed by `a' as the first
#digit and `b' as the second digit?

#Hint2: You can use a double comprehension.

base = 10
digits = {0,1,2,3,4,5,6,7,8,9}
all_two_digit_numbers = {(a*base + b) for a in digits for b in digits}
#print all_two_digit_numbers
#Task 2
#Write a set comprehension which will generate the intersection
#of two sets without using the intersection operator, &. 

#Hint: use a set comprehension with a test to select only those
#elements of the first set which are there in the second set also.

S = {1,2,3,4}
T = {3,4,5,6}
S_intersect_T = {u for u in S for v in T if u == v}
#print S_intersect_T

#Task 3 (very easy!)
#Write an expression which will generate average of the list: [10, 20, 5, 6]
l = [10,20,5,6]
sum_list = 0
for i in l:
    sum_list += i
L_average = float(float(sum_list) / float(len(l)))
#print L_average 

#Task 4
#Write an expression which will compute sum of elements of a list of lists
#Hint: use a list comprehension and two invocations of `sum'

LofL = [[1,2,3], [4], [5,6,7]]
LofL_sum = sum([sum(i) for i in LofL])
#print LofL_sum


#Task 5
#Write a list comprehension which will extract the first element of a list of
#two element tuples.
#For example, say your list of tuples is: [(1,2), (3,4), (5,6), (7,8)]
#The output list should be [1, 3, 5, 7]
#You MUST use tuple-unpacking in the comprehension

List_of_two_tuples = [(1,2),(3,4),(5,6),(7,8)]
list_of_first_elements = [a for (a,b) in List_of_two_tuples]
#print list_of_first_elements


#Please do NOT modify any of the lines below

#--------------------Test Routines-----------------------

def testcase_1():
    return all_two_digit_numbers == set(range(100))

def testcase_2():
    return S_intersect_T == {3,4}

def testcase_3():
    return L_average == 10.25

def testcase_4():
    return LofL_sum == 28

def testcase_5():
    return list_of_first_elements == [1,3,5,7]
print testcase_1()
print testcase_2()
print testcase_3()
print testcase_4()
print testcase_5()
