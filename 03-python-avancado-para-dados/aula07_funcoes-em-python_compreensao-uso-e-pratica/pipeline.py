from __future__ import annotations

from pathlib import Path

import etl


def main() -> None:
    caminho_csv = Path(__file__).with_name("vendas.csv")
    dados = etl.ler_csv(caminho_csv)
    dados_por_categoria = etl.processar_dados(dados)
    totais = etl.calcular_vendas_categoria(dados_por_categoria)
    etl.exibir_resultados(totais)


if __name__ == "__main__":
    main()
