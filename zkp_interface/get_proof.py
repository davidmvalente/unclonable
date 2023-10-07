
from scripts.utils import generate_circuit, get_ppm_parameters
import argparse
# python3 src/get_proof.py to generate the input JSON file and circuit file
if __name__ == '__main__':
    #parse arguments 
    parser = argparse.ArgumentParser(description='Generate input JSON file and circuit file')
    parser.add_argument('png', type=str, help='path to the photo')
    parser.add_argument('output', type=str, help='path to the output JSON file')
    args = parser.parse_args()
    json, width, height, length, header_len = get_ppm_parameters(args.png, args.output)
    
    circuit_path = generate_circuit({'Nt': width, 'Mt': height, 'SIZEt': length,'HEADERt': header_len},
                                     './zkp_interface/circuits/base/pngToRgb.circom')
    
