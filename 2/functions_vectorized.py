import numpy as np


def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """
    x = x.diagonal()
    x = x[np.nonzero(x)]
    return x.prod()
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Vectorized implementation.
    """
    x.sort()
    y.sort()
    return np.all(x == y)
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Vectorized implementation.
    """
    z = np.where(x == 0)[0] + 1
    x = np.append(x, x.min())
    return x[z].max()
    pass

def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x num_channels)
    coefs -- 1-d numpy array (length num_channels)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """
    img = np.multiply(img[:, :], coefs)
    #print(img)
    return np.sum(img, axis = 2)
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """
    n = len(x)
    starts = np.r_[0, np.flatnonzero(~(x[1:] == x[:-1])) + 1]
    lengths = np.diff(np.r_[starts, n])
    values = x[starts]
    return values, lengths
    pass

#    return np.linalg.norm(a - b)

def substract_vect(a, b):
    return a - b

def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vectorized implementation.
    """
    n = x.shape[0]
    m = y.shape[0]
    k = x.shape[1]
    a = np.repeat(x, m, axis=0).reshape(n, m, k) 
    b = np.repeat(y[:][np.newaxis][:], n, axis=0)
    z = a - b 
    return np.apply_along_axis(np.linalg.norm, 2, z)  