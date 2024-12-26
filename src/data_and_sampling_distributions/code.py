from typing import Any
import src.exploratory_data_analysis.code as eda
import math


_z = {
    '0.9': 1.645,
    '0.95': 1.96,
    '0.99': 2.58,
}


def sample(
        data: Any,
        error_margin: float = 0.05,
        confidence_level: float = 0.95
) -> Any:
    sample_size = (
        ((_z[str(confidence_level)] * eda.std(data))/error_margin)**2
    )
    return data.sample(sample_size)


def sample_distribution(
        data: Any, sd_size: int, statistic: str
) -> dict:
    return {
        statistic: [
            eda.mean(sample(data[statistic]))
            for _ in range(sd_size)
        ],
        'type': f'Mean of {sd_size}'
    }


def std_error(sample: Any) -> float:
    sample_std = eda.std(sample)
    n = len(sample)
    return sample_std/math.sqrt(n)


def bootstrap(
        data: Any,
        sample_size: int,
        statistic: str = 'mean'
) -> Any:
    pass
