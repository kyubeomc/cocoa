def say_hello(name, age) :
    return f"Hello {name} you are {age} years old"

def say_hello2(name age) :
    return "Hello" + name + "you are" + age + "years old" 
hello = say_hello("Kyu","20")

hello2 = say_hello2("Kyu","20")
print(hello)
print(hello2)