from fastapi import APIRouter

from init import cmc_client

router = APIRouter(
    prefix="/cryptocurrencies"
)


@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/{coin_id}")
async def get_coin(coin_id: int):
    return await cmc_client.get_coin(coin_id)


