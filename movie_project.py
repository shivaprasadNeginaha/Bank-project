class Movies:
    '''
    initializing tht class and objects
    '''

    def __init__(self):
        '''
        stroing the movies for view.movies and find.movies
        '''
        self.movies = [{'name': 'sherlock', 'year': '2009', 'genre': 'thriller'},
                       {'name': 'titanic', 'year': '1997', 'genre': 'drama'},
                       {'name': 'andhadhun', 'year': '2018', 'genre': 'crime'}]

    def find_movie(self):
        '''
        function to find the movie
        '''
        try:
            choice = input(
                "\nPlease type 'name' to find by name/ 'year' to find by year/ 'genre' to find by genre\nHow  do you want to find your movie:")
            if choice == 'name' or choice == 'year' or choice == 'genre':
                user_input = input("\nWhat are you looking for?  ")
            movie_list = list(
                filter(lambda movie: movie[choice] == user_input, self.movies))
        except Exception:
            print("Invalid option, Please try again with valid input.")
            choice = input(
                "Please type 'name' to find by name or 'year' to find by year or 'genre' to find by genre\nHow do you want to find your movie:")
            user_input = input("\nWhat are you looking for?  ")
            movie_list = list(
                filter(lambda movie: movie[choice] == user_input, self.movies))
        for movie in movie_list:
            print(f"\nMovie Name : {movie['name']}",
                  f"  Movie Year : {movie['year']}", f"  Movie Genre : {movie['genre']}")

    def add_movie(self):
        '''
        function to add the movie
        '''
        self.movies.append({'name': input("Please input name:"), 'year': input(
            "Please input year:"), 'genre': input("Please input genre:")})
        print(f"\nThe movie you said is been added to your collection: \n",
              self.movies)

    def view_movie(self):
        '''
        function to view the movie
        '''
        for movie in self.movies:
            print(f"Movie Name : {movie['name']}",
                  f"  Movie Year : {movie['year']}",
                  f"  Movie Genre : {movie['genre']}")


new_movie = Movies()
running = True
while running:
    inp = input("Please type 'find' to find any movie/ 'add' to add new movie/ 'view' to view your collection/ 'end' to end program\nWhat would you like to do: ")
    if inp == "find":
        new_movie.find_movie()
    elif inp == "add":
        new_movie.add_movie()
    elif inp == "view":
        new_movie.view_movie()
    elif inp == "end":
        print("\nThank you!")
        running = False
    else:
        print("\nPlease try again\nThank you!")
        running = False
