import numpy as np


def get_events(parametric_dict):
    """
    Converts the dictionary of parametric data into a list containing the task being done at each time point
    :return:
    events: a list containing the task state at each time point
    """
    keys = list(parametric_dict.keys())
    events = [None] * len(list(parametric_dict[keys[0]]))
    for key in keys:
        data = parametric_dict[key]
        data = list(np.bool_(data))
        for index, data_point in enumerate(data):
            if data_point:
                events[index] = key

    cleaned_events = []
    for event in events:
        if not event:
            cleaned_events.append("Transition_State")
        else:
            cleaned_events.append(event)
    return cleaned_events
