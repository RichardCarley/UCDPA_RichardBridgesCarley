import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("vgsales.csv")
print(data.head())
print(data.shape)
print(data.columns)
print(data.info)
vg_sort = data.sort_values(["Platform", "Year"])


data_year = data.sort_values("Year")
print(data_year.head())

print(data.index)





#top 4 selling selling consoles across all regions
PS2 = [572.92,332.63,137.54,190.47]
X360 = [586.86,272.84,12.30,83.46]
PS3 = [383.74,332.24,74.41,138.24]
Wii = [496.80,263.48,68.28,79.08]
sales_region = ["North America", "Europe", "Japan", "Rest of the World"]
fig, ax = plt.subplots()
ax.plot(sales_region, PS2, label="PS2", linestyle  ="-", marker =".")
ax.plot(sales_region, X360, label="X360", linestyle ="--", marker ="x")
ax.plot(sales_region, PS3, label="PS3", linestyle ="-.", marker ="v")
ax.plot(sales_region, Wii, label="Wii", linestyle =":", marker  ="s")
#plt.xlabel("Sales Region")
#plt.ylabel("Total Sales (Millions)")
fig.suptitle('Top Selling Consoles')
ax.set(xlabel='Sales Region', ylabel='sales (millions)')
ax.legend()
plt.show()
