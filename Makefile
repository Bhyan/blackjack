run: 
	python3 main.py

Test:
	python3 -m unittest -v test/test_blackjack.py

clean:
	rm -rf ./test/__pycache__
	rm -rf ./blackjack/__pycache__
