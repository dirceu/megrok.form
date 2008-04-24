from setuptools import setup, find_packages
from os import sep
from os.path import curdir

version = '0.2.4'

long_description = open(sep.join((curdir, 'src','megrok','form','README.txt'))).read()

setup(name='megrok.form',
      version=version,
      description="Fields, Widgets and Constraints for Grok",
      long_description=long_description,
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Zope Public License',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP',
                   ],
      keywords="grok form widgets fields constraints",
      author="Dirceu Pereira Tiegs",
      author_email="dirceutiegs@gmail.com",
      url="http://svn.zope.org/megrok.form",
      license="ZPL",
      package_dir={'': 'src'},
      namespace_packages=['megrok'],
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'zc.resourcelibrary == 1.0.1',
                        'z3c.widget == 0.1.6',
                        'zc.datetimewidget == 0.5.2',
                        'collective.namedfile == 1.1',
                        'collective.namedblobfile == 0.3',
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
