import matplotlib.pyplot as plt
import pandas as pd
du_lieu_1 = ['Los Angeles', 'San Diego', 'California City', 'San Jose', 'Bakersfield', 'Fresno', 'Sacramento', 'Lancaster','Palm Springs', 'Riverside']
du_lieu_2 = [1302, 964, 527, 466, 393, 296, 259, 245, 246, 210]
df = pd.DataFrame()
df['City'] = du_lieu_1
df['area_total_km2'] = du_lieu_2
df = df.sort_values(by='area_total_km2', ascending=True)
plt.barh(df['City'], df['area_total_km2'])
plt.title('10 thanh pho lon nhat California')
plt.xlabel('dien tich (km2)')
plt.ylabel('thanh pho')
plt.tight_layout()
plt.show()