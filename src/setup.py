# -*- coding: utf-8 -*-

from distutils.core import Extension, setup
from distutils.command.build_ext import build_ext
import os
import re
import shutil

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
version = re.match(r"AC_INIT\(.*?, \[(.*?)\]\)", open(os.path.join(root_dir, "configure.ac")).read()).group(1)
long_description = open(os.path.join(root_dir, "README.md")).read()
prebuilt_frida_extension = os.environ['PREBUILT_FRIDA_EXTENSION']

class FridaPrebuiltExt(build_ext):
    def build_extension(self, ext):
        target = self.get_ext_fullpath(ext.name)
        try:
            os.makedirs(os.path.dirname(target))
        except Exception, e:
            pass
        shutil.copyfile(prebuilt_frida_extension, target)

setup(
    name='frida',
    version=version,
    packages=['frida'],
    license="GNU GPLv3",
    description="Frida is an open-source toolkit for interactive and scriptable reverse-engineering",
    long_description=long_description,
    url="http://frida.github.io",
    author="Frida Developers",
    author_email="ole.andre.ravnas@tillitech.com",
    ext_modules=[Extension('_frida', [])],
    cmdclass={
        'build_ext': FridaPrebuiltExt
    }
)