import pylab as pl
import numpy as np

# setup time domain
tmin,tmax = 0,10
delta = 0.01
nsteps = (tmax-tmin)/delta
times = np.linspace(tmin,tmax,int(nsteps))
print('tmin =',tmin)
print('tmax =',tmax)
print('nsteps =', nsteps)

# parameters
P0 = 10000 # initial condition
mu = 1 # growth rate
Panalytical = P0*np.exp(mu*times)

# figure
f,ax=pl.subplots()
ax.set_xlabel('Time (days)')
ax.set_ylabel('Cells (ml$^{-1}$)')
ax.plot(times,Panalytical,label='Analytical solution')
pl.show()

f.savefig('../figures/exponential_growth')
