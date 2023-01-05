# This setup.py file serves the only purpose to dynamically create a
# _meta.py file which then is imported from conf.py.

import datetime
import distutils.core
import os
from pathlib import Path
import subprocess
from setuptools import setup
import setuptools.command.install


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


class meta(distutils.core.Command):

    description = "generate a _meta.py file"
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
        values = {
            'version': self.distribution.get_version(),
            'date': git.get_date().strftime("%e %B %Y").strip(),
        }
        with open("_meta.py", "wt") as f:
            print(self.meta_template % values, file=f)


class install(setuptools.command.install.install):
    def run(self):
        self.run_command('meta')
        super().run()


setup(
    use_scm_version=True,
    python_requires='>= 3.6',
    setup_requires=['setuptools_scm'],
    py_modules=[],
    cmdclass = {'meta': meta, 'install': install},
)
