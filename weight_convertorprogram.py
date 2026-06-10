unit = input("(l)bs or (k)g :")
weight = float(input("enter your weight : "))


if unit == "l":
    convert = weight*0.45
    print("weight in kg : ",convert)

elif unit == "k":
    convert = weight/0.45
    print("weight in lbs : ",convert)
