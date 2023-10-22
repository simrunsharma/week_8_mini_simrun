python_install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

python_test:
	# no testing

python_format:	
	black *.py

python_deploy:
	# deploy goes here

python_lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

python_all: python_install python_lint python_deploy python_format python_test
