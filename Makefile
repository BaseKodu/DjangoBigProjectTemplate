.PHONY: runserver
runserver:
	poetry run python -m dbpt.manage runserver

.PHONY: migrate
migrate:
	poetry run python -m dbpt.manage migrate

.PHONY: makemigrations
makemigrations:
	poetry run python -m dbpt.manage makemigrations

.PHONY: shell
shell:
	poetry shell

.PHONY: test
test:
	poetry run python -m dbpt.manage test

.PHONY: install
install:
	poetry install

.PHONY: add
add:
	poetry add $(package)

.PHONY: superuser
superuser:
	poetry run python -m dbpt.manage createsuperuser

.PHONY: update
update: install migrate ;

