#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
Project: cms_codebook_demo
App: apps.
FILE: util
Created: 11/15/17 1:14 AM

Created by: ''
"""
import os
import argparse

INDEX_TEMPLATE_START = """
<html>\n
<body>\n
<h2>CMS CodeBook Demo - The Fee-For-Service Codes</h2>\n

<p><a href="https://hhsidealab.github.io/cms_codebook_demo/">Back to the Github Repository</a></p>

<p>\n
"""

INDEX_TEMPLATE_END = """
</p>\n
<p><a href="https://hhsidealab.github.io/cms_codebook_demo/">Back to the Github Repository</a></p>

</body>\n
</html>\n
"""


def file_count(dir, ext="*", counter=0):
    """
    returns number of files in dir and subdirs
    :param dir:
    :param ext:
    :param counter:
    :return:
    """
    for pack in os.walk(dir):
        for f in pack[2]:
            if f.endswith(ext):
                counter += 1
    return "\n" + dir + " : " + str(counter) + "files"


def build_github_page_index(dir, files_list):
    """
    build an index.html

    :param dir:
    :param ext:
    :return:
    """

    index = open(dir + "index.html", 'w')

    index.write(INDEX_TEMPLATE_START)

    for name in sorted(files_list):
        index.write('<li> <a href="' + name + '">' + name + '</a></li>\n')

    index.write("<br/><br/><p>Files:%s </p><br/>\n" % len(files_list))

    index.write(INDEX_TEMPLATE_END)
    index.close()

    return
