.PHONY: help
help:
	@echo "Available targets:"
	@echo -e "\tformat\tFormat source code using yapf"
	@echo -e "\ttest\tRun tests using pytest"

.PHONY: format
format:
	yapf inflammation/ tests/ --recursive -i

.PHONY: test
test:
	python -m pytest tests/
