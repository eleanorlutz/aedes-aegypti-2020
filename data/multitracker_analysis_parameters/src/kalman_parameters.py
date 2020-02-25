import numpy as np

### Define kalman filter properties ########
phi = np.matrix([                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

H   = np.matrix([                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
P0  = 10*np.eye(10)
Q   = 40*np.matrix(np.eye(10)) # originally 0.2
# Q = how much the tracker relies on a constant velocity model
# lower is more reliance
R   = 2*np.matrix(np.eye(5)) # originally 50
# R = how much the tracker relies on the actual data
# lower is more reliance

gamma  = None
gammaW = None

max_covariance = 60
max_velocity = 10000

association_matrix = np.matrix([[1,1,0,0,0]], dtype=float).T
association_matrix /= np.linalg.norm(association_matrix)
