import os
import json

class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating, year, budget, box_office, profitable, oscar_nominated, oscar_win, trailer):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer = trailer
        self.storage_address = self.get_storage_address()
        self.upload_file()

    def save_data(self):
        data = {
            "title": self.title,
            "description": self.description,
            "director": self.director,
            "writer": self.writer,
            "cast": self.cast,
            "running_time": self.running_time,
            "country": self.country,
            "language": self.language,
            "imdb_rating": self.imdb_rating,
            "year": self.year,
            "budget": self.budget,
            "box_office": self.box_office,
            "profitable": self.profitable,
            "oscar_nominated": self.oscar_nominated,
            "oscar_win": self.oscar_win,
            "trailer": self.trailer
        }

        film_folder = os.path.join('film_storage', self.title[0].upper(), self.title)
        os.makedirs(film_folder, exist_ok=True)

        file_path = os.path.join(film_folder, 'film.json')

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def upload_file(self):
        film_folder = os.path.join('film_storage', self.title[0].upper(), self.title)
        os.makedirs(film_folder, exist_ok=True)

        file_path = os.path.join(film_folder, f'{self.title}.txt')
        with open(file_path, 'w') as file:
            file.write(f"Film: {self.title}\nYear: {self.year}\nDirector: {self.director}")

    def get_storage_address(self):
        return os.path.join('film_storage', self.title[0].upper(), f'{self.title}.txt')