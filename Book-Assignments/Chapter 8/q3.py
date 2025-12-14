import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='-', color='b') 


plt.title("Line Graph of X vs Y")
plt.xlabel("X Values")
plt.ylabel("Y Values (Squared)")


plt.show()