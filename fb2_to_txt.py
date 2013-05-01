#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from lxml import etree

file_path = sys.argv[1]
tree = etree.parse(file_path)
root = tree.getroot()
for element in root:
    tag = element.xpath("local-name()")
    if tag == "binary":
        continue
    for text in element.itertext():
        if text.strip():
            print text.encode("utf-8")
