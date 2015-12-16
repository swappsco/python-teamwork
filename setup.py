from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='python-teamwork',
      version='0.1.3',
      description='Python Wrapper for Teamwork API',
      long_description=readme(),
      url='https://github.com/swappsco/python-teamwork',
      author='Andres Gonzalez',
      author_email='andresgz@gmail.com',
      license='MIT',
      packages=['teamwork'],
      install_requires=[
          'requests',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
