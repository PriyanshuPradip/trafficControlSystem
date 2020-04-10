import random
import math

arrCarsAtPoints = []
maxCarAtPoint = 0
time = 0
defaultTime = 3
avgTime = 0
avgCar= 0

def generateRandomCars(maxNum):
    global arrCarsAtPoint
    for i in range(4):
        arrCarsAtPoints.append(random.randrange(1,maxNum,1))    
    
def arrangeCars(carAtPoint,time):
    global avgCar
    maxCarAtPoint = carAtPoint.index((max(carAtPoint)))
    avgCar = 12 if avgCar < 12 else avgCar
    
    if maxCarAtPoint == 0  or maxCarAtPoint == 1:      
        print(" At Time :", time,"\n           xxxxxxxx LIGHT = GREEN xxxxxxxx \tCars MOVE in 1 (^) and 2 (v) direction")
        print("\n           xxxxxxxx LIGHT = RED xxxxxxxx \tCars WAIT in 3 (<) and 4 (>) direction")
            
        arrCarsAtPoints[0]-= avgCar
        arrCarsAtPoints[1]-= avgCar
    else: 
        print(" At Time :", time,"\n           xxxxxxxx LIGHT = GREEN xxxxxxxx \tCars MOVE in 3 (<) and 4 (>) direction")
        print("\n           xxxxxxxx LIGHT = RED xxxxxxxx \tCars WAIT in  1 (^) and 2 (v)direction")
            
        arrCarsAtPoints[2]-= avgCar
        arrCarsAtPoints[3]-= avgCar
    
def avgTimeCar():
        global avgCar; global avgTime
        maxA =max(arrCarsAtPoints[1],arrCarsAtPoints[0])
        maxB =max(arrCarsAtPoints[3],arrCarsAtPoints[2])
        avgCar = math.ceil((maxA+maxB)/2)
        avgTime = math.ceil(avgCar/4)
        return avgCar,avgTime
    
print("==========================================================")
print("\t\tINTELLIGENT TRAFFIC CONTROL SYSTEM")
print("==========================================================")
print("\t		   ( 1 )               ")
print("\t		     ^                                      4cars in 1 secs can pass the light ")
print("\t	   	     |                  ")
print("\t	( 3 )	 <---+--->    ( 4 )    ")
print("\t                     |                  ")
print("\t		     v                  ")
print("\t		   ( 2 )              \n ")
print("\t A. RANDAMIZED DEMO.          ")
print("\t B. MANUAL DEMO.              ")
print(" Enter your choice :     ")
demoType = str(input())
maxCars = 50
print("Maximun number of vehicle at any Point--> ",maxCars)

if  demoType == "A" :   
    print("==========================================================")
    print("\t\t RANDOMIZED INTELLIGENT TRAFFIC CONTROL SYSTEM")
    print("==========================================================")		 
    generateRandomCars(maxCars)

elif demoType =="B" :
    print("==========================================================")
    print("\t\t MANUAL INTELLIGENT TRAFFIC CONTROL SYSTEM")
    print("==========================================================")
    for i in range (4):
          print("Input Cars at each point :", i+1)
          arrCarsAtPoints.append(int(input()))    
          
else :
    print("Exiting : YOU HAVENT ENTERED VALID OPTION")   
    
avgCar,avgTime = avgTimeCar()
print ("avgCar",avgCar,"avgTime",avgTime)
print("\n ______________________________________________________________________________________________________")
print(" Cars at each point is :")
for i in range(4):
    if arrCarsAtPoints[i]<0:
            arrCarsAtPoints[i]= 0
    print("\tCars POINT ( ",i+1," ) --> ",arrCarsAtPoints[i])
while max(arrCarsAtPoints)>0:  
    arrangeCars(arrCarsAtPoints,time)
    print("\n ______________________________________________________________________________________________________")
    if avgTime > defaultTime :
        time = time + avgTime
        avgCar,avgTime = avgTimeCar()
    else:
        time += defaultTime
        avgCar,avgTime = 12,3
    print("\n ______________________________________________________________________________________________________")
    print(" Cars at each point is :")
    for i in range(4):
        if arrCarsAtPoints[i]<0:
            arrCarsAtPoints[i]= 0
        print("\tCars POINT ( ",i+1," ) --> ",arrCarsAtPoints[i])            
