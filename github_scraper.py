import requests  
from bs4 import BeautifulSoup as bs 

github_user = input("Input Github User:")
""" For web scraping, the first step is going to be sending a request to the github URL( with the username from the user input)

    A response of 200 means the request was successful 


"""
url = 'https://github.com/'+github_user  # this takes you to the github users profile page
r = requests.get(url) # sends request to the url of the user input 




soup = bs(r.content, "html.parser")  # r is the response (e.g  HTTP 200 OK successful response status code indicates that a request has succeeded.) 
profile_image = soup.find("img", class_="avatar avatar-user width-full border color-bg-default")

print(profile_image)
#.parser - parse into html code
# . content is everything on the url( html source code)