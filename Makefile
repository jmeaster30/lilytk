.PHONY : help clean install test upload-package upload-test-package 

help : 
	@echo "lilytk - makefile help"
	@echo "----------------------"
	@echo ""
	@echo "clean               - cleans up the build artifacts"
	@echo "test                - runs unit tests"
	@echo "upload-package      - builds and uploads the package to PyPi"
	@echo "upload-test-package - builds and uploads the package to Test PyPi"

bump :
	

clean :
	rm -rf dist

dist/* :
	python -m build

install : dist/*
	echo "Installing..."

upload-package : dist/*
	twine upload --repository pypi dist/*
