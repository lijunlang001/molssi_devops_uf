"""
molssi_math.py
A sample repository for MolSSI workshop at UF

Some math functions.
"""
def mean(num_list):
    """
    calculate the mean/average ogf a list of numbers

    Parameters
    -----------
    num_list : list
        The list to take the average of

    Returns
    ----------
    mean_list : float
        The mean of the list
    """
    #check that input is type list


    if not isinstance(num_list, list):
        raise TypeError('Invalid input %s - Input must be a list')

    #check that list is not empty
    if len(num_list) == 0:
        raise ValueError('Cannot apply mean function to empty list.'%(num_list))

    try:
        mean_list = sum(num_list)/len(num_list)
    except:
        raise TypeError('Cannot calculate mean of a list - all list elements should be numeric')



    mean_list = sum(num_list) / len(num_list)

    return mean_list


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
