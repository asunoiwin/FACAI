.PHONY: run test

run:
	uvicorn web.main:app --reload

test:
	pytest
