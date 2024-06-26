import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define sensor data file (replace with your actual file path)
df = pd.read_csv('./csv/A1/data_highres.csv')
df_br = pd.read_csv('./csv/A1/data_raven_highres.csv')

sensitivity = 0.031  # mG/LSB (converted to g)

total_time = 50
dt = 0.004  # Time step (seconds)
dt_br = 0.002  # Time step (seconds)

t = [dt*x for x in range(int(total_time / dt))]
t_br = df_br["Flight_Time_(s)"][0:int(total_time / dt_br)]

# Extract and scale sensor data
accel = np.array([
    [d['accel_x'] * sensitivity,
     d['accel_y'] * sensitivity,
     d['accel_z'] * sensitivity]
    for (_, d) in df.iterrows()
])

accel_br = np.array([
    [d['Accel_X'],
     -d['Accel_Z'],
     d['Accel_Y']]
    for (_, d) in df_br.iterrows()
])

plt.plot(t, accel[0:int(total_time / dt), 0])
plt.plot(t_br, accel_br[0:int(total_time / dt_br), 0])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.legend(["A1 Avionics", "Blue Raven"])
plt.savefig("./plot/accel/Accel_X.png")

plt.figure()
plt.plot(t, accel[0:int(total_time / dt), 1])
plt.plot(t_br, accel_br[0:int(total_time / dt_br), 1])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.legend(["A1 Avionics", "Blue Raven"])
plt.savefig("./plot/accel/Accel_Y.png")

plt.figure()
plt.plot(t, accel[0:int(total_time / dt), 2])
plt.plot(t_br, accel_br[0:int(total_time / dt_br), 2])
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.legend(["A1 Avionics", "Blue Raven"])
plt.savefig("./plot/accel/Accel_Z.png")
print("Figures saved to /plot/accel/")
