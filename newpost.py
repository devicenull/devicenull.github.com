#!/usr/bin/python
import time, subprocess 

title = raw_input("Title:")

filename = "_posts/%s-%s.textile" % (time.strftime('%Y-%m-%d'), title.replace(" ","-").lower().strip())

print "filename: %s" % filename

f = open(filename,"w")

f.write(
"""---
layout: post
title: %s
---

""" % title)

f.close()

