# imports
import berserk
from dotenv import load_dotenv
import os
# import time
import threading
import queue

def setup():
    # import variable here (token, board position)
    # connect to API
    pass

def find_game():

    # send a challenge to sarbor
    game_id = "foo"

    return(game_id)

def play(game):

    # set up
    # set up a thread to listen for moves and chuck them in the queue
    # set up a thread to handle the camera and chuck outputs into the queue
    # figure out if white or black / whose

    # if we're black
    # also query the other api endpoint
    # make sure the board is up to date

    # run an asynchronous function to manage everything
    # when something gets chucked in the queue
        # if the move is not equal to the turn: error
        # if the move is equal to the turn:
            # if it's opponent's move
                # announce the move
                # pass move to the camera
    pass

def stream_lichess_events(client, lichess_queue):
    event_stream = client.board.stream_incoming_events()

    for event in event_stream:
        print(event)
        lichess_queue.put(event)

def stream_game_events(client, game_id, opponents_moves):
    event_stream = client.board.stream_incoming_events()

    for event in event_stream:
        print(event)
        lichess_queue.put(event)

if __name__ == '__main__':
    # run setup code
    
    # let the user specify the board
    # fine tune img recognition options
    # change the API token etc.


    # find a game

    load_dotenv()  # Load environment variables from .env file
    API_TOKEN = os.getenv('API_TOKEN')
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)

    # send a challenge
    lichess_queue = queue.Queue()
    t = threading.Thread(target=stream_lichess_events,
                         daemon=True,
                         kwargs={'client':client, 'lichess_queue':lichess_queue})
    t.start()

    while True:
        event = lichess_queue.get()
        print(f"Processing event: {event}")

        if event['type'] == "gameStart":
            print("game start!")
            id = event['game']['fullId']
            break

    print(f"Initialising game with {id}")
    print(lichess_queue)

    # potential flip board


    # play the game
    turn_white = True
    my_moves = queue.Queue()
    opponents_move = queue.Queue()

    # Main thread can continue running other tasks


    # multithreading bs

    pass