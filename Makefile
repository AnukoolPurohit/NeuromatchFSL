install:
	@make pip-tools
	@make pip-packages

conda-update:
	@conda env update --prune -f environment.yml
	@echo "!!!! Run Right now:\nconda activate FSL"

pip-tools:
	pip install pip-tools

pip-packages:
	pip-compile -v requirements/prod.in && pip-compile -v requirements/dev.in
	pip-sync -v requirements/prod.txt requirements/dev.txt
