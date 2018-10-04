#!/usr/bin/env python
"""Authenticate with FMC and get a token to be used in subsequent API calls."""

import requests
import requests.auth


# Providing hostnames and access credentials in your source code is okay for
# learning, not for production.  We recommend getting information like this
# from the environment, CLI input, or from a configuration file.
FMC_HOST = "10.19.66.126"
FMC_PORT = "40003"
FMC_USER = "apiuser"
FMC_PASSWORD = "C1sc0123"

FMC_LOGIN_URL = "https://{host}:{port}/api/fmc_platform/v1/auth/generatetoken"


def get_auth_token(username, password, host, port):
    """Authenticate with FMC and get a token."""
    login_url = FMC_LOGIN_URL.format(hostname=host, port=port)
    headers = {'Content-Type': 'application/json'}
    authentication = requests.auth.HTTPBasicAuth(username, password)

    response = requests.post(
        url=login_url,
        headers=headers,
        auth=authentication,
        verify=False,
    )
    response.raise_for_status()

    token = response.headers.get('X-auth-access-token')

    return token


if __name__ == "__main__":
    auth_token = get_auth_token(FMC_USER, FMC_PASSWORD, FMC_HOST, FMC_PORT)
    print(
        """
        Successfully authenticated to FMC {host}
        Received Auth Token: {auth_token}
        """.format(
            host=FMC_HOST,
            auth_token=auth_token,
        )
    )
