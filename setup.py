from setuptools import setup, find_packages

setup(name="saaskit-user-site",
           version="0.1",
           description="Django project for user sites of saaskit",
           author="SaaS kit",
           author_email="admin@saaskit.org",
           packages=find_packages(),
           include_package_data=True,
)

