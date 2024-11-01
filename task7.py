import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    
    die1 = np.random.randint(1, 7, num_rolls)  
    die2 = np.random.randint(1, 7, num_rolls) 
    sums = die1 + die2  
    return sums


def calculate_probabilities(sums):
    
    counts = np.bincount(sums)[2:13]
    probabilities = counts / len(sums)  
    return probabilities


num_rolls = 100000  
sums = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sums)


print("Ймовірності сум при киданні двох кубиків:")
for total, prob in zip(range(2, 13), probabilities):
    print(f"Сума {total}: {prob:.4f}")


plt.bar(range(2, 13), probabilities, color='skyblue')
plt.xticks(range(2, 13))
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.grid(axis='y')
plt.show()