from Crypto.Cipher import AES
def decrypt_packet_no_header(cipher_text_hex, key, iv):
    cipher_bytes = bytes.fromhex(cipher_text_hex)
    if len(cipher_bytes) % 16 != 0:
        raise ValueError("طول البيانات غير صالح لفك AES-CBC: يجب أن يكون مضاعف 16")    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_bytes = cipher.decrypt(cipher_bytes)
    return plain_bytes.hex()

key = bytes([42, 139, 16, 190, 123, 124, 251, 251, 84, 3, 0, 80, 84, 1, 0, 48])
iv = bytes([27, 179, 99, 176, 123, 127, 235, 255, 82, 66, 0, 48, 74, 2, 16, 49])
#key = bytes([27, 179, 99, 176, 123, 127, 235, 255, 82, 66, 0, 48, 74, 2, 16, 49])
#iv = bytes([42, 139, 16, 190, 123, 124, 251, 251, 84, 3, 0, 80, 84, 1, 0, 48])

cipher_text = "0515000002e0e8086c33daf7aeaf27d751681ba81bc7ab926ddca4927f9dfe3c396393b25e3d42579ecc56739cec12f6a401682d09e73c6db2fd50f2121b596eab91e382e9e1b0f190b50d5fb54ca7a7337050d981fd65be819919c59c461857f820ef22ee9bbf238bb65ba5bd763d1c38ed1badeb0592bd0313c8cde8b6aff8a4ed18fdadc30fd12b6239b5a18ba8ac5f629b580999c957a333a63c35e162f4b73891deb31b37df16e0105ed2356002d342c70f9460739ba8e89b5c58758a701779436d533b8c5ddfe39d1d3f5547f6ff38cd2ba6d81d1f0f7dfc7d30bdb66c57831d8a7fcb0f5f6c84fe21ed400e892fafc7d6579c8e3de1aac67b228ad31c3b1ca65f29dd4a601ff38a76c778133cfd7d47e341d0834ead8ba180715d4a40584b32dbf36e8450822a981089e5abf4aef1c57c1506e415fecca03e7fdfbeb1cb27e75e9e881fc42fea7b20db7c8fedd8b9debd4bd24d56e0ed6ed7853a03fb836b18fc25562f08bd0ad78b5ad17a43422465a78804446aea95715e36e115cad86e80b1ab852a883fff401cbddccc8214956a17b82eb5fd8aaa3eb93e47e03cfbef67b1a54857eebbdadbe129fc13c92d59aca1d6bb184a9eff5c75039daf347a8dd52da97b9e928acbc201b55bb4996c253c49ccddcfa9c09d0a89cdcd8cf20808452417e9e1302b44666d15be87dbb9df5aa1f497cf3b8c75c027d43ac33f439409516de62ed16bf90c28c56d95b14a65ec73a55a9a26f095930ae30c148397563e63382379143ed4ce0f8a6020ebb4f60fce01fd2e5d1ffcbab43cfdbba994e20c2eae7ee7369c7d9b66a9ed43ea6ef535edb1bd161c28cef604d56cb145afea8a9f3b9fdbb44a8006bb5928d13801690f52621ed192cf6225a0f5e711667d7af26bfcc5a6d43c253f333c05ef8f8f2dbfe68b0e6fccc6b8d53fdbdcfeba3e0c3676fd54537ae73f779db86d70d9af2fd92a462907f1e462d67d7a395b7f67644710e77ed027c9d6b9f6137ce0d6d9cac2060d3aca73774324ef723fc28e0453cb83ef8c"
plain_hex = decrypt_packet_no_header(cipher_text, key, iv)
print(plain_hex)