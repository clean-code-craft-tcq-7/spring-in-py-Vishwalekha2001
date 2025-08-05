


import math

def calculateStats(numbers):
    if not numbers:
        return {"avg": math.nan, "max": math.nan, "min": math.nan}
    
    avg = sum(numbers) / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    
    return {"avg": avg, "max": max_value, "min": min_value}
