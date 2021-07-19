import nilearn
import numpy as np
import nibabel as nib
from fsl_experiment_suite import Path, hrf
from fsl_experiment_suite.data.utils import load_evs, EXPERIMENTS
from fsl_experiment_suite.data.core import get_events
from nilearn.decoding import Decoder
from nilearn.decomposition import CanICA
from nilearn.glm.first_level import FirstLevelModel
from nilearn import image

DATA_DIR = Path("/home/anukoolpurohit/Documents/AnukoolPurohit/Datasets/fslcourse/fslcourse_data")

EXPERIMENT_TYPE = "parametric"
TR = EXPERIMENTS[EXPERIMENT_TYPE]["TR"]


parametric_stimulus_data = load_evs(EXPERIMENT_TYPE)
events = get_events(parametric_stimulus_data)

fmri_img = nib.load(DATA_DIR/EXPERIMENT_TYPE/"fmri_data.nii.gz")

# decoder = CanICA(t_r=TR, standardize=True, verbose=3)
# decoder.fit(fmri_img, events)

model = FirstLevelModel(t_r =TR, verbose=10, standardize=True)
model.fit(image.iter_img(fmri_img), events)
