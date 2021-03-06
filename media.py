import webbrowser

"""This class provides a way to store movie related information"""


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """This Docstring explains the contructor method, it's inputs and outputs if any"""  # NOQA
    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    """This Docstring explains what the show_trailer function does"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
