class MovieDetails:
    def __init__(self,artistName,yearOfRelease,ratings):
        self.name=artistName
        self.year=yearOfRelease
        self.ratings=ratings
    
    def Add(self,movieName):
        self.movieName=movieName
    def Display(self):
        print(self.name)
        print(self.year)
        print(self.ratings)
        print(self.movieName)
details=MovieDetails(input("Enter Artist Name"),int(input("Enter Movie Year")),int(input("Enter Movie Rating")))
details.Add(input("Enter Movie Name : "))
details.Display()
