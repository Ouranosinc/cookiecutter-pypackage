BAKE_OPTIONS ?= --no-input
NO_CRUFT = generated_with_cruft=n

help:
	@echo "bake 	Generate project using defaults"
	@echo "help 	Show this help"
	@echo "test 	Run the tests"
	@echo "replay 	Replay last cookiecutter run and watch for changes"
	@echo "watch 	Generate project using defaults and watch for changes"


bake:  # Generate project using defaults
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists $(NO_CRUFT)

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/ $(NO_CRUFT)

replay: BAKE_OPTIONS=--replay
replay: watch
	;

test:
	pytest
