# birth_year = input("what is your birthyear? ")
# age = 2022 - int(birth_year)
# print("Your age is " + str(age))


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

out = ''

for row in picture:
    for i in row:
        out += '*' if i else ' '
    # new row, add newline character
    out += '\n'

print(out)
