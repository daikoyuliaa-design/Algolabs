def find_longest_peak_sequence(arr):
    n = len(arr)
    max_length = 0

    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            length = 1
            left = i - 1

            while left >= 0 and arr[left] < arr[left + 1]:
                length += 1
                left -= 1

            right = i + 1
            while right < n and arr[right] < arr[right - 1]:
                length += 1
                right += 1

            max_length = max(max_length, length)

    return max_length
