import requests
from pydantic import BaseModel


class PokemonSchema(BaseModel):
    name: str
    type: str


def pegar_pokemon(pokemon_id: int) -> PokemonSchema:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        return PokemonSchema(
            name=data["name"], type=data["types"][0]["type"]["name"]
        )
    raise ValueError("Erro ao buscar Pokémon")


if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(1))
    print(pegar_pokemon(13))
