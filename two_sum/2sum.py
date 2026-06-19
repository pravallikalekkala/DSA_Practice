import numbers

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    """Return indices of two numbers that add up to target.

    Returns None when no valid pair exists.
    """
    if not isinstance(nums, (list, tuple)):
        raise TypeError("nums must be a list or tuple")
    if not isinstance(target, numbers.Number):
        raise TypeError("target must be a number")
    if len(nums) < 2:
        return None

    seen = {}
    for i, value in enumerate(nums):
        if not isinstance(value, numbers.Number):
            raise TypeError("nums must contain only numbers")
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i

    return None


def main():
    result = two_sum(nums, target)
    if result is None:
        print(f"No two-sum pair found for nums={nums} and target={target}")
    else:
        print(result)


if __name__ == "__main__":
    main()                                                