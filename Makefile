install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#no testing

format:	
	black *.py 

deploy:
	#deploy goes here

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
		
all: install lint deploy format test 
