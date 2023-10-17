#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 16, 2023
# This program Calculates the area and perimeter of a hexagon with
# the imputed dimensions.

import math


def main():
    # Extra functionality - getting specific calculation
    print("Before we start,")
    print("Click the corresponding number for what you would like to calculate?")
    calculate = int(input("Perimeter(1),Area(2) or Both(3).\n"))

    if calculate not in (1, 2, 3):
        print("Invalid value imputed restart programming!")
        return

    # Input - getting length and units.
    # Extra functionality - getting unit
    unit = input("What unit would you like the calculations measured in?\n")
    # defining the variable "length".
    length = int(input("What is the length of the sides of the Hexagon "))

    if calculate == 3:
        # process - Calculating area and perimeter.
        area = (3 * (3**0.5) / 2) * (length**2)
        perimeter = 6 * length
        # output
        print(f"The area of the rectangle is {area:.2f}{unit}7^2")
        print(f"The perimeter of the rectangle is {perimeter:.2f}{unit}")

    if calculate == 2:
        # process - Calculating area.
        area = (3 * (3**0.5) / 2) * (length**2)
        # output
        print(f"The area of the rectangle is {area:.2f}{unit}^2")

    if calculate == 1:
        # process - Calculating  perimeter.
        perimeter = 6 * length
        # output
        print(f"The perimeter of the rectangle is {perimeter:.2f}{unit}")


if __name__ == "__main__":
    main()
