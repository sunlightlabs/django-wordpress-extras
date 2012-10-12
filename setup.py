from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='the-real-django-wordpress-extras',
    version="0.1",
    description="A collection of non-WordPress extensions for django-wordpress (the real one)",
    long_description=long_description,
    author='Jeremy Carbaugh',
    author_email='jcarbaugh@sunlightfoundation.com',
    url='http://github.com/sunlightlabs/django-wordpress-extras/',
    packages=['wordpressext'],
    package_data={'wordpressext': ['templates/wordpressext/mail/*.txt']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
    license='BSD License',
    platforms=["any"],
)
