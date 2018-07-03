import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

import plotly.plotly as py
import plotly.graph_objs as go
py.tools.set_credentials_file(username='singh_shakti', api_key='UUpfVEFAoa8KqL0zUtca')



raw_data = pd.read_csv("clean_data.csv")
df = raw_data.groupby(["PERMIT_TYPE"], as_index=False).count()
bins = np.arange(7) - 0.5
plt.hist(raw_data.PERMIT_TYPE, bins=bins, rwidth=0.5)
plt.yticks(np.arange(0,70000, step=5000))
plt.show()


# plot of 3
raw_data["DATE_OF_APPLICATION"] = raw_data["DATE_OF_APPLICATION"].astype(str).apply(lambda x: x.replace("T", " "))
raw_data["DATE_OF_PERMIT_ISSUANCE"] = raw_data["DATE_OF_PERMIT_ISSUANCE"].astype(str).apply(lambda x: x.replace("T", " "))

raw_data["DATE_OF_APPLICATION"] = pd.to_datetime(raw_data["DATE_OF_APPLICATION"], format="%Y-%m-%d %H:%M:%S")
raw_data["DATE_OF_PERMIT_ISSUANCE"] = pd.to_datetime(raw_data["DATE_OF_PERMIT_ISSUANCE"], format="%Y-%m-%d %H:%M:%S")

raw_data["TIME_DELAY_PERMIT"] = raw_data["DATE_OF_PERMIT_ISSUANCE"] - raw_data["DATE_OF_APPLICATION"]
a = raw_data["TIME_DELAY_PERMIT"].apply(lambda x: (x.total_seconds())/(24*3600))

plt.scatter(a, raw_data["BP_ID"], s=1)
plt.show()


# plotly plot
trace = go.Scatter(
    x = a,
    y = raw_data["BP_ID"],
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')
plt.show()
# plot_url = py.plot(data, filename='basic-scatter')

# plot 4
raw_data.isnull().sum()
data = pd.DataFrame(raw_data["ALTERNATE_BUILDING_TYPE"])
data["ESTIMATED_VALUE"] = raw_data["ESTIMATED_VALUE_OF_PROJECT"]
data = data.dropna()
data_splits = np.array_split(data, 2)
print(data_splits[0])
# plt.scatter(x=data.ALTERNATE_BUILDING_TYPE, y=data.ESTIMATED_VALUE, c=data.ALTERNATE_BUILDING_TYPE)
# sns.stripplot("ALTERNATE_BUILDING_TYPE", "ESTIMATED_VALUE", data=data)

plt.figure()
ax = sns.stripplot("ALTERNATE_BUILDING_TYPE", "ESTIMATED_VALUE", data=data_splits[0])
ax.tick_params(labelsize=5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
plt.tight_layout()
plt.show()


plt.figure()
ax = sns.stripplot("ALTERNATE_BUILDING_TYPE", "ESTIMATED_VALUE", data=data_splits[1])
ax.tick_params(labelsize=5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
plt.tight_layout()
plt.show()


# plot 5
plt.figure(figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
ax = sns.swarmplot("ALTERNATE_BUILDING_TYPE", "ESTIMATED_VALUE_OF_PROJECT",
                   data=raw_data, hue="COMMUNITY", size=5, alpha=0.5)
ax.tick_params(labelsize=5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
plt.tight_layout()
plt.show()

# --------------
fig, ax = plt.subplots()
for c, df in raw_data.groupby('COMMUNITY'):
    ax.scatter(df['ALTERNATE_BUILDING_TYPE'], df['ESTIMATED_VALUE_OF_PROJECT'], label=c)
ax.legend()
ax.set_title('Engine Displacement in Liters vs Highway MPG')
ax.set_xlabel('Engine Displacement in Liters')
ax.set_ylabel('Highway MPG')


# ---------------------
# 3D plot
fig = plt.figure()
ax = Axes3D(fig)
X = raw_data["ALTERNATE_BUILDING_TYPE"]
Y = raw_data["COMMUNITY"]
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
Z = raw_data["ESTIMATED_VALUE_OF_PROJECT"]

ax.scatter(X, Y, cmap=plt.cm.hot)
# ax.contour(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
# ax.set_zlim(-2,2)
plt.show()


# --------pie------------
# Data to plot
labels =
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

# ------------------
df = raw_data[["COMMUNITY", "ALTERNATE_BUILDING_TYPE", "ESTIMATED_VALUE_OF_PROJECT"]]
df = df.dropna()
a = df.groupby(["COMMUNITY","ALTERNATE_BUILDING_TYPE"]).count()
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap()