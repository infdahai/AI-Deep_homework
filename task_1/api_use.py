import urllib.request
import json


class Chat_API():
    def __init__(self, *args, **kwargs):
        self.api_url = "http://openapi.tuling123.com/openapi/api/v2"
        with open('./data','r') as f:
            self._key= f.readline()[:-1]
            self._userid = f.readline()
        self._city= "合肥"
        self._province = "安徽"
        self.info = ""
        self.data={}

    def _update(self,info):
        self.data = {
            "reqType":0,
            "perception":{
                "inputText":{
                    "text":info
                },
                "selfInfo":{
                    "location":{
                        "city":self._city,
                        "province":self._province
                    }
                }
            },
            "userInfo":{
                        "apiKey":self._key,
                        "userId":self._userid
            }
        }
        return self.data

    def run(self,info):
        #self.info = input()
        self._update(info)
        req = json.dumps(self.data).encode('utf8')
        http_post = urllib.request.Request(self.api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        response_dic = json.loads(response_str)
        response_text = response_dic['results'][0]['values']['text']
        return response_text




