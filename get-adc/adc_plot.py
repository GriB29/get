import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.grid(True, alpha=.3)
    plt.ylim(0, max_voltage)
    plt.xlabel("time, s")
    plt.ylabel("voltage, V")
    plt.show()
    plt.close()
