from sys import argv
script,user_name,id=argv
prompt = '>'

print(f"Hi {id},I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {id}?")
likes = input(prompt)

print(f"Where do you live {id}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, {id} your name is {user_name}
You said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")