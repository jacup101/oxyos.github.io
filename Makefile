all:
	python3 src/main.py

build:
	python3 src/main.py build

clean:
	rm -r about what-we-do events resources static
	rm favicon.ico index.html qa.pdf robots.txt
