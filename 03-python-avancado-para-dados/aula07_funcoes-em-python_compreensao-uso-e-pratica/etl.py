from __future__ import annotations

import csv
from pathlib import Path
from typing import TypedDict


class VendaLinha(TypedDict):
    Produto: str
    Categoria: str
    Quantidade: int
    Venda: float


def ler_csv(caminho: Path) -> list[VendaLinha]:
    linhas: list[VendaLinha] = []
    with caminho.open(mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for indice, linha in enumerate(leitor, start=2):
            linhas.append(_parse_linha(linha, indice))
    return linhas


def _parse_linha(linha: dict[str, str], indice: int) -> VendaLinha:
    try:
        return VendaLinha(
            Produto=linha["Produto"].strip(),
            Categoria=linha["Categoria"].strip(),
            Quantidade=int(linha["Quantidade"]),
            Venda=float(linha["Venda"]),
        )
    except KeyError as exc:
        raise KeyError(f"Coluna ausente no CSV (linha {indice}).") from exc
    except ValueError as exc:
        raise ValueError(f"Valor invalido no CSV (linha {indice}).") from exc


def processar_dados(dados: list[VendaLinha]) -> dict[str, list[VendaLinha]]:
    por_categoria: dict[str, list[VendaLinha]] = {}
    for item in dados:
        categoria = item["Categoria"]
        por_categoria.setdefault(categoria, []).append(item)
    return por_categoria


def calcular_vendas_categoria(
    dados_por_categoria: dict[str, list[VendaLinha]]
) -> dict[str, float]:
    totais: dict[str, float] = {}
    for categoria, itens in dados_por_categoria.items():
        total = 0.0
        for item in itens:
            total += item["Quantidade"] * item["Venda"]
        totais[categoria] = total
    return totais


def exibir_resultados(totais: dict[str, float]) -> None:
    for categoria, total in totais.items():
        print(f"{categoria}: {total:.2f}")
