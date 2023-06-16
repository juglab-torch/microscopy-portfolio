from pathlib import Path

from microscopy_portfolio import PortfolioManager

if __name__ == "__main__":
    # Create a portfolio object
    portfolio = PortfolioManager()

    # Path to the datasets list
    path_to_datasets = Path(
        ".", "src", "microscopy_portfolio", "datasets", "registry.txt"
    )

    # Export the portfolio to json
    portfolio.to_registry(path_to_datasets)
