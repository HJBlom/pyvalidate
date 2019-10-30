release:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://pypi.takealot.com -u admin -p  dist/*
