from typing import List, Tuple, Sequence


def get_fmri_chunk_indices(sequence: Sequence) -> List[Tuple[int, int]]:
    flag_entered_chunk = False
    indices = []
    sequence = list(sequence)
    sequence += [0]
    for i, number in enumerate(sequence):
        if number == 1 and not flag_entered_chunk:
            first_index = i
            flag_entered_chunk = True
        elif number == 0 and flag_entered_chunk:
            indices.append((first_index, i))
            flag_entered_chunk = False
    return indices
