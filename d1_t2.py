
#Coding Tasks Group 2
#Source: Exercises from Coursera's "Coding the Matrix: Linear Algebra through Computer Science Applications"
#course by Dr.Philip Klein
#URL: https://www.coursera.org/course/matrix

#Note: You are allowed to modify only the right hand side
#of those expressions which are marked `None'

#Task 1
#Suppose S is a set of integers {-4, -2, 1, 2, 5, 0}. Write a triple comprehension
#whose value is a list of all three element tuples (i,j,k) such that i,j,k are elements
#of S whose sum is zero

S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k == 0]
#print zero_sum_list

#Task 2
#Modify the above comprehension so that the resulting list does not include (0,0,0)
#Hint: modify the `if' part of the comprehension

excluded_zero_sum_list = [(i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i!=0 or j!=0 or k!=0)]
#print excluded_zero_sum_list

#Task 3
#Use `zip' and list comprehension to solve the following problem.
#Given two lists: for example: [1,2,3,4] and [5,6,7,8], generate
#a new list each element of which is the sum of the corresponding
#elements of the other two lists. For example, in the above case, the
#output would be [6, 8, 10, 12]

List_A = [1,2,3,4]
List_B = [5,6,7,8]
List_Sum =[(a+b) for a,b in zip(List_A,List_B)]

#Task 4
#Here is a sample list-of-dictionaries:
#[{'name':'Kiran', 'mark':85}, {'name':'Alex', 'mark':88}, {'name':'Rahul', 'mark':90}]
#Write a comprehension which will, given a specific key (say 'name'), generate a list
#of the form: ['Kiran', 'Alex', 'Rahul']. 
#If the key is say 'mark', the resulting list will be of the form:
#[85, 88, 90]. 
#Assume that the key used is present in all the dictionaries which are elements of the
#given list.

List_of_dicts = [{'name':'Kiran', 'mark':85},
                 {'name':'Alex', 'mark':88},
                 {'name':'Rahul', 'mark':90}]

key_1 = 'name'

List_of_values = [i[key_1] for i in List_of_dicts]
#print List_of_values

#Task 5
#Similar to the above example, but the key need not be
#present in all the dict's. If the key is not present, 
#a string  'not present' should be returned.
#In the example below, the output should be:
#['Kiran', 'Alex', 'not present']

#Hint. Use the .get method of a dictionary instead of 
#simple indexing. The get method accepts a second parameter
#which is the value to be returned in case the key given 
#as the first parameter is not present in the dictionary.
#You might try help({}.get) in the interactive python prompt
#to get a description of this method.

List_of_dicts_2 = [{'name':'Kiran', 'mark':85},
                 {'name':'Alex', 'mark':88},
                 {'age':19, 'mark':90}]


key_2 = 'name'

List_of_values_2 = [i.get(key_1,"not present") for i in List_of_dicts_2]
#print List_of_values_2


#Please do NOT modify any of the lines below

#--------------------Test Routines-----------------------


def testcase_1():
    r = [(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
    return zero_sum_list == r

def testcase_2():
    r = [(0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
    return excluded_zero_sum_list == r

def testcase_3():
    return List_Sum == [6,8,10,12]

def testcase_4():
    return List_of_values == ['Kiran', 'Alex', 'Rahul']

def testcase_5():
    return List_of_values_2 == ['Kiran', 'Alex', 'not present']
print testcase_1()
print testcase_2()
print testcase_3()
print testcase_4()
print testcase_5()
