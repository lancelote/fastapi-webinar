import fastapi

import services.live_weather
from models.location import Location
from models.umbrella_status import UmbrellaStatus

router = fastapi.APIRouter()


@router.get("/api/umbrella", response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    data = await services.live_weather.get_live_report(location)

    weather = data.get("weather", {})
    category = weather.get("category", "unknown")

    forecast = data.get("forecast", {})
    temp = forecast.get("temp", "unknown")

    bring = category.lower().strip() in {"rain", "mist"}

    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)
