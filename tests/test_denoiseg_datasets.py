import pytest
from data_portfolio import Portfolio
from data_portfolio.denoiseg_datasets import NoiseLevel, NoisyObject
from data_portfolio.portfolio import PortfolioEntry

from .utils import (
    download_checker,
    list_heavy_datasets,
    list_light_datasets,
    portoflio_entry_checker,
    unique_md5_checker,
    unique_url_checker,
)

LIGHT_DATASETS = list_light_datasets(Portfolio().denoiseg)
HEAVY_DATASETS = list_heavy_datasets(Portfolio().denoiseg)


@pytest.mark.dataset
@pytest.mark.parametrize("dataset", LIGHT_DATASETS)
def test_light_datasets(tmp_path, dataset: PortfolioEntry):
    """Test that all light DenoiSeg datasets download properly.

    This test also checks the files and size.

    Parameters
    ----------
    tmp_path : Path
        Path to temporary directory.
    dataset : Dataset
        Dataset object.
    """
    download_checker(tmp_path, dataset)


@pytest.mark.dataset
@pytest.mark.parametrize("dataset", HEAVY_DATASETS)
def test_heavy_datasets(tmp_path, dataset):
    """Test that all heavy DenoiSeg datasets download properly.

    This test also checks the files and size.

    Parameters
    ----------
    tmp_path : Path
        Path to temporary directory.
    dataset : Dataset
        Dataset object.
    """
    download_checker(tmp_path, dataset)


def test_unique_hashes(portfolio: Portfolio):
    """Test that all DenoiSeg dataset hashes are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    unique_md5_checker(portfolio.denoiseg)


def test_unique_urls(portfolio: Portfolio):
    """Test that all DenoiSeg dataset URLs are unique.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    unique_url_checker(portfolio.denoiseg)


def test_no_empty_dataset_entry(portfolio: Portfolio):
    """Test that no DenoiSeg dataset entry is empty.

    Parameters
    ----------
    portfolio : Portfolio
        Portfolio object.
    """
    for entry in portfolio.denoiseg:
        portoflio_entry_checker(entry)


@pytest.mark.parametrize("noise_level", [NoiseLevel.N0, NoiseLevel.N10, NoiseLevel.N20])
def test_noisy_dataset(noise_level):
    """Test that the NoisyDataset class works properly."""
    noisy_object = NoisyObject(noise_level=noise_level)
    assert noisy_object.noise_level == noise_level
