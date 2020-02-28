.PHONY: test

clean:
	rm -rf models/ *.dot

retrain: clean
	rasa train

validate:
	rasa data validate -vv

test:
	rasa test --stories test/e2e_stories.md --e2e --fail-on-prediction-errors
