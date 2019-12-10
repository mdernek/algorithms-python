# How to Find all Pairs in Array of Integers
# Whose sum is Equal to a Given Number
# https://javarevisited.blogspot.com/2014/08/how-to-find-all-pairs-in-array-of-integers-whose-sum-equal-given-number-java.html?source=post_page---------------------------


class FindAllPairsInArray:

    def sum_using_set(self, arr, k):
        s = set()
        n = len(arr)
        result = []

        if n < 2:
            return result

        for i in range(n):
            pair = k-arr[i]

            if pair not in s:
                s.add(arr[i])
            else:
                result.append((arr[i], pair))

        return result

    def find_pairs_using_tw_pointers(self, arr, k):
        n = len(arr)
        result = []

        if n < 2:
            return result

        left = 0
        right = n

        arr = sorted(arr)

        while left < right:
            total = arr[left]+arr[right]
            if total == k:
                result.append((left, right))
            elif total < k:
                left += 1
            else:
                right -= 1

        return result
