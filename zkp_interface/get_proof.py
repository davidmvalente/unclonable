
from scripts.utils import generate_circuit, generate_input

# python3 src/get_proof.py to generate the input JSON file and circuit file
if __name__ == '__main__':
    photo = ''
    output = ''

    width, height, length = generate_input(photo, output)
    circuit_path = generate_circuit({'Nt': width, 'Mt': height, 'SIZEt': length},
                                     './zkp_interface/circuits/base/pngToRgb.circom',
                                     '')