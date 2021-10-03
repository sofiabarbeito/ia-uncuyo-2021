import random
from algo1 import*

class Environment:
    def __init__(self,reinas):
        self.reinas = reinas
        self.grilla = Array(reinas,Array(reinas))

