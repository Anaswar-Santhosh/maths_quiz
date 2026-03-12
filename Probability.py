import random
even = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
print(f"A bag contains {random.choice(even)} marbles:")
red = round(20 / 100 * even)
blue = round(30 / 100 * even)
green = round(38 / 100 * even)
yellow = round(12 / 100 * even)
print(f"{red} red")
print(f"{blue} blue") 
print(f"{green} green")
print(f"{yellow} yellow")
