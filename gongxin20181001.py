#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 01 11:37:09 2018

@author: alex
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor.
"""

import numpy as np

number = 16
target_pool = [(651, 383, 4, 19),
(400, 270, 5, 25),
(764, 242, 6, 29),
(17, 23, 2, 10),
(215, 27, 3, 15),
(538, 324, 5, 25),
(819, 172, 5, 24),
(125, 500, 6, 29),
(676, 383, 4, 20),
(80, 569, 6, 30),
(795, 242, 6, 30),
(192, 27, 3, 16),
(387, 270, 5, 25),
(857, 172, 10, 25),
(17, 23, 2, 10),
(261, 487, 4, 20)]

mat = np.array(target_pool)

S = []          #area
nrow = len(mat)
ncol = len(mat[0])
#cpmpute the area
for i in range(nrow):
    mid = round(ncol/2)
    S.append([mat[i][x]*mat[i][x+1] for x in range(mid,mid+1)])
    
#define the function to measure the Similarity degree between
#target 1 and target 2

def similar_deg(loc1, S1, loc2, S2, fac):
    #fac is the ratio between location and area.Eg,when fac is quite
    #big,we will pay much more attention on the area of target
    sim_deg = np.linalg.norm(np.array(loc1) - np.array(loc2))\
    +fac*np.linalg.norm(np.array(S1) - np.array(S2))
    return sim_deg

simdeg = []
output = []
#show the match output
while len(mat) > 1:
    loc = mat[:,:2]   #location
    
    for i in range(1,len(mat)):
        simdeg.append(similar_deg(loc[i], S[i], loc[0], S[0], 1))
        
    print(simdeg) 
    deN = simdeg.index(min(simdeg))+1
    
    output.append([mat[0],mat[deN]])#output the target pairs
   
    S.remove(S[deN])
    S.remove(S[0])  
    #remove the target's data that has been paired
 
    mat = np.delete(mat, deN, 0)
    mat = np.delete(mat, 0, 0) 
    #remove the target's data that has been paired
    simdeg = [] #reset similar degree list
print(output)  #show the match output
#the first 6 pairs match well, while the last 2 pairs match poorly...
#we may have the chance to improve the result through adjusting the value of fac
