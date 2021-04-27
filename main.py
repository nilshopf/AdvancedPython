# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import functions
def print_hi(name):
    print(f'Hello, {name}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fruits = ["banana", "apple", "pineapple"]
    for i in fruits:
        #print_hi('PyCharm')
        if i == "banana":
            n = 0
            while n != 5:
                functions.print_hi(i)
                print_hi(i)
                functions.secondfunction()
                n += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
