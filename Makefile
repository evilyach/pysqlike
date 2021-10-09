.DEFAULT_GOAL := init

.PHONY: debug
debug:
	. .env/bin/activate
	python3 src/main.py
	deactivate

init:
	python3 -m venv .env
