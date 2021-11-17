# Confusing Frequencies
### A Computational neuroscience project for Neuromatch Academy
Human performance on a word recognition task should degrade with higher word frequency. In our project, we try to investigate plausible reasons behind it. We hypothesize that this involves the Visual Word form area and Visual regions of the brain. We have a couple of hypotheses on this: 
either the VWFA cannot function properly at higher word frequency or
The Visual region cannot provide proper signals to the brain at a higher frequency because of seeing blurry images.

We will test this hypothesis out by looking at the relationship between the bold response and the words per minute frequency in the VWFA. We will use a GLM to encode the stimulus signals and then plot the relationship between the weights for the voxels in the VWFA and visual regions with the frequencies. We believe the relationship should either be an inverted U curve if the VWFA degrades at higher word frequencies or a linearly increasing relationship if the VWFA actually pays more attention to recognize words even at the higher frequencies.

## Work in progress