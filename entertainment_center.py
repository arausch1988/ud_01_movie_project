import media
import fresh_tomatoes

# movie instaces are built

toy_story = media.Movie("Toystory",
                        "Kids Movie",
                        ("https://images-na.ssl-images-amazon.com/images/M/" +
                         "MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@." +
                         "_V1_UY268_CR3,0,182,268_AL_.jpg"),
                        "https://www.youtube.com/watch?v=P6jMPoIXG1g")
avatar = media.Movie("Avatar",
                     "Science Fiction blue man movie",
                     ("https://upload.wikimedia.org/wikipedia" +
                      "/en/b/b0/Avatar-Teaser-Poster.jpg"),
                     "https://www.youtube.com/watch?v=l0GnS1yNZd4")
schokolade = media.Movie("Schokolade zum Fruehstueck",
                         "Bridget is getting married",
                         "https://www.cinemaxx.de/art/film/web/" +
                         "60/72/8a/58157_poster_gross_w300.jpg",
                         "https://www.youtube.com/watch?v=dkrEyS5bj2w")
toni_erdmann = media.Movie("Toni Erdmann",
                           "crazy German movie",
                           ("http://dl9fvu4r30qs1.cloudfront.net/40/f6/" +
                            "33de00fa4b778f694eba61d9563c/" +
                            "toni-erdmann-poster.jpg"),
                           "https://www.youtube.com/watch?v=j0uwi5EPnpA")
die_hard = media.Movie("Die Hard 4.0",
                       "Famous movie with Bruce Willis",
                       ("http://www.dvd-forum.at/img/uploaded/" +
                        "kinoplakate/large/121437775143902600.jpg"),
                       "https://www.youtube.com/watch?v=3EUJYh32KVw")
mission_impossible = media.Movie("Mission Impossible 5",
                                 "Agent Thriller with Tom Cruise",
                                 ("https://gfx.videobuster.de/archive/v/" +
                                  "cbQtsDb_Izcn_WVhXCBMscQcz0lMkawqyUyR" +
                                  "qglMkZpbWGZJTJGanBlZyUyRmYzYjDJY2amYzV" +
                                  "kYWM1YWZkx9HYtNxiYTQuanBnJnI9d-84/mission" +
                                  "-impossible-5-rogue-nation.jpg"),
                                 "https://www.youtube.com/watch?v=4e0U_aajiBA")
# instances are added to an array
movies = [toy_story, avatar, toni_erdmann,
          schokolade, die_hard, mission_impossible]

# function to create movie page is called
fresh_tomatoes.open_movies_page(movies)
