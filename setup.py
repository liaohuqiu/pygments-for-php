from setuptools import setup, find_packages

setup(
    name = 'pygments-for-php',
    version = '0.0.1',
    keywords = ('pygments-cube-server', 'cube-rpc', 'cubi', 'cube-rpc'),
    description = 'pygments RPC server based on cubi RPC protocol',
    license = 'MIT License',
    install_requires = ['cubi>=0.0.3', 'pygments'],

    author = 'http://www.liaohuqiu.net',
    author_email = 'liaohuqiu@gmail.com',
    url = 'https://github.com/liaohuqiu/pygments-cube-server',

    packages = find_packages(),
    platforms = 'any',
)
