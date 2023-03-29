# Write a program which accepts a string as input to print "Yes" if the 
# string is "yes" or "YES" or "Yes", otherwise print "No".

input = 'Ye'
def print_yes(input):
    return 'Yes' if input.lower() == 'yes' else 'No'

print(print_yes(input))