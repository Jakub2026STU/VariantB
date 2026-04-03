
import numpy as np

def get_constellation(modulation):
    """
    Returns the constellation points for the specified modulation scheme.

    Parameters:
    modulation (str): The modulation scheme ('BPSK', 'QPSK').

    Returns:
    numpy.ndarray: Array of constellation points.
    """
    modulation = modulation.upper()

    constellations = {
    'BPSK': lambda: np.array([-1, 1]),
    'QPSK': lambda: np.array([1+1j, 1-1j, -1+1j, -1-1j])
    }


    if modulation in constellations:
        return constellations[modulation]()
    else:
        raise ValueError("Unsupported modulation type. Use 'BPSK', 'QPSK'.")

def get_symbol_map(modulation):
    """
    Returns the symbol map for the specified modulation scheme.

    Parameters:
    modulation (str): The modulation scheme ('BPSK', 'QPSK').

    Returns:
    list: A list of symbol indices for the specified modulation scheme.
    """
    modulation = modulation.upper()
    symbol_counts = {
        'BPSK': 2,
        'QPSK': 4,
    }

    if modulation in symbol_counts:
        return [i for i in range(symbol_counts[modulation])]
    else:
        raise ValueError("Unsupported modulation type. Use 'BPSK', 'QPSK'.")


import math

def calculate_noise(modulation: str, ebno: float, k: int): 
    if modulation == 'BPSK':
        snr_linear = 10 ** (ebno / 10) + 10*math.log(k/7,10)
        noise_variance = 1 / snr_linear 
        noise = math.sqrt(noise_variance)
        return noise

    elif modulation == 'QPSK':
        snr_db = ebno + 10*math.log(2,10) + 10*math.log(k/7,10)
        snr_linear = 10 ** (snr_db / 10)
        noise_variance = 1 / snr_linear 
        noise = math.sqrt(noise_variance)
        return noise