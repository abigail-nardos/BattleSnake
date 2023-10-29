# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing


# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
    print("INFO")

    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#6F2DA8",  # TODO: Choose color
        "head": "evil",  # TODO: Choose head
        "tail": "freckled",  # TODO: Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {
      "up": True, 
      "down": True, 
      "left": True, 
      "right": True
    }
  
    my_head = game_state["you"]["body"][0] 

    # Prevents snake from hitting the bounds
    board_width = game_state['board']['width']
    board_height = game_state['board']['height']
    
    if my_head["x"]+1 == board_width:
      is_move_safe["right"] = False
    if my_head["x"] == 0:
      is_move_safe["left"] = False
    if my_head["y"]+1 == board_height:
      is_move_safe["up"] = False
    if my_head["y"] == 0:
      is_move_safe["down"] = False
     

    # Prevents snake from colliding with itself
    my_body = game_state['you']['body']
    nadya = [] #2d array of body on board matrix
    for i in my_body:
      position = []
      position.append(i["x"])
      position.append(i["y"])
      nadya.append(position)

    snakes = []
    opponents = game_state['board']['snakes']
    for snake in opponents:
      cur = snake['body']
      for j in cur:
        position = []
        position.append(j["x"])
        position.append(j["y"])
        snakes.append(position)
      
    
    right = []
    right.append(my_head["x"]+1)
    right.append(my_head["y"])

    left = []
    left.append(my_head["x"]-1)
    left.append(my_head["y"])

    up = []
    up.append(my_head["x"])
    up.append(my_head["y"]+1)
  
    down = []
    down.append(my_head["x"])
    down.append(my_head["y"]-1)
  
    if right in snakes:
      is_move_safe["right"] = False
    if left in snakes:
      is_move_safe["left"] = False
    if up in snakes:
      is_move_safe["up"] = False
    if down in snakes:
      is_move_safe["down"] = False     

  
    # Are there any safe moves left?
    safe_moves = []
    for move, isSafe in is_move_safe.items():
        if isSafe:
            safe_moves.append(move)

    if len(safe_moves) == 0:
        print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
        return {"move": "down"}

    # Choose a random move from the safe ones
    next_move = random.choice(safe_moves)

    # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
    

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}
  

# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({
        "info": info, 
        "start": start, 
         "move": move, 
        "end": end
    })
