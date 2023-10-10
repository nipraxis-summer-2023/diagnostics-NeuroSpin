""" Module with routines for finding outliers
"""
import sys
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd

PACKAGE_DIR = Path(__file__).parent / '..'
sys.path.append(str(PACKAGE_DIR))

from findoutlie.metrics import dvars
from findoutlie.detectors import iqr_detector, zscore_detector
from findoutlie.spm_funcs import get_spm_globals


def detect_outliers(fname):
    """ Return outlier indices in fname image.

    Parameters
    ----------
    fname : str
        image path.

    Returns
    -------
    outliers : list
        List of outlier indices in image.
    """
    img = nib.load(fname)

    # compute metrics
    dvars_values = dvars(img)
    spm_values = get_spm_globals(fname)

    # compute outlier flags from detectors
    outliers_dvars_iqr = np.concatenate([[False],iqr_detector(dvars_values, iqr_proportion=3)])  # We add false for the first picture because dvars metrics is of size n-1; the first image is not analysed
    outliers_dvars_zscore = np.concatenate([[False],zscore_detector(dvars_values, 3)])

    outliers_spm_iqr = iqr_detector(spm_values, iqr_proportion=3)
    outliers_spm_zscore = zscore_detector(spm_values, 3)

    # process detectors outputs for each volume to decide whether it is an outlier
    outliers = []
    for i in range(img.shape[-1]):
        is_outlier = outliers_dvars_iqr[i] or outliers_spm_iqr[i] or outliers_dvars_zscore[i] or outliers_spm_zscore[i]
        if is_outlier:
            outliers.append(i)
    
    return outliers


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = Path(data_directory).glob('**/sub-*.nii.gz')
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
