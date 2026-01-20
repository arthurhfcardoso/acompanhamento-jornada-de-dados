from __future__ import annotations

import argparse
from pathlib import Path

from etl import load_json, save_csv, save_parquet, transform_df
from schema import build_schema, validate_df


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ETL simples com Pandas + Pandera."
    )
    parser.add_argument(
        "--input",
        "-i",
        nargs="+",
        help="Caminho(s) para arquivo(s) JSON (ex.: data/arquivo.json).",
    )
    parser.add_argument(
        "--input-dir",
        default="data",
        help="Pasta para buscar JSONs quando --input nao for informado.",
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Caminho do arquivo de saida (ex.: saidas/resultado.parquet).",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["csv", "parquet"],
        default="parquet",
        help="Formato de saida.",
    )
    return parser.parse_args()


def resolve_inputs(input_paths: list[str] | None, input_dir: str) -> list[str]:
    if input_paths:
        return input_paths
    return [str(p) for p in Path(input_dir).glob("*.json")]


def run(input_paths: list[str], output_path: str, output_format: str) -> None:
    df = load_json(input_paths)
    df = transform_df(df)
    schema = build_schema(df)
    df = validate_df(df, schema)

    output_path = str(Path(output_path))
    if output_format == "csv":
        save_csv(df, output_path)
    else:
        save_parquet(df, output_path)


def main() -> None:
    args = parse_args()
    input_paths = resolve_inputs(args.input, args.input_dir)
    if not input_paths:
        raise SystemExit(
            "Nenhum JSON encontrado. Informe --input ou use --input-dir."
        )
    run(input_paths, args.output, args.format)


if __name__ == "__main__":
    main()
