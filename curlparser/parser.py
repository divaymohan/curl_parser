import argparse
import json
import shlex

from collections import OrderedDict, namedtuple
from urllib.parse import urlparse, parse_qs

ParsedCommand = namedtuple(
    "ParsedCommand",
    [
        "method",
        "url",
        "auth",
        "cookies",
        "data",
        "json",
        "header",
        "verify",
        "query_param"

    ],
)

curl_parser = argparse.ArgumentParser()

curl_parser.add_argument("command")
curl_parser.add_argument("url")
curl_parser.add_argument("-A", "--user-agent")
curl_parser.add_argument("-I", "--head")
curl_parser.add_argument("-H", "--header", action="append", default=[])
curl_parser.add_argument("-b", "--cookie", action="append", default=[])
curl_parser.add_argument("-d", "--data", "--data-ascii", "--data-binary", "--data-raw", default=None)
curl_parser.add_argument("-k", "--insecure", action="store_false")
curl_parser.add_argument("-u", "--user", default=())
curl_parser.add_argument("-X", "--request", default="")


def is_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def get_query_param(url: str) -> [dict, str]:
    parse_result = urlparse(url)
    url = parse_result.scheme + "://" + parse_result.netloc + parse_result.path
    dict_result = parse_qs(parse_result.query)
    return dict_result, url


def parse(curl_command: str) -> ParsedCommand:
    cookies = OrderedDict()
    header = OrderedDict()
    body = None
    method = "GET"
    print(curl_command)
    curl_command = curl_command.replace("\\\n", " ")
    print(curl_command)

    tokens = shlex.split(curl_command)
    parsed_args = curl_parser.parse_args(tokens)

    if parsed_args.command != "curl":
        raise ValueError("Not a valid cURL command")

    if not is_url(parsed_args.url):
        raise ValueError("Not a valid URL for cURL command")

    data = parsed_args.data
    if data:
        method = "POST"

    if data:
        try:
            body = json.loads(data)
        except json.JSONDecodeError:
            header["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            header["Content-Type"] = "application/json"

    if parsed_args.request:
        method = parsed_args.request

    params, url = get_query_param(parsed_args.url)

    for arg in parsed_args.cookie:
        try:
            key, value = arg.split("=", 1)
        except ValueError:
            pass
        else:
            cookies[key] = value

    for arg in parsed_args.header:
        try:
            key, value = arg.split(":", 1)
        except ValueError:
            pass
        else:
            header[key] = value

    user = parsed_args.user
    if user:
        user = tuple(user.split(":"))

    return ParsedCommand(
        method=method,
        url=url,
        auth=user,
        cookies=cookies,
        data=data,
        json=body,
        header=header,
        verify=parsed_args.insecure,
        query_param=params
    )
