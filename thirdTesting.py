#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
import sys
import time

from requests.exceptions import ConnectTimeout

reload(sys)
sys.setdefaultencoding('utf-8')

class HttpJSONClient(object):
    def __init__(self):
        self.session = requests.session()
        # 设置Header不走缓存,需要后台根据后台的设置修改
        self.session.headers.update({'Cache-Control': "no-cache"})

    req_session = requests.session()

    def get(self, url, *args, **kwargs):
        """使用get请求访问url

        :param url: str 具体的网址

        :rtype dict
        :return
        {
            "status_code": 200,  # 状态码
            "content": ""  # 页面内容
        }
        """
        response = self.session.get(url, *args, **kwargs)
        data = {
            "status_code": response.status_code,
            "content": response.text
        }
        return data


def test_url(url):
    """测试一个url是否能访问

    :param url: str 访问网址
    """
    timeout = 3  # 访问请求超时时间
    http_client = HttpJSONClient()
    try:
        data = http_client.get(url, timeout=timeout)
    except ConnectTimeout:
        print("访问 %s 超时了,当前超时时间为: %d" % (url, timeout))
    else:
        # 判断状态码是否等于 200
        if data["status_code"] == 200:
            # 判断页面内容是否为空
            if data["content"]:
                print("访问 %s 成功, 且成功获取到页面内容。" % url)
            else:
                print("访问 %s 成功，但没有获取到页面内容。" % url)
        else:
            print("访问 %s 失败" % url)


def main():
    number = 3  # 总共访问多少次
    sleep_time = 5  # 每次访问结束后等待几秒再次访问
    count = 0  # 当前已经访问的次数
    url = "https://www.jiedaibao.com/"  # 要测试的网址
    while count < number:
        try:
            # 访问一次url
            test_url(url)
            # 统计当前已经访问的次数
            count += 1
            # 等待 sleep_time 秒后再次访问
            time.sleep(sleep_time)
        except Exception as e:
            print("函数发生了未知错误: %s" % e.message)
            # 退出程序
            sys.exit(1)


if __name__ == '__main__':
    main()
