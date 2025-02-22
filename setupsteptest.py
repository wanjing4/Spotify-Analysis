import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample data
data = {
    "A": np.random.randn(100),
    "B": np.random.randn(100),
}
df = pd.DataFrame(data)

# Plot the data
sns.histplot(df["A"], kde=True)
plt.show()
