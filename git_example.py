```
This python file si a goood starting pouint.
Activation Funstions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  # enter code below
  return ((1-numpy.exp(-2*x))/(1+numpy.exp(-2*x)))
  
def relu(x):
  # entr code below
  if x > 0:
    return 0
  else:
    return x
  
