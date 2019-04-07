#参考記事
#https://myenigma.hatenablog.com/entry/2015/10/09/223629

import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

uniform_data = np.random.rand(24, 100)
ax = sns.heatmap(uniform_data)
plt.axis("off")
plt.show()