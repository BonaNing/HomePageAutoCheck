#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests


class HttpJSONClient(object):
    def __init__(self):
        self.session = requests.session()
        # 设置Header不走缓存,需要后台根据后台的设置修改
        self.session.headers.update({'Cache-Control': "no-cache"})

    req_session = requests.session()

    def get(self, url, *args, **kwargs):
        """使用get请求访问url

        :param url: str 具体的网址
        """
        response = self.session.get(url, *args, **kwargs)
        data = {
            "status_code": response.status_code,  # 状态码
            "content": response.text  # 页面内容
        }
        return data


def main():
    url = "http://cms.office.jiedaibao.com/"  # 访问网址
    timeout = 3  # 访问请求超时时间
    http_client = HttpJSONClient()
    data = http_client.get(url, timeout=timeout)
    print "访问 %s 状态码: %s, 内容: %s" % (url, data["status_code"], data["content"])


if __name__ == '__main__':
    main()