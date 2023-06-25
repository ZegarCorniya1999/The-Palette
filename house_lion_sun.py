#Create class ArtStudio that contains all of the variables needed to define an art studio.
class ArtStudio:
  def __init__(self,name,location,classes,workshops,events):
    self.name = name
    self.location = location
    self.classes = classes
    self.workshops = workshops
    self.events = events

#Create function that will create a new ArtStudio object, populate its variables, and add it to an array of studios. 
def create_art_studio(name,location,classes,workshops,events):
  art_studio = ArtStudio(name,location,classes,workshops,events)
  art_studios_array.append(art_studio)

#Create function to display all information about an ArtStudio object.
def print_art_studio(studio):
  for studio in art_studios_array:
    print('Name: ', studio.name)
    print('Location: ', studio.location)
    print('Classes: ', studio.classes)
    print('Workshops: ', studio.workshops)
    print('Events: ', studio.events)
    print('\n')

#Create array to hold all of the ArtStudio objects.
art_studios_array = []

#Prompt user for information to create a new ArtStudio and add it to our array.
name = input('Please enter the name of your art studio: ')
location = input('Please enter the location of your art studio: ')
classes = input('Please enter the classes offered by your art studio: ')
workshops = input('Please enter the workshops offered by your art studio: ')
events = input('Please enter the events offered by your art studio: ')

#Create a new art studio using the user's information.
create_art_studio(name,location,classes,workshops,events)

#Print out all of the information we have about our art studios.
print_art_studio(art_studios_array)