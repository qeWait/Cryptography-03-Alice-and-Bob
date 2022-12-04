class ECPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def ECPointToString(self) -> str:
        return f"[{round(self.x, 1)}, {round(self.y, 1)}]"

    def PrintECPoint(self) -> None:
        print(self.ECPointToString())

    def DoubleECPoint(self, curve):
        x = ( (3*self.x**2 + curve.a) / (2*self.y) )**2 - 2*self.x
        y = -self.y + ( (3*self.x**2 + curve.a) / (2*self.y) ) * (self.x - x)

        return ECPoint(int(x), int(y))

    def ScalarMult(self, n: int):
        if not 0 <= n <= 9:
            raise ValueError(f'{n} не є натуральним числом.')
        x = self.x * n
        y = self.y * n

        return ECPoint(int(x), int(y))

    def IsOnCurveCheck(self, curve):
        return self.y**2 == int((self.x**3 + curve.a*self.x + curve.b))