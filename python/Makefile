.PHONY: run
run: venv
	. venv/bin/activate; python3 script.py $(ARGS)

.PHONY: setup
setup: venv

venv: requirements.txt
	python3 -m venv venv
	. venv/bin/activate; python3 -m pip install -r requirements.txt

.PHONY: clean
clean:
	rm -fr venv
