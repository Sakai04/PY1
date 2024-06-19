import requests


website = ( "http://apple.com",
            "google.com",
            "microsoft.com" ) # Tuple


for w in website: # Loop through the tuple
    if not w.startswith("http://"):# if the item does not start with "http://"
        w = f"http://{w}"# add "http://" to the beginning of the item


