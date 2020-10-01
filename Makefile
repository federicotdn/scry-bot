.PHONY: test

clean:
	rm -rfv models/ *.dot __pycache__ results
	rm -fv *.db*

retrain: clean
	rasa train --force

talk:
	rasa shell

actions:
	rasa run actions --auto-reload
