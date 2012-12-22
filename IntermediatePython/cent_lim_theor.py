import numpy as np
import scipy as sp
from scipy import stats
from pylab import plot, show,hist,clf
sim_size = 10000
unirv = sp.stats.uniform.rvs
sim = unirv(size=sim_size)
print sim.mean(), sim.var()
# Show Law of Large Numbers
x = np.arange(sim_size)
plot(x,0.5*np.ones(len(x)))
plot(x,sp.cumsum(sim)/x)
#show()
# Show central limit theorem
row = 10
col = 5000
# An array of uniform(0,1) distributed random numbers is reshaped into a row x col matrix
sim2 = unirv(0,1,size=row*col).reshape(row,col)
clf() # Erase plot window
hist(sim2.mean(0),bins=(np.linspace(-1,1,2000))) #plot histogram of means of the columns.
show()
# It can be seen that the histogram follows a rough normal distribution, centered around the mean 0.5.
