""" main entry point to the package
"""

from {{cookiecutter.package_name}}.subpackage.core import generate_possible_int


def main_impl():
    """implementation of the main entry point"""
    numbers_l = [1, 2.5, 1.2, 0.1, -5.1, 10, 15.9]
    gen_value_l = generate_possible_int(numbers_l)
    print(f"the generated value is {gen_value_l}")
