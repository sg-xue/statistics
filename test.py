import numpy as np

data1 = [1, 3, 5, 7]
print np.mean(data1)
print np.std(data1)

data2 = [2, 4, 6, 8]
print np.mean(data2)
print np.std(data2)

data = np.array([data1, data2])
data_cov = np.cov(data,bias=1)
print data_cov

print np.corrcoef(data)

