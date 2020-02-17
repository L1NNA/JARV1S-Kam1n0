from setuptools import setup


from os import path
this_directory = path.abspath(path.dirname(__file__))
this_directory = path.abspath(path.join(this_directory, path.pardir))
readme = path.join(this_directory, 'README.md')
long_description = ""
if path.exists(readme):
    with open(readme, encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='kam1n0',
    packages=['kam1n0'],
    version='0.0.1',
    license='Apache 2.0',
    description='Python wrapper for Kam1n0 batch mode.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steven Ding',
    author_email='ding@cs.queensu.ca',
    url='https://github.com/L1NNA/JARV1S-Kam1n0',
    download_url='https://github.com/L1NNA/JARV1S-Kam1n0',
    keywords=['Kam1n0', 'Binary Analysis'],
    install_requires=[
        'requests',
        'tqdm',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
