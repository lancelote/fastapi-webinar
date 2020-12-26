import httpx

from models.location import Location


async def get_live_report(location: Location):
    base_url = "https://weather.talkpython.fm/api/weather"
    url = f"{base_url}?city={location.city}&country={location.country}&units=imperial"

    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    return data
