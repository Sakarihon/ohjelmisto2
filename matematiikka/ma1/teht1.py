import numpy as np

#tehtävä1

A=np.array([2.493,0.911])
for i in A:
    print(np.degrees(i))

#tehtävä2

A=np.array([137.7,62.3])
for i in A:
    print(np.radians(i))

#tehtävä3
A=np.array([30,45,60,90,120,135,150,180,270,360])
print(f"{"Asteet":<8}Radiaanit")
for i in A:
    print(f"{i:<9}{np.radians(i):<9.5f}")

#2tehtävän hypotenuusa tehtävä

vastaus=np.hypot(1.6, 2.2)
print(f"Hypotenuusa on {vastaus:.3f}m")
