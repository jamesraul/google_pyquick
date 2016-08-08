#!/usr/bin/env python
# Google Pyquick class first example


import sys

def Hello(name):
    name = name + "!!!"
    print "Hello,", name

# Define a main() function that prints a little greeting
def main():
    print "You supplied the following arguments: " + sys.argv[1]
    Hello(sys.argv[1])

# this runs the main function if this python script is called directly via python
if __name__ == '__main__':
    main()