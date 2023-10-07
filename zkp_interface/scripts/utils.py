
import json 
from PIL import Image
import numpy as np

#from image get the 3d vector of bits 
def get_3d_byte_array_from_png(image_path):
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
    with open(image_path, 'rb') as file:
        byte_stream = file.read()
    return byte_stream

def generate_input(image_path, output_path):
    l, length = read_png_as_bytes(image_path)
    byte_stream = list(l)
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

    return width, height, length


import random, os

def generate_input(output_path):
    """
    Generate a random input for a circuit of a given size
    :param output_path: path to the output file
    :param size: size of the input
    """
    shape = (3, 3, 3)

    # Generate random integers
    random_ints = [[[random.randint(0, 9) for _ in range(shape[2])] for _ in range(shape[1])] for _ in range(shape[0])]

    json_input = {'in':random_ints}
    os.makedirs('input',exist_ok=True)
    with open(output_path, 'w') as outfile:
        json.dump(json_input, outfile)
        

def read_chunk(file):
    length = int.from_bytes(file.read(4), byteorder='big')
    chunk_type = file.read(4).decode('ascii')
    data = file.read(length)
    crc = file.read(4)
    return length, chunk_type, data, crc


def convert_png_to_ppm(input_path, output_path):
    # Open the PNG image
    with Image.open(input_path) as img:
        # Convert to RGB mode (PPM format supports RGB)
        img = img.convert('RGB')        
        # Save as PPM format
        img.save(output_path, 'PPM')

def ppm_to_bytearray(file_path):
    with open(file_path, 'rb') as file:
        byte_stream = file.read()
    return [str(val) for val in byte_stream]

def get_3d_byte_array_from_ppm(image_path):
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
    with open(image_path, 'rb') as file:
        byte_stream = file.read()
    return byte_stream

def write_on_jsonfile(bitmap_array,image_array,output_path):
    # Convert single quotes to double quotes
    json_string = json.dumps({'bitmap_array': bitmap_array}).replace("'", '"')
    json_string2 = json.dumps({'png_array': image_array})
    dict1 = json.loads(json_string)
    dict2 = json.loads(json_string2)

    # Merge the dictionaries
    data = {**dict1, **dict2}

    # Convert the merged dictionary back to a JSON string
    final_json_string = json.dumps(data)
    
    # Write to a JSON file
    with open(output_path, 'w') as json_file:
        json_file.write(final_json_string)


def read_ppm_header(file_path):
    with open(file_path, 'rb') as ppm_file:
        # Read and decode the first line which contains the magic number
        magic_number = ppm_file.readline().decode().strip()

        # Read lines until the first non-comment line (which starts with "#")
        while True:
            line = ppm_file.readline().decode().strip()
            if not line.startswith("#"):
                break

        # Read image dimensions and maximum color value
        width, height = map(int, line.split())
        max_color_value = int(ppm_file.readline().decode().strip())

        # Calculate field sizes
        magic_number_size = len(magic_number) + 1  # Add 1 for newline character
        header_size = len(line) + 1 + len(str(max_color_value)) + 1  # Add 1 for newline character after max_color_value
        
        file_size = os.path.getsize(file_path)

        return width, height, file_size, header_size

def get_ppm_parameters(file_path_png,file_path_json):   
    #convert png to ppm 
    file_path_ppm = file_path_png.replace('.png', '.ppm')
    convert_png_to_ppm(file_path_png, file_path_ppm)
    
    #get array to ppm
    image_array = ppm_to_bytearray(file_path_ppm)
    bitmap_array,_,_ = get_3d_byte_array_from_ppm(file_path_ppm) 
    
    #write file in json format 
    write_on_jsonfile(bitmap_array,image_array,file_path_json)
    
    #get parameters of ppm
    w, h, fs, hs = read_ppm_header(file_path_ppm)
    
    return file_path_json, w, h, fs, hs
