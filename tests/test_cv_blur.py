import numpy as np

from dltools.cv.blur import generate_kernel, generate_psf


def test_generate_kernel_shape_and_sum() -> None:
    kernel = generate_kernel(15)
    assert kernel.shape == (15, 15)
    assert np.isclose(kernel.sum(), 1.0)


def test_generate_psf_sum_and_anchor() -> None:
    psf, anchor = generate_psf(length=21, angle=15.0)
    assert psf.ndim == 2
    assert psf.shape[0] > 0
    assert psf.shape[1] > 0
    assert isinstance(anchor, tuple)
    assert len(anchor) == 2
    assert np.isclose(psf.sum(), 1.0)
