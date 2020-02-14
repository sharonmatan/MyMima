# Website Structure



## Important Pages in mima website:

https://www.mima.co.il/
* #### home page:
    * logo, search bar, submit button.
    * link by artist first letter
    * link by song first letter

----------------------------------------------------

https://www.mima.co.il/fact_page.php?song_id=502

* #### song page:
    * name, artist and facts.

----------------------------------------------------


https://www.mima.co.il/artist_page.php?artist_id=19

* #### artist's list songs page:
    * list of all the artist songs

----------------------------------------------------


https://www.mima.co.il/search_result.php
* #### search result
    * list of all artists, song names and facts review from the searchbar input(from landing page)   

----------------------------------------------------


https://www.mima.co.il/artist_letter.php?let=%D7%90
* #### artist list page by first letter
    * list of artists name that their names starting with the same letter

----------------------------------------------------


https://www.mima.co.il/song_letter.php?let=%D7%90
* #### song list page by first letter
    * list of songs name that their names starting with the same letter

## models

* #### song name
    * song_name = CharField(max_length=150)
* #### artist name
    * artist_name = CharField(max_length=150)
* #### facts
    * fact = TextField()
    * optional: media
    
* #### to run the crawler:
    * run create_song after making a new migration

    
   




