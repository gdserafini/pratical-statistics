from typing import Any
import math

_MAD_K = 1.4826

def _validate_numbers(numbers: list) -> None:
    if not numbers or not isinstance(numbers, list) or len(numbers) <= 0:
        raise ValueError('Invalid data params.')

def mean(numbers: list[Any]) -> Any:
    """
    Calculates the mean of a list of numbers.
    :param numbers: A list of numbers -> list[Any].
    :return: The mean of the numbers -> Any.
    :raises ValueError: If 'numbers' is invalid.
    """
    _validate_numbers(numbers)
    return sum(numbers)/len(numbers)

def trimmed_mean(numbers: list, p: float) -> float:
    if not numbers or p <= 0: return 0
    numbers_len = len(numbers)
    #calculate how many values will be dropped -> p %
    trim = int(p * numbers_len)
    if 2 * trim > numbers_len: return 0
    #sort and drop
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

def meanad(numbers: list[Any]) -> float:
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
