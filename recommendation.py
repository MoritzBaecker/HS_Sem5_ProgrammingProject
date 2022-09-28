import csv

import pandas
import json

# os, multiprocessing as mp

# from itertools import count
# from multiprocessing import process

listOfMovies = []
listOfRecommendations = []


def getListOfMovies():
    global listOfMovies
    df = pandas.read_csv('data/movie_titles_quotes.csv', quotechar="|",  engine='python')
    return df.to_json(orient="values")

def getMovie(movie_index):
    df = pandas.read_csv('data/movie_titles_quotes.csv', quotechar="|",  engine='python')
    searchvalue = [int(movie_index)]
    print(searchvalue)
    return df.loc[df['Index'].isin(searchvalue)].to_json(orient="values")

def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None
