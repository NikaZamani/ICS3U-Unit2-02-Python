#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program calculates the area and perimeter of a rectangle
#    with radius inputted from the user


def main():
    # this function calculates area and perimeter
    
    # input
    length = int(input("Enter Length of the rectangle (mm): 10 "))
    width = int(input("Enter width of the rectangle (mm): 12 "))


    # process
    area = length * width
    perimeter = 2 * (length + width)
    
    # output
    print('')
    print("Area is｛0｝mm².".format(area))
    print("Perimeter is｛0｝mm.".format(perimeter))
    

if __name__ == "__main__":
    main()
