#!/usr/bin/env python

import math


def side_length_from_inradius(nbr_sides, inradius):
    return 2.0 * inradius * math.tan(math.pi / nbr_sides)


def side_length_from_circumradius(nbr_sides, circumradius):
    return 2.0 * circumradius * math.sin(math.pi / nbr_sides)


def inradius_from_side_length(nbr_sides, side_length):
    return 0.5 * side_length / math.tan(math.pi / nbr_sides)


def inradius_from_circumradius(nbr_sides, circumradius):
    return circumradius * math.cos(math.pi / nbr_sides)


def circumradius_from_side_length(nbr_sides, side_length):
    return 0.5 * side_length / math.sin(math.pi / nbr_sides)


def circumradius_from_inradius(nbr_sides, inradius):
    return inradius / math.cos(math.pi / nbr_sides)


def vertices(nbr_sides, center_x, center_y, circumradius, init_angle=0.0):
    rad = 2.0 * math.pi / nbr_sides
    v = []
    for i in range(nbr_sides):
        x = center_x + circumradius * math.cos(init_angle + (rad * i))
        y = center_y + circumradius * math.sin(init_angle + (rad * i))
        v.append((x, y))
    return v


class RegularPolygon:

    nbr_sides: float
    center_x: float
    center_y: float
    init_angle: float
    circumradius: float
    inradius: float
    side_length: float

    def __init__(self, nbr_sides, center_x=0.0, center_y=0.0, init_angle=0.0):
        self.nbr_sides = nbr_sides
        self.center_x = center_x
        self.center_y = center_y
        self.init_angle = init_angle

    def vertices(self):
        return vertices(self.nbr_sides, self.center_x, self.center_y, self.circumradius, self.init_angle)


class Triangle(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, init_angle=0.0):
        super(Triangle, self).__init__(nbr_sides=3, center_x=center_x, center_y=center_y, init_angle=init_angle)

    @staticmethod
    def from_side_length(side_length, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Triangle(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.side_length = side_length
        poly.inradius = inradius_from_side_length(poly.nbr_sides, side_length)
        poly.circumradius = circumradius_from_side_length(poly.nbr_sides, side_length)
        return poly

    @staticmethod
    def from_inradius(inradius, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Triangle(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.inradius = inradius
        poly.side_length = side_length_from_inradius(poly.nbr_sides, inradius)
        poly.circumradius = circumradius_from_inradius(poly.nbr_sides, inradius)
        return poly

    @staticmethod
    def from_circumradius(circumradius, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Triangle(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.circumradius = circumradius
        poly.side_length = side_length_from_circumradius(poly.nbr_sides, circumradius)
        poly.inradius = inradius_from_circumradius(poly.nbr_sides, circumradius)
        return poly


class Square(RegularPolygon):

    def __init__(self, center_x=0.0, center_y=0.0, init_angle=0.0):
        super(Square, self).__init__(nbr_sides=4, center_x=center_x, center_y=center_y, init_angle=init_angle)

    @staticmethod
    def from_side_length(side_length, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Square(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.side_length = side_length
        poly.inradius = inradius_from_side_length(poly.nbr_sides, side_length)
        poly.circumradius = circumradius_from_side_length(poly.nbr_sides, side_length)
        return poly

    @staticmethod
    def from_inradius(inradius, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Square(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.inradius = inradius
        poly.side_length = side_length_from_inradius(poly.nbr_sides, inradius)
        poly.circumradius = circumradius_from_inradius(poly.nbr_sides, inradius)
        return poly

    @staticmethod
    def from_circumradius(circumradius, center_x=0.0, center_y=0.0, init_angle=0.0):
        poly = Square(center_x=center_x, center_y=center_y, init_angle=init_angle)
        poly.circumradius = circumradius
        poly.side_length = side_length_from_circumradius(poly.nbr_sides, circumradius)
        poly.inradius = inradius_from_circumradius(poly.nbr_sides, circumradius)
        return poly
  

if __name__ == '__main__':
    tri = Triangle.from_side_length(2, init_angle=math.radians(90))
    print(tri)
    print(tri.vertices())
