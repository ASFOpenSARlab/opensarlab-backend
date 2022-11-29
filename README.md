# opensarlab-backend

## Intro

OpenSARLab is a customized JupyterHub instance running in AWS and operated by the Alaska Satellite Facility (ASF). The purpose of OpenSARLab is make Synthetic Aperture Radar (SAR) data more accessible.

This Python library is for common code used in the backend of OpenSARLab that would be better served in a pip-able package.

It is intended that these code can be found on PyPi: 

```
python3 -m pip install opensarlab-backend
```

## Auth Package

### Module: encryptedjwt

```
from opensarlab.auth import encryptedjwt
```

Take data, encode into a jwt token, and encrypt the token. Also decrypt the token and decode the data.

The encode/encrypt secret is by default found at `/run/secrets/sso_token`. If not found there, then it will check for the path to the token defined in the environment variable `OPENSARLAB_SSO_TOKEN_PATH`.

This module safely allows the sharing of JupyterHub user information between separate servers/containers.
