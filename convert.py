#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import re


class PathStructer(object):
    def __init__(self, filename):
        self.dic_chain = ["none"]
        self.current_depth = 0
        self.filename = filename

    def __reload_file(self) -> str:
        with open(self.filename, "r") as f:
            for line in f:
                yield line

    def __get_dir_chain(self):
        print("/".join(self.dic_chain))

    def __process_line(self, line):
        level = len(re.findall(r"\t", line))
        folder_name = line.lstrip("\t").rstrip("\n")
        return level, folder_name

    def __process(self, level, folder_name):
        if self.current_depth < level:
            # tree depth increse
            self.current_depth += 1
            self.dic_chain.append(folder_name)
        elif self.current_depth == level:
            # tree depth no change
            self.dic_chain[self.current_depth] = folder_name
        elif self.current_depth > level:
            # tree depth decrese
            self.dic_chain.pop()
            self.current_depth -= 1
            self.dic_chain[self.current_depth] = folder_name
        self.__get_dir_chain()

    def run(self):
        for index, line in enumerate(self.__reload_file()):
            level, folder_name = self.__process_line(line)
            if index == 0 and level != 0:
                raise Exception("The first foldername should have no TABs")
            else:
                self.__process(level, folder_name)


p = PathStructer("sample.txt")
p.run()
