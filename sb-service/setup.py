from setuptools import setup

setup(
    name='src',
    packages=['src', 'src.configs', 'src.models', 'src.routes', 'src.libs'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
