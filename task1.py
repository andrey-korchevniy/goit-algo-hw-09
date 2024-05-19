import timeit
import timeit
import matplotlib.pyplot as plt
import pandas as pd


coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(sum):
    rest = {}
    for coin in coins:
        if sum >= coin:
            count, sum = divmod(sum, coin)
            rest[coin] = count

    return rest

 # Динамічне програмування
def find_min_coins(sum):
   # Масив для зберігання мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (sum + 1)
    # Словник для зберігання монет, що використовуються для кожної суми
    coin_used = [None] * (sum + 1)

    # Обробляємо випадок, коли сума дорівнює 0
    min_coins[0] = 0

    # Рахуємо мінімальну кількість монет для кожної суми
    for current_sum in range(1, sum + 1):
        for coin in coins:
            if coin <= current_sum and min_coins[current_sum - coin] + 1 < min_coins[current_sum]:
                min_coins[current_sum] = min_coins[current_sum - coin] + 1
                coin_used[current_sum] = coin

    # Визначаємо, які монети використовувалися
    result = {}
    current_sum = sum
    while current_sum > 0:
        coin = coin_used[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin

    return result

# Тестування
# Набір сум для тестирования
test_sums = [18, 131, 1894, 25987, 364852]
greedy_times = []
dp_times = []

# Тестирование часу виконання алгоритмів
print('\nРезультати жадібного алгоритму')
for test_sum in test_sums:
    # Жадібний алгоритм
    print(find_coins_greedy(test_sum))
    greedy_time = timeit.timeit(f'find_coins_greedy({test_sum})', globals=globals(), number=10)
    greedy_times.append(greedy_time)

print("\nРезультати динамічного програмування")
for test_sum in test_sums:
    # Динамічне програмування
    dp_time = timeit.timeit(f'find_min_coins({test_sum})', globals=globals(), number=10)
    dp_times.append(dp_time)

data = {
    'Сума': test_sums,
    'Жадібний алгоритм (сек)': greedy_times,
    'Динамічне програмування (сек)': dp_times
}
results_df = pd.DataFrame(data)

# Таблиця
print(results_df)

# Графік
plt.figure(figsize=(10, 5))
plt.plot(test_sums, greedy_times, label='Жадібний алгоритм')
plt.plot(test_sums, dp_times, label='Динамічне програмування')
plt.xlabel('Сума')
plt.ylabel('Час виконання (секунди)')
plt.legend()
plt.title('Порівняння часу виконання алгоритмів')
plt.grid(True)
plt.show()