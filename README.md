# SINR_optimization

### What is SINR?
SINR (Signal to Interference & Noise Ratio) measures how strong a desired signal is compared to unwanted interference and noise. It's the ratio of the signal power to the combined interference power and background noise power.
```
SINR = signal power / (noise + interference power)
```

<img src="/diagram.png">

### About the code
SINR_optimization optimizes the transmission of two signals in a wireless network by adjusting power levels to maximize signal quality. It considers factors like transmitter-receiver distances (d1, d2, d3, d4) and signal strength. The program runs various scenarios with different power levels to calculate the SINR sum for each case.

<p float="center">
  <img src = "/demo.png">
</p>


The goal is to find optimal power levels (p1 and p2) that maximize SINR and ensure clear signal transmission by iterating through random settings and using minimization techniques.
