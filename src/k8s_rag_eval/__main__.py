"""Entry point for `python -m k8s_rag_eval`."""

from k8s_rag_eval import __version__


def main() -> int:
    print(f"k8s-rag-eval {__version__}")
    print("Scaffold only. Pipeline stages land in later sessions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
