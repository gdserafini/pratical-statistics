class ExploratoryDataAnalysis:
    def mean(self, numbers: list) -> float:
        return sum(numbers)/len(numbers) if numbers else 0

    def trimmed_mean(self, numbers: list, p: float) -> float:
        """
            This method calculate the mean of a list without the p-smallest and p-biggest values
            :param numbers: list to calculation: list[numbers]
            :param p: p value (%) to drop: float
            :return: mean of numbers: float
        """
        if not numbers: return 0
        numbers_len = len(numbers)
        #calculate how many values will be dropped -> p %
        trim = int(p * numbers_len)
        if 2 * trim > numbers_len: return 0
        #sort and drop
        trimmed_numbers = sorted(numbers)[trim:numbers_len-trim]
        return sum(trimmed_numbers)/len(trimmed_numbers) - 2*trim

    def weighted_mean(self, numbers: list, weights: list) -> float:
        if not numbers or not weights: return 0
        if len(numbers) != len(weights):
            raise ValueError('Number of numbers and weights do not match')
        weighted_sum = sum(n * w for n, w in zip(numbers, weights))
        return weighted_sum / sum(weights)

    def trimmed_weighted_mean(self, numbers: list, weights: list, p: float) -> float:
        if not numbers or not weights: return 0
        if len(numbers) != len(weights):
            raise ValueError('Number of numbers and weights do not match')
        numbers_len = len(numbers)
        trim = int(p * len(numbers))
        if 2 * trim > len(numbers): return 0
        trimmed_numbers = sorted(numbers)[trim:numbers_len-trim]
        trimmed_weights = sorted(weights)[trim:numbers_len-trim]
        trimmed_weight_sum = sum(n * w for n, w in zip(trimmed_numbers, trimmed_weights))
        return trimmed_weight_sum / sum(trimmed_weights)

def main() -> None:
    print((1*2 + 2*3 + 3*4)/9)
    eda = ExploratoryDataAnalysis()
    assert eda.weighted_mean([1,2,3],[2,3,4]) == 2.2222222222222223

if __name__ == '__main__':
    main()