from construct.core import *
from construct.lib import *
from binascii import hexlify

## The section of the code that need to be updated are
## indicated with XXXX
salt = b'\xf7\xca\x79\xfa'
seq_num = 5
ext_seq = True


IIV_Nonce = Struct(
  ## Replace XXXX by the appropriated value which 
  ## indicates the length of the salt as 
  ## a number of bytes
  "salt" / Bytes(4),
  "iv" / IfThenElse(this._.ext_seq_num_flag,
    Struct( "zero" / Const(b'\x01\x02\x03\x04'),
            "seq_num_counter" / Int32ub),
    Struct( "seq_num_counter" / Int64ub)
    )
)

def show_nonce(salt, seq_num, ext_seq):
  ## defining the structure
  nonce = { 'salt' : salt, \
            'iv' : {'seq_num_counter' : seq_num } }

  try:
    ## converting structure to binary
    byte_nonce = IIV_Nonce.build(\
                   nonce, 
                   ext_seq_num_flag=ext_seq)
    print(byte_nonce)
    ## parsing binary to structure 
    struct_nonce = IIV_Nonce.parse(\
                    byte_nonce, 
                    ext_seq_num_flag=ext_seq)

    ## printing the different representations
    print("\n---")
    print("Inputs:")
    print("    - salt: %s"%salt)
    print("    - sec_num: %s"%seq_num)
    print("    - ext_seq_flag: %s"%ext_seq)
    print("Nonce (binary)")
    print("    - nonce [%s bytes]: %s"%(len(byte_nonce),
                                        byte_nonce))
    print("Nonce (structure)")
    print("    - nonce: %s"%struct_nonce)
    print("---\n")
  except:
    print("\n---")
    print("> ERROR : Unable to generate the nonce")
    print("> Inputs:")
    print(">    - salt: %s"%salt)
    print(">    - sec_num: %s"%seq_num)
    print(">    - ext_seq_flag: %s"%ext_seq)
    print("-----\n")
  return 
show_nonce(salt, seq_num, ext_seq)



