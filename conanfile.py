#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class SmlConan(ConanFile):
    name = "sml"
    version = "1.1.0"
    license = "MIT"
    author = "Alexander Zaitsev zamazan4ik@tut.by"
    url = "https://github.com/ZaMaZaN4iK/conan-sml"
    homepage = "https://github.com/boost-experimental/sml"
    description = "[Boost].SML: C++14 State Machine Library"
    topics = ("sml", "boost", "metaprogramming", "design-patterns", "state-machine")
    no_copy_sources = True

    _source_subfolder = "source_subfolder"

    def source(self):
        checksum = "5b51a0b0318fb155c65621f77179ae80f61d136789ea749dde18c4a1fca51a74"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=checksum)      
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy("*hpp", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_info(self):
        self.info.header_only()
