import os, sys, subprocess
from setuptools import setup
from setuptools.command.install import install
class CustomInstall(install):
	def run(self):
		install.run(self)
		print "here is custom command"
		subprocess.call(['setupAuto.sh'])

setup (name='piforge',
	version='1.3.3',
	description='iforge for rPi server component',
	url='',
	author='Trevor Shaw',
	author_email='shawt@genlrn.com',
	license='MIT',
	scripts=['piforge/setupAuto.sh'],
	entry_points={
          'console_scripts': [
              'piforge = piforge.__main__:main'
          ]
      },
	packages=['piforge'],
	install_requires=[
		'web.py',
	],
	zip_safe=False,
	cmdclass={'install': CustomInstall})
		
