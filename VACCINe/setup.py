from setuptools import setup

setup(
   name='VACCINe',
   version='1.0',
   description='Set of predefined function to facilitate creating datasets like VACCINe by minimizing technical knowledge required by users',
   author='Sajjad Abedian',
   author_email='sajjad.abedian@yahoo.com',
   packages=['VACCINe'],  #same as name
   install_requires=['pandas', 'numpy'], #external packages as dependencies
)
