clean:
	rm -rf models/ *.dot

retrain: clean
	rasa train

validate:
	rasa data validate -vv
