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


class GitProps:
    """Determine properties of the git repository.
    """

    def __init__(self, root="."):
        self.root = Path(root).resolve()

    def _exec(self, cmd):
        proc = subprocess.run(cmd.split(),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              cwd=self.root,
                              check=True,
                              env=dict(os.environ, LC_ALL='C'),
                              universal_newlines=True)
        return proc.stdout.strip()

    def is_dirty(self):
        return bool(self._exec("git status --porcelain --untracked-files=no"))

    def get_date(self):
        if self.is_dirty():
            return datetime.date.today()
        else:
            ts = int(self._exec("git log -1 --format=%cd --date=unix"))
            return datetime.date.fromtimestamp(ts)


class meta(setuptools.Command):

    description = "generate meta files"
    user_options = []
    meta_template = '''
__version__ = "%(version)s"
__date__ = "%(date)s"
'''

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        git = GitProps()
        version = self.distribution.get_version()
        log.info("version: %s", version)
        values = {
            'version': version,
            'date': git.get_date().strftime("%e %B %Y").strip(),
        }
        with Path("_meta.py").open("wt") as f:
            print(self.meta_template % values, file=f)


class install(setuptools.command.install.install):
    def run(self):
        self.run_command('meta')
        super().run()


setup(
    use_scm_version=True,
    url = "https://github.com/rdawg-pidinst/white-paper",
    python_requires = '>= 3.6',
    install_requires = ['setuptools_scm'],
    py_modules=[],
    cmdclass = {'meta': meta, 'install': install},
)
