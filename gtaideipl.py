import struct

# Function to read a string from a binary file
def read_string(file):
    string = ""
    while True:
        char = file.read(1).decode('ascii')
        if char == '\0':
            break
        string += char
    return string

# Function to read a 4-byte integer from a binary file
def read_int(file):
    return struct.unpack("i", file.read(4))[0]

# Function to read a 4-byte float from a binary file
def read_float(file):
    return struct.unpack("f", file.read(4))[0]

# Function to read an IDE file
def read_ide_file(file_path):
    ide_data = []
    with open(file_path, "rb") as ide_file:
        num_items = read_int(ide_file)
        for _ in range(num_items):
            model_name = read_string(ide_file)
            model_id = read_int(ide_file)
            draw_distance = read_float(ide_file)
            flags = read_int(ide_file)
            ide_data.append((model_name, model_id, draw_distance, flags))
    return ide_data

# Function to read an IPL file
def read_ipl_file(file_path):
    ipl_data = []
    with open(file_path, "rb") as ipl_file:
        num_items = read_int(ipl_file)
        for _ in range(num_items):
            model_name = read_string(ipl_file)
            x = read_float(ipl_file)
            y = read_float(ipl_file)
            z = read_float(ipl_file)
            rotation = read_float(ipl_file)
            ipl_data.append((model_name, x, y, z, rotation))
    return ipl_data

# Example usage
ide_file_path = "example.ide"
ipl_file_path = "example.ipl"

ide_data = read_ide_file(ide_file_path)
ipl_data = read_ipl_file(ipl_file_path)

# Print the imported data
print("IDE Data:")
for item in ide_data:
    print(item)

print("\nIPL Data:")
for item in ipl_data:
    print(item)
