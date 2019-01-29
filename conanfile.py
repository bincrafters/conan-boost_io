#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostIoConan(base.BoostBaseConan):
    name = "boost_io"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_io"
    lib_short_names = ["io"]
    header_only_libs = ["io"]
    b2_requires = ["boost_config"]
