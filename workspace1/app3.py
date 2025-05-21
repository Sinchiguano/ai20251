def computeAreaSquare(side):
    return side*side

def computeAreaCircle(radius):
    pi=3.1415
    return pi*radius**2



print(f"The area of an square with side 3cm is {computeAreaSquare(3)}")
print(f"The are of a circle with a radius of 3 is {computeAreaCircle(3):.2f}")


class Geometry:
    pi=3.1415
    def __init__(self,side,radius):
        self.side=side
        self.radius=radius
        print("The object was created successfully!")
    def area(self):
        squareArea=self.side*self.side
        circleArea=Geometry.pi*self.radius**2
        return [squareArea,circleArea]

areaSquareCircle=Geometry(3,3)
result=list()
result=areaSquareCircle.area()
print(len(result))
print(f"The are of the square and cicle are: {result[0]}, {result[1]:.2f}")


print('STUDENT CLASS!!!!!!!!!!!!!!')

import statistics

class Student:
    def __init__(self,name, grades):
        self.name=name
        self.grades=grades

    def average_grade(self):
        score=statistics.mean(self.grades)
        return score



wilmerStudent=Student('Wilmer',[6,5,4.5,10])

millerStudent=Student('Miller',[7,5.5,7.5,10])

eddyStudent=Student('Eddy',[7,10,8.5,10])


print(f"THE SCORE OF WILMER IS {wilmerStudent.average_grade():.2f}")

print(f"THE SCORE OF MILLER IS {millerStudent.average_grade():.2f}")

print(f"THE SCORE OF EDDY IS {eddyStudent.average_grade():.2f}")






print(("OK"))