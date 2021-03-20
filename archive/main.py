import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("vgsales.csv")
print(data.head(5))
print(data.tail(5))
print(data.shape)
print(data.columns)
print(data.dtypes)

data["Year"] = data["Year"].astype(str)

data.isnull().sum()
data_row = data.dropna(axis=0)
print(data_row.shape)
data_col = data.dropna(axis=1)
print(data_col.shape)

df = data[(data["Year"] >= "2000") & (data["Year"] <= "2015")]
print(df.head())
print(df.loc[1:20, "Name":"Publisher"])
df.isnull().sum()
print(df[df["Publisher"].isnull()])
df.isnull()

df["Year"] = df["Year"].astype(str)
df['Year'].str.extract(r'^(\d{4})', expand=False)
print(df.dtypes)
df.dropna()
print(df.head())

df_sales = df.sort_values("Global_Sales", ascending=False)
print(df_sales)

top_game = df_sales.head(7)
print(top_game)

# top selling games
fig: object
fig, ax = plt.subplots()
ax.bar(top_game["Name"], top_game["Global_Sales"], color="r")
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel("Global Sales (Millions)")
ax.set_xlabel("Games")
ax.set_title('Top Selling Games 2000 - 2015')
plt.xticks(rotation=45)
plt.show()

print(top_game.head())
tsg = ["Wii Sports", "Mario Kart Wii","Wii Sports Resort","New Super Mario Bros","Wii Play"]
for games in tsg:
    print(games)
    if games == "New Super Mario Bros":
        break

# total sales by platform
platform = df.groupby("Platform").sum().sort_values("Global_Sales", ascending=False).drop("Rank", axis="columns")
print(platform.head(4))
for platform, row in platform.iterrows():
    print(platform)
    print(row)
# top 4 selling selling consoles across all regions
PS2 = (572.92, 332.63, 137.54, 190.47)
X360 = (586.86, 272.84, 12.30, 83.46)
PS3 = (383.74, 332.24, 74.41, 138.24)
Wii = (496.80, 263.48, 68.28, 79.08)
sales_region = ("North America", "Europe", "Japan", "Rest of the World")

fig, ax = plt.subplots()
ax.plot(sales_region, PS2, label="PS2", linestyle="-", marker=".")
ax.plot(sales_region, X360, label="X360", linestyle="--", marker="x")
ax.plot(sales_region, PS3, label="PS3", linestyle="-.", marker="v")
ax.plot(sales_region, Wii, label="Wii", linestyle=":", marker="s")
plt.xlabel("Sales Region")
plt.ylabel("Total Sales (Millions)")
plt.title('Top Selling Consoles')
ax.set(xlabel='Sales Region', ylabel='sales (millions)')
ax.legend()
plt.show()

df_yr = df.groupby("Year").sum()
print(df_yr)
#yea of best selling video games
best_yr = print(df_yr.loc["2008.0"])

# sales by year
df_yr_sales = {2000: 201.56, 2001: 331.47, 2002: 395.52, 2003: 357.52, 2004: 419.31, 2005: 459.94, 2006: 521.04,
               2007: 611.13, 2008: 678.90, 2009: 667.30, 2010: 600, 2011: 515.99, 2012: 363.54, 2013: 368.11,
               2014: 337.05}
keys = list(df_yr_sales.keys())
values = list(df_yr_sales.values())
plt.xlabel("Year")
plt.ylabel("Total sales (Millions)")
plt.title("Total Video Game Sales per Year")
plt.bar(keys, values)
plt.show()
