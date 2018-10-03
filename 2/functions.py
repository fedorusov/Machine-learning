def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    ans = 1
    n = min(len(x), len(x[0]))
    for i in range(0, n):
        if x[i][i] != 0:
            ans *= x[i][i]
    return ans
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x = sorted(x)
    y = sorted(y)
    n = len(x)
    if n != len(y):
        return False
    for i in range(0, n):
        if x[i] != y[i]:
            return False
    return True
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    n = len(x)
    mx = 0
    b = True
    for i in range(1, n):
        if x[i - 1] == 0:
            if b:
                b = False
                mx = x[i]
            elif x[i] > mx:
                mx = x[i]
    return mx
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x num_channels)
    coefs -- 1-d numpy array (length num_channels)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    H = len(img)
    W = len(img[0])
    C = len(img[0][0])
    ans = [[0 for i in range(W)] for j in range(H)]
    for i in range (0, H):
        for j in range (0, W):
            cur = 0
            for k in range(0, C):
                cur += img[i][j][k] * coefs[k]
            ans[i][j] = cur
    return ans
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    n = len(x)
    ansx, ansy = list(), list()
    cur = 1
    for i in range(1, n):
        if x[i] != x[i - 1]:
            ansx.append(x[i - 1])
            ansy.append(cur)
            cur = 1
        else:
            cur += 1
    ansx.append(x[n - 1])
    ansy.append(cur)
    return (ansx, ansy)
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    n = len(x[0])
    kx = len(x)
    ky = len(y)
    ans = [[0 for j in range(0, ky)] for i in range(0, kx)]
    for i in range(0, kx):
        for j in range(0, ky):
            cur = 0
            for z in range(0, n):
                cur += (x[i][z] - y[j][z]) ** 2
            ans[i][j] = cur ** 0.5
    return ans
    pass