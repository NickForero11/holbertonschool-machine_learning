#!/usr/bin/env python3
"""Module to perform any convolution on grayscale images.
"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Performs any convolution on grayscale images.

    Arguments:

        images (numpy.ndarray):             an array with shape (m, h, w)
                                            containing multiple grayscale
                                            images, where:
                                                - m is the number of images.
                                                - h is the height in pixels of
                                                the images.
                                                - w is the width in pixels of
                                                the images.

        kernel (numpy.ndarray):             an array with shape (kh, kw)
                                            containing the kernel for the
                                            convolution, where:
                                                - kh is the height of the
                                                kernel.
                                                - kw is the width of the
                                                kernel.

        padding (tuple(int, int) or str):   a tuple of (ph, pw) where:
                                                - if ‘same’, performs a same
                                                convolution.
                                                - if ‘valid’, performs a valid
                                                convolution.
                                                - if a tuple:
                                                    * ph is the padding for
                                                    the height of the image.
                                                    * pw is the padding for
                                                    the width of the image.
                                                - the image should be padded
                                                with 0’s.

        stride (tuple (int, int)):          a tuple of (sh, sw) where:
                                                - sh is the stride for the
                                                height of the image.
                                                - sw is the stride for the
                                                width of the image.

    Take in account that the image will be padded with 0’s

    Returns:
        numpy.ndarray: an array containing the convolved images.
    """
    # Save Dimmensions
    kh, kw = kernel.shape
    sh, sw = stride

    # Compute padding if needed
    if padding in ('same', 'valid'):
        if padding == 'same':
            (m, h, w) = images.shape
            pw = int(np.ceil((((w - 1) * sw) + kw - w) / 2))
            ph = int(np.ceil((((h - 1) * sh) + kh - h) / 2))
        else:
            (ph, pw) = (0, 0)
    else:
        (ph, pw) = padding

    # Apply padding to images
    padded_images = np.pad(
        images,
        [(0, 0), (ph, ph), (pw, pw)]
    )

    # Compute shape of the outputs
    (m, h, w) = padded_images.shape
    output_shape = (m, int(((h - kh) / sh) + 1), int(((w - kw) / sw) + 1))

    # Make output template
    output = np.zeros(output_shape)

    # Fill template
    for row in range(output_shape[1]):
        for column in range(output_shape[2]):
            # Split the part that you need from every image
            sub_matrix = padded_images[
                :,
                (row * sh): (row * sh) + kh,
                (column * sw): (column * sw) + kw
            ]
            # Apply the kernel and sum every resultant matrix to get
            # the convolution value in that point for every image
            output[:, row, column] = (sub_matrix * kernel).sum(axis=(1, 2))

    return output
