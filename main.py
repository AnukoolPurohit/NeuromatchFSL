import nilearn
import numpy as np
import nibabel as nib
from fsl_experiment_suite import Path, hrf
from fsl_experiment_suite.data.utils import load_evs
from fsl_experiment_suite.glm import glm
from nilearn.glm.first_level import FirstLevelModel


DATA_DIR = Path("/home/anukoolpurohit/Documents/AnukoolPurohit/Datasets/fslcourse/fslcourse_data")


parametric_stimulus_data = load_evs("parametric")

img = nib.load(DATA_DIR/"parametric"/"fmri_data.nii.gz")

data_fmri = img.get_fdata()

parametric_stimulus_data = load_evs('parametric')
