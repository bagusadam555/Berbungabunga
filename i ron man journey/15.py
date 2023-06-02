import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Membuat variabel input dan domainnya
curah_hujan = np.arange(0, 151, 1)

# Membuat fungsi keanggotaan untuk masing-masing fuzzy set
cs = fuzz.trapmf(curah_hujan, [0, 0, 10, 40])
hl = fuzz.trapmf(curah_hujan, [30, 45, 100, 110])
hb = fuzz.trapmf(curah_hujan, [100, 125, 150, 150])

# Visualisasi fungsi keanggotaan
plt.figure()
plt.plot(curah_hujan, cs, 'b', linewidth=1.5, label='CS')
plt.plot(curah_hujan, hl, 'g', linewidth=1.5, label='HL')
plt.plot(curah_hujan, hb, 'r', linewidth=1.5, label='HB')
plt.title('Fungsi Keanggotaan Curah Hujan')
plt.ylabel('Derajat Keanggotaan')
plt.xlabel('Curah Hujan (mm)')
plt.legend()

# Menampilkan plot
plt.show()
