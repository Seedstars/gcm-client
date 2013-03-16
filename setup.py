from distutils.core import setup

setup(
    name='gcm-client',
    version='0.1',
    author='Sardar Yumatov',
    author_email='ja.doma@gmail.com',
    #url='http://readthedocs.org',
    description='Python client for Google Cloud Messaging (GCM)',
    long_description=open('README.rst').read(),
    packages=['gcmclient'],
    license=open('LICENSE').read(),
    keywords='gcm push notification google cloud messaging android',
    requires=['requests'],
    platforms = ('Any',),
    classifiers = [ 'Development Status :: 4 - Beta',
                    'License :: OSI Approved :: Apache 2.0 License',
                    'Programming Language :: Python',
                    ],
)
