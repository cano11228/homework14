from media_player import Player
from films_worker import Film

# Створюємо екземпляр класу Player
player = Player(name="MyPlayer",
                video_link="https://uakino.club/filmy/genre_comedy/291-ce-bezgluzde-kohannya.html",
                duration=120)

# Викликаємо методи класу Player
player.play("https://uakino.club/filmy/genre_comedy/291-ce-bezgluzde-kohannya.html")
player.pause()
player.save_last_time(60)
player.change_quality("4K")


film = Film(
    title="Crazy, Stupid, Love.",
    description="A middle-aged husband's life changes dramatically...",
    director=["Glenn Ficarra", "John Requa"],
    writer="Dan Fogelman",
    cast=["Steve Carell", "Ryan Gosling", "Julianne Moore"],
    running_time=118,
    country="United States",
    language="English",
    imdb_rating=7.4,
    year=2011,
    budget="$50 million",
    box_office="$145 million",
    profitable=True,
    oscar_nominated=False,
    oscar_win=False,
    trailer="https://www.imdb.com/video/vi3722091801/"
)

film.save_data()
print(f"Film address: {film.get_storage_address()}")