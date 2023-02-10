# adapted from the docs on websockets:
# https://websockets.readthedocs.io/en/stable/howto/quickstart.html


import asyncio
import websockets

# can change the function name from hello just make sure its changed in main call
async def hello(websocket):

    # here you await the text being sent
    message = await websocket.recv()
    # this is to confirm you got the text and its stored as a string
    print(f" Received: {message}")
    print(type(message))

    # do the calculations and store in the variable here
    reading_grade_level = "Grade 9"

    # send back the reading grade level to my web app :)
    await websocket.send(reading_grade_level)

async def main():
    async with websockets.serve(hello, "localhost", 8999):
        await asyncio.Future()  # run forever

asyncio.run(main())