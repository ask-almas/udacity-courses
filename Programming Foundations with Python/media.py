import webbrowser

class Movie():
    """ This class provides a way to store movie information """
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(this, movie_title, movie_storyline, poster_image, trailer_youtube):
        this.title=movie_title
        this.storyline=movie_storyline
        this.poster_image_url=poster_image
        this.trailer_youtube_url=trailer_youtube

    def show_trailer(this):
        webbrowser.open(this.trailer_youtube_url)
