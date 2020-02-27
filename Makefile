install:
	poetry install

run:
	poetry run brain-games

run_even:
	poetry run brain-even

run_calc:
	poetry run brain-calc

run_gcd:
	poetry run brain-gcd

run_progression:
	poetry run brain-progression

run_prime:
	poetry run brain-prime

build:
	rm -rf dist/
	poetry build

publish: build
	poetry publish -r test

lint:
	poetry run flake8 ./brain_games/
