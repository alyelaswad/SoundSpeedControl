import numpy as np
import math
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def ReduceSpeed(inFilename, reductionFactor, methodNum, outFilename):

    sampleRate, data = wavfile.read(inFilename);
    output_length = int(len(data) / reductionFactor)
    data = data.astype(np.float32)

    if methodNum == 1:
        # Method 1: Nearest Neighbor
        output_data = np.zeros(output_length, dtype=data.dtype)
        for n in range(output_length):
            original_index = round(n * reductionFactor)
            if original_index < len(data):
                output_data[n] = data[original_index]
        wavfile.write(outFilename, sampleRate, output_data.astype(np.int16))
    elif methodNum == 2:
        output_data = np.zeros(output_length, dtype=data.dtype)
        for n in range(output_length):

            newVal = n * reductionFactor
            Xlower = min(math.floor(newVal),len(data)-1)
            Xupper = min(math.ceil(newVal),len(data)-1)
            if Xlower < len(data) and Xupper < len(data):
                Ylower = data[Xlower]
                Yupper = data[Xupper]

                output_data[n] = Ylower + (Yupper-Ylower) * (newVal - Xlower)
        wavfile.write(outFilename, sampleRate, output_data.astype(np.int16))
    elif methodNum == 3:
        output_data = np.zeros(output_length, dtype=data.dtype)
        for n in range(output_length):

            newVal = n * reductionFactor


            Z1_index = min(math.floor(newVal), len(data) - 1)
            Z2_index = min(math.ceil(newVal), len(data) - 1)

            Z1 = data[Z1_index]
            Z2 = data[Z2_index]

            m = newVal - Z1_index  # This gives us the fractional part of newVal
            a = (Z2 - Z1) / 2  # Here 'a' can be derived based on the difference between the two samples
            b = Z1  # This is the value at Z1_index

            # Calculate the output value using the interpolation equation
            output_data[n] = a * (m ** 2) + b
        wavfile.write(outFilename, sampleRate, output_data.astype(np.int16))
    else:
        print("Invalid method number.")

    return output_data

nearestNeighbour=ReduceSpeed("Sports.wav", 0.85, 1, "Sports_1_85.wav")
LinearInterpo=ReduceSpeed("Sports.wav", 0.85, 2, "Sports_2_85.wav")
NonLinearInterpo=ReduceSpeed("Sports.wav", 0.85, 3, "Sports_3_85.wav")

plt.plot(nearestNeighbour[: 500], label= 'Nearest Neighbour',color = 'green', linewidth=2.5, alpha=0.7 )
plt.plot(LinearInterpo[: 500], label= 'Linear Interpolation',color = 'blue', linewidth=2.5, alpha=0.7 )
plt.plot(NonLinearInterpo[: 500], label= 'Non - Linear Interpolation',color = 'red', linewidth=2.5, alpha=0.7)
plt.legend()
plt.show()