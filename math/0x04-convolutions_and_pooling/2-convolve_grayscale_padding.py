#!/usr/bin/env python3
"""Module to perform a valid convolution on grayscale images
with custom padding.
"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Performs a valid convolution on grayscale images with custom padding.

    Arguments:
        images (numpy.ndarray):     an array with shape (m, h, w)
                                    containing multiple grayscale images,
                                    where:
                                        - m is the number of images.
                                        - h is the height in pixels of the
                                        images.
                                        - w is the width in pixels of the
                                        images.
        kernel (numpy.ndarray):     an array with shape (kh, kw)
                                    containing the kernel for the convolution,
                                    where:
                                        - kh is the height of the kernel.
                                        - kw is the width of the kernel.
        padding (tuple(int, int)):  a tuple of (ph, pw) where:
                                        - ph is the padding for the height of
                                        the image.
                                        - pw is the padding for the width of
                                        the image.

    Take in account that the image will be padded with 0’s

    Returns:
        numpy.ndarray: an array containing the convolved images.
    """
    # Save Dimmensions
    (ph, pw) = padding
    kh, kw = kernel.shape
    # Apply padding to images
    padded_images = np.pad(
        images,
        [(0, 0), (ph, ph), (pw, pw)]
    )
    m, h, w = padded_images.shape
    # Make output template
    output_shape = (m, h - kh + 1, w - kw + 1)
    output = np.zeros(output_shape)
    # Fill template
    for row in range(output_shape[1]):
        for column in range(output_shape[2]):
            # Split the part that you need from every image
            sub_matrix = padded_images[:, row: row + kh, column: column + kw]
            # Apply the kernel and sum every resultant matrix to get
            # the convolution value in that point for every image
            output[:, row, column] = (sub_matrix * kernel).sum(axis=(1, 2))

    return output
