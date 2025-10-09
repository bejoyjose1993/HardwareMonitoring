import aiohttp

async def send(endpoint: str, data: dict):
    """
    Send metrics to an HTTP endpoint asynchronously.
    """
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(endpoint, json=data) as response:
                if response.status == 200:
                    print(f"[INFO] Successfully sent data to {endpoint}")
                else:
                    print(f"[WARN] HTTP {response.status} when sending to {endpoint}")
        except Exception as e:
            print(f"[ERROR] HTTP send failed: {e}")