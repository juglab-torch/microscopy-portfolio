from pathlib import Path

from careamics_portfolio import PortfolioManager

if __name__ == "__main__":
    # Create a portfolio object
    portfolio = PortfolioManager()

    # Path to the datasets list
    path_to_datasets = Path(
        ".", "src", "careamics_portfolio", "datasets", "datasets.json"
    )

    # Export the portfolio to json
    portfolio.to_json(path_to_datasets)
