import requests
import json

key='9d01a34eff114d69b5ecb56039fb200b'
info='你好'
userid='cluster'
data={
    "reqType":0,
    "perception":{
        "inputText":{
            "text":info
        },
        "selfInfo":{
            "location":{
                "city":"合肥",
                "province":"安徽"
            }
        }
    },
    "userInfo":
            {
                "apikey":key,
                "userId":userid
            }
}

js = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
r=requests.post('http://openapi.tuling123.com/openapi/api/v2',js)
