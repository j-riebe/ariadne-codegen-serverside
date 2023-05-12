check: mypy pyright

mypy:
	mypy .

pyright:
	pyright .

install:
	poetry install
