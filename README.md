

### What is SINR?
SINR (Signal to Interference & Noise Ratio) measures how strong a desired signal is compared to unwanted interference and noise. It's the ratio of the signal power to the combined interference power and background noise power.
```
SINR = signal power / (noise + interference power)
```

<img src="/diagram.png">

### About the code
SINR_optimization aims to optimize the transmission of two signals in a wireless network. In wireless communication, signals can get disrupted by interference and background noise. This program focuses on maximizing the quality of these signals by adjusting the power levels allocated to each signal. It does this through an optimization process where it considers various factors like the distance between transmitters and receivers (d1, d2, d3, d4), and the signal strength of each transmission point. By running through multiple scenarios with different power levels for the signals, it calculates the SINR sum for each case.

<p float="center">
  <img src = "/demo.png">
</p>


The goal is to find the power allocation (p1 and p2) that maximizes the SINR sum, ensuring that the desired signals come through strongly relative to interference and background noise. The code iterates through random initial power settings multiple times, using a mathematical technique called minimization to find the best power levels that result in the clearest transmission for both signals.
