import numpy as np
from ..path import Path


DATA_DIR = Path("/home/anukoolpurohit/Documents/AnukoolPurohit/Datasets/fslcourse/fslcourse_data")


EXPERIMENTS = {
    'fluency':
        {
            'TR': 4.2,  # time resolution in seconds
            'ntimes': 106,  # number of time points
            'EVs': ['Gen', 'Shad']  # conditions
        },
    'parametric':
        {
            'TR': 0.933,
            'ntimes': 1100,
            'EVs': ['WPM_0050', 'WPM_0350', 'WPM_0650', 'WPM_0950', 'WPM_1250']
        }

}


def load_evs(exp):
  """Load EVs (explanatory variables) data for one task experiment.

  Args:
    experiment (str) : Name of experiment

  Returns
    evs (dict)

  """
  TR = EXPERIMENTS[exp]['TR']
  EVs = []
  for ev in EXPERIMENTS[exp]['EVs']:
    ev_file  = f"{DATA_DIR}/{exp}/EVs/{ev}.txt"
    ev_array = np.loadtxt(ev_file, ndmin=2, unpack=True)
    ev       = dict(zip(["onset", "duration", "amplitude"], ev_array))
    # Determine when trial starts, rounded down
    start = np.floor(ev["onset"] / TR).astype(int)
    # Use trial duration to determine how many frames to include for trial
    duration = np.ceil(ev["duration"] / TR).astype(int)
    # Take the range of frames that correspond to this specific trial
    frames = [s + np.arange(0, d) for s, d in zip(start, duration)]
    a = np.zeros(EXPERIMENTS[exp]['ntimes'])
    for frame in frames:
      a[frame] = 1
    EVs.append(a)

  return dict(zip(EXPERIMENTS[exp]['EVs'],EVs))