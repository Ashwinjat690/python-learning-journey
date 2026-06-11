numbers = []
i = 0
while i<6:
    num = int(input("enter your numbers : "))
    numbers.append(num)
    i+=1
print(numbers)

total = sum(numbers)
print(total)

vegtable = ["tomato", "potato", "onion", "carrot", "cabbage"]
veg2 = input("enter your vegtable : ")
if veg2 in vegtable:
    print("yes")
else:
    print("no")