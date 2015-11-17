from setuptools import setup

setup(name='python-teamwork',
      version='0.1.0',
      description='Python Wrapper for Teamwork API',
      url='https://github.com/andresgz/python-teamwork',
      author='Andres Gonzalez',
      author_email='andresgz@gmail.com',
      license='MIT',
      packages=['teamwork'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
