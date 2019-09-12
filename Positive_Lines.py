import numpy as np
import matplotlib.pyplot as plt

def probs(line):
    if line < 0:
        return (-line)/(-line+100.)
    elif line > 0:
        return (100.)/(100.+line)
    else:
        print("Something is wrong")
        return None

def lineFOIL(lines):
    probarr = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            probarr.append(probs(lines[0][i])*probs(lines[1][j]))
    return np.asarray(probarr).T

def Adjust_Vig(probarr):
    ### Be aware of subtraction of nearly equal number;
    vig = sum(probarr)-1.
    vig /= 3
    ### Subtract 1/3 of vig from 3 win scenarios
    return np.asarray([probarr[0]-vig,probarr[1]-vig,probarr[2]-vig,probarr[3]])

def Ratio_Range(lines,numpoints):
    ### Isolate plus bets
    ### Bet on poslines[0] = lower/upper*bet on poslines[1]
    lines = lines.flatten('C')
    print(lines)
    poslines = [lines[0],lines[2]]
    lowerlimit = 100./poslines[0]
    upperlimit = poslines[1]/100.
    skip = (upperlimit - lowerlimit)/numpoints
    return np.arange(lowerlimit,upperlimit+skip,skip),poslines

def Profits(bet,line):
    if line > 0:
        return (bet*line)/100.
    elif line < 0:
        return (bet*100.)/line
    else:
        print("Something is wrong")


def Driver(lines):
    for lines in linesarr:
        probarr0 = np.asarray(lineFOIL(lines))
        probarr0 = Adjust_Vig(probarr0)
        ratiorange,poslines = Ratio_Range(lines,10)
        B1range = np.arange(1,10.1,0.1)
        expectedarr = []
        for ratio in ratiorange:
            for B1 in B1range: 
                B0 = ratio*B1
                P0 = Profits(B0,poslines[0])
                P1 = Profits(B1,poslines[1])
                B0 = P1
                P0 = Profits(B0,poslines[0])
                betarr = np.asarray([P0+P1,P0-B1,P1-B0,-(B0+B1)])
                expected = sum(betarr*probarr0)
                expectedarr.append(expected)
                if expected > 0:
                    print("Bet on Line " + str(poslines[0]) + ":")
                    print(B0)
                    print("Bet on Line " + str(poslines[1]) + ":")
                    print(B1)
        print(np.max(expectedarr))
        plt.plot(expectedarr,'o')
        plt.show()

linesarr = [[[115,-135],[110,-130]],[[245,-290],[370,-440]]]
linesarr = np.asarray(linesarr)
Driver(linesarr)

