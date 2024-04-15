import numpy as np 

def calculate_stat(data):
    """
    Calculate mean, median, and standard deviation of numerical data.

    Parameters
    ----------
    data : list of float or int
        List of numerical data.

    Returns
    -------
    dict
        Dictionary containing mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("The list cannot be empty.")

    mean = sum(data) / len(data)
    median = np.median(data)
    std = np.std(data)

    return {"mean": mean, "median": median, "std": std}
