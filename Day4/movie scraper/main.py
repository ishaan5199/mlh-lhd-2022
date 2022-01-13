from bs4 import BeautifulSoup
import requests
from termcolor import colored

pagination = int(input("Number of responses : "))

html_text = requests.get("https://gadgets.ndtv.com/entertainment/upcoming-hollywood-movies").text
soup = BeautifulSoup(html_text, "lxml");

movieList = soup.find_all("div", class_ = "_mvbx _flx")

print("\nUpcoming (Hollywood) films ->")

for movie in movieList:
    
    if pagination >= 1:
        title = colored(movie.find("h3", class_ = "_hd").text, "green")
        director = movie.find("li", class_ = "_mvdrc lclamp").text.split(" ")[1:]
        cast = movie.find("li", class_ = "lclamp").text
        release = movie.find("div", class_ = "_flx")
        genre = movie.find("li", class_ = "_mvgenre").text
        moreInfo = movie.find("a")["href"]
        fullName = " ".join(director)

        print(f"\nTitle : {title.strip()}")
        print(f"Director : {fullName}")
        print(f"Cast : {cast.strip()}")
        print(f"Genre : {genre.strip()}")
        actualRelease = colored(release.text if release else "TBD", "red")
        print(f"Release Date : {actualRelease.strip()}")
        print(f"More info : {moreInfo}")
    
    pagination -= 1