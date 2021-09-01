# django-webcrawling-nlp-app
Web App crawling through internet, searching for comments related to video games and modeling sentiment using NLP

Currently in developement!! - app is still being trained!

Currently:
User is able to search title of video game. API request is made to rawg.io API, and 10 titles that have best title match are displayed. 

After clicking on 1 of 10 titles, new page is being rendered with background corresponding the backround of video game and simple game details are displayed (tittle, rating, year, but in the future more can be fetched from the same API).

All entries are saved to Postgresql

Upon clicking run NLP button - crawler runs through the pages and fetches latest comments about the game. Due to pages having infinite comment load, I've used Selenium to run headless Chrome. 

All comments are fetched and saved to Postgres

Currently I train the model by picking positive/negative comments, which is taking time and many runs to fetch more comment data from different games.



To do:

-fix gevent's monkey_patching (although looking online seems like a common problem, might not be solvable)

-add more sources 

-improve front end

-train model (in progress!!)

-dockerise 


