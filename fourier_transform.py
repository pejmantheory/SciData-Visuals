import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
sampling_rate = 1000
t = np.linspace(0, 1, sampling_rate)
freq = 5
amplitude = np.sin(2 * np.pi * freq * t)

# Compute Fourier Transform
ft = np.fft.fft(amplitude)
frequencies = np.fft.fftfreq(len(ft))

# Plot the original signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, amplitude)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the Fourier Transform
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(ft))
plt.title('Fourier Transform')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.xlim(0, 10)  # Limiting x-axis to view the peak clearly

plt.tight_layout()
plt.show()
