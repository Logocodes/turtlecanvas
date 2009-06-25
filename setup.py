from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='logocodes.turtlecanvas',
      version=version,
      description="Manage turtle graphics canvases and export to bitmap",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='ElevenCraft Inc.',
      author_email='matt@logocodes.com',
      url='http://github.com/11craft/logocodes.turtlecanvas/',
      license='MIT',
      namespace_packages=['logocodes'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
