from setuptools import setup

setup(
    name='head_controller',
    packages=['head_controller'],
    description='A package to learn and understand 2 axis head movements',
    version='0.1',
    url='',
    author='Dan Scott',
    author_email='danscottlearns@gmail.com',
    keywords=['head','controller','nueral net','movement','axis','recognition'],
    install_requires=[
          'opencv-python',
          'mysqlclient',
          'pymysql',
          'sklearn'
      ],
    )
