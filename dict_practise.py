student = {"name" : "ashwin",
           "age" : 19,
           "branch" : "AIML",
           "college" : "NMIMS"}

student["skills"] = "python"
print(student["branch"])
print(student["college"])
print(student)


marks = {}

marks["maths"] = int(input("enter your marks : "))
marks["physics"] = int(input("enter your marks : "))
marks["chemistry"] = int(input("enter your marks : "))

total = marks["maths"] + marks["physics"] + marks["chemistry"]
avg = total/3

print("Total marks ",total)
print("average marks",avg)