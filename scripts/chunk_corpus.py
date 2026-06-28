from pathlib import Path

from perseus_cts.chunker import Chunker
from perseus_cts.models import Corpus


def _urn_to_path(urn: str) -> Path:
    bare = urn.removeprefix("urn:cts:greekLit:")

    return Path(*bare.split("."))


def chunk_corpus(corpus_dir: Path, protopage_dir: Path):
    corpus = Corpus(corpus_dir)

    for doc in corpus.documents():
        if doc.metadata.urn.startswith(
            "urn:cts:greekLit:tlg0016.tlg001"
        ) or doc.metadata.urn.startswith("urn:cts:greekLit:tlg0003.tlg001"):
            try:
                compiler = Chunker(doc)
                compiler.compile(protopage_dir / _urn_to_path(doc.metadata.urn))
            except Exception as exc:
                print(f"  FAILED:    {doc.path.name}: {exc}")


ROOT_DIR = Path(__file__).parent.parent
CORPUS_DIR = ROOT_DIR / "corpus"
PROTOPAGE_DIR = ROOT_DIR / "proto-pages" / "greekLit"

if __name__ == "__main__":
    PROTOPAGE_DIR.mkdir(exist_ok=True)

    chunk_corpus(CORPUS_DIR, PROTOPAGE_DIR)
