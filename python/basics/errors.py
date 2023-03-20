# Error Handling: allows us to continue the program running
# There are many different error types:
# https://docs.python.org/3/library/exceptions.html
while True:
    try:
        age = int(input('What is your age? '))
        10 / age
        print(age)
        # can raise own errors
        # raise ValueError('Cut it out')
    except ValueError:  # excepts a specific type of error
        print('Please enter a number')
    except ZeroDivisionError:
        print('0 is an invalid input')
    else:
        # executes when no error occurred
        print('thank you')
        break
    finally:  # executes in any case; useful for logging activities for example
        print('One last note...')


def summ(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:  # can except different error types simultaneously
        print(f'something went wrong {err}!')


print(summ(1, 0))
