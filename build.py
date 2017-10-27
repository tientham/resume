#!/usr/bin/env python

from jinja2 import Environment, Template, FileSystemLoader
import markdown2
import sys
import codecs

if len(sys.argv) < 3:
    print "Usage: %s <markdown file> <html file>" % sys.argv[0]
    exit(1)

env = Environment(loader = FileSystemLoader('views'))
template = env.get_template("layout.html")

text = codecs.open(sys.argv[1], 'r', 'utf-8').read()
md = markdown2.markdown(text)
title = text[2:text.index('\n')]

with codecs.open(sys.argv[2], 'w', 'utf-8') as f:
    html = template.render(title = title, content = md)
    f.write(html)

