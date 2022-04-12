import numpy as np
import pandas as pd
import pylab as pl

control_df = pd.read_csv('../data/phaeocystis_control.csv')
infection_df = pd.read_csv('../data/phaeocystis_PgV_one_step.csv')

f,ax = pl.subplots()
ax.plot(control_df.time,control_df.host)

ax.set_xlabel('Time (days)')
ax.set_ylabel('Abundance (ml$^{-1}$)')

pl.show()



