.PHONY: local

local:
	py manage.py runserver

deploy:
	git push heroku main

# Generate an image of the models in the system.
graph:
	py manage.py graph_models -a -g -o my_project_visualized.png

coverage:
	pytest --cov=journal/accounts/tests/ --migrations -n 2 --dist loadfile

# fcov == "fast coverage" by skipping migrations checking. Save that for CI.
fcov:
	@echo "Running fast coverage check"
	@pytest --cov=journal/accounts/tests/ -n 4 --dist loadfile -q

# mypy:
# 	mypy homeschool project manage.py