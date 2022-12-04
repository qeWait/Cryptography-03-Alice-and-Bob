from ECurve import ECurve

curve = ECurve(3, 4)

baseGpoint = curve.BasePointGGet()

alice_d = 3
bob_d = 6

alice_H = baseGpoint.ScalarMult(alice_d)
bob_H = baseGpoint.ScalarMult(bob_d)

compute_alice_H_by_Bob = alice_H.ScalarMult(bob_d)
compute_bob_H_by_Alice = bob_H.ScalarMult(alice_d)

compute_alice_H_by_Bob.PrintECPoint()
compute_bob_H_by_Alice.PrintECPoint()