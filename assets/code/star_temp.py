def star_temperature(image):
    """
    This function looks just like `cat_or_dog` but is actually different
    since the return value does not have a range.
    """
    return 10000 * image.sum() / image.size
