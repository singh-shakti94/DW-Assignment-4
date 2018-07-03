from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import read_csv
import pandas as pd

# Data downloaded from 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
# Setting up custom style
style.use(['seaborn-poster'])

DataFrame = read_csv('Building_Permits.csv')
df = DataFrame.groupby(by=["X", "Y"], as_index=False)["PERMIT_NUMBER"].agg({'n_permits': pd.Series.nunique})

lngs = df['X'].astype('float')
lats = df['Y'].astype('float')
mags = df['n_permits'].astype('float').apply(lambda x: x*0.1)


plt.figure(figsize=(14, 8))
earth = Basemap()
# 105.3,-13.9,151.6,22.1 Phillipines
# earth = Basemap(llcrnrlon=105.3,llcrnrlat=-13.9,urcrnrlon=151.6,urcrnrlat=22.1)
earth.drawcoastlines(color='0.50', linewidth=0.25)
#earth.fillcontinents(color='0.95')
#earth.bluemarble(alpha=0.95)
earth.shadedrelief()
plt.scatter(lngs, lats, mags,
            c='blue',alpha=0.5, zorder=10)
#
# plt.scatter(lngs, lats,
#             c='blue',alpha=0.5, zorder=10)
plt.xlabel("Buildings")


# Workaround for blank image saving
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('n_permits.png', dpi=350)

