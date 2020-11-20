.PHONY: test actions

clean:
	rm -rfv *.dot actions/__pycache__ results
	rm -fv *.db*

retrain: clean
	rasa train --force

talk:
	rasa shell

actions:
	rasa run actions --auto-reload
