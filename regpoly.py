#!/usr/bin/env python

"""
This module provides a RegularPolygon class.
A RegularPolygon is a convex polygon with sides of equal length.
"""

import math

TRIANGLE = 3
SQUARE = 4
PENTAGON = 5
HEXAGON = 6
HEPTAGON = 7
OCTAGON = 8
NONAGON = 9
DECAGON = 10
HENDECAGON = 11
DODECAGON = 12
TRIDECAGON = 13
TETRADECAGON = 14


class RegularPolygon:
    """A RegularPolygon is a convex polygon with sides of equal length."""

    nbr_sides: int
    center_x: float
    center_y: float
    rotation: float
    circumradius: float
    inradius: float
    side_length: float

    def center(self):
        """Returns a tuple (X,Y) describing the center of the polygon."""
        return self.center_x, self.center_y

    def vertices(self):
        """Returns a list of the polygon's vertices.

        Each item in the list is a tuple describing a vertex point. The first item in the tuple is the X position of the
        point. The second item in the tuple is the Y position of the point. Adjacent vertices in the list are adjacent
        on the polygon.
        """
        rad = 2.0 * math.pi / self.nbr_sides
        v = []
        for i in range(self.nbr_sides):
            x = self.center_x + self.circumradius * math.cos(self.rotation + (rad * i))
            y = self.center_y + self.circumradius * math.sin(self.rotation + (rad * i))
            v.append((x, y))
        return v

    def interior_angle(self):
        """Returns the interior angle.

        The angle on the interior of the polygon formed by two adjacent sides at the common vertex.
        """
        return (self.nbr_sides - 2.0) / self.nbr_sides * math.pi

    def exterior_angle(self):
        """Returns the exterior angle.

        The angle on the exterior of the polygon formed by two adjacent sides at the common vertex.
        """
        return 2.0 * math.pi - self.interior_angle()

    def sagitta(self):
        """Returns the sagitta.

        The sagitta is the difference between the circumradius and inradius. In other words,
        it is the maximum perpendicular distance from a side to the circle that circumscribes
        the polygon.
        """
        return self.circumradius - self.inradius

    def side_midpoints(self):
        """Returns a list of the midpoints on each of the polygon's sides.

        Each item in the list is a tuple describing a side's midpoint. The first item in the tuple is the X position of
        the midpoint. The second item in the tuple is the Y position of the midpoint. Adjacent midpoints in the list are
        belong to adjacent sides of the the polygon.
        """
        v = self.vertices()
        m = []
        midpoint = (lambda x1, x2: 0.5 * (x1 + x2))
        for i in range(self.nbr_sides):
            p1 = v[i]
            p2 = v[i+1] if i+1 < self.nbr_sides else v[0]
            x = midpoint(p1[0], p2[0])
            y = midpoint(p1[1], p2[1])
            m.append((x, y))
        return m

    def translate(self, x: float = 0.0, y: float = 0.0):
        """Returns a new regular polygon that is the result of translating this polygon.
        :rtype: RegularPolygon
        """
        poly = RegularPolygon()
        poly.nbr_sides = self.nbr_sides
        poly.center_x = self.center_x + x
        poly.center_y = self.center_y + y
        poly.rotation = self.rotation
        poly.circumradius = self.circumradius
        poly.inradius = self.inradius
        poly.side_length = self.side_length
        return poly

    def rotate(self, angle: float):
        """Returns a new regular polygon that is the result of rotating this polygon by the given angle.
        :rtype: RegularPolygon
        """
        poly = RegularPolygon()
        poly.nbr_sides = self.nbr_sides
        poly.center_x = self.center_x
        poly.center_y = self.center_y
        poly.rotation = self.rotation + angle
        poly.circumradius = self.circumradius
        poly.inradius = self.inradius
        poly.side_length = self.side_length
        return poly

    def scale(self, pcnt: float):
        """Returns a new regular polygon that is the result of scaling this polygon by the given percentage.
        :rtype: RegularPolygon
        """
        if pcnt > 1.0:
            pcnt = 1.0
        elif pcnt < 0.0:
            pcnt = 0.0
        poly = RegularPolygon.from_circumradius(self.nbr_sides, self.circumradius * pcnt, self.center_x, self.center_y, self.rotation)
        return poly

    @staticmethod
    def side_length_from_inradius(nbr_sides: int, inradius: float):
        """Computes a regular polygon's side length based upon the given inradius."""
        return 2.0 * inradius * math.tan(math.pi / nbr_sides)

    @staticmethod
    def side_length_from_circumradius(nbr_sides: int, circumradius: float):
        """Computes a regular polygon's side length based upon the given circumradius."""
        return 2.0 * circumradius * math.sin(math.pi / nbr_sides)

    @staticmethod
    def inradius_from_side_length(nbr_sides: int, side_length: float):
        """Computes a regular polygon's inradius based upon the given side length."""
        return 0.5 * side_length / math.tan(math.pi / nbr_sides)

    @staticmethod
    def inradius_from_circumradius(nbr_sides: int, circumradius: float):
        """Computes a regular polygon's inradius based upon the given circumradius."""
        return circumradius * math.cos(math.pi / nbr_sides)

    @staticmethod
    def circumradius_from_side_length(nbr_sides: int, side_length: float):
        """Computes a regular polygon's circumradius based upon the given side length."""
        return 0.5 * side_length / math.sin(math.pi / nbr_sides)

    @staticmethod
    def circumradius_from_inradius(nbr_sides: int, inradius: float):
        """Computes a regular polygon's circumradius based upon the given inradius."""
        return inradius / math.cos(math.pi / nbr_sides)

    @staticmethod
    def from_side_length(nbr_sides: int,
                         side_length: float,
                         center_x: float = 0.0,
                         center_y: float = 0.0,
                         rotation: float = 0.0):
        """Constructs a RegularPolygon using side length to compute circumradius and inradius.
        :rtype: RegularPolygon
        """
        poly = RegularPolygon()
        poly.nbr_sides = nbr_sides
        poly.center_x = center_x
        poly.center_y = center_y
        poly.rotation = rotation
        poly.side_length = side_length
        poly.inradius = RegularPolygon.inradius_from_side_length(poly.nbr_sides, side_length)
        poly.circumradius = RegularPolygon.circumradius_from_side_length(poly.nbr_sides, side_length)
        return poly

    @staticmethod
    def from_inradius(nbr_sides, inradius, center_x=0.0, center_y=0.0, rotation=0.0):
        """Constructs a RegularPolygon using inradius to compute circumradius and side length.
        :rtype: RegularPolygon
        """
        poly = RegularPolygon()
        poly.nbr_sides = nbr_sides
        poly.center_x = center_x
        poly.center_y = center_y
        poly.rotation = rotation
        poly.inradius = inradius
        poly.side_length = RegularPolygon.side_length_from_inradius(poly.nbr_sides, inradius)
        poly.circumradius = RegularPolygon.circumradius_from_inradius(poly.nbr_sides, inradius)
        return poly

    @staticmethod
    def from_circumradius(nbr_sides, circumradius, center_x=0.0, center_y=0.0, rotation=0.0):
        """Constructs a RegularPolygon using circumradius to compute circumradius and side length.
        :rtype: RegularPolygon
        """
        poly = RegularPolygon()
        poly.nbr_sides = nbr_sides
        poly.center_x = center_x
        poly.center_y = center_y
        poly.rotation = rotation
        poly.circumradius = circumradius
        poly.side_length = RegularPolygon.side_length_from_circumradius(poly.nbr_sides, circumradius)
        poly.inradius = RegularPolygon.inradius_from_circumradius(poly.nbr_sides, circumradius)
        return poly
