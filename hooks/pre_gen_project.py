#!usr/bin/env python
import re

def check_regex(regex_p, str_p):
    return re.match(regex_p, str_p)

def check_project_name(project_name_p):
    """names accepted by PyPI"""
    PACAGE_REGEX = r'^[a-zA-Z][a-zA-Z0-9_-]*$'
    if not check_regex(PACAGE_REGEX, project_name_p):
        raise ValueError(f"The package name `{project_name_p}` is not valid. Name must follow this regex : {project_name_p}")

def check_package_name(package_name_p):
    """names accepted by PyPI"""
    PACAGE_REGEX = r'^[a-zA-Z][a-zA-Z0-9_]*$'
    if not check_regex(PACAGE_REGEX, package_name_p):
        raise ValueError(f"The package name `{package_name}` is not valid. Name must follow this regex : {package_name}")


if __name__ == "__main__":
    project_name = "{{ cookiecutter.project_name }}"
    check_project_name(project_name)

    package_name = "{{ cookiecutter.package_name }}"
    check_package_name(package_name)
