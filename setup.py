from setuptools import setup, find_packages

setup(name="saaskit-user",
           version="0.1",
           description="Django project for user sites of saaskit",
           author="SaaSkit",
           author_email="admin@saaskit.org",
           packages=find_packages(),
           include_package_data=True,
)

