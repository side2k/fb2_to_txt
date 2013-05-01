#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from lxml import etree

file_path = sys.argv[1]
tree = etree.parse(file_path)
root = tree.getroot()
for element in root.xpath("//*"):
    tag = element.xpath("local-name()")
    if tag == "binary":
        continue
    text = (element.text if element.text else '') + element.tail if element.tail else ''
    if text:
        print text.encode("utf-8")
