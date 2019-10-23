#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/21 13:56
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : request_and_response.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃  ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃      ┻  ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import weakref
from collections import defaultdict
from time import time
from urllib.parse import urljoin

import six
from scrapy.exceptions import NotSupported
from scrapy.http import Headers
from scrapy.http.common import obsolete_setter
from scrapy.link import Link
from scrapy.utils.python import to_bytes
from scrapy.utils.url import escape_ajax
from w3lib.url import safe_url_string

live_refs = defaultdict(weakref.WeakKeyDictionary)


class object_ref(object):
    """继承这个类（而不是object）保持对激活实例的记录"""

    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        live_refs[cls][obj] = time()
        return obj


class RequestScrapy(object_ref):

    def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None):
        # 这是第一个被设置的参数，用于与编码 URL，或者转换 body 为字符（如果body是
        # unicode 编码）
        self._encoding = encoding
        self.method = str(method).upper()
        self._set_url(url)
        self._set_body(body)
        assert isinstance(priority, int), f"需要整型数据 priority"
        self.priority = priority

        if callback is not None and not callable(callback):
            raise TypeError(f"callback 必须是可调用对象，实际上是 {type(callback).__name__}")
        if errback is not None and not callable(errback):
            raise TypeError(f"errback 必须是可调用对象，实际上是 {type(errback).__name__}")
        assert callback or not errback, "callback 必须配置 errback"
        self.callback = callback
        self.errback = errback

        self.cookies = cookies or {}
        self.headers = Headers(headers or {}, encoding=encoding)
        self.dont_filter = dont_filter

        self._meta = dict(meta) if meta else None
        self.flags = [] if flags is None else list(flags)

    @property
    def meta(self):
        if self._meta is None:
            self._meta = {}
        return self._meta

    def _get_url(self):
        return self._url

    def _set_url(self, url):
        if not isinstance(url, six.string_types):
            raise TypeError(f'请求必须为 str 或者 unicode，而实际内容为 {type(url).__name__} 类型')

        s = safe_url_string(url, self.encoding)
        self._url = escape_ajax(s)

        if ":" not in self._url:
            raise ValueError(f"缺失请求：{self._url}")

    url = property(_get_url, obsolete_setter(_set_url, 'url'))

    def _get_body(self):
        return self._body

    def _set_body(self, body):
        if body is None:
            self._body = b''
        else:
            self._body = to_bytes(body, self.encoding)

    @property
    def encoding(self):
        return self._encoding

    def __str__(self):
        return f"<{self.method} {self.url}>"


class ResponseScrapy(object_ref):

    def __int__(self, url, status=200, headers=None, body=b'', flags=None, request=None):
        self.headers = Headers(headers or {})
        self.status = int(status)

    def _get_url(self):
        return self._url

    def _set_url(self, url):
        if isinstance(url, str):
            self._url = url
        else:
            raise TypeError(f"{type(self).__name__} URL 必须ui字符串，结果是 {type(url).__name__}")

    url = property(_get_url, obsolete_setter(_set_url, 'url'))

    def _get_body(self):
        return self._body

    def _set_body(self, body):
        if body is None:
            self._body = b''
        elif not isinstance(body, bytes):
            raise TypeError("Response 必须为字节串，如果需要传输 unicode 内容，"
                            "使用 TextResponse 或者 HtmlResponse")

    body = property(_get_body, obsolete_setter(_set_body, 'body'))

    def __str__(self):
        return f"<{self.status} {self.url}>"

    __repr__ = __str__

    def copy(self):
        return self.replace()

    def replace(self, *args, **kwargs):
        """创建一个新的 Response，拥有同样的属性"""
        for x in ['url', 'status', 'headers', 'body', 'request', 'flags']:
            kwargs.setdefault(x, getattr(self, x))
        cls = kwargs.pop('cls', self.__class__)
        return cls(*args, **kwargs)

    def urljoin(self, url):
        """合并响应和相对url路径，成绝对路径"""
        return urljoin(self.url, url)

    @property
    def text(self):
        """如果是 TextResponse 子类，将返回文本类型内容"""
        raise AttributeError("Response 不是 text 类型")

    def css(self, *a, **kw):
        raise NotSupported("Response content isn't text")

    def xpath(self, *a, **kw):
        raise NotSupported("Response content isn't text")

    def follow(self, url, callback=None, method='GET', headers=None, body=None,
               cookies=None, meta=None, encoding='utf-8', priority=0,
               dont_filter=False, errback=None):
        if isinstance(url, Link):
            url = url.url
        elif url is None:
            raise ValueError("url can't be None")
        url = self.urljoin(url)
        return RequestScrapy(url, callback,
                             method=method,
                             headers=headers,
                             body=body,
                             cookies=cookies,
                             meta=meta,
                             encoding=encoding,
                             priority=priority,
                             dont_filter=dont_filter,
                             errback=errback)


if __name__ == '__main__':
    RequestScrapy(url='http://www.baidu.com', method='post', body="{'a': 1, 'b': 2}")
