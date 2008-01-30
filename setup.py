from setuptools import setup, find_packages

version = '0.1'

setup(name='megrok.form',
      version=version,
      description="",
      long_description="""\
""",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[], 
      keywords="",
      author="Dirceu Pereira Tiegs",
      author_email="dirceutiegs@gmail.com",
      url="",
      license="ZPL",
      package_dir={'': 'src'},
      namespace_packages=['megrok'],
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'zc.resourcelibrary',
                        'z3c.widget',
                        'zc.datetimewidget',
                        'collective.namedfile',
                        # Add extra requirements here
                        ],
      entry_points="""
      # Add entry points here
      """,
      )
