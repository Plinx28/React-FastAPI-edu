from functools import lru_cache
from aiohttp import ClientSession

class HttpClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )

class CMCHTTPClient(HttpClient):
    @lru_cache(maxsize=None)
    async def get_listings(self):
        async with self.session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]

    @lru_cache(maxsize=None)
    async def get_coin(self, coin_id):
        async with self.session.get(
                "/v2/cryptocurrency/quotes/latest",
                params={"id": coin_id}
        ) as response:
            result = await response.json()
            return result["data"][str(coin_id)]

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()
