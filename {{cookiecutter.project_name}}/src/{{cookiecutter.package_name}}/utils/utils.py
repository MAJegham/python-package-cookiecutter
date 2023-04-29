"""Utils"""

import math
import random
from typing import Any


def is_numeric(value: Any) -> bool:
    """returns true if the passed value is numeric
    Parameters
    ----------
    value : Any
        value to check if it is numeric
    Note
    ----
        Only float and int are considered numeric.
        Complex numbers are not considered numeric neither are numeric arrays.
    """
    return isinstance(value, (float, int))


def random_integer(lower: float = 0, upper: float = 100) -> int:
    r"""returns a random integer between `lower` (inclusive) and upper (exclusive)
    Parameters
    ----------
    lower : float or int, defaults to 0
        the lower bound for generated values
    upper : float or int, defaults to 100
        the exclusive upper bound for generated values

    Raises
    ------
    TypeError
        if the input is not numeric
    ValueError
        if the lower bound is greater than the upper bound

    Examples
    --------
    >>> random_integer(0, 10)
        9
    >>> random_integer()
        57
    >>> random_integer(99)
        99
    """
    if not is_numeric(lower):
        raise TypeError(f"lower ({lower}) needs to be numeric.")
    if not is_numeric(upper):
        raise TypeError(f"upper ({upper}) needs to be numeric.")
    if lower > upper:
        raise ValueError(
            f"lower ({lower}) needs to be less or equal to upper ({upper})."
        )
    lower_l: int = math.ceil(lower)
    upper_l: int = math.ceil(upper)
    rand_value_l: int = random.randint(lower_l, upper_l)
    return rand_value_l
