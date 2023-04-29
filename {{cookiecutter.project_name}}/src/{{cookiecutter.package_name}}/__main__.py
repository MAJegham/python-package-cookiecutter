"""main script exected when using `python -m {{cookiecutter.package_name}}`"""

from {{cookiecutter.package_name}}._main import main_impl

if __name__ == "__main__":
    print("pass through __main__.py")
    main_impl()
