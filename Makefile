clean:
	rm -rf models/ *.dot

retrain: clean
	rasa train
