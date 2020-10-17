all:
	python3 main.py

build:
	python3 main.py build

clean:
	rm -r about contact events __pycache__ resources static
	rm favicon.ico index.html qa.pdf robots.txt
