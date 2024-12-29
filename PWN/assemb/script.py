def string_to_hex(s):
    hex_string = ""
    for char in s:
        hex_string += "\\x" + format(ord(char), "02x")
    return hex_string

def split_string(s, chunk_size):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

def main():
    input_string = "barbeapapaoldifjlsdfjlsfjldskjfsjdkfmjlds"
    # Split the string into chunks of 8 characters
    chunks = split_string(input_string, 8)
    for chunk in chunks:
        # Reverse each chunk to match the little-endian format
        reversed_chunk = chunk[::-1]
        hex_chunk = string_to_hex(reversed_chunk)
        print(f"Chunk: {chunk} -> {hex_chunk}")

if __name__ == "__main__":
    main()