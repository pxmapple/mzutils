def remove_elements_from_list(lst: list, elements: list):
    """
    remove elements from lst.
    """
    return [e for e in lst if e not in elements]


def pad_list(lst: list, length: int, element=''):
    """
    pad a list to length with elements.
    returned list will have length equal to length.
    """
    if len(lst) >= length:
        return lst[:length]
    
    return lst + [element for _ in range(length - len(lst))]