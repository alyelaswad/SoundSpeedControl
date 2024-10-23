# Audio Playback Speed Controller

## Overview

The Audio Playback Speed Controller is a Python program that allows users to adjust the playback speed of audio files using three different interpolation methods: Nearest Neighbor, Linear Interpolation, and Non-Linear Interpolation. This tool is designed to provide flexibility for audio manipulation, making it useful for musicians, language learners, and audio enthusiasts who wish to slow down or speed up audio playback while maintaining sound quality.

## Features

- **Adjust Playback Speed**: Change the playback speed of audio files using different methods.
- **Three Interpolation Methods**:
  1. Nearest Neighbor
  2. Linear Interpolation
  3. Non-Linear Interpolation
- **Visual Comparison**: Plot the output of each method for comparison.

## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install numpy scipy matplotlib
```

## Usage

To use the `ReduceSpeed` function, follow these steps:

1. Prepare your audio file (WAV format).
2. Call the `ReduceSpeed` function with the desired parameters.

### Function Definition

```python
def ReduceSpeed(inFilename, reductionFactor, methodNum, outFilename):
```

- `inFilename`: The input audio file path (e.g., "Sports.wav").
- `reductionFactor`: The factor by which to reduce the playback speed (e.g., 0.85).
- `methodNum`: The interpolation method to use (1, 2, or 3).
- `outFilename`: The output audio file path.

### Example

```python
nearestNeighbour = ReduceSpeed("Sports.wav", 0.85, 1, "Sports_1_85.wav")
LinearInterpo = ReduceSpeed("Sports.wav", 0.85, 2, "Sports_2_85.wav")
NonLinearInterpo = ReduceSpeed("Sports.wav", 0.85, 3, "Sports_3_85.wav")
```

### Visualization

The following code snippet will plot the results of the three methods for visual comparison:

```python
import matplotlib.pyplot as plt

plt.plot(nearestNeighbour[:500], label='Nearest Neighbor', color='green', linewidth=2.5, alpha=0.7)
plt.plot(LinearInterpo[:500], label='Linear Interpolation', color='blue', linewidth=2.5, alpha=0.7)
plt.plot(NonLinearInterpo[:500], label='Non-Linear Interpolation', color='red', linewidth=2.5, alpha=0.7)
plt.legend()
plt.show()
```

## Methods Description

1. **Nearest Neighbor**: This method selects the closest sample to the desired index, which is simple but may result in a blocky sound quality.
  
2. **Linear Interpolation**: This method calculates the value between two samples, creating a smoother sound than the Nearest Neighbor method.
  
3. **Non-Linear Interpolation**: This method utilizes a quadratic equation to provide a more refined output by considering the curvature between samples, resulting in improved sound quality.

## Conclusion

This project demonstrates the application of different interpolation methods for audio playback speed control. Feel free to explore the code, modify parameters, and experiment with your own audio files!
