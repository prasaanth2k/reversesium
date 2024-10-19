class BROOKER:

    def hex_to_bytes(self,hex_value):
        try:
            if hex_value.startswith('0x'):
                hex_value = hex_value[2:]
            
            decimal_value = int(hex_value,16)

            print(f"Total Bytes {decimal_value}")
        except ValueError:
            raise ValueError("Invaild hexadecimal input")