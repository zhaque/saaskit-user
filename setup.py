from setuptools import setup, find_packages

setup(name="saaskit-user-site",
           version="0.1",
           description="Django project for user sites of saaskit",
           author="CrowdSense",
           author_email="admin@crowdsense.com",
           packages=find_packages(),
           include_package_data=True,
)

