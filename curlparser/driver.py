from parser import parse

curl_list = [
    "curl https://api.github.com/repos/nlecoy/curlparser",
    "curl --insecure https://api.github.com/repos/nlecoy/curlparser",
    "curl -X DELETE https://api.github.com/repos/nlecoy/curlparser",
    "curl -b 'foo=bar' -b 'hello' https://api.github.com/repos/nlecoy/curlparser",
    "curl -u nlecoy:my_password https://api.github.com/repos/nlecoy/curlparser",
    "curl -d 'foo=bar' https://api.github.com/repos/nlecoy/curlparser",
    """
            curl \
              --header 'Content-Type: application/json' \
              --header 'Hello World' \
              --request PUT \
              --user nlecoy:my_password \
              --data '{"username":"xyz", "password":"xyz"}' \
              https://api.github.com/repos/nlecoy/curlparser
            """,
    """curl 'http://localhost:8080/verification' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJUYXJ0YW4iLCJpYXQiOjE2OTIzNTA4NDIsImV4cCI6MTcyMzkwNzc5NH0._LyE-r4IOYWV2Vk2eeB_pxhKWDMtaK7y9K4YW7v-5-YyPCMEKti9nan4-APWr_-_2CLo25gBxrFrXAEn89_yPQ' \
--data '{ \
    "category": "individual-pii-data", \
    "type": "pan-detail-v1", \
    "applicationId": "test", \
    "data": { \
        "panNumber": "CDNPD4498R" \
    } \
}'"""
]


curl_ = """curl 'https://www.google.com/verification?id=100' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJUYXJ0YW4iLCJpYXQiOjE2OTIzNTA4NDIsImV4cCI6MTcyMzkwNzc5NH0._LyE-r4IOYWV2Vk2eeB_pxhKWDMtaK7y9K4YW7v-5-YyPCMEKti9nan4-APWr_-_2CLo25gBxrFrXAEn89_yPQ' \
--data '{ \
    "category": "individual-pii-data", \
    "type": "pan-detail-v1", \
    "applicationId": "test", \
    "data": { \
        "panNumber": "CDNPD4498R" \
    } \
}'"""

if __name__ == '__main__':
    # for curl in curl_list:
    #     result = parse(curl)
    #     print(result._asdict())
    result = parse(curl_)
    print(result._asdict())
