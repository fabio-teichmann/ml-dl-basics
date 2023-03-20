# to avoid having to manually close the file, use `with`
# modes:
# r = read
# w = write (deletes content and writes new; can create a new file if not exists)
# r+ = read and write (overwrites existing characters)
# a = append
try:
    with open("test.txt", mode='a') as my_file:
        text = my_file.write('Hey, it\'s me!')
        print(text)
except FileNotFoundError as e:
    print(f'Error: {e}')
except IOError as e:
    print(f'Error: {e}')
    
# reading uses the cursor concept, after once read, the cursor is at the end of a file
# print(my_file.read())
# set cursor back to beginning
# my_file.seek(0)

# read a single line
# print(my_file.readline())


# return list of lines
# print(my_file.readlines())

# after work has been done, close file
# my_file.close()
