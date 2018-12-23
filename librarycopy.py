from abc import ABCMeta,abstractmethod
import abc
class Shape(object):
    __metaclass__ = ABCMeta
    @abc.abstractmethod
    def area(self):
        return 0

class Square(Shape):
    width = 5
    length =10
    def area(self):
        print self.width * self.length

class Rectangle(Shape):
    side = 4
    def area(self):
        print self.side * 2
        print "Succeess this id copyfor config"

sq = Square()
rect = Rectangle()
rect.area()
sq.area()



