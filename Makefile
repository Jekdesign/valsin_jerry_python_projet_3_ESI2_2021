# define the name of the virtual environment directory
CONV := my_convert

#activate
activate: 
	$(CONV)/bin/activate

start:
	python3 main.py

#desactiver
deactivate: 
	$(CONV)/bin/deactivate

