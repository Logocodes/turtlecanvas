from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='turtlecanvas',
    version=version,
    description="Manage turtle graphics canvases and export to bitmap",
    long_description="""\
    What does this application do?
    ==============================

    - Manages turtle graphics canvases, including their turtle state.
    - Efficiently renders canvas states to PNG.
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='ElevenCraft Inc.',
    author_email='matt@logocodes.com',
    url='http://github.com/11craft/turtlecanvas/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PIL',
    ],
    entry_points="""
    """,
)
