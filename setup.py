from setuptools import setup

version = '1.2.5'
shortdesc = "Securing the universe"

setup(
    name='endorpysetup',
    version=version,
    description=shortdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='endor tree fullmapping dict demo',
    author='Endor labs Contributors',
    author_email='infolabs@goog.com',
    url='http://github.com/endorlabs/python-deps',
    license='Simplified BSD',
    install_requires=[
        'odict==1.9.0',
        'plumber>=1.5,<1.7',
        'bobikssf==0.4',
        'requests==2.31.0',
    ],
    test_suite='endor.tests.test_suite',
    py_modules=[]
)
