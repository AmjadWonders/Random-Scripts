# Done in 5/7/2018 12:50 AM. this one is pretty direct.
name = input("what is your name?")
weight_kg = float(input("what is your weight (KG):"))
height_m = float(input("what is your height (m):"))
bmi = weight_kg / (height_m ** 2)
print("bmi:",round(bmi,2))
if bmi < 18:
    print(name, "is underweight")
elif bmi < 25:
    print(name,"is normal")
elif bmi > 25.0 < 29.9:
    print(name,"is overweight")
elif bmi > 30.0:
    print(name,"is obese")