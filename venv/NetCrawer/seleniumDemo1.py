#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from selenium import webdriver


url='http://www.baidu.com'
browser=webdriver.firefox
browser.get(url)