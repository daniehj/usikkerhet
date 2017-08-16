# usikkerhet

A script module for calculating uncertainties in python. Uses two vectors and calculates the uncertainties and prints them.
Can also make a plot with a linear regression.

### Prerequisites

For running usikkerhet you need:

Pylab

### Installing

To install the python modules:

```
pip install pylab
```

For use of the module, put usikkerhet.py in your python site-packages dir

```
%PYTHON_PATH%\Lib\site-packages\
```


## Usage

Import module

```
import usikkerhet
```

Call module, use two-vectors, add plot if plot figure with linear regression needed

```
usikkerhet(x,y,plot)
```

### Example and screenshot

Uses two vectors and takes a lienaer regression

```python
x = [somevector]
y = [somevector]

usikkerhet(x,y,plot)
```

And we get the answer

```
>
linear regression: -1.493143x + 8.811429
Delta m:  0.014331355662
Delta c:  0.0216951670224
```

![Plot with linearregression]()
