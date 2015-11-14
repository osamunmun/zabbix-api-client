from setuptools import setup, find_packages

long_description = open('./README.rst').read()

setup(
    name="zabbix-api-client",
    version="0.0.1",
    install_requires=[],
    description='Zabbix API client library',
    long_description=long_description,
    url='https://github.com/osamunmun/zabbix-api-client',
    author='Osamu Takayasu',
    author_email='osamu.takayasu@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zabbix_cl = zabbbix-api-client.core:main',
        ]
    }
)
