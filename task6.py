


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_calories += info["calories"]
            total_cost += info["cost"]

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    # Список страв
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]
    n = len(items)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(1, budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]

    selected_items = []
    total_calories = dp[n][budget]
    total_cost = 0
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(item_names[i - 1])
            total_cost += costs[i - 1]
            b -= costs[i - 1]

    selected_items.reverse()  
    return selected_items, total_calories, total_cost

budget = 100

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])
print("Сумарна вартість:", greedy_result[2])

dp_result = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_result[0])
print("Сумарна калорійність:", dp_result[1])
print("Сумарна вартість:", dp_result[2])
