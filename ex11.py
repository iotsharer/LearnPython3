print("How old are you? ",end='') #end='' not to end the line with a new line
age =input() 
age2 =int(input("How old are you? ")) #converts string to integer
print("How tall are you?")
height = input()
height2 = int(input("How tall are you? "))
print("How much do you weigh? ")
weight = input()
weight2 = int(input("How much do you weigh? "))
all = age + height + weight
all2 = age2 + height2 + weight2 #test int()
print(f"So, you're {age} old,{height} tall and {weight} heavy.")
print(f"{all}.")
print(f"{all2}.")