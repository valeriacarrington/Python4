import matplotlib.pyplot as plt

# Дані для візуалізації (приклад)
categories = ['Sports', 'Diet', 'Sleep', 'Leisure', 'Skincare']
values = [25, 40, 35, 20, 30]

# Створення гістограми
plt.bar(categories, values, color=['darkturquoise', 'blueviolet', 'fuchsia', 'cyan', 'deeppink'])

# Додавання заголовка та підписів до вісей
plt.title('Bar chart for your healthcare')
plt.xlabel('Categories')
plt.ylabel('Values')

# Відображення гістограми
plt.show() 
