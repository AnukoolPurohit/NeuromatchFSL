import numpy as np


def glm(Y,X,C=None,mask=None):
    """
        Run a general linear model

        Args:
        Y (2d array) : time-by-space data matrix
        X (2d array) : time-by-regressors design matrix
        C (2d array) : contrasts-by-regressor contrrast matrix [default=Identity]
        mask (1d array) : spatial mask wherre GLM is run

        Returns:
        contrast maps
        t-stats
    """
    if C is None:
        C = np.identity(X.shape[1])
    if mask is None:
        mask = np.ones(Y.shape[1])

    # initialise matrices
    beta    = np.zeros((X.shape[1],Y.shape[1]))
    cope    = np.zeros((C.shape[0],Y.shape[1]))
    varbeta = np.zeros_like(beta)
    tstat   = np.zeros_like(beta)

    # solve glm
    beta[:,mask>0] = np.linalg.pinv(X)@Y[:,mask>0]
    # apply contrasts
    cope[:,mask>0] = np.dot(C,beta[:,mask>0])

    # calculate uncertainty (varcope)
    r    = Y - X@beta
    dof  = X.shape[0] - np.linalg.matrix_rank(X)
    sig2 = np.sum(r**2,axis=0)/dof
    varcope = np.outer(C@np.diag(np.linalg.inv(X.T@X))@C.T,sig2)
    # calculate t-stats
    # mask = mask.astype(int)
    tstat[:,mask] = cope[:,mask] / np.sqrt(varcope[:,mask])
    return cope, tstat