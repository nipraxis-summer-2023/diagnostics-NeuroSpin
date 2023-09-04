""" Scan outlier metrics
"""

# Any imports you need
# +++your code here+++

import numpy as np


def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    # This is a placeholder, replace it to write your solution.

    return np.sqrt(np.mean((np.diff(img.get_fdata()))**2, axis=(0,1,2)))

    ## equivalent to :
    # data = img.get_fdata()
    # dvar_val_list = []
    # for i in range(data.shape[-1]-1): #ajout -1 pour éviter out of range dans data[...,i+1]
    #     data_1=data[...,i]
    #     data_2=data[...,i+1]
    #     dvar_val_list.append(np.sqrt(np.mean((data_1 - data_2)**2)))
    
    # return dvar_val_list
    
    raise NotImplementedError('Code up this function')
