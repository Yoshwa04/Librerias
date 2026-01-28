from typing import Dict


class CurrencyConverter:
    """
    Simple currency converter class.
    Rates should be provided as a dictionary like {'USD': 1.0, 'EUR': 0.95, 'JPY': 140}.
    """
    def __init__(self, rates: Dict[str, float]) -> None:
        self.rates = rates

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Converts amount from one currency to another using the provided rates.

        Args:
            amount: Amount of money to convert.
            from_currency: Source currency code (e.g., 'USD').
            to_currency: Target currency code (e.g., 'EUR').

        Returns:
            float: Converted amount.

        Raises:
            ValueError: If currency code is not in rates.
        """
        
        if from_currency not in self.rates:
            raise ValueError(f"Unknown currency: {from_currency}")
        if to_currency not in self.rates:
            raise ValueError(f"Unknown currency: {to_currency}")
        usd_amount = amount / self.rates[from_currency]  # Convert to USD as base
        return usd_amount * self.rates[to_currency]
