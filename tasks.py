from ECurve import ECurve

curve = ECurve(3, 4)

baseGpoint = curve.BasePointGGet()
baseGpoint.PrintECPoint()

a = 3
b = 6

Ha = baseGpoint.ScalarMult(a)
Hb = baseGpoint.ScalarMult(b)

compute_alice_H_by_Bob = Ha.ScalarMult(b)
compute_bob_H_by_Alice = Hb.ScalarMult(a)

compute_alice_H_by_Bob.PrintECPoint()
compute_bob_H_by_Alice.PrintECPoint()