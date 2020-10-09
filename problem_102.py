''' Solves problem # 102 on https://projecteuler.net
Sergey Lisitsin. February 2020
'''

from math import sqrt

class Point:

	''' A class of objects representing points on plane
	Has two coordinate variables, x and y and a list of
	associated triangles.'''

	def __init__(self, x: float, y: float):
		self.name = str(x)+str(y)
		self.x = x
		self.y = y
		self.mytriangles = set()

	def coordinates(self):
		''' Returns point's coordinates x and y'''
		return self.x, self.y

	def sectozero(self):
		zero = Point(0,0)
		return Section(self,zero)

	def __repr__(self):
		return ('{}: {} {}'.format(self.__class__.__name__, self.x, self.y))

	def __eq__(self, other):
		return (self.x, self.y) == (other.x, other.y)

	def __lt__(self, other):
		return self.x < other.x

	def __hash__(self):
		return hash(repr(self))


class Section:
    ''' A class of objects representing a section. Has
    name, and two point objects, representing the ends of
    a section. Also has length that is calculated'''

    def __init__(self, a: Point, b: Point):
        self.name = a.name + b.name
        self.a = a
        self.b = b
        self.deltax = float(abs(self.b.x - self.a.x))
        self.deltay = float(self.b.y - self.a.y)
        if self.deltax == 0.0:
            self.slope = 0.0
        else:
            self.slope = (self.deltay) / (self.deltax)  # Finding the slope
        self.rais = self.a.y - self.a.x * self.slope  # Finding the raise
        hypsqr = (self.deltax * self.deltax) + (self.deltay * self.deltay)
        self.length = sqrt(hypsqr)


class Triangle:
    ''' A class of objects representing a triangle.
    Consists of three point objects that don't lie
    on the same	line. Has perimeter and area '''

    def __init__(self, a: Point, b: Point, c: Point):
        self.name = a.name + b.name + c.name
        self.adjacents = set()
        self.a = a  # points and sections of the triangle
        self.b = b  #
        self.c = c  #
        self.section1 = Section(self.a, self.b)  #
        self.section2 = Section(self.b, self.c)  #
        self.section3 = Section(self.a, self.c)  #

        if istriangle(self.a, self.b, self.c):
            self.real = True
        else:
            self.real = False

        self.perimeter = self.section1.length + \
                         self.section2.length + self.section3.length

        self.halfper = self.perimeter / 2
        self.semisection1 = self.halfper - self.section1.length
        self.semisection2 = self.halfper - self.section2.length
        self.semisection3 = self.halfper - self.section3.length
        if (self.halfper * self.semisection1 * self.semisection2 * self.semisection3) > 0:
            self.area = sqrt(self.halfper * self.semisection1 * self.semisection2 * self.semisection3)
        else:
            self.area = 0

    def returnpoints(self):
        return (self.a, self.b, self.c)

    def returnsections(self):
        return (self.section1, self.section2, self.section3)

def istriangle(a: Point, b: Point, c: Point):
	''' This function finds out whether all 3
	points lie on the same line, in which case
	they can't form a triangle. It uses linefunc
	to find out whether all 3 points belong to
	the line built by the same function'''

	first = linefunc(a,b)				#function of the first two points
	second = linefunc(b,c)				#function of the second two points
	if first == second:					#if they are the same, then you
		return False					# can't build a triangle with these 3 lines
	else:
		return True

def linefunc(a: Point, b: Point):
	''' This function returns slope and raise for a line
	defined by two points'''
	if a.x == b.x:
		rais = False
		slope = 0

	if a.x < b.x:
		slope = (b.y-a.y)/(b.x-a.x)	# Finding the slope if a is closer to Y axis
		rais  = a.y-a.x*slope		# Finding the raise if a is closer to Y axis
	elif b.x < a.x:
		slope = (a.y-b.y)/(a.x-b.x) # Finding the slope if b is closer to Y axis
		rais = b.y-b.x*slope		# Finding the raise if b is closer to Y axis
	return (slope,rais)



def isinside(t: Triangle, point: Point):
	''' This function finds out whether the point is
	inside of a given triangle's perimeter '''

	if point.x == t.a.x and point.y == t.a.y:
		return False
	if point.x == t.b.x and point.y == t.b.y:
		return False
	if point.x == t.c.x and point.y == t.c.y:
		return False
	if not istriangle(point, t.a, t.b):
		return False
	if not istriangle(point, t.b, t.c):
		return False
	if not istriangle(point, t.a, t.c):
		return False

	sub1 = Triangle(point, t.a, t.b)
	sub2 = Triangle(point, t.b, t.c)
	sub3 = Triangle(point, t.a, t.c)

	if (round(sub1.area, 2) + round(sub2.area, 2) + \
		round(sub3.area, 2)) > round(t.area, 2):
		return False
	else:
		return True

f = open('p102_triangles.txt','r')
file = f.readlines()
lines = []
for x in file:
    lines.append(x.replace('\n',''))
triangles = []
for x in lines:
    y =  x.split(',')
    p1 = Point(float(y[0]),float(y[1]))
    p2 = Point(float(y[2]),float(y[3]))
    p3 = Point(float(y[4]),float(y[5]))
    triangle = Triangle(p1,p2,p3)
    triangles.append(triangle)

zero = Point(0,0)
count = 0

for x in triangles:
    if isinside(x, zero):
        count +=1
print(count)