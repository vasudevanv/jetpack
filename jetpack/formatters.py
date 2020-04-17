import re


def underscore(word):
    """
    Make an underscored, lowercase form from the expression in the string.
    
    Examples
    --------
         >>> camel_to_underscore('SpamEggsAndBacon')
        'spam_eggs_and_bacon'

        >>> camel_to_underscore('Spam_and_bacon')
        'spam_and_bacon'

    As a rule of thumb you can think of :func:`underscore` as the inverse of
    :func:`camelize`, though there are cases where that does not hold::

        >>> camelize(underscore("IOError"))
        'IoError'
    """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


def camelize(name, uppercase_first=True):
    """Convert camel case style naming to underscore style naming

    If there are existing underscores they will be collapsed with the
    to-be-added underscores. Multiple consecutive capital letters will not be
    split except for the last one.
    """
    if uppercase_first:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), string)
    else:
        return name[0].lower() + camelize(name)[1:]


def myround(x, base):
    """ Rounding values

    x: float
        Input value

    base: int
        Rounding basis
    """
    return base * round(x/base)