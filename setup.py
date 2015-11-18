from setuptools import setup, find_packages

long_description = open('./README.rst').read()

setup(
    name="zabbix-api-client",
    version="0.0.1",
    install_requires=[
      'requests==2.8.1'
    ],
    description='Zabbix API client library',
    long_description=long_description,
    url='https://github.com/osamunmun/zabbix-api-client',
    author='Osamu Takayasu',
    author_email='osamu.takayasu@gmail.com',
    license='MIT',
    packages=['zabbix_api_client']
)
