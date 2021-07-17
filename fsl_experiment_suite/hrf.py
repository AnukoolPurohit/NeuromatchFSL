import numpy as np


def get_HRF(duration,TR,peak):
    """
        Really dumb Haemodynamic response function (not physiologically plausible)
        It simply goes up and down linearly from 0 to peak and back down

        Args:
        duration (float) : in seconds
        TR (float)       : in seconds
        peak (float)     : in seconds

        Returns:
        1D array
    """
    n = int(np.ceil(duration/TR))
    x = np.linspace(0,duration,n)
    h = np.zeros(n)
    h[x<peak]  = x[x<peak]/peak
    h[x>=peak] = (x[x>=peak]-duration)/(peak-duration)
    h = h/np.sum(h)
    return h