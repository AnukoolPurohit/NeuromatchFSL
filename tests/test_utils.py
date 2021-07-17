import pytest
import random
import numpy as np
from fsl_experiment_suite.utils import get_fmri_chunk_indices


@pytest.mark.parametrize("input_sequence, output_indices",
                         [
                          (np.array([0., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1., 1., 1.]),
                           [(4, 7), (10, 13)]),

                          (np.array([1., 1., 1., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 1.]),
                           [(0, 4), (7, 10), (13, 14)]),
                          ]
                         )
def test_get_fmri_chunk_indices(input_sequence, output_indices):
    assert get_fmri_chunk_indices(input_sequence) == output_indices
    index = random.choice(output_indices)
    chunk = input_sequence[index[0]: index[1]]
    assert len(chunk) == sum(chunk)
    if index[0] > 0:
        assert input_sequence[index[0]-1] == 0
    if index[1] < len(input_sequence):
        assert input_sequence[index[1]+1] == 0
    return
