from typing import Any

def mean(numbers: list) -> Any:
    if not numbers or not isinstance(numbers, list) or len(numbers) <= 0:
        raise ValueError('Invalid data params.')
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