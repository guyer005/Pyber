# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 18:35:06 2019

@author: guye0
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

City = pd.read_csv('city_data.csv')
Ride = pd.read_csv('ride_data.csv')

Merge_df = pd.merge(City,Ride,on="city")
#getting the relevant statistics
Fares_df = Merge_df.groupby(["city","type","driver_count"],as_index=False)[["fare"]].mean()
Rides_df = Merge_df.groupby(["city","type","driver_count"],as_index=False)[["fare"]].count()

Rides = Rides_df.rename(columns={"fare":"rides"})

Fares_df["rides"] = Rides["rides"]

colors = {'Urban':'Coral', 'Suburban':'SkyBlue', 'Rural':'Gold'}

FSplit = dict(tuple(Fares_df.groupby("type")))


fig, ax = plt.subplots()
ax.scatter(FSplit["Urban"]["rides"], FSplit["Urban"]["fare"], FSplit["Urban"]["driver_count"]*4, edgecolors='black', c='Coral', label = 'Urban',alpha=0.8)
ax.scatter(FSplit["Suburban"]["rides"], FSplit["Suburban"]["fare"], FSplit["Suburban"]["driver_count"]*4, edgecolors='black', c='SkyBlue', label = 'Suburban',alpha=0.8)
ax.scatter(FSplit["Rural"]["rides"], FSplit["Rural"]["fare"], FSplit["Rural"]["driver_count"]*4, edgecolors='black', c='Gold', label = 'Rural',alpha=0.8)

#I spent an hour experimenting with linewidth but nothing changes the scale of the legend circles.  
ax.legend(title="City Types")
plt.title('Pyber Ride Sharing Data (2016)')
plt.xlabel('Total Number of Rides (Per City)')
plt.ylabel('Average Fare ($)')
plt.text(42,30,"Note:")
plt.text(42,28,"Circle size relates to driver count per city")

#Supporting the conclusion section
print(f"The correlation between Average Fare and Number of Rides was {round(np.corrcoef(Fares_df['fare'],Fares_df['rides'])[0,1],3)}")

plt.show()
#Pie Graphs
Pie1 = Merge_df.groupby(["type"],as_index=False)[["fare"]].sum()
Pie2 = Fares_df.groupby(["type"],as_index=False)[["rides"]].sum()
Pie3 = Fares_df.groupby(["type"],as_index=False)[["driver_count"]].sum()

explode = (0.1,0.1,0) 

#Fares by city type
plt.pie(Pie1["fare"], explode=explode, labels=Pie1["type"], colors=["Gold","SkyBlue","Coral"],
        autopct="%1.1f%%", shadow=True, startangle=160)

plt.title('% of Total Fares by City Type')
# Create axes which are equal so we have a perfect circle
plt.axis("equal")
plt.show()


plt.pie(Pie2["rides"], explode=explode, labels=Pie1["type"], colors=["Gold","SkyBlue","Coral"],
        autopct="%1.1f%%", shadow=True, startangle=160)

plt.title('% of Total Rides by City Type')
# Create axes which are equal so we have a perfect circle
plt.axis("equal")
plt.show()


plt.pie(Pie3["driver_count"], explode=explode, labels=Pie1["type"], colors=["Gold","SkyBlue","Coral"],
        autopct="%1.1f%%", shadow=True, startangle=160)

plt.title('% of Total Drivers by City Type')
# Create axes which are equal so we have a perfect circle
plt.axis("equal")
plt.show()





"""
Merge_df = pd.merge(Clin,MDD,on="Mouse ID")
Treat_df = pd.DataFrame(dict(x=Merge_df["Timepoint"], y=Merge_df["Tumor Volume (mm3)"], label=Merge_df["Drug"]))

Treat = Treat_df.groupby(["x","label"])[['y']].mean()
print(Treat)

#d2 = Treat.groupby(level='label').pct_change()
#print(d2)

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in Treat:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=2, label=name)
ax.legend()

plt.show()


Treat.get_groups("x")
#from stats import mean, median, mode, multi_mode

prices = [27,35,42,30,29]

#from spread 
import pandas as pd
import matplotlib.pyplot as plt
#from stats import median
import numpy as np

sumx = 0
arr = np.array([2.3, 10.2,11.2, 12.3, 14.5, 14.6, 15.0, 15.1, 19.0, 24.0])

for i in range(len(arr)):
    sumx += arr[i]
meanx = sumx/len(arr)
if len(arr) % 2 == 0:
        medianx = (arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2
Y = np.percentile(arr,[25,75])
IQR = Y[1]-Y[0]
arr_df = pd.DataFrame(arr)
arr_df.rename(columns={"0":"Spurious Data"})
arr_df.plot.box(grid="True",showmeans="True")

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

div = 20
housing_data = pd.read_csv("housing_data.csv", header=None)
housing_data = housing_data.sample(frac=1).reset_index(drop=True)
#grabbing whole dataset and randomizing the order

lim = len(housing_data) // div #divide but give me an integer
samples = [housing_data.iloc[(i * div):(i * div + div), 13]
           for i in range(0, lim)]

meanxy = [np.mean(samples[y]) for y in range(len(samples))]
stdxy = [np.std(samples[y]) for y in range(len(samples))]

xplace = [x for x in range(len(samples[0]))]

plt.errorbar(xplace,meanxy,xerr=xplace,yerr=stdxy)

"""