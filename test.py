#!/usr/bin/env python
import pycurl
c = pycurl.Curl()
c.setopt(c.URL, 'https://yx.3.cn')
c.perform()
