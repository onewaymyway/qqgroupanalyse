#!/usr/bin/env python3

import json
from urllib import request, parse

from qqrobot import QQClient, QQHandler
import mlogger as log


class QQTulingHandler(QQHandler):
    url_req = "http://www.tuling123.com/openapi/api"

    def __init__(self, APIKey=None):
        pass;
##        if str(APIKey) in ('None', ''):
##            print('You\'ll have to provide an APIKey first.')
##            print('Get it @ http://tuling123.com')
##            raise ValueError('APIKey not available')
##        else:
##            self.key = APIKey

    def on_buddy_message(self, uin, msg):
##        d = parse.urlencode(
##            {'key': self.key, 'info': msg, 'userid': uin}).encode('utf-8')
##        with request.urlopen(self.url_req, data=d) as f:
##            j = json.loads(f.read().decode('utf-8'))
##        log.i('Tuling', ':'.join((str(uin), msg)))
##        log.i('Tuling', 'response:' + j['text'])
##        self.send_buddy_message(uin, j['text'])
        info=self.get_user_info(uin);
        print(info)
        self.get_user_qqNum(uin);
        self.send_buddy_message(uin, "heihei:"+info["nick"]+":"+info["city"])


if __name__ == "__main__":
    a = QQClient()
    h = QQTulingHandler("")

    # you can save your verification
    #a.QR_veri()
    #a.login()
    # a.login(save_veri=True) to save verfication file when
    # login succeeded, or use the following method when
    # you want to save the verification file.
    #a.save_veri()  # default filename will be ./`QQClient.uin`.veri

    # or load from a file instead
    # a.load_veri('path/to/your/verification/file')
    # a.login(get_info=False)

    a.load_veri("1073810002.veri")
    a.login(get_info=False)

    a.add_handler(h)
    a.listen(join=True)
