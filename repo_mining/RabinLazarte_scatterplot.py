import numpy as np
from RabinLazarte_CollectFiles import dictfiles
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.cm as cm
    
all_dates = {
    datetime.fromisoformat(t["date"].replace("Z"," +00:00"))
    for touches in dictfiles.values()
    for t in touches
}

start_date = min(all_dates)

def week_number(dt):
    delta = dt - start_date
    return delta.days / 7

x = [] # weeks 
y = [] # file touches
authors = []

for filename, touches in dictfiles.items():
    for t in touches:
        x.append(week_number(all_dates))
        y.append(len(touches))
        authors.append(t["author"])
    
uniqueAuthors = list(set(authors))
cmap = cm.get_cmap("Lab20", len(uniqueAuthors))
authorColor = {a: cmap(i) for i, a in enumerate(uniqueAuthors)}
colors = [authorColor[a] for a in authors]

plt.figure(figsize=(12,6))
plt.scatter(x, y, c=colors, alpha = 0.7, edgecolors='w', s=60)

plt.xlabel("weeks")
plt.ylabel("file")
plt.title("File touches per week")

for i, a in enumerate(uniqueAuthors):
    plt.scatter([], [], color=cmap[i], label=a)
plt.tight_layout
plt.show()