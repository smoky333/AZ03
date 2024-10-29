import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome()


driver.get("https://www.vetementpro.com/55-vestes-cuisine")
time.sleep(5)


price_elements = driver.find_elements(By.CLASS_NAME, "price")
price_list = []


for element in price_elements:
    price_text = element.text.replace("€", "").replace(",", ".").strip()  # Убираем знак €
    if price_text.replace(".", "").isdigit():  # Проверка, что это число
        price_list.append(float(price_text))



driver.close()


with open("price.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Price"])
    for price in price_list:
        writer.writerow([price])


df = pd.read_csv("price.csv", encoding="utf-8-sig")
print(df)


average_price = df["Price"].mean()
print("Средняя цена:", average_price)


plt.hist(df["Price"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Цена (€)")
plt.ylabel("Частота")
plt.title("Гистограмма цен на куртки")
plt.show()
