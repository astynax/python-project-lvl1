install:
	poetry install

run:
	poetry run brain-games

build:
	rm -rf dist/
	poetry build
