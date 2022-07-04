# Open the file String_methods.py, and complete the code so that the counter function is not executed while we import main as
# a module into the file test_module.py.
# Check results by running the file test_module.py.

count = 0
def counter(the_list):
    global count
    for element in the_list:
        count += 1
    return len(the_list)

if __name__ == "__main__": # __name__ contains the name of the module.
    my_list = [i+1 for i in range(5)]
    print(counter(my_list) == count)