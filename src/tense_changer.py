# waiting for some rules from Anca Dinu
import argparse


def _build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--sentence",
        help=f"sentence to change",
        type=str,
    )
    args = parser.parse_args()
    return args


def main(sentence: str):
    return sentence


if __name__ == "__main__":
    args = _build_parser()
    main(args.sentence)
