from setuptools import setup

setup(name='pythonwhois',
      version='2.4.4',
      description='Module for retrieving and parsing WHOIS data for domains. Supports most domains. No dependencies.',
      author='Sven Slootweg',
      author_email='pythonwhois@cryto.net',
      url='http://cryto.net/pythonwhois',
      packages=['pythonwhois'],
      package_dir={"pythonwhois": "pythonwhois"},
      package_data={"pythonwhois": ["*.dat"]},
      install_requires=['argparse'],
      provides=['pythonwhois'],
      scripts=["pwhois"],
      license="WTFPL",
      classifiers=[
            'Development Status :: 1 - Beta',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Operating System :: Microsoft',
            'Operating System :: POSIX :: Linux',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: User Interfaces'
      ]
)
