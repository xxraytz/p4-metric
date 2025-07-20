import numpy as np

def p4_metric(conf_matrix: np.ndarray) -> float:
    """
    Compute the P4 metric based on the paper Harmonic Averaging in Classifier Quality Assessment.
    The link: https://link.springer.com/article/10.1134/S1054661824701220

    Parameters
    ----------
    conf_matrix : np.ndarray, shape (K, K)
        Confusion matrix for K classes.

    Returns
    -------
    float
        The P4 score.
    """

    if conf_matrix.ndim != 2 or conf_matrix.shape[0] != conf_matrix.shape[1]:
        raise ValueError("Input must be a square confusion matrix.")

    tp = np.diag(conf_matrix).astype(float)
    fp = conf_matrix.sum(axis=0) - tp
    fn = conf_matrix.sum(axis=1) - tp
    total = conf_matrix.sum()
    tn = total - (tp + fp + fn)

    # ignore division-by-zero and invalid warnings
    with np.errstate(divide='ignore', invalid='ignore'):
        inv_terms = (1 / tp) + (1 / tn)
        p_vals = 4 / (inv_terms * (fp + fn) + 4)
    
    # replace any NaN or infinite values with 0
    p_vals = np.nan_to_num(p_vals, nan=0.0, posinf=0.0, neginf=0.0)

    k = conf_matrix.shape[0]
    return k / np.sum(1 / p_vals)