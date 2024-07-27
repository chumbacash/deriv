import asyncio
import websockets
import json

app_id = 1089  # Replace with your app_id or leave the current one for testing.
url = f"wss://ws.derivws.com/websockets/v3?app_id={app_id}"

async def get_active_symbols():
    async with websockets.connect(url) as websocket:
        # Define the request payload to get active symbols
        active_symbols_request = {
            "active_symbols": "brief",
            "product_type": "basic",
        }
        
        # Send the request
        await websocket.send(json.dumps(active_symbols_request))

        while True:
            # Wait for a message from the WebSocket server
            response = await websocket.recv()
            data = json.loads(response)
            
            # Check for errors
            if 'error' in data:
                print('Error:', data['error'].get('message', 'Unknown error'))
                break
            
            # Process active symbols response
            if data.get('msg_type') == 'active_symbols':
                print('Active Symbols:', data.get('active_symbols'))
                break

# Run the async function
asyncio.run(get_active_symbols())
