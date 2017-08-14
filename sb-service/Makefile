# ENVIRONMENT VARIABLES
export FLASK_APP := src
export FLASK_DEBUG := true


install: 
	sudo pip install -e .

run:
	flask run

clean:
	rm -rf src.egg-info
	rm -rf *__pycache__
	
all: install run
	
