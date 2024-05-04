format:
	rye run isort -rc -sl .
	rye run autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables .
	rye run black .
	rye run isort -rc -m 3 .

test:
	#rye run mypy .
	rye run pytest
