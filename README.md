# SINR_optimization

### What is SINR?
SINR (Signal to Interference and Noise Ratio) measures the strength of a desired signal relative to interference and noise. It is the ratio of signal power to the sum of interference power and background noise power.
```
SINR = signal power / (noise + interference power)
```

<img src="/diagram.png">

### About the code
SINR_optimization adjusts power levels to maximize signal quality for two signals in a wireless network. It considers transmitter-receiver distances (d1, d2, d3, d4) and signal strength, running various scenarios to calculate the SINR sum.

<p float="center">
  <img src = "/demo.png">
</p>


The goal is to find optimal power levels (p1 and p2) that maximize SINR and ensure clear transmission, using minimization techniques and random settings.
