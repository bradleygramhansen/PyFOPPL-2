from foppl import *  # ignored by the compiler, but keeps the IDE happy

x = sample(normal(1.0, 5.0))
y = x + 1
observe(normal(y, 2.0), 7.0)
y
