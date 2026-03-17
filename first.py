# # print("Hello World")
# # print(23+19,12)
# # name = "Bob"
# # age = 31
# # print(name, "is", age, "years old.")
# # print("Next year,", name, "will be", age + 1, "years old.")
# # print("The sum of 15 and 27 is", 15 + 27)
# # print("Goodbye!")
# # print(type(name))
# # print(type(age))
# # print("Is age greater than 25?", age > 25)
# # print("Is name equal to 'Bob'?", name == "Bob")
# # print("What is 10 multiplied by 5?", 10 * 5)
# # print("What is 100 divided by 4?", 100 / 4)
# # print("What is 7 minus 3?", 7 - 3)
# # print("What is 8 plus 12?", 8 + 12)
# # print("Is age less than or equal to 30?", age <= 30)
# # print("Is name not equal to 'Alice'?", name != "Alice")
# # print("What is 2 to the power of 3?", 2 ** 3)
# # print("What is the remainder of 10 divided by 3?", 10 % 3)
# # print("What is the integer division of 20 by 6?", 20 // 6)
# # print(name, "has been learning Python for", age - 20, "years.")
# # a=5
# # b=10
# # sum=a+b
# # print("The value of a is", a)
# # print("The value of b is", b)
# # print("The sum of a and b is", sum)
# # x="2"
# # y=3
# # txt="@" 
# # print(2*txt*3)
# # print((x+txt)*y)
# # c=10
# # d=5.0
# # print(c*d)
# # e=5
# # f=-2
# # print(e%f)
# # print(e/f)
# # print(e//f)
# # name=input("Enter your name: ")
# # print("Hello,", name)  
# # age=int(input("Enter your age: ")) 
# # print("Next year you will be", age + 1, "years old.")
# # price=float(input("Enter the price of the item: "))
# # quantity=int(input("Enter the quantity: "))
# # total=price*quantity
# # print("The total cost is:", total)
# # light = input("light:")
# # if light == "green":
# #     print("Go") 
# # elif light == "yellow":
# #     print("Slow down")
# # elif light == "red":
# #     print("Stop")
# # else:
# #     print("light is broken")

# # marks = int(input("Enter your marks: "))
# # if marks >= 90:
# #     print("Grade: A")
# # elif marks >= 80:
# #     print("Grade: B")
# # elif marks >= 70:
# #     print("Grade: C")
# # elif marks >= 60:
# #     print("Grade: D")
# # else:
# #     print("Grade: F")

# # A = int (input ("A : "))
# # G = input("M/F : ")
# # if ( A == 1 or A == 2) and G == "M":
# #     print("fee is 100")
# # elif(A == 3 or A == 4 or G == "F"):
# #     print("fee is 200")
# # elif(A == 5 and G == "M"):
# #     print("fee is 300")
# # else:
# #     print("no fee")

# # food= input("Enter a food item: ")
# # eat="yes" if food == "pizza" else "no"
# # print(eat)

# # num1=20
# # num2=30
# # print(( num1 == num2) or (num1 < num2))

# #sum of two numbers
# # num1=int(input("num1:"))
# # num2=int(input("num2:"))
# # sum=num1+num2
# # print("The sum is:", sum)


# #side of square
# # side=int(input("side:"))
# # area=side*side
# # print("area:", area)

# #float number and print there avarage
# # num1=float(input("num1:"))
# # num2=float(input("num2:"))
# # avarage=(num1+num2)/2
# # print("avarage:", avarage)

# #comapre 2 int numbers
# # a=int(input("a:"))
# # b=int(input("b:"))
# # print(a>=b)
# # if a>=b:
# #     print("true")

# # else:
# #     print("false")



# # slicing in python
# # string="DeepBadrakiya"
# # print(string[4:6])


# #input users first name and print its length

# # first_name=input("first name:")
# # length=len(first_name)
# # print("length:", length)


# # #count $ in string

# # str="$$$I am $$ learning $$$ Python$$$"
# # count=str.count("$")
# # print("count of $ is:", count)

# # # chake the entered number is even or odd


# # num=int(input("num:"))
# # if num%2==0:
# #     print("even")
# # else:
# #     print("odd")


# # #find the gratest of 3 numbers input by user
# # num1=int(input("num1:"))
# # num2=int(input("num2:"))
# # num3=int(input("num3:"))    
# # if num1>=num2 and num1>=num3:
# #     print("gratest is num1:", num1)
# # elif num2>=num1 and num2>=num3:
# #     print("gratest is num2:", num2)
# # else:       
# #     print("gratest is num3:", num3)  


# # chake the input number is multiple by 7 or not 

# # x=int(input("input num:"))
# # if x%7==0:
# #     print(" ",x,"is multiple of 7")
# # else:   
# #      print("",x,"is not multiple of 7") 


# #list of 5 numbers and print it 


# # numbers=[10,20,30,40,50]
# # print(numbers)  
# # print(numbers[0])  
# # print(numbers[1])  
# # print(type(numbers) )
# # numbers[0] = 15
# # print(numbers)
# # print(numbers[0:3])
# # print(numbers[-3 : ])


# #List methods
# # append() method is used to add an element to the end of a list. It modifies the original list by adding the new element at the end.

# # numbers=[30,40,10,50,20]
# # numbers.append(60)
# # print(numbers)

# # # sort() method is used to sort the elements of a list in ascending order. It modifies the original list by rearranging the elements in sorted order.

# # numbers=[30,40,10,50,20]
# # numbers.sort()
# # print(numbers)

# # #sort reverse() method is used to sort the elements of a list in descending order. It modifies the original list by rearranging the elements in reverse sorted order.

# # numbers=[30,40,10,50,20]
# # numbers.sort(reverse=True)
# # print(numbers)

# # # reverse() method is used to reverse the order of elements in a list. It modifies the original list by reversing the order of the elements.

# # numbers=[30,40,10,50,20]
# # numbers.reverse()
# # print(numbers)

# # #insert() method is used to insert an element at a specific index in a list. It modifies the original list by adding the new element at the specified index and shifting the existing elements to the right.

# # numbers=[30,40,10,50,20]
# # numbers.insert(2, 25)  # Insert 25 at index 2
# # print(numbers)

# # #remove() method is used to remove the first occurrence of a specified element from a list. It modifies the original list by removing the specified element.

# # numbers=[30,40,10,50,20]
# # numbers.remove(10)  # Remove the first occurrence of 10
# # print(numbers)

# # #pop() method is used to remove and return an element from a list at a specified index. If no index is provided, it removes and returns the last element of the list. It modifies the original list by removing the specified element.

# # numbers=[30,40,10,50,20]
# # removed_element = numbers.pop(2)  # Remove and return the element at index 2
# # print("Removed element:", removed_element)
# # print(numbers)


# #tuple is unmutable data type in python which means we cannot change the values of tuple once it is created.
# #It is defined using parentheses () and can contain elements of different data types.

# # tuple = (10, 20, 30, "Hello", 3.14)
# # print(tuple)
# # print(tuple[0])
# # print(tuple[3])
# # print(type(tuple))

# # #tuple[0] = 15  # This will raise a TypeError because tuples are immutable

# # #slicing in tuple

# # print(tuple[1:4])  # Output: (20, 30, 'Hello')
# # print(tuple[-3:])   # Output: (30, 'Hello', 3.14)       

# # #tuple methods
# # # count() method is used to count the number of occurrences of a specified element in a tuple. It returns the count as an integer.          

# # tuple = (10, 20, 30, "Hello", 3.14, 20)
# # count_20 = tuple.count(20)
# # print("Count of 20 in the tuple:", count_20)    

# # # index() method is used to find the index of the first occurrence of a specified element in a tuple. It returns the index as an integer. If the element is not found, it raises a ValueError.
# # tuple = (10, 20, 30, "Hello", 3.14, 20)
# # index_hello = tuple.index("Hello")
# # print("Index of 'Hello' in the tuple:", index_hello)    

# # #WAP to ask user to insert there 3 favorite movies name & store them in a list.

# # movies = []
# # mov1= input("Enter your first favorite movie:1. ")
# # mov2= input("Enter your second favorite movie:2. ")
# # mov3= input("Enter your third favorite movie:3. ")
# # movies.append(mov1)
# # movies.append(mov2)
# # movies.append(mov3)
# # print(movies)

# #other way to do this

# # movies = []
# # movies.append(input("Enter your 1st favorite movie:"))
# # movies.append(input("Enter your 2nd favorite movie:"))        
# # movies.append(input("Enter your 3rd favorite movie:")) 

# # print(movies)

# #WAP to chake the given list is palindrome elements or not.

# list1 = [1, 2, 3, 2, 1]
# copy_list1= list1.copy()
# copy_list1.reverse()

# if list1 == copy_list1:
#     print("list1 is palindrome")
# else:
#     print("list1 is not palindrome")

# list2 = [1,"abc","abc",1]
# copy_list2= list2.copy()
# copy_list2.reverse()
# if list2 == copy_list2:
#     print("list2 is palindrome")
# else:
#     print("list2 is not palindrome")    


# list3 = [1, 2, 3, 4, 2, 1]
# copy_list3= list3.copy()
# copy_list3.reverse()
# if list3 == copy_list3:
#     print("list3 is palindrome")
# else:
#     print("list3 is not palindrome")    


# WAP to count the numbers of students with "A" from the following tuple.

# students_grades = ("A", "B", "C", "A", "D", "A", "B")
# count_A = students_grades.count("A")
# print("Number of students with grade 'A':", count_A)


# #store the above values in a list and and sort them in "A" to "D" .
# list=list(students_grades)
# list.sort()
# print("Sorted list of student grades:", list)


# dictinary in python is a collection of key-value pairs. It is defined using curly braces {} and each key is separated from its value by a colon (:). The keys in a dictionary must be unique and immutable, while the values can be of any data type.
#dictinary
#dictinary is unorderd, mutable and can't have duplicate keys in dictinary


# example of dictinary
# student = {                 #this is a dictinary which contains key-value pairs
#     "name": "Deep",           #key is "name" and value is "Deep"
#     "age": 20,                   #key is "age" and value is 20   
#     "city": "Vadodara",         #key is "city" and value is "Vadodara"
#     "is_student": True          #key is "is_student" and value is True
# }



# dictinary = {
#     "name": "Deep",
#     "age": 20,
#     "city": "Vadodara",
#     "is_student": True
# }

# print(dictinary)
# print(dictinary["name"])
# print(dictinary["age"])
# print(dictinary["city"])
# print(dictinary["is_student"])

# dictinary["age"] = 21  # can change the value of existing key in dictinary
# print(dictinary)
# dictinary["country"] = "India" # can add new key-value pair to dictinary
# print(dictinary)
# del dictinary["is_student"]  # can remove key-value pair from dictinary
# print(dictinary)

# #nested dictinary 
# # A nested dictionary is a dictionary that contains another dictionary as a value. 

# from os import name


# student = {
#     "name": "Deep",
#     "age": 20,
#     "grades": {
#         "math": "A",
#         "science": "B",
#         "english": "A"
#     }
# }

# print(student)
# print(student["name"])
# print(student["age"])
# print(student["grades"])    
# print(student["grades"]["math"])
# print(student["grades"]["science"])
# print(student["grades"]["english"]) 
# print(type(student))
# print(type(student["grades"]))  
# print(type(student["grades"]["math"]))


# #dictinary methods
# # keys() method is used to return a view object that displays a list of all the keys in a dictionary. The view object is dynamic, meaning that it reflects any changes made to the dictionary

# print(student.keys()) # Output: dict_keys(['name', 'age', 'grades'])


# #values() method is used to return a view object that displays a list of all the values in a dictionary. The view object is dynamic, meaning that it reflects any changes made to the dictionary.

# print(student.values())  # Output: dict_values(['Deep', 20, {'math': 'A', 'science': 'B', 'english': 'A'}])

# # items() used to returns all (key:value) pairs as tuples

# print(student.items())

# #get() used to returns keys according to value

# print(student.get("name")) # Output: Deep

# #update() method is used to update the values of existing keys in a dictionary or add new key-value pairs to the dictionary. 

# student.update({"age": 21, "city": "Vadodara"})     # Update existing key "age" and add new key "city"
# print(student)


# #pop() method is used to remove a specified key and return its corresponding value from a dictionary. If the key is not found, it raises a KeyError.
# removed_value = student.pop("age")  # Remove the key "age" and return its value
# print("Removed value:", removed_value)  # Output: Removed value: 21
# print(student)  # Output: {'name': 'Deep', 'grades': {'math': 'A', 'science': 'B', 'english': 'A'}, 'city': 'Vad

# #set in python is a collection of unique elements. It cant have duplicate values. It is defined using curly braces {} or the set() constructor. Sets are unordered, mutable, and do not allow duplicate elements.

# set1 = {1, 3, 2, 2, 2,"Hello", 3.14, True}
# print(set1)
# print(type(set1))
# print(len(set1))

# # # empty set
# set2 = set()
# print(type(set2))

# #set methods
# # add() method is used to add an element to a set. If the element already exists in the set, it will not be added again, as sets do not allow duplicate elements.
# set2.add(4)
# print(set2)

# # remove() method is used to remove a specified element from a set. If the element is not found in the set, it raises a KeyError.
# set1 = {1, 3, 2, 2, 2,"Hello", 3.14, True}
# set1.remove(2)  # Remove element 2 from set1
# print(set1)

# #clear() method is used to remove all elements from a set, resulting in an empty set.
# set1.clear()
# print(set1)

# # pop() method is used to remove and return an random element from a set. If the set is empty, it raises a KeyError.
# set3 = {"deep","jay", "Hello", "vijay","pavan" }
# print(set3.pop())  # Remove and return an random element from set3

# #union() method is used to return a new set that contains all the unique elements from both sets. It does not modify the original sets.
# setA = {1, 2, 3}    
# setB = {3, 4, 5}
# print(setA.union(setB))  # Output: {1, 2, 3, 4, 5}
# print(setA)  # Output: {1, 2, 3}    
# print(setB)  # Output: {3, 4, 5}

# #intersection() method is used to return a new set that contains only the elements that are common to both sets. It does not modify the original sets.
# setC = {1, 2, 3}    
# setD = {2, 3, 4}
# print(setC.intersection(setD)) #output: {2,3}


# #pratice questions

# #store the followinng word meaning in a dictinary 
# dictinary = { "cat": "a small animal","Table":["a piece of furniture ","list of facts and figures"]}
# print(dictinary)
# print(dictinary["Table"])

# #You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# subjects = ["Java", "C++", "Python", "Javascript", "C","Java", "Python","Python","C++","Java"]
# print("Number of classrooms needed:", len(set(subjects))) #print the length of set 
# #The set will remove the duplicate subjects and give us the unique subjects, which is equal to the number of classrooms needed.


# #WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
# marks = {}
# x=int(input("enter marks for Math: "))
# y=int(input("enter marks for Science: "))
# z=int(input("enter marks for English: "))
# marks.update({"Math": x})
# marks.update({"Science": y})
# marks.update({"English": z})
# print(marks)

# #Figure out a way to store 9 & 9.0 as separate values in the set.
# values={9,"9.0"}  #both are the same so make one of them a string 
# print(values)
# #another way
# #(You can take help of built-in data types)
# values={("int",9),("float",9.0)}  #both are the same so make one of them a tuple with data type
# print(values)


# #Loops in pyhton


# While loop

#while loop is used to execute a block of code repeatedly as long as a specified condition is true. The syntax of a while loop is as follows:
# while condition:
#     # code to be executed 


# i=1
# while i<=5:
#     print(i)
#     i+=1  #increment the value of i by 1 in each iteration

# print("Loop has ended")
# print("The value of i after the loop is:", i)


# practice questions

# print num 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i+=1

#print num 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# print the multiplication table of number
# n = int(input("Enter a number: "))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1


#Print the elements of the following list using a loop:
# nums = [11, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx <len(nums):
#     print(nums[idx])
#     idx += 1
#Search for a number x in this tuple using loop:

nums_tuple = (11, 4, 9, 16, 25, 36, 49, 64, 81, 100,11)
x = int(input("Enter a number to search in the tuple: "))
idx=0
while idx < len(nums_tuple):
    if nums_tuple[idx] == x:
        print(x, "found at index", idx)
        
    idx += 1
else:
    print(x, "not found in the tuple")

 

   