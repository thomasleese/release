from setuptools import setup


setup(
    name='rewease',
    version='0.1.0',
    description='Tool for making it easy to release software',
    author='Thomas Leese',
    author_email='thomas@leese.io',
    url='https://github.com/thomasleese/rewease',
    packages=['rewease'],
    install_requires=[
        'cairosvg>=2.1',
    ],
    license='MIT',
)
