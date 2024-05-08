# This setup.py file serves the only purpose to dynamically create a
# _meta.py file which then is imported from conf.py.

import setuptools
from setuptools import setup
import setuptools.command.install
from distutils import log
import datetime
import os
from pathlib import Path
import subprocess
import gitprops

version = str(gitprops.get_version())


class meta(setuptools.Command):

    description = "generate meta files"
    user_options = []
    meta_template = '''
version = "%(version)s"
date = "%(date)s"
'''

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        version = self.distribution.get_version()
        log.info("version: %s", version)
        values = {
            'version': version,
            'date': gitprops.get_date().strftime("%e %B %Y").strip(),
        }
        with Path("_meta.py").open("wt") as f:
            print(self.meta_template % values, file=f)


class install(setuptools.command.install.install):
    def run(self):
        self.run_command('meta')
        super().run()


setup(
    version = version,
    url = "https://github.com/rdawg-pidinst/white-paper",
    python_requires = '>= 3.6',
    install_requires = ["setuptools", "git-props"],
    py_modules = [],
    cmdclass = {'meta': meta, 'install': install},
)
