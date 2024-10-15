class ExploratoryDataAnalysis:
    def mean(self, numbers: list) -> float:
        return sum(numbers)/len(numbers) if numbers else 0

    def trimmed_mean(self, numbers: list, p: float) -> float:
        if not numbers or p <= 0: return 0
        numbers_len = len(numbers)
        #calculate how many values will be dropped -> p %
        trim = int(p * numbers_len)
        if 2 * trim > numbers_len: return 0
        #sort and drop
        trimmed_numbers = sorted(numbers)[trim:numbers_len-trim+1]
        return sum(trimmed_numbers)/(len(trimmed_numbers) - 2*trim)

    def weighted_mean(self, numbers: list, weights: list) -> float:
        if not numbers or not weights: return 0
        if len(numbers) != len(weights):
            raise ValueError('Number of numbers and weights do not match')
        weighted_sum = sum(n * w for n, w in zip(numbers, weights))
        return weighted_sum / sum(weights)

    def trimmed_weighted_mean(self, numbers: list, weights: list, p: float) -> float:
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

def main() -> None:
    pass

if __name__ == '__main__':
    main()
