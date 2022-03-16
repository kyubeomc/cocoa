import os 
os.system('clear')




def age_check (age):
    print(f"you are {age}")
    if age <18:
        print("you can't drink")
    elif age == 18 or age ==19:
        print("you are new to this!")
    else :
        print("you are still kind of young")
    

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
    print(x)

doc = {}


c = 'icoeeen' 
b = 'thomas'
doc[c] = b
print(doc)