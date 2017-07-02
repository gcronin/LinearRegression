import csv
from random import randint

sign_deltaSlope = 1           #incrementing or decrementing slope change
sign_deltaIntercept = 1       #incrementing or decrementing intercept change
slope = 250                   #initial guess
intercept = 0                 #initial guess
deltaSlope = 1                #how much does slope change with each iteration
deltaIntercept = 1            #how much does intercept change with each iteration
cost = 0                      #sum of squares of differences between predicted and actual data
previousCost = 0              #stores cost from previous iteration so we can see if cost is decreasing

with open('data.csv') as f:
    reader = csv.reader(f, delimiter=',')
    data = [(float(col1), float(col2))
                for col1, col2 in reader]

def CalculateCost():
    global previousCost
    global cost
    previousCost = cost
    cost = 0
    for i in range(0, len(data)):
        cost += ((slope*data[i][0] + intercept) - data[i][1])**2

def LinearRegression():
    global slope
    global intercept
    global sign_deltaSlope
    global sign_deltaIntercept
    global deltaSlope
    global deltaIntercept
    global cost
    global previousCost
    if(randint(0,1)):
        slope += sign_deltaSlope*deltaSlope
        changeSlope = True
    else:
        intercept += sign_deltaIntercept*deltaIntercept
        changeSlope = False
    CalculateCost()
    if(cost > previousCost):
        if(changeSlope):
            sign_deltaSlope *= -1
        else:
            sign_deltaIntercept *= -1



for x in range(0,2000):
    LinearRegression()
    print('Slope: {0:.2f}'.format(slope), ' Intercept: {0:.2f}'.format(intercept), ' Cost: {0:.3f}'.format(cost), '  Previous Cost: {0:.3f}'.format(previousCost))
