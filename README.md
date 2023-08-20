# CURL Parser

```python
>>> result = parse(
    """
    curl \
      --header 'Content-Type: application/json' \
      --request PUT \
      --user divay:password \
      --data '{"username":"dm", "password":"dmfire"}' \
      https://localhost:8080/verification
    """
)

>>> result.url
'https://localhost:8080/verification'

>>> result.auth
('divay', 'password')

>>> result.json
{'username': 'dm', 'password': 'dmfire'}
```

## Available parameters

- method
- url
- auth
- cookies
- data
- json
- header
- verify
- query_param
