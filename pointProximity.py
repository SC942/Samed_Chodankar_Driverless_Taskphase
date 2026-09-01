import math

class pointProximity:
    def sortCoords(self, coords, refPoint):
        return sorted(
            coords,
            key = lambda p: math.hypot(p[0] - refPoint[0], p[1] - refPoint[1])
        )