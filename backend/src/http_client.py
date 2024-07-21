from aiohttp import ClientSession
from async_lru import alru_cache


# Это интерфейс, поэтому API_KEY лучше передать в конструктор, а не
# инициализировать при создании объекта класса
class HttpClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )


class CMCHTTPClient(HttpClient):
    @alru_cache
    async def get_listings(self):
        async with self.session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]

    @alru_cache
    async def get_coin(self, coin_id):
        async with self.session.get(
                "/v2/cryptocurrency/quotes/latest",
                params={"id": coin_id}
        ) as response:
            result = await response.json()
            return result["data"][str(coin_id)]

