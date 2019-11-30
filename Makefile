define green
	@tput setaf 2
	@tput bold
	@echo $1
	@tput sgr0
endef
WADER_SERVICES_PATH ?= ../DWP_Test

.PHONY: run_api
run_api: clean_pyc run_dwp_api
	$(call green,"[Build successful]")

.PHONY: clean_pyc
clean_pyc:
	find . -name "*.pyc" -delete
	$(call green,"[Cleanup loitering pyc files]")

.PHONY: run_dwp_api
run_dwp_api:
	python3 dwp_api.py

.PHONY: run_dwp_api_unit_tests
run_dwp_api_unit_tests:
	python3 -m pytest -q dwp_api.py
	$(call green,"[Running Unit Tests On API]")