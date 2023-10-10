""" Test script for outfind functions

Run these tests with::

    python3 findoutlie/tests/test_outfind.py

or better, in IPython::

    %run findoutlie/tests/test_outfind.py
"""

from pathlib import Path
import sys
import os

MY_DIR = Path(__file__).parent
EXAMPLE_FILENAME = 'sub-08_task-taskzero_run-01_bold.nii.gz'

CODE_DIR = (MY_DIR / '..').absolute()
sys.path.append(str(CODE_DIR))

import numpy as np

import nibabel as nib

# This import needs the directory containing the findoutlie directory
# on the Python path.
from outfind import detect_outliers, find_outliers

def test_find_outliers():
    example_dir = MY_DIR / 'test_images'
    expected_keys = [example_dir / 'sub-08_task-taskzero_run-01_bold.nii.gz']
    outlier_dict = find_outliers(example_dir)
    print(outlier_dict)
    assert outlier_dict is not None
    assert isinstance(outlier_dict, dict)
    assert list(outlier_dict.keys()) == expected_keys
    assert isinstance(outlier_dict[expected_keys[0]], list)
    assert all(isinstance(x, int) for x in outlier_dict[expected_keys[0]])


def test_detect_outliers():
    # load a real image
    example_path = MY_DIR / 'test_images' / EXAMPLE_FILENAME
    img = nib.load(example_path)

    # create fals outliers in the image volumes
    data = img.get_fdata()
    expected_outliers = [34, 58, 103]
    for index in expected_outliers:
        # we replace expected outlier volumes by random noise of same mean and std as the original volume
        data[..., index] = np.random.random_sample((data.shape[:-1]))*np.std(data[..., index]) + np.mean(data[..., index])
    
    # export image as a real nifit image
    fake_image_path = MY_DIR / 'test_images' / 'test_detect_outliers.nii.gz'
    new_img = nib.Nifti1Image(data, np.eye(4))
    nib.save(new_img, fake_image_path)

    # apply outlier detection to this fake image and check output
    outliers = detect_outliers(fake_image_path)
    assert isinstance(outliers, list)
    assert all(isinstance(x, int) for x in outliers)
    assert all(outlier in outliers for outlier in expected_outliers)

    os.remove(fake_image_path)

if __name__ == '__main__':
    # File being executed as a script
    test_detect_outliers()
    test_find_outliers()
    print('Tests passed')
