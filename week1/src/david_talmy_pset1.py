import pylab as pl
import numpy as np

# setup figure
py, ax = pl.subplots()
ax.plot()
pl.show()

# setup time domain
tmin,tmax = 0,10
delta = 0.01
nsteps = (tmax-tmin)/delta
times = np.linspace(tmin,tmax,nsteps)
print('tmin =',tmin)
print('tmax =',tmax)
print('nsteps =', nsteps)

