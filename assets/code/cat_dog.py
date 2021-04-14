def cat_or_dog(image):
    """
    Do something smart to the image.
    Returns a numbers to tell your confidence in the image being a cat instead of a dog.
    In this function how likely it is a cat is affected by the image brightness.
    Obviously not a good way.
    """
    result = image.sum() / image.size
    assert 0.0 <= result <= 1.0
    return result
