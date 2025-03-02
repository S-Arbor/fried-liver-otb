import asyncio, berserk, json, os
from dotenv import load_dotenv
import os

def establish_session_client():
    
    # load token
    load_dotenv()
    API_TOKEN = os.getenv('API_TOKEN')

    # establish client and session
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)

    return session, client

def listen_match():
    

# Queue to store opponent moves safely
# move_queue = asyncio.Queue()
# event_stream = client.board.stream_incoming_events()

# # Function to listen for opponent moves using WebSocket
# async def fetch_moves():
#     headers = {"Authorization": f"Bearer {LICHESS_TOKEN}"}
    
#     async with websockets.connect(LICHESS_WS_URL, extra_headers=headers) as ws:
#         async for message in ws:
#             data = json.loads(message)
#             if "state" in data and "moves" in data["state"]:
#                 moves = data["state"]["moves"].split()
#                 opponent_move = moves[-1] if moves else None
#                 if opponent_move:
#                     await move_queue.put(opponent_move)
#                     print(f"\nOpponent moved: {opponent_move}")
#                     print("Your turn:", end=" ", flush=True)