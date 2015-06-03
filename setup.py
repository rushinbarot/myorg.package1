from setuptools import setup
version = "0.0.0"
setup(
    name="myorg.package1",
    version=version,
    install_requires=['requests','flask'],
    namespace_packages=['myorg'],
    packages = [
                "myorg.package1",],
    package_data = {
        # data files need to be listed both here (which determines what gets
        # installed) and in MANIFEST.in (which determines what gets included
        # in the sdist tarball)
        "myorg.package1": [
            "static/*",
            'scripts/*'],
        },
    author="Peter",
    license="Copyright 2015",
    description="""Example package for REST API and checking log files""",
    entry_points={
        'console_scripts': [
        'check_services=myorg.package1.check_services:check_services',
        'check_logfiles=myorg.package1.check_logfiles:check_logfiles',
        ],
 })
