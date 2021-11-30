from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/"
                               "https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_site = response.text

soup = BeautifulSoup(empire_web_site, "html.parser")
# print(soup.text)

movie_title = soup.find_all("h3", class_="title")
top100_list = []
for num in range(len(movie_title)-1, -1, -1):
    print(num)
    with open("movie.txt", "a", encoding="UTF-8") as movie_list:
        movie_list.write(movie_title[num].text + "\n")
    # top100_list.append(movie_title[num].text

print(top100_list)