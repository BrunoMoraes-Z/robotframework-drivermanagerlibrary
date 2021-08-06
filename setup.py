from setuptools import setup

setup(
    name='drivermanagerlibrary',
    description='Library for WebDriverManager from Selenium Automations',
    version='1.0.0',
    url='https://github.com/BrunoMoraes-Z/robotframework-drivermanagerlibrary',
    keywords=['robotframework', 'robot', 'framework', 'webdriver', 'python', 'manager'],
    author='Bruno Moraes',
    license='MIT',
    packages=['DriverManagerLibrary'],
    include_package_data=True,
    install_requires=[
        'robotframework',
        'robotframework-seleniumlibrary',
        'webdriver-manager'
    ]
)