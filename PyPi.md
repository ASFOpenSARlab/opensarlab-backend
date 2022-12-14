# Steps to build and upload to PyPi

*The following assumes a Unix-like environment.*

Following the instructions at https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

Starting at the root of this repo...

1. Create and activate a python environment

```
python3 -m venv sandbox
source sandbox/bin/activate
```

1. Install "twine" and "build"

```
python3 -m pip install twine build
```

1. Make sure `setup.py` is ready. Watch for the version number.

1. Change into setup.py directory

```
cd opensarlab-backend
```

1. Build Python wheel. If rebuilding, you might need to remove the previous build artifacts in dist/.

```
python3 -m build --wheel
```

1. Check integrity of build with "twine"

```
twine check dist/*
```

1. If needed, create a PyPi account. 

1. Create new API token.

    https://pypi.org/manage/account/#api-tokens

    Save this token locally `$HOME/.pypirc`:

    ```
    [pypi]
    username = __token__
    password = <the token value, including the `pypi-` prefix>
    ```

1. Push to PyPi

```
twine upload dist/*
```