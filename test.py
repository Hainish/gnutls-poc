#!/usr/bin/env python
import pycurl
c = pycurl.Curl()
c.setopt(c.URL, 'https://apt.linode.com/')
c.perform()
