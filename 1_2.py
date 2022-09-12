from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # Representation 표현하다
        return "Vector(%r, %r)" % (self.x, self.y)

    # 사용자가 이해할 수 있는 객체의 모습을 표현한다.
    # 어떤 객체의 '출력될 수 있는 표현'을 문자열의 형태로 반환한다.

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
