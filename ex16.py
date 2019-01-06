from sys import argv

script,filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that,hit CTRL-C(^C).")
print("If you do want that.hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w') #'w' for writing (truncating the file if it already exists)

print("Truncating the file.Googbye!")
target.truncate() # Empties the file

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm goning to write these to the file.")

txt = line1 + "\n" + line2 + "\n" + line3 + "\n"
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# target.write(txt)
target.write("{}\n{}\n{}\n".format(line1,line2,line3))

print("And finally,we close it.")
target.close()

