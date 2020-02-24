install:
	poetry install

run:
	poetry run brain-games

build:
	rm -rf dist/
	poetry build

publish:
	poetry publish --build -r test

lint:
	poetry run flake8 ./brain_games/
