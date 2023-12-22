all:
	
	clear
	python3 makefile.py

F:	
	clear
	cd basico && python3 main.py

criar:
	venv/bin/pip3 freeze > requirements.txt

instalar:
	venv/bin/pip3 install -r requirements.txt

limp1:
	sudo apt-get clean
limp2:
	sudo apt-get autoremove
limp3:
	sudo apt-get autoremove --purge
limp4:
	sudo apt-get autoclean
limp5:
	sudo apt-get update
limp6:
	sudo apt-get upgrade
