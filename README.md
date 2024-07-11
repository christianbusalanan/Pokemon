# Pokémon Pokedex Web Scraping Project

This project demonstrates how to scrape data from the Pokémon Database (PokemonDB) website using Python with `urllib.request` , convert the scraped data into a DataFrame using `pandas`, and store it in an SQLite database using `sqlite3`.

## Overview

The project involves scraping Pokémon information from the Pokémon Database (PokemonDB) website, converting the scraped data into a structured format (DataFrame), and storing it in an SQLite database (`pokedex.db`). It provides a basic CLI interface to interact with the database.

### Features

- **Web Scraping**: Utilizes `urllib.request` and `pandas` for scraping HTML and extracting Pokémon data.
- **Data Handling**: Converts the scraped data into a DataFrame using `pandas`.
- **SQLite Database**: Stores Pokémon data (e.g., name, type, stats) in an SQLite database (`pokedex.db`).

## Requirements

- Python 3.x
- pandas (`pandas`)
- SQLite3 (comes pre-installed with Python)
