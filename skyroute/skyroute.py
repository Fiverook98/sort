from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmarks_choices import landmark_choices


landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += f"{letter} - {landmark}"

station_under_construct = ['Olympic Village']
#gettin station under construction
def get_active():
  updated_metro = vc_metro.copy()
  for station in station_under_construct:
    for cur_station, neighbor in vc_metro.items():
      if not cur_station is station:
        updated_metro[cur_station] -= {station} if station in neighbor else set()
      else:
        updated_metro[cur_station] = set([])
  return updated_metro
  
#showing landmarks
def show_landmarks():
  see_land = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_land == 'y':
    print(landmark_string)

#Greetings
def greet():
  print("Hi there and welcome to SkyRoute!")
  print(f"We'll help you find the shortest route between the foolowing Vancouver landmarks:\n{landmark_string}")

#Goodbye
def goodbye():
  print("Thanks for using SkyRoute!")

#setting start and end
def set_start_and_end(start_point, end_point):
  if not start_point is None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")

    if change_point == "b":
      start_point = get_start()
      end_point = get_end()

    elif change_point == 'o':
      start_point = get_start()

    elif change_point == 'd':
      end_point = get_end()

    else:
      print("Oops, than isn't 'o', 'd' or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()

  return start_point, end_point

#Obtaing start
def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's nota landmark we have data on. Let's try this again...")
    get_start()

#obtaing end
def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    show_landmarks()
    print("Sorry, that's nota landmark we have data on. Let's try this again...")
    get_end()

#change route
def new_route(start_point = None, end_point = None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  short_route = get_route(start_point, end_point)
  if short_route != None:
    short_route_str = '\n'.join(short_route)
    print(f"The shortest metro route from {start_point} to {end_point} is:\n{short_route_str}")
  else:
    print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance.")

  again =input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    show_landmarks()
    new_route(start_point, end_point)

#geating shortest route
def get_route(start_point, end_point):

  start_station = vc_landmarks[start_point]
  end_station = vc_landmarks[end_point]
  routes = []

  for start in start_station:

    for end in end_station:

      metro_sys = get_active() if station_under_construct else vc_metro

      if station_under_construct != []:
        pos_route = dfs(metro_sys, start, end)
        if pos_route:
          routes.append(pos_route)
        continue

      route = bfs(metro_sys, start, end)

      if route != None:
        routes.append(route)

  if routes:
    shortest_route = min(routes, key = len)
    return shortest_route

def skyroute():
  greet()
  new_route()
  goodbye()

skyroute()