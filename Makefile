.PHONY: test

clean:
	rm -rfv models/ *.dot __pycache__/ actions/__pycache__ results
	rm -fv *.db*

retrain: clean
	rasa train --force

talk:
	rasa shell

actions:
	rasa run actions --auto-reload

validate:
	rasa data validate -vv

test:
	rasa test --stories test/e2e_stories.md --e2e --fail-on-prediction-errors
