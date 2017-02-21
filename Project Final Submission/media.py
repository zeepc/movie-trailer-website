import webbrowser

class Movie():
    """
    Movie is the program blueprint. When called,
    each instance will display its unique attributes
    according to the specifications defined within
    """
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
