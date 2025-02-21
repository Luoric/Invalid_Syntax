#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}
darkKNight_movie = {
    "title": "The Dark Knight",
    "id": "tt0468569",
    "year_released": 2008,
    "rating": "PG13",
    "score": 9.0,
    "reviews": 5994,
    "genre" : ['Action', 'Crime', 'Drama', 'Thriller']
}

lotr_movie = {
    "title": "The Lord of the Rings: The Return of the King",
    "id": "tt0167260",
    "year_released": 2003,
    "rating": "PG13",
    "score": 8.9,
    "reviews": 3442,
    "genre" : ['Adventure', 'Drama', 'Fantasy']
}


inside_movie['year_released'] = 2015
inside_movie['score'] = 8.2
inside_movie['reviews'] = 944
del inside_movie['out_of']
inside_movie['genre'] = ['Animation', 'Adventure', 'Comedy', 'Drama', 'Family', 'Fantasy']

my_movies = [lotr_movie, darkKNight_movie, inside_movie]

find_genre = raw_input("Enter the movie genre: ")
movieRatings = {}
#string formatting print("%s:%s" % (key, value))
for movies in my_movies:
    if find_genre in movies['genre']:
        movieRatings[movies['title']] = movies['score']

maxSoFar = 0.0
for ratings in movieRatings.values():
    if ratings > maxSoFar:
        maxSoFar = ratings

for key, value in movieRatings.items():
    if maxSoFar == value:
        print("The movie is " + key + " with the rating of " + str(value))

# Do not edit the code above!

# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt2096673/
