# SSL Checker

An internal tool for checking site SSL Certificate expiry. Ideally it would be run once a fortnight.

## Commands

- `ssl_checker <domain name>`
- `check_all_ssl`

## In docker

### Build image:

`$ docker build . -t ssl-checker`

### Check all urls:

`$ docker run --rm ssl-checker`

### Check individual certificate:

`$ docker run --rm ssl-checker ./ssl-checker.py ssl-checker example.com`

## Without Docker

### Check all urls

`$ pipenv run ./ssl-checker.py check-all-ssl`

### Check individual url:

`$ pipenv run ./ssl-checker.py ssl-checker example.com`

## Setup

This Guide assumes you have [pipenv](https://github.com/pypa/pipenv) and Python 3.8 installed on your system.

### Initial project setup

Clone repository:

`$ git clone git@github.com:liquorice/ssl-checker.git`
`$ cd ssl-checker`

Then create file called `config.py` which a variable called `CHECK_HOSTS`.

For example:

```
CHECK_HOSTS = [
    "google.com",
    "exmaple.com",
    "liquorice.com.au"
]
```

Install dependencies and create virtual environment:

`$ pipenv lock --pre`
`$ pipenv install`
