import fresh_tomatoes #imports file which contains layout and open browser function.

import media #imports the media file which contains the "blueprint" for project.

# Instances of the class Movie, which contain attirubutes movie_title, poster_image, trailer_youtube. 
namesake = media.Movie("The Namesake",
                       "https://upload.wikimedia.org/wikipedia/en/8/8b/The_Namesake.jpg",
                       "https://www.youtube.com/watch?v=_sOaA-4Y8tI")

#Love Aaj Kal
love_aaj_kal = media.Movie("Love Aaj Kal",
                           "http://mimg.sulekha.com/hindi/love-aaj-kal/images/wallpaper/1024-768/love-aaj-kal-new-wallpaper02.jpg",
                           "https://www.youtube.com/watch?v=dLH1gmk9_iE")

#The Hundred Foot Journey
hundred_foot_journey = media.Movie("The Hundred-Foot Journey",
                                   "https://upload.wikimedia.org/wikipedia/en/1/11/The_Hundred_Foot_Journey_(film)_poster.jpg",
                                   "https://www.youtube.com/watch?v=d2PFqd6zDrs")
# The Man Who Knew Infinity
man_infinity = media.Movie("The Man Who Knew Infinity",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3Njg4MDM3OV5BMl5BanBnXkFtZTgwMjE5ODM3ODE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=oXGm9Vlfx4w")
# Lion
lion = media.Movie("Lion",
                   "http://www.impawards.com/2016/posters/lion.jpg",
                   "https://www.youtube.com/watch?v=-RNI9o06vqo")
# Bend it Like Beckham
beckham = media.Movie("Bend It Like Beckham",
                      "http://www.impawards.com/2003/posters/bend_it_like_beckham_ver1.jpg",
                      "https://www.youtube.com/watch?v=-sETt_XmwSE")


# instances to be called on the website 
movies = [namesake, love_aaj_kal, hundred_foot_journey,
          man_infinity, lion, beckham]

# will call the function open_movies inside of the fresh_tomatoes file,
# displaying the movies in the class Movie isnde the media file.
fresh_tomatoes.open_movies_page(movies)


