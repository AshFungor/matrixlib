PYTHON = python3
PIP = pip3

test:
	$(PYTHON) -m unittest tests/test-matrix.py

build: matrixlib/matrix/matrix.py test
	$(PYTHON) setup.py bdist_wheel

clean:
	rm -r build dist *egg-info
	find . -type d -name '*cache*' -exec rm -r {} +

install: build
	$(PIP) install --force-reinstall dist/*.whl