import json
import os 
from PIL import Image

def get_3d_byte_array_from_png(image_path):
    """
    Returns a 3D array of bytes from a PNG image
    :param image_path: The path to the PNG image
    :return: A 3D array of bytes
    """
    with Image.open(image_path) as img:
        # Convert the image to RGB mode (if it's not already)
        img = img.convert('RGB')
        
        # Get the width and height of the image
        width, height = img.size

        # Get the pixel data as a flat list
        pixel_data = list(img.getdata())

        # Reshape the list into a 3D array (height x width x 3 for RGB)
        byte_array = [pixel_data[i:i+width] for i in range(0, len(pixel_data), width)]

        string_array = [[str(val) for val in inner_tuple] for outer_tuple in byte_array for inner_tuple in outer_tuple]
        string_array = [string_array[i:i+width] for i in range(0, len(string_array), width)]
        return string_array, width, height
    
def read_png_as_bytes(image_path):
    """
    Returns a byte stream from a PNG image
    :param image_path: The path to the PNG image
    :return: A byte stream
    """
    with open(image_path, 'rb') as file:
        byte_stream = file.read()
    return byte_stream

def generate_input(image_path, output_path):
    """
    Given a PNG image, generates a JSON file containing the image's byte stream and 3D array of bytes
    :param image_path: The path to the PNG image
    :param output_path: The path to the output JSON file
    :return: The width, height of the image and length of the byte stream derived from the image
    """
    byte_stream = list(read_png_as_bytes(image_path))
    byte_stream = [str(val) for val in byte_stream]
    byte_array, width, height = get_3d_byte_array_from_png(image_path)

    # Convert single quotes to double quotes
    json_string = json.dumps({'bitmap_array': byte_array}).replace("'", '"')
    json_string2 = json.dumps({'png_array': byte_stream})
    dict1 = json.loads(json_string)
    dict2 = json.loads(json_string2)

    # Merge the dictionaries
    data = {**dict1, **dict2}

    # Convert the merged dictionary back to a JSON string
    final_json_string = json.dumps(data)
    
    # Write to a JSON file
    with open(output_path, 'w') as json_file:
        json_file.write(final_json_string)

    return width, height, len(byte_stream)

def generate_circuit(info,circuit_template,id = None):
    """
    Given a circuit template, generates a circuit file with the given info
    :param info: A dictionary containing the information to be replaced in the circuit template
    :param circuit_template: The path to the circuit template
    :param id: The id of the circuit if there are multiple circuits generated from the same template
    :return: The path to the generated circuit file
    """

    out_circuit = circuit_template.split('/')[-1].split('.')[0]
    os.makedirs('./zkp_interface/circuits/instances',exist_ok=True)

    with open(circuit_template, 'r') as infile:
        circuit = infile.read()
        for k,v in info.items():
            circuit = circuit.replace(k, str(v))
        circuit = circuit.replace('//MAIN', '')

    id = f'_{id}' if id is not None else ''
    out_path = f'./zkp_interface/circuits/instances/{out_circuit}{id}.circom'
    with open(out_path, 'w') as outfile:
        outfile.write(circuit)
    return out_path

if __name__ == '__main__':
    raise Exception('This file is not meant to be run directly')