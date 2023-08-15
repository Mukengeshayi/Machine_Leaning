import math
import statistics
import random
import os
import glob

#MATH

print(math.cos(2*math.pi))
print(math.exp(5))

#STATISTICS

list_1=[10,40,40,50,40,20]
print(statistics.mean(list_1))
print(statistics.variance(list_1))

#RANDOM

print(random.choice(list_1))
print(random.random()) #float
print(random.randint(20,40)) #int
print(random.randrange(20)) # entre o et 20
print(random.sample(range(100),15)) 
print(random.sample(range(100),random.randrange(10))) #liste aleatoire
print(random.shuffle(list_1))
