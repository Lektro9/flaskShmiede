# flaskShmiede
This was my first website I made with Flask. This was with the help of sentdexs videos on youtube.

I even took the "Dictionary-Concept" to have some kind of simple "Database" to store the Flashcards and all the links (or "slugs"). You can find the dictionaries in project/rly.py, I am importing it into routes.py and giving the information with the @app.route function wrapper to the template I am loading.

As you can see this project became more and more out of control, as I tried to change to a real database for certain new beneficial reasoons:

Live editing: I really wanted to add content to my website without creating a new HTML file, slug and a route every time AND THEN restarting the webserver. Also new categories was a lot of work.
Users: User creation and them creating content on my website would be way more cool and efficient.
I am aware that all my goals are somehow also achievable in Flask. But it would have cost me way more time than to just use another framework, which offers a lot of my goals out of the box already.

So I decided to try out Django.

# To make this run
I recommend setting up a virtual environment and then simply:
- pip install flask

After that you just run the "__init__.py" file and it should be starting the server at various IPs (I used 0.0.0.0:5000, which picks all IPs available on the computer).
To see the website go to the browser and type in 127.0.0.1:5000. This is only for debugging and developement, please consider using apache2 and wsgi when hosting as a live website.
