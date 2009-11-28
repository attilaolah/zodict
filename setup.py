# Copyright 2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2 or later

from setuptools import setup, find_packages
import sys, os

version = '1.6.0'
shortdesc = 'zope.interface compliant ordered dictionary.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()
tests_require = ['interlude']

setup(name='zodict',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Framework :: Zope3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
      ],
      keywords='odict',
      author='Robert Niederreiter',
      author_email='rnix@squarewave.at',
      url=u'https://svn.plone.org/svn/archetypes/AGX/zodict',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'uuid', # only python2.4!
          'odict',
          'zope.interface',
          'zope.location',
      ],
      tests_require=tests_require,
      test_suite="zodict.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
      )