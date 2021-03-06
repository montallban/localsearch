# first choice hill climbing

# student name: Michael Montalbano
# date: 3/30/2020

import copy
from random import Random
import random
import numpy as np
import sys

seed = 5113
myPRNG = Random(seed)

# number of elements in a solution
n = 150

# initialize instance of knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))

#define max weight for the knapsack
maxWeight = 1500

#monitor the number of solutions evaluated
solutionsChecked = 0

#function used to evaluate a solution x
def evaluate(x):
    a = np.array(x)
    b = np.array(value)
    c = np.array(weights)
    totalValue = np.dot(a,b)    # compute the value of the knapsack selection
    totalWeight = np.dot(a,c)   # compute the weight

    if totalWeight > maxWeight:
        totalValue = 0

    return [totalValue, totalWeight]

def neighborhood(x):
    '''
    Generates n neighbors, where each neighbor has exactly one element flipped
    '''
    nbrhood = []
    for i in range(0,n):
        nbrhood.append(x[:]) # set nbrhood to current solution
        if nbrhood[i][i] == 1: # set the i-th solution's i-th element to 0 if it was 1
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
    
    return nbrhood 

def shuffle(x):
    '''
    shuffles (randomizes order) of a list
    '''
    return random.sample(x,n)

#create the initial solution
def initial_solution():
    x = []
    for i in range(0,n):
        x.append(myPRNG.randint(0,1))   # random list of 0's and 1's, 
    for idx, a in enumerate(x): # take items out of knapsack until totalWeight < maxWeight
        x[idx] = 0
        if evaluate(x)[0] != 0:
            break
    return x

solutionsChecked = 0

x_curr = initial_solution()
x_best = x_curr[:]
f_curr = evaluate(x_curr)

f_best = f_curr[:]

# begin local search overall logic ------------
done = 0

while done == 0:
    Neighborhood = neighborhood(x_curr) #create a list of all neighbors in the neighborhood of x_curr
    for s in Neighborhood:
        solutionsChecked = solutionsChecked + 1
        if evaluate(s)[0] > f_best[0]:
            x_best = s[:]
            f_best = evaluate(s)[:]
            break                       #once we get a better solution, break out of the loop
        
    if f_best == f_curr:
        done = 1
    else:
        x_curr = x_best[:]
        f_curr = f_best[:]

    print("\nTotal number of solutions checked: ", solutionsChecked)
    print("Best value found so far: ", f_best)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)