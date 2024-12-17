from typing import Any


def _z_value(data: Any) -> float:
    pass


def sample(
    data: Any, replacement: bool = False,
    error_margin: float = 0.05, confidence_level: float = 0.95,
    distribution: float = 0.5, increase: float = 0.0,
    stratum_column: str = None, strata: list[str] = None
) -> Any:
    pass
