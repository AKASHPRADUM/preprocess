import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess', 
	include_package_data=True,
	version = '0.1.3',
	author = 'Position6',
	author_email = 'pradum@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
