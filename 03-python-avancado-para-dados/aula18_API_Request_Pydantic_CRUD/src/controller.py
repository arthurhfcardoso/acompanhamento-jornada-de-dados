import requests
from db import Base, SessionLocal, engine
from models import Pokemon
from schema import PokemonSchema

Base.metadata.create_all(bind=engine)


def fetch_pokemon_data(pokemon_name: str) -> PokemonSchema:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    )
    if response.status_code == 200:
        data = response.json()
        types = ", ".join([t["type"]["name"] for t in data["types"]])
        return PokemonSchema(name=data["name"], type=types)
    else:
        raise ValueError("Erro ao buscar Pokémon")


def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(
            name=pokemon_schema.name, type=pokemon_schema.type
        )
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    db.close()
    return db_pokemon
