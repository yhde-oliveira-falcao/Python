#!/usr/bin/env python3
# -*- coding: utf-8 -*-
xlst = []
ylst = []

def mpoint():
    X = int(input("Enter the x-demension, must be a positive integer:"))
    Y = int(input("Enter the y-demension, must be a positive integer:"))
    num = int(input("How many people will join the meeting?:"))
    xlst = []
    ylst = []
    for i in range(num):
        xx = int(input("Enter the your x-position:"))
        yy = int(input("Enter the your y-position:"))
        while xx > X or yy > Y:
            print(f"Your position should be within the {X}*{Y} grid.")
            xx = int(input("Enter the your x-position:"))
            yy = int(input("Enter the your y-position:"))
        xlst.append(xx)
        ylst.append(yy)
    xmean = round(sum(xlst)/len(xlst), 0)
    ymean = round(sum(xlst)/len(xlst), 0) 
    print("The meeting point should be: ")     
    print(xmean, ymean) 
    return xmean, ymean
    
mpoint()
