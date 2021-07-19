import numpy as np
from fsl_experiment_suite.data.core import get_events


def test_get_events():
    """
    Tests the get event function
    """
    parametric_dict = {"WPM1": np.array([0., 0., 0., 1., 0.]),
                       "WPM2": np.array([1., 0., 0., 0., 0.]),
                       "WPM3": np.array([0., 0., 1., 0., 0.]),
                       "WPM4": np.array([0., 0., 0., 0., 1.])}
    events = ["WPM2", "Transition_State", "WPM3", "WPM1", "WPM4"]

    assert get_events(parametric_dict) == events
    return
