"""
string_util.py
A sample repo for the MolSSIworkshop at UF

Misc.string pocessing function
"""
def title_case(sentence):
    """
    Convert a string to title case.

    Parameters
    ---------
    sentence:string
        string to b converted to title case
    Returns
    ---------
    title_case_sentence : string
        String converted to title case
    Example
    ---------
    """
    #a = sentence.lower()
    #title_case_sentence = a.capitalize()
    if not isinstance(sentence,str):
        raise TypeError('Invalid input %s - Input must be type string' %(sentence))

    #error if empty string
    #if isinstance(sentence,' '):
    #    raise TypeError('Invalid input %s - Input must not be empty' %(sentence))
    if len(sentence) == 0:
        raise ValueError('Cannot apply title function to empty string.')
    
    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i-1] == ' ':
            ret += sentence[i].upper()
        else:
            ret += sentence[i].lower()

    return ret
