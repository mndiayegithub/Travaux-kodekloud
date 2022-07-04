import math


def division():
    global number1, number2
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")

    if not (number1.isnumeric() and number2.isnumeric()):
        print("Please enter valid numbers.")
        division()
    if float(number2) == 0:
        print("Zero division error, please try again.")
        division()
    elif float(number2) != 0:
        print(float(number1) / float(number2))
    else:
        print("Hmm, something went wrong, try again.")
        division()


# Rewrite the code above so that all if/elif/else statements are replaced by a try/except code block.
def tryandexcept():
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")

    try:
        print(float(number1) / float(number2))
    except ZeroDivisionError:
        print("Zero division error, please try again.")
        division()
    except TypeError:
        print("Please enter valid numbers.")
        division()
    except Exception:
        print("Hmm, something went wrong, try again.")
        division()



#division()
tryandexcept()

#raise
# Manually raise an exception to handle your code.
# If we had raise in an exception, it will immediately reraise the same exception
# raise ZeroDivisionError
def calculate_user_input():
    raise ZeroDivisionError

try:
    calculate_user_input()
except ZeroDivisionError:
    print("You cannot divide by zero.")
except:
    print("Something else went wrong")

def callculate_user_input():
    try:
        x=int(input("Enter a number:"))
        y=1/x
        print(y)
    except:
        print("Something went wrong !")
        raise

    return None
#Handle the raise again
try:
    callculate_user_input()

except ZeroDivisionError:
    print("You cannot divide by zero.")
except:
    print("Something else went wrong")


#assert
#Raise an AssertionError if the expression evaluates to a false value
x=input("Enter a number")
assert x>= 0 # The assert keyword evaluates an expression and if this expression is evaluates to True or non-zero num value  ...

x=math.sqrt(x)
print("Result:",x)



#