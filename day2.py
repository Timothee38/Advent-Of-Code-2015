#-------------------------------------------------------------------------------
# Name:        day1
# Purpose:
#
# Author:      Timothee
#
# Created:     02/12/2015
# Copyright:   (c) Timothee Craig 2015
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: UTF -8 -*-

#Day 2: I Was Told There Would Be No Math

def part1():
    """
    This function returns the total ammount of paper needed in square feet:

    The elves are running low on wrapping paper,
    and so they need to submit an order for more.
    They have a list of the dimensions (length l, width w, and height h) of each present,
    and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism),
    which makes calculating the required wrapping paper for each gift a little easier:
    find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the smallest side.
    """


    inputFile = open('inputday2.txt', 'r')

    totalAmount=0
    for line in inputFile.readlines():
        s = line.split('\n')
        s = s[0]
        dimensions = s.split("x")
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])
        LxW = 2*length*width
        WxH = 2*width*height
        HxL = 2*height*length
        listOfSides=[LxW, WxH, HxL]
        listOfSides.sort()
        scrap = (listOfSides[0])/2.0
        totalAmount += LxW + WxH + HxL + scrap

    inputFile.close()

    return totalAmount

def part2():
    """
    This function returns the amount of ribbon for the elves:

    The elves are also running low on ribbon. Ribbon is all the same width,
    so they only have to worry about the length they need to order,
    which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides,
    or the smallest perimeter of any one face.
    Each present also requires a bow made out of ribbon as well;
    the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.
    Don't ask how they tie the bow, though; they'll never tell.
    """

    inputFile = open('inputday2.txt', 'r')

    totalAmount=0
    for line in inputFile.readlines():
        s = line.split('\n')
        s = s[0]
        dimensions = s.split("x")
        length = int(dimensions[0])
        width = int(dimensions[1])
        height = int(dimensions[2])
        totalAmount += length*width*height + 2*(sum([length, width, height]) - max(length, width, height))
    inputFile.close()

    return totalAmount

print "Amount of paper (in square feet): "
print part1()
print "Amount of ribbon (in feet): "
print part2()