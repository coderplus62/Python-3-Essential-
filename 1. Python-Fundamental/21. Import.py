from science_package import physics_module as p

s = p.speed(d=80,t=2)
a = p.acceleration(v=s,u=0,t=0.5)
f = p.force(m=20,a=a)

from science_package.physics_module import circle_area as area, pressure as p
# from physics_module import * (* means take a all)
area = area(7)
pressure = p(f=f,a=area)