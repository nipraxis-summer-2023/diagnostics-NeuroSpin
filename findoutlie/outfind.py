""" Module with routines for finding outliers
"""
import sys
from pathlib import Path
import nibabel as nib

PACKAGE_DIR = Path(__file__).parent / '..'
sys.path.append(str(PACKAGE_DIR))

from findoutlie.metrics import dvars
from findoutlie.detectors import iqr_detector


def detect_outliers(fname):
    img = nib.load(fname)

    # find iqr outliers from dvars
    dvars_values = dvars(img)
    outliers = iqr_detector(dvars_values)

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
