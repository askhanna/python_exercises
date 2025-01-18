from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
#print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))

"""
birthday = input('Enter your birthday: ') 
if (birthday in pi_string):
    print("Your birthday appears in firs is present in pi.")
else:
    print("Sorry. Your birthday is not present in pi.")
"""
writefile = Path("Write_file.txt")
writefile.write_text("I love our daughter.")

