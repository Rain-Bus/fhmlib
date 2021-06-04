import json

import requests

import conf

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def fast_post(data):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.post(conf.url, cookies=conf.cookies[0], headers=conf.header, verify=False,
                      timeout=3, data=data)

    if "40001" in r.text:
        # raise Exception("Token expired!")
        print("身份认证过期")
        exit()
    elif "errors" in r.text:
        err_msg = json.loads(r.text)['errors'][0]['msg']
        if "该座位已经被人预定了" in err_msg:
            return r
        # raise Exception(err_msg)
        print("出错了:" + err_msg)
        exit()

    return r
