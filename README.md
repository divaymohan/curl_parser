# cURL Parser

<a href="https://github.com/nlecoy/curlparser/actions?query=workflow%3ATests" target="_blank">
    <img src="https://github.com/nlecoy/curlparser/workflows/Tests/badge.svg" alt="Tests">
</a>
<a href="https://codecov.io/gh/nlecoy/curlparser" target="_blank">
    <img src="https://codecov.io/gh/nlecoy/curlparser/branch/main/graph/badge.svg?token=qSvHcn7TGz" alt="Coverage">
</a>
<a href="" target="_blank">
    <img src="https://img.shields.io/pypi/l/curlparser.svg" alt="Pypi">
</a>
<a href="https://pypi.org/project/curlparser" target="_blank">
    <img src="https://img.shields.io/pypi/v/curlparser?color=%2334D058&label=pypi%20package" alt="Package version">
</a>

Parse cURL commands returning object representing the request.

## How to install?

`curlparser` is available on PyPi:

### Using pip

```shell
$ pip install curlparser
```
### Using poetry

```shell
$ poetry add curlparser
```

### Using pipenv

```shell
$ pipenv install curlparser
```

## How to use?

```python
>>> import curlparser

>>> result = curlparser.parse(
    """
    curl \
      --header 'Content-Type: application/json' \
      --request PUT \
      --user nlecoy:my_password \
      --data '{"username":"xyz", "password":"xyz"}' \
      https://api.github.com/repos/nlecoy/curlparser
    """
)

>>> result.url
'https://api.github.com/repos/nlecoy/curlparser'

>>> result.auth
('nlecoy', 'my_password')

>>> result.json
{'username': 'xyz', 'password': 'xyz'}
```

## Available parameters

`curlparser`'s parse method will return a `ParsedCommand` object containing the following fields:

- method
- url
- auth
- cookies
- data
- json
- header
- verify

## License

cURL Parser is distributed under the Apache 2.0. See [LICENSE](LICENSE) for more information.
