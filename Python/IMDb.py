import io
import imdb
import pygame as py
from urllib.request import urlopen
py.init()
imdb = imdb.IMDb()

def NewFilm():
    global screen,MoviePoster
    
    MovieIDs = imdb.search_movie(input("Enter Film Title: "))
    for (i, item) in enumerate(MovieIDs, start=1):
        print(i, item['long imdb canonical title'])
    MovieID = MovieIDs[int(input("Enter ID: ")) - 1].getID()
    Movie = imdb.get_movie(MovieID)
    screen = py.display.set_mode((1,1),py.RESIZABLE)
    MoviePosterURL = Movie['full-size cover url']
    MoviePoster = py.image.load(io.BytesIO(urlopen(MoviePosterURL).read())).convert()
    screen = py.display.set_mode((MoviePoster.get_width(),MoviePoster.get_height()),py.RESIZABLE)
    screen.fill((255,255,255))

NewFilm()

while True:
    screen.blit(py.transform.scale(MoviePoster,(screen.get_width(),screen.get_height())),(0,0))
    py.display.flip()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            raise SystemExit