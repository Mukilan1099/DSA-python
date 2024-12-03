
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.


def minEatingSpeed(piles, h):

    low=1
    high=max(piles)
    result = high  # Start with the largest possible speed as the default answer=>more than that it is not needed.

    while low <= high:
        mid = (low + high) // 2
        total_time = 0  # Total time required at speed `mid`

        # Calculate the time required at this (mid)speed
        for pile in piles:
            total_time += (pile + mid - 1) // mid

        # If Koko can eat all bananas within h hours
        if total_time <= h:
            result = mid  # Update the result
            high = mid - 1  # Try smaller speeds   =>move pointer
        else:
            low = mid + 1  # Increase speed to reduce time

    return result

# Example Usage
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
