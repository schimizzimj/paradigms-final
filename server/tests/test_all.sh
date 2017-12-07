#!/bin/bash


recipes
printf "testing /recipes/\n"
python3 test_movies_index.py

printf "\ntesting /recipes/:recipe_id\n"
python3 test_movies.py

printf "\ntesting /ratings/:recipe_id\n"
python3 test_ratings.py

printf "\ntesting /recommendations/\n"
python3 test_recommendations_index.py

printf "\ntesting /recommendations/:user_id\n"
python3 test_recommendations.py
