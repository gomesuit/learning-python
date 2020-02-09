import urllib.parse

parameters = {
    "param_1" : "テスト",
    "param_2" : 3,
    "param_3" : [1],
    "param_4" : [1, 2, 3],
}

print(urllib.parse.urlencode(parameters))
