from pathlib import Path
import os
import numpy
import shutil
import tarfile
import urllib.request as request

from contextlib import closing


PROJECT_DATA_DIR = Path.cwd().parent / "data"


def _download_sift(url: str, download_dst: Path):
    download_dst.parent.mkdir(parents=True, exist_ok=True)
    with closing(request.urlopen(url)) as r:
        with open(download_dst, "wb") as f:
            shutil.copyfileobj(r, f)

    tar = tarfile.open(download_dst, "r:gz")
    tar.extractall(download_dst.parent)


def download_sift_1M(data_dir: Path = PROJECT_DATA_DIR) -> None:
    _download_sift("ftp://ftp.irisa.fr/local/texmex/corpus/sift.tar.gz", data_dir / "sift.tar.gz")


def download_sift_10K(data_dir: Path = PROJECT_DATA_DIR) -> None:
    _download_sift("ftp://ftp.irisa.fr/local/texmex/corpus/siftsmall.tar.gz", data_dir / "siftsmall.tar.gz")


def _load_sift(
    data_path: Path, queries_path: Path, labels_path: Path
) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    return (
        read_vecs(data_path),
        read_vecs(queries_path),
        read_vecs(labels_path, ivecs=True)[:, 0],
    )


def load_sift_10K(data_dir: Path = PROJECT_DATA_DIR) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    if not (data_dir / "siftsmall" / "siftsmall_base.fvecs").exists():
        print(f"Downloading SIFT10K to {data_dir} ...")
        download_sift_10K(data_dir)
        print("Download completed.")
    data_dir = data_dir / "siftsmall"

    return _load_sift(
        data_dir / "siftsmall_base.fvecs",
        data_dir / "siftsmall_query.fvecs",
        data_dir / "siftsmall_groundtruth.ivecs",
    )


def load_sift_1M(data_dir: Path = PROJECT_DATA_DIR) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
    if not (data_dir / "sift" / "sift_base.fvecs").exists():
        print(f"Downloading SIFT1M to {data_dir} ...")
        download_sift_1M(data_dir)
        print("Download completed.")
    data_dir = data_dir / "sift"

    return _load_sift(
        data_dir / "sift_base.fvecs",
        data_dir / "sift_query.fvecs",
        data_dir / "sift_groundtruth.ivecs",
    )


def read_vecs(path: Path, ivecs: bool = False) -> numpy.ndarray:
    a = numpy.fromfile(path, dtype="int32")
    d = a[0]
    matrix = a.reshape(-1, d + 1)[:, 1:].copy()

    if not ivecs:
        matrix = matrix.view("float32")

    return matrix


def evaluate(gold: numpy.ndarray, predictions: numpy.ndarray) -> float:
    """
    Compute Recall@1;
        - gold: array of shape (k,) -- integers
        - predictions: array of shape (k,) -- integers
    """
    return sum(gold == predictions)
