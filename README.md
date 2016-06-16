#Cinema Information Retrieval from Wikipedia
This is my Final Project from my Natural Language Processing class at NYU. 

First, unzip Data.zip and move the directories "Movies" and "Actors" to the same directory as Cosine.py. Then run ```python Cosine.py````.

The Austin and Luiz files are results from tests I conducted with my friends.

The program asks for an output file name, where it will print results. It also asks for which ngram it should use (see NLP_FINAL.pdf for more details) - please choose 1 or 2. Then it asks for a query. Your query should be one of the following 
* Several actors who were in a certain movie (ie Leonardo Dicaprio, Kathy Bates, Kate Winslet)
* Several movies that one actor was in (ie Inception, Titanic, Shutter Island)
The program will then guess at the link between the elements of your query.

#Dependencies:
* sklearn
