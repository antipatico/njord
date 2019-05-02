all: source build

source:
	python3 setup.py sdist

build:
	python3 setup.py bdist_wheel

clean:
	rm -rf build/ *.egg-info/
	find njord -name "__pycache__" -type d -exec rm -rfv \{} +

cleanall: clean uninstall uninstall-dev
	rm -rf dist/

install:
	pip3 install dist/njord-*.whl --force-reinstall

install-dev:
	python3 setup.py develop

uninstall:
	pip3 uninstall -y njord

uninstall-dev:
	python3 setup.py develop --uninstall

venv:
	python3 -m virtualenv venv

.PHONY: *
