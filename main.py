from base64 import b64decode

def pssh_parse(b64_pssh):
    decoded_pssh = b64decode(b64_pssh)
    print(decoded_pssh.hex())
    box = {
        'size': decoded_pssh[0:4],
        'type': decoded_pssh[4:8],
        'version': decoded_pssh[8:9],
        'flags': decoded_pssh[9:12],
        'drm_system_id': decoded_pssh[12:28],
        'key_id_count': decoded_pssh[28:32],
        'rest' : decoded_pssh[32:]

    }
    # print(int.from_bytes(decoded_pssh[28:32], 'big'))
    # for key_id in range(0, int.from_bytes(decoded_pssh[28:32], 'big')): # pssh delivered via network and the network uses big endian order/
    #     print('{0} - {1}'.format(32+(key_id*16), 32+((key_id+1)*16)))
    #     print(decoded_pssh[32+(key_id*16): 32+((key_id+1)*16)])

    return box
if __name__=='__main__':
    b64_pssh = 'AAAAT3Bzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAAC8IARIQZjE1ODc2MDRhNWQyZWRkNBoDQ0FQIhBGMzUwMV9GMzUwMDAwMDAwKgJIRA=='

    box = pssh_parse(b64_pssh)

    # print(box['size'].hex())
    # print(box['type'].hex())
    # print(box['version'].hex())
    # print(box['flags'].hex())
    # print(box['drm_system_id'].hex())
    print(box['key_id_count'].hex())
    print(len(box['rest'].hex()))

