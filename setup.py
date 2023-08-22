from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bmd_erpnext_integration/__init__.py
from bmd_erpnext_integration import __version__ as version

setup(
	name="bmd_erpnext_integration",
	version=version,
	description="Bmd Erpnext Integration",
	author="Phamos GmbH",
	author_email="support@phamos.eu[Du",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
