import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys",
                      "http://www.wetpaint.com/wp-content/uploads/2015/11/toy-story-20th-anniversary.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar=media.Movie("Avatar",
                   "A marine travels to alien planet",
                   "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(toy_story.title)
#print(avatar.storyline)
#avatar.show_trailer()
movies=[toy_story, avatar]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)
