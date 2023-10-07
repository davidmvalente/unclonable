
from scripts.utils import generate_circuit, get_ppm_parameters

# python3 src/get_proof.py to generate the input JSON file and circuit file
if __name__ == '__main__':
    photo = './zkp_interface/scripts/sakura.png'
    output = 'sakura.json'

    

    json, width, height, length, header_len = get_ppm_parameters(photo, output)
    
    circuit_path = generate_circuit({'Nt': width, 'Mt': height, 'SIZEt': length,'HEADERt': header_len},
                                     './zkp_interface/circuits/base/pngToRgb.circom')
    
