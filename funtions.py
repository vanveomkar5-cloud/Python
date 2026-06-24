# def greet():
#     name = input("enter Name: ")
#     return"Good Morning " + name
# print(greet())

#LIST
# 1 function: append
# student=["mayur", "aditya"]
# l1=["apple", "banana"]
# t1=("red", "green")
# dic1={"jspm", "dy-patil"}

# student.append("astik")
# student.append(l1)
# student.append(t1)
# student.append(dic1)

# print(student)


# 2 function: insert
# student=["mayur", "aditya"]
# student.insert(1,"astik")
# print(student)


# 3 function: remove
# student=["mayur", "aditya", "astik"]
# student.remove("aditya")
# print(student)


# 4 function: pop
# student=["mayur", "aditya", "astik"]
# student.pop()#pop last element by default
# student.pop(0)
# print(student)


# 5 function: sort
# student=["mayur", "aditya", "astik"]
# student.sort()#sort in ascending order, same with No. also
# print(student)


# 6 function: reverse
# student=["mayur", "aditya", "astik"]
# student.reverse()
# print(student)


# 7 function: count
# student=["mayur", "aditya", "mayur", "astik"]
# print(student.count("mayur"))


# 8 function: index
# student=["mayur", "aditya", "astik"]
# print(student.index("aditya"))


# 9 function: min/max
# student=["mayur", "aditya", "astik"]
# print(min(student))


# TUPLE
# 1 function: count
# days=("mon", "tue", "wed", "thu", "fri", "thu", "sat")
# print(days.count("thu"))


# 2 function: index
# days=("mon", "tue", "wed", "thu", "fri", "thu", "sat")
# print(days.index("wed"))


# 3 function: len
# days=("mon", "tue", "wed", "thu", "fri", "thu", "sat")
# print(len(days))


# DICTIONARY
# 1 function: keys
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# print(dict1.keys())


# 2 function: values
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# print(dict1.values())


# 3 function: items
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# print(dict1.items())


# 4 function: get
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# print(dict1.get("age"))


# 5 function: update
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# dict1.update({"city":"Pune"})#remember format
# print(dict1)


# 6 function: pop
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# dict1.pop("age")
# print(dict1)


# 7 function: clear
# dict1={
#     "name":"Mayur",
#     "age":"18",
#     "branch":"Cpmputer"
# }
# dict1.clear()
# print(dict1)



# SET
# students={"mayur", "sheryash", "pooja"}
# st2={"vaibhav", "tanmay", "mayur"}
# students={10,20,30,40}
# st2={10,50,60,70,80}
# students.add("jspm")
# students.remove("jspm")
# students.discard("amit")
# students.remove("jspm")#throw error
# students.pop()
# students.clear()

# print(students)
# print(students.union(st2))
# print(students.intersection(st2))#common element show
# print(students.difference(st2))#different element show which is not in list 2, but in list 1


#string functions
# name= "pranav"
# name1= "hello world"
# data= "python,java,ai,ml,dl"
# ndata=" python "
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name1.replace("hello","python"))
# print(data.split(","))#seperate everyone
# print(ndata.strip())#remove extra space
# print(ndata.find("h"))#count space also
# print(ndata.count("p"))


