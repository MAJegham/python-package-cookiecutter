"""Core"""

from typing import Iterable, Tuple

from {{cookiecutter.package_name}}.subpackage import formulas as my_f
from {{cookiecutter.package_name}}.utils.utils import random_integer


def learn_bounds(numbers: Iterable[float]) -> Tuple[float, float]:
    """learns the generation bounds based on the input list of numbers
    Parameters
    ----------
    numbers : Iterable of floats
        processed values to base generation on.
    """
    numbers_l = [my_f.transform(number_t) for number_t in numbers]
    lb_l = min(numbers_l)
    ub_l = max(numbers_l)
    return lb_l, ub_l


def generate_possible_int(numbers: Iterable[float]) -> int:
    """generates an integer based on some implemented rule and the values provided in an input list
    Parameters
    ----------
    numbers : Iterable of floats
        processed values to base generation on.
    """
    lb_l, ub_l = learn_bounds(numbers)
    print(f"the computed bounds are {lb_l} and {ub_l}")
    return random_integer(lb_l, ub_l)
