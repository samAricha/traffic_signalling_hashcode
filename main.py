from cars import *
from streets import *

class Main(object):
    def __init__(self):
        pass

    def readF(self, filename):
        print("inside read file")
        f = open(filename)
        lines = f.readlines()
        sTime, nIntersections, nStreets, nCars, pDestination = [int(x) for x in lines[0].split(' ')[0:5]]
        streetsL = []
        carsL = []
        for i in range(nStreets):
            i1, i2, sName, tTime = [str(x) for x in lines[i+1].split(' ')[0:4]]
            streetsL.append(Streets(i1, i2, sName, tTime))
            # print(streetsL[i].i1)
            # print(streetsL[i].i2)
            # print(streetsL[i].sName)
            # print(streetsL[i].tTime)

#NB: find out how to start from 1(or any no. of choice) in the for loop and not 0
        for i in range(nCars): 
            line = lines[i+nStreets+1]
            splitLine = line.split(' ')
            carsL.append(Cars(splitLine[0], splitLine[1:]))
            print(carsL[i].nStreets)
            print(carsL[i].path)
            
             

    def writeF(self):
        pass

    def solveAll(self, filename):
       self.readF(filename)

a_txt = "./data/a.txt"
b_txt = "./data/b.txt"
c_txt = "./data/c.txt"
d_txt = "./data/d.txt"
e_txt = "./data/e.txt"
f_txt = "./data/f.txt"

main = Main()
main.solveAll(a_txt)

