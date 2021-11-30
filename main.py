from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/"
                               "https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_site = response.text

soup = BeautifulSoup(empire_web_site, "html.parser")
# print(soup.text)

movie_title = soup.find_all("h3", class_="title")


all_movies = [movie.getText() for movie in movie_title]
movies = all_movies[::-1]
with open("movie.txt", "w", encoding="UTF-8") as movie_file:
    for movie in movies:
        movie_file.writelines(f"{movie}\n")







# for num in range(len(movie_title)-1, -1, -1):
#     print(num)
#     with open("movie.txt", "a", encoding="UTF-8") as movie_list:
#         movie_list.write(movie_title[num].text + "\n")
    # top100_list.append(movie_title[num].text
