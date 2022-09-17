import httpx
import logging
from loguru import logger

from pydantic import BaseModel


class PropagateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logger.add(PropagateHandler(), format="{message}")


class Generation(BaseModel):
    name: str

class PokemonResponse(BaseModel):
    id: int
    name: str
    generation: Generation

class PokeapiClient():
    async def retrieve_pokemon_info(pokemon_name: str):
        try:
            async with httpx.AsyncClient() as client:
                logger.info(f"Retrieving info for {pokemon_name}")
                #logging.info(f"Retrieving info for {pokemon_name}")
                result = await client.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/")
            result.raise_for_status()
        except httpx.HTTPError as err:
            logger.error('http error while retrieving pokemon species')
            #logging.error('http error while retrieving pokemon species')            
            return str(err)
        logger.info(f"HTTP RESULT -> {result}")
        #logging.info(f"HTTP RESULT -> {result}")
        return PokemonResponse(**dict(result.json()))