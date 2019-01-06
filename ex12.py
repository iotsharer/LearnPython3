from sys import argv
script,first,second,third=argv

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Youe third variable is:",third)

first = input("input first:")
second = input("input second:")
third = input("input third:")
print("{} {} {}".format(first,second,third))