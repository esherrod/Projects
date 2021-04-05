import random

def estimate_pi(n):
    points_in_circle = 0
    points_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            points_in_circle +=1
        points_total +=1
    
    return 4 * points_in_circle/points_total

print(estimate_pi(2000000))
