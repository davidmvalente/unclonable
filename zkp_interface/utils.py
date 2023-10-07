#img-> Immagine 
#json dove associo png in byte (array monodimensionale): png_array 
#bitmap organizzata in un vettore (3 X n X m) in byte : bitmap_array
#"png_array":["1","3"]
import json 
from PIL import Image

#from image get the 3d vector of bits 
def get_3d_byte_array_from_png(image_path):
    with Image.open(image_path) as img:
        # Convert the image to RGB mode (if it's not already)
        img = img.convert('RGB')
        
        # Get the width and height of the image
        width, height = img.size
        print(img.size)

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