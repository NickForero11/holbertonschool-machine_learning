#!/usr/bin/env python3
"""Module to perform a same convolution on grayscale images.
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images.

    Arguments:
        images (numpy.ndarray): an array with shape (m, h, w)
                                containing multiple grayscale images,
                                where:
                                    - m is the number of images.
                                    - h is the height in pixels of the images.
                                    - w is the width in pixels of the images.
        kernel (numpy.ndarray): an array with shape (kh, kw)
                                containing the kernel for the convolution,
                                where:
                                    - kh is the height of the kernel.
                                    - kw is the width of the kernel.

    Returns:
        numpy.ndarray: an array containing the convolved images.
    """

    # Save Dimmensions
    kh, kw = kernel.shape
    m, h, w = images.shape
    # Calculate padding for width and height
    pw = int(kw / 2 if kw % 2 == 0 else (kw - 1) / 2)
    ph = int(kh / 2 if kh % 2 == 0 else (kh - 1) / 2)
    # Apply padding to images
    padded_images = np.pad(
        images,
        [(0, 0), (ph, ph), (pw, pw)]
    )
    # Create template
    output = np.zeros(images.shape)
    # Fill template
    for row in range(h):
        for column in range(w):
            # Split the part that you need from every image
            sub_matrix = padded_images[:, row: row + kh, column: column + kw]
            # Apply the kernel and sum every resultant matrix to get
            # the convolution value in that point for every image
            output[:, row, column] = (sub_matrix * kernel).sum(axis=(1, 2))

    return output
