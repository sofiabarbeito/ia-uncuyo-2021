from Agent import*
from Environment import*
import math

print("Backtracking 10 Reinas")
E = Environment(10)
A = Agent(E)

print(A.backtracking())
grilla = A.env.grilla
for x in range(0,8):
    print(grilla[x])


print("ForwardChecking 10 Reinas")
E = Environment(10)
A = Agent(E)

print(A.forwardChecking())
grilla = A.env.grilla
for x in range(0,8):
    print(grilla[x])
