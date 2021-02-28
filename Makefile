# define the name of the virtual environment directory
CONV := my_convert

install:
	python3 -m venv my_convert

#activate environment
activate:
	pwd
	source $(CONV)/bin/activate
	
dependencies:
	pip3 install -r requirement.txt
	pip3 install currencyconverter
	pip3 install PySide6


start:
	python3 main.py

#desactivate environment
deactivate:
	$(CONV)/bin/deactivate