import numpy as np

sample=100000
#Here I am assuming a coordinate plane with coordinate axes. And taking random values for the coordinates using random.
count=0
i=0
while i<sample:
  x = np.random.uniform(low=0, high=9)#Taking a random value for x-coordinate.
  y = np.random.uniform(low=0, high=4.5)#taking a random value for y-coordinate.
  if x>6.0 and y>2.0:#Checking whether the point is in the lake or not and altering the count accordingly.
    count+=1
  i+=1


     
Pr= count/ sample         #calculation of Pr= no. of points in the lake/total no.of points in the rectangle
print("probability that the helicopter crashed inside the lake = ", Pr)