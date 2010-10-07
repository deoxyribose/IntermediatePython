import numpy as np
import scipy as sp
from scipy import stats

beta = sp.stats.beta
n = 20
data = beta.rvs(0.3, 0.7, size = n)
# print data
true_mean = np.median(data)

