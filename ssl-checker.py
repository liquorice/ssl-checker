#!/usr/bin/env python3
import os
import json
import socket
import ssl
from datetime import datetime
from datetime import timedelta
import click


@click.group()
def cli():
    pass


@click.command()
@click.argument("hostname")
@click.option("--port", default=443, help="Port to test. Defaults to 443.")
def ssl_checker(hostname, port=443):
    check_ssl(hostname, port)


def check_ssl(hostname, port=443):
    """Check current expiry date of certificate.

    :param hostname: String. Hostname, ie google.com
    :param port: Int. Port to check. Defaults to `443`
    :return: `notAfter` value of certificate
    :rtype: datetime object
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=1) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                data = ssock.getpeercert()
    except:
        click.secho(f"{hostname} timed out", fg="red")
        return
    expiry = datetime.strptime(data["notAfter"], "%b %d %H:%M:%S %Y %Z")
    now = datetime.utcnow()
    expiries_in = expiry - now
    colour = "green"
    if expiries_in.days < 14:
        colour = "red"
    click.secho(
        "{} expires in {} days on {}".format(hostname, expiries_in.days, expiry),
        fg=colour,
    )
    return data["notAfter"]


@click.command()
def check_all_ssl():
    """Checks all SSL in CHECK_HOSTS environment variable."""
    try:
        import config

        hosts = config.CHECK_HOSTS
    except ImportError:
        click.secho(
            "Please create config.py file with a CHECK_HOSTS variable.", fg="red"
        )
        return
    except AttributeError:
        click.secho(
            "Please make sure you config.py file has a CHECK_HOSTS variable.", fg="red"
        )
        return

    for hostname in config.CHECK_HOSTS:
        check_ssl(hostname)


cli.add_command(ssl_checker)
cli.add_command(check_all_ssl)


if __name__ == "__main__":
    cli()
