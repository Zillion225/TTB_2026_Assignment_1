"""
This script provides a simple Caesar cipher decryption function.
"""
from typing import List

def transform_alphabet_to_number(input_str: str) -> List[int]:
    """Converts a string of alphabetic characters to a list of ASCII codes.

    Args:
        input_str: The input string.

    Returns:
        A list of ASCII codes.
    """
    return [ord(char) for char in input_str.upper()]

def transform_number_to_string(input_list: List[int]) -> str:
    """Converts a list of ASCII codes to a string.

    Args:
        input_list: The list of ASCII codes.

    Returns:
        The resulting string.
    """
    return "".join([chr(num_code) for num_code in input_list])

def shift_logic(ascii_code: int, shift_position: int) -> int:
    """Shifts an ASCII code by a given position, wrapping around the alphabet.

    Args:
        ascii_code: The ASCII code to shift.
        shift_position: The number of positions to shift.

    Returns:
        The shifted ASCII code.
    """
    # Handle cases where shift_position > 26
    shift_position %= 26  
    result = ascii_code - shift_position
    
    alphabet_start = ord('A')
    alphabet_end = ord('Z')

    if result < alphabet_start:
        result += 26
    elif result > alphabet_end:
        result -= 26
        
    return result

def simpleCipher(encrypted: str, k: int) -> str:
    """Decrypts a string using a simple Caesar cipher.

    Args:
        encrypted: The encrypted string.
        k: The shift key.

    Returns:
        The decrypted string.
    """
    ascii_list = transform_alphabet_to_number(encrypted)
    shifted_list = [shift_logic(code, k) for code in ascii_list]
    return transform_number_to_string(shifted_list)

def main():
    """
    Main function to demonstrate the simple cipher decryption.
    """
    encrypted_text = 'VTAOG'
    k = 2
    decrypted_text = simpleCipher(encrypted_text, k)
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    main()
