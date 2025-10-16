
class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

title = input("Kino nomi: ")
genre = input("Kino janri: ")
duration = float(input("Davomiyligi (minutda, masalan 123.5): "))
rating = int(input("Kino reytingi: "))

movie1 = Movie(title, genre, duration, rating)

print(f"\nNatija:")
print(f"Kino nomi: {movie1.title}")
print(f"Kino janri: {movie1.genre}")
print(f"Kino davomiyligi: {movie1.duration} minut")
print(f"Reytingi: {movie1.rating}")
