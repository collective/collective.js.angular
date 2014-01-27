from setuptools import setup, find_packages
import os

version = '1.2.10.2'
shortdesc = 'AngularJS JavaScript Library Packaged for Plone'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()

setup(name='collective.js.angular',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
            "Framework :: Plone",
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='GPLv2',
      url='https://pypi.python.org/pypi/collective.js.angular',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'setuptools',
            'Plone',
      ],
      entry_points={
          'z3c.autoinclude.plugin': 'target = plone',
      },
)
