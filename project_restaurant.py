# Define a function to check if the selected city matches the city of a restaurant
def city_place(city,city_array) :
   point = 0
   if city == "" :      # If no city is specified by the user: If user leaves it blank
       point += 1
   elif city == city_array :    # If the city matches
       point += 1
   else :                 # If the city does not match
       point += 0
   return point
# Define a function to check if the selected food category matches the food category of a restaurant
def food_category(food,food_array) :
   point = 0
   if food == "":             # If no food category is specified by the user : If user leaves it blank
       point += 1
   elif food == food_array:       # If the food category matches
       point += 1
   else:                         # If the food category does not match
       point += 0
   return point
# Define a function to check if the selected restaurant type matches the restaurant type
def restaurant_function(restaurant,restaurant_array):
   piste = 0
   if restaurant == "":
       piste += 1
   elif restaurant == restaurant_array:
       piste += 1
   else:
       piste += 0
   return piste
# Define a function to check if the selected price range matches the price range of a restaurant
def price_range(price,price_array) :
   point = 0
   if price == "":
       point += 1
   elif  price == price_array :
       point += 1
   else:
       point += 0
   return point
# Define a function to check if the selected Michelin star rating matches the Michelin star rating of a restaurant
def michel_stars(star,array_star) :
   piste = 0
   if star == "":
       piste += 1
   elif star == array_star:
       piste += 1
   else:
       piste += 0
   return piste

import sys

def main() :
   print("Welcome to the Restaurant Lover! We offer you different restaurant recommendations according to your own liking in Spain and in Switzerland! Let's start")
   # Ask user the name of the file which the user want to use(the swiss or the spanish one)
   file_name = input("Enter the name of the file you'd like to read:Choices(Swiss_Restaurants or Spanish_Restaurants)\n")
   if file_name == "Swiss_Restaurants":
       print("Swiss city options are : Basel, Neuchâtel, Zürich, Sankt Gallen, Lausanne, Genève, Bern, Crissier, Lucerne, Fribourg, Andermatt, Lugano")
   elif file_name=="Spanish_Restaurants":
       print("Spanish city options are: Madrid, Barcelona, Girona")
   else:
       print("File not found. Program ends. Please check that you spelled the file name correctly.")
       sys.exit (1)

   # Get the user's criteria for the restaurant
   print("Enter your criteria for the restaurant. Submit an empty line if the specific criterion does not matter.")
   city_choice = input("Which city should the restaurant be located in?\n")
   valid_city = ["Basel", "Neuchâtel", "Zürich", "Sankt Gallen", "Lausanne", "Genève", "Bern", "Crissier", "Lucerne", "Fribourg", "Andermatt", "Lugano", "Madrid", "Girona", "Barcelona"]
   if city_choice not in valid_city:
       print ("invalid city entered. Program ends. Please check that the city name was spelled correctly.")
       sys.exit(1)
   valid_food = ["pizza", "pasta", "burgers", "vegan", "multiple"]
   food_choice = input('What type of food would you like? The options are "pizza", "pasta", "burgers", "vegan" and "multiple".\n')
   if food_choice not in valid_food:
       print ("invalid food choice entered. Program ends. Please check that the chosen food type was spelled correctly.")
       sys.exit(1)
   valid_restaurant = ["fine dining", "casual dining", "fast food", "pop-up"]
   restaurant_options = input('How about the kind of restaurant you would like to go to? The options are "fine dining", "casual dining", "fast food" and "pop-up".\n')
   if restaurant_options not in valid_restaurant:
       print ("invalid restaurant type entered. Program ends. Please check that the chosen restaurant type was spelled correctly.")
       sys.exit(1)
   valid_price =  ["$","$$","$$$"]
   price_choice = input('What is your desired price range? The options are "$","$$" and "$$$"\n')
   if price_choice not in valid_price:
       print ("invalid price range entered. Program ends. Please check that the chosen price range was spelled correctly.")
       sys.exit(1)
   valid_star  = ["1","2","3","0"]
   michel_star_choice = input("How many Michelin stars should the restaurant have?\n")
   if michel_star_choice not in valid_star:
       print ("invalid michelin star choice entered. Program ends. Please note that the amount of possible stars ranges from 0 to 3.")
       sys.exit(1)
   # Creating lists to store points and chosen restaurants
   points = []
   chosen_restaurants = []
   word_list = {}
   i = 0
   recommendations = []
   try :
       # Open the specified file for reading
       file = open(file_name, "r")
       for array in file :
           array = array.rstrip()
           parts = array.split(",")
           if len(parts) != 6 :   # Validate the format of each line
               print("Invalid line:",array)
               print()
           else :
               # Calculate points based on user criteria
               city = city_place(city_choice,parts[1])
               if city == 1 :
                   food = food_category(food_choice,parts[2])
                   restaurant = restaurant_function(restaurant_options,parts[3])
                   price = price_range(price_choice,parts[4])
                   michelin_star = michel_stars(michel_star_choice,parts[5])
                   point = int(city) + int(food) + int(restaurant) + int(price) + int(michelin_star)
                   # Store the points and corresponding restaurant
                   points.append(point)
                   chosen_restaurants.append(array)
                   word_list[array] = point
       file.close()    # Close the file
       # Sort points to find the chosen  restaurants
       points2 =sorted(points)
       for word in range(len(word_list)) :
           if word_list[chosen_restaurants[i]] == points2[len(points2)-1] :
               recommendations.append(chosen_restaurants[i])
           i += 1
       # Print the recommended restaurant(s)

       if len(recommendations)  == 0 :
           print("Unfortunately, no restaurants that matched any of your criteria were found. We apologize for the inconvenience and recommand you to change your search criterion.")

       else :
           print("The recommended restaurant(s):")
           for ravinto in recommendations :
               print(ravinto)
               print("Thank you for using Restaurant Lover!")

   except OSError :
       print("There was an error in reading the file. Program ends.")


# Run the main function
main()











