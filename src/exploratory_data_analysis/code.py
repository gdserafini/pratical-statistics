from typing import Any
import math
from collections.abc import Iterable


_MAD_K = 1.4826
_P25TH = 25
_P50TH = 50
_P75TH = 75


def _validate_numbers(numbers: Iterable) -> None:
    if not isinstance(numbers, Iterable) or len(list(numbers)) <= 0:
        raise ValueError('Invalid data params.')


def mean(numbers: Iterable) -> float:
    """
    Calculates the mean of a list of numbers.
    :param numbers: A list of numbers -> Iterable.
    :return: The mean of the numbers -> float.
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    return sum(numbers)/len(list(numbers))


def trimmed_mean(numbers: list, p: float) -> float:
    if not numbers or p <= 0: return 0
    numbers_len = len(numbers)
    trim = int(p * numbers_len)
    if 2 * trim > numbers_len: return 0
    trimmed_numbers = sorted(numbers)[trim:numbers_len-trim+1]
    return sum(trimmed_numbers)/(len(trimmed_numbers) - 2*trim)


def weighted_mean(numbers: list, weights: list) -> float:
    if not numbers or not weights: return 0
    if len(numbers) != len(weights):
        raise ValueError('Number of numbers and weights do not match')
    weighted_sum = sum(n * w for n, w in zip(numbers, weights))
    return weighted_sum / sum(weights)


def trimmed_weighted_mean(numbers: list, weights: list, p: float) -> float:
    if not numbers or not weights or p <= 0: return 0
    numbers_len = len(numbers)
    if numbers_len != len(weights):
        raise ValueError('Number of numbers and weights do not match')
    trim = int(p * numbers_len)
    if 2 * trim > numbers_len: return 0
    trimmed_numbers = sorted(numbers)[trim:numbers_len-trim+1]
    trimmed_weights = sorted(weights)[trim:numbers_len-trim+1]
    trimmed_weight_sum = sum(n * w for n, w in zip(trimmed_numbers, trimmed_weights))
    return trimmed_weight_sum / sum(trimmed_weights)


def median(numbers: list) -> float | None:
    numbers_len = len(numbers)
    if numbers_len == 0: return None
    if numbers_len % 2 != 0:
        return sorted(numbers)[numbers_len//2]
    else:
        sorted_numbers = sorted(numbers)
        return (
                sorted_numbers[numbers_len//2] +
                sorted_numbers[numbers_len//2 - 1]
        )/2


def mean_ad(numbers: list[Any]) -> float:
    """
    Calculates the mean absolute deviation of a list of numbers.
    The mean difference between the observed data and the mean of the list.
    :param numbers: A list of numbers -> list[Any].
    :return: MAD -> float
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    numbers_mean = mean(numbers)
    abs_deviation = sum(abs(_ - numbers_mean) for _ in numbers)
    return abs_deviation/len(numbers)


def variance(numbers: list[Any]) -> float:
    """
    Calculate the variance of a list.
    The mean of squared deviations.
    :param numbers: A list of numbers -> list[Any].
    :return: V -> float
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    numbers_mean = mean(numbers)
    return (sum((_ - numbers_mean)**2 for _ in numbers))/(len(numbers)-1)


def std(numbers: list[Any]) -> float:
    """
    Calculate the standard deviation of a list.
    The square root of the variance.
    :param numbers: A list of numbers -> list[Any].
    :return: V -> float
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    return math.sqrt(variance(numbers))


def mad(numbers: list[Any], normalize: bool = False) -> float:
    """
    Calculate the median absolute deviation (MAD) of a list.
    The median of the abolutes deviations of the median.
    :param numbers: A list of numbers -> list[Any].
    :param normalize: Normalize if is a normal distribution.
    :return: V -> float
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    numbers_median = median(numbers)
    abs_median_deviation = [abs(_ - numbers_median) for _ in numbers]
    mad = median(abs_median_deviation)
    return mad * _MAD_K if normalize else mad


def percentile(numbers: list[Any], p: float) -> float:
    """
    Calculate the percentile value of a sorted list. 
    The value that is equal or bigger than p-percent of a sorted list.
    :param numbers: A list of numbers -> list[Any].
    :param p: p-percent.
    :return: percentile(p) -> float
    :raises ValueError: If 'numbers' or 'p' is invalid.
    """
    _validate_numbers(numbers)
    if not p or p < 0 or p > 100:
        raise ValueError('Invalid p.')
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    k = (p/100)*(n-1)
    j = int(k)
    w = k - j
    return (1-w) * sorted_numbers[j] + w * sorted_numbers[j+1]\
        if j <= n - 1 else 0.0


def iqr(numbers: list[Any]) -> float:
    """
    Calculate the interquartile range (IQR) of a sorted list. 
    The difference between the 25th and 75th percentiles.
    :param numbers: A list of numbers -> list[Any].
    :return: iqr -> float
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    return percentile(numbers, _P75TH) - percentile(numbers, _P25TH)


def quartiles(numbers: list[Any]) -> dict:
    """
    Calculate the quartiles of a sorted list. 
    25th, 50th and 75th.
    :param numbers: A list of numbers -> list[Any].
    :return: percentiles table -> dict
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    pths = [_P25TH, _P50TH, _P75TH]
    return {
        str(p): percentile(numbers, p) for p in pths
    }


def box_plot_marks(numbers: list[Any]) -> dict:
    """
    Calculate the marks of a sorted list for a boxplot. 
    Q1, Q2, Q3, whiskers up and whiskers down.
    :param numbers: A list of numbers -> list[Any].
    :return: boxplot table -> dict
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    iqr_ = iqr(numbers)
    quartiles_ = quartiles(numbers)
    up = quartiles_['75'] + 1.5 * iqr_
    down = quartiles_['25'] - 1.5 * iqr_
    return {
        'WD': down,
        '25': quartiles_['25'],
        '59': quartiles_['50'],
        '75': quartiles_['75'],
        'WP': up
    }


def outliers(numbers: list[Any]) -> dict:
    """
    Get the outliers of a list.
    Dict with 'top' (> Q3 + 1.5 * IQR) and 'bottom' (< Q1 - 1.5 * IQR).
    :param numbers: A list of numbers -> list[Any].
    :return: outliers -> dict
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    iqr_ = iqr(numbers)
    quartiles_ = quartiles(numbers)
    up = quartiles_['75'] + 1.5 * iqr_
    down = quartiles_['25'] - 1.5 * iqr_
    return {
        'top': list(filter(lambda n: n > up, numbers)),
        'bottom': list(filter(lambda n: n < down, numbers))
    }


def frequency_table(numbers: list[Any], bins: int = 1) -> dict:
    """
    Get the frequencies of a sorted list.
    :param numbers: A list of numbers -> list[Any].
    :param bins: Number of bins.
    :return: frequency -> dict
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    if not bins or bins <= 0 or not isinstance(bins, int):
        raise ValueError("Invalid 'bins' value.")
    min_value = min(numbers)
    max_value = max(numbers)
    bin_width = (max_value - min_value) / bins
    bins = [
        (min_value + i * bin_width, min_value + (i+1) * bin_width)
        for i in range(bins)
    ]
    frequency_table = {
        f"[{i + 1} ({round(b[0], 2)} - {round(b[1], 2)}]": 0
        for i, b in enumerate(bins)
    }
    for num in numbers:
        for i, (start, end) in enumerate(bins):
            if start <= num < end:
               frequency_table[f"Bin {i + 1} ({round(start, 2)} - {round(end, 2)}]"] += 1
               break
    return frequency_table


def kernel(
    x: float, xi: float, bandwidth: float) -> float:
    """
    Calculate the gaussian kernel of a value.
    :param x: x value -> float.
    :param xi: xi value -> float.
    :param bandwidth: bandwidth -> float.
    :return: gaussian kernel density (point) -> float.
    :raises ValueError: If params is invalid.
    """
    if not x or not xi or not bandwidth:
        raise ValueError('Invalid params values.')
    return (
        (1/math.sqrt(2 * math.pi)) * (math.e ** (-0.5 * ((x - xi) / bandwidth) ** 2))
    )

def density(
        x: float, numbers: list[float],
        bandwidth: float) -> float:
    """
    Calculate the density of a sorted list.
    :param x: x value -> float.
    :param numbers: A list of numbers -> list[Any].
    :param bandwidth: bandwidth -> float.
    :return: density -> float.
    :raises ValueError: If params is invalid.
    """
    numbers_len = len(numbers)
    return (
        (1/numbers_len*bandwidth) *
        sum(kernel(x, xi, bandwidth) for xi in numbers)
    )


def counter(values: list[Any]) -> dict:
    """
    Count the occurrences of a number in a list of numbers.
    :param values: A list of numbers -> list[Any].
    :return: Counter -> dict
    :raises ValueError: If params is invalid.
    """
    _validate_numbers(values)
    count = {}
    for value in values:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    return count


def proportion(values: list[Any]) -> dict:
    """
    Calculate the proportion of a value in list.
    :param values: A list of numbers -> list[Any].
    :return: Proportion -> dict
    :raises ValueError: If params is invalid.
    """
    count = counter(values)
    total = sum(count.values())
    proportion = {}
    for value in count:
        proportion[value] = round((count[value] / total), 2)
    return proportion


def mode(numbers: list[Any]) -> float:
    """
    Calculate the mode of a sorted list.
    :param numbers: A list of numbers -> list[Any].
    :return: Mode -> float.
    :raises ValueError: If params is invalid.
    """
    _validate_numbers(numbers)
    count = counter(numbers)
    sorted_numbers = dict(
        sorted(count.items(), key=lambda item: item[1], reverse=True)
    )
    return list(sorted_numbers.keys())[0]


def expected_value(values: list[Any], probabilities: list[float]) -> float:
    """
    Calculate the expected value of a list of numbers.
    :param values: A list of numbers -> list[Any].
    :param probabilities: A list of probabilities -> list[float].
    :return: Expected value -> float.
    :raises ValueError: If params is invalid.
    """
    _validate_numbers(values)
    _validate_numbers(probabilities)
    return sum(v * p for v, p in zip(values, probabilities))


def probability(value: Any, numbers: list[Any]) -> float:
    """
    Calculate the probability of a value in a list of numbers.
    :param value: Value -> float.
    :param numbers: A list of numbers -> list[Any].
    :return: Probability -> float.
    :raises ValueError: If params is invalid.
    """
    if not value or value not in numbers:
        raise ValueError('Invalid value.')
    _validate_numbers(numbers)
    proportions = proportion(numbers)
    return proportions[value]


def _get_r_metrics(x: list[Any]) -> tuple:
    return mean(x), std(x)


def correlation_coefficient(x: list[Any], y: list[Any]) -> float:
    """
    Calculate the correlation coefficient of a sorted list of numbers.
    :param x: A list of numbers -> list[Any].
    :param y: A list of numbers -> list[Any].
    :return: Correlation coefficient -> float.
    :raises ValueError: If params is invalid.
    """
    _validate_numbers(x)
    _validate_numbers(y)
    if len(x) != len(y):
        raise ValueError('x and y must have the same length.')
    mean_x, std_x = _get_r_metrics(x)
    mean_y, std_y = _get_r_metrics(y)
    sum_r = sum((x - mean_x) * (y - mean_y) for x, y in zip(x, y))
    return sum_r / ((len(x) - 1) * std_x * std_y)