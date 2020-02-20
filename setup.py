from setuptools import setup

setup(
    name='do_mpc',
    version='4.0.0dev1',
    packages=['do_mpc','do_mpc.tools'],
    author='Sergio Lucia',
    author_email='sergio.lucia@tu-berlin.de',
    url='https://do-mpc.readthedocs.io',
    license='LICENSE.txt',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "casadi",
        "numpy",
        "matplotlib"
    ],
)
