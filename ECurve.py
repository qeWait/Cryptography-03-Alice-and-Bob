from ECPoint import ECPoint

class ECurve:
    def __init__(self, a, b) -> None:
        self.ValidateECurve(a, b)
        self.a = a
        self.b = b

    def ValidateECurve(self, a, b):
        if (a == 0 and b == 0):
            raise ValueError('Такої еліптичної кривої не існує.')

    def AddECPoints(self, P: ECPoint, Q: ECPoint) -> ECPoint:
        m = (P.y - Q.y) / (P.x - Q.x)

        x = m**2 - P.x - Q.x
        y = P.y + m * (x - P.x)

        return ECPoint(int(x), int(y))

    def EquationToString(self):
        return f'Рівняння еліптичної кривої: y^2 = x^3 + {self.a}x + {self.b}'

    def PrintEquation(self) -> None:
        print(self.EquationToString())

    def BasePointGGet(self) -> ECPoint:
        x = (self.a**self.b * self.b**self.a) / self.b * self.a + self.a**self.a
        y = (self.b**self.a * self.a**self.b) * self.b + self.a * self.b**self.a

        return ECPoint(int(x), int(y))