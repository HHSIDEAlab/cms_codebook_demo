#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
Project: cms_codebook_demo
App: apps.
FILE: html_labeler
Created: 11/15/17 1:08 AM

Created by: '@ekivemark'
"""
import os
from shutil import copy2

from util import build_github_page_index

SOURCE_DIR = "../content/codebook_ffs_claims/"
TARGET_DIR = "../content/codes/"
FILE_EXT = ".html"


# for file in os.listdir(SOURCE_DIR):
#     if file.endswith(FILE_EXT):
#         print(os.path.join(SOURCE_DIR, file))
#
# print(file_count(SOURCE_DIR, FILE_EXT))

files_to_index = []

for f in os.listdir(SOURCE_DIR):
    if f.endswith(FILE_EXT):
        content = open(SOURCE_DIR + f, 'r')

        # initialize the label and code_name variables
        label = ""
        prev_line = ""
        code_name = ""

        for line in content:
            # we are looking for:
            # <div id="ta_19" class="t s5_19">LABEL:</div>
            if "LABEL:" in line:
                code_name = prev_line

                print("Writing file: %s%s%s" % (TARGET_DIR,
                                                code_name.lower(),
                                                FILE_EXT))
                files_to_index.append(code_name.lower() + FILE_EXT)

                copy2(SOURCE_DIR + f, TARGET_DIR + code_name.lower() + FILE_EXT)

                label = "LABEL:"

            else:
                split_line = line.split(">")

                # print("Split Line: %s" % split_line)

                if len(split_line) > 1:
                    chop_line = split_line[1].split("</")
                    prev_line = chop_line[0]
                else:
                    prev_line = split_line

write_index = build_github_page_index(TARGET_DIR, files_to_index)
