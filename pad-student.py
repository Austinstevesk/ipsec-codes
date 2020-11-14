def pad(self, data_len):
  """ return the Padding field 

  Args:
    data_len: the length of the Data Payload 
  """
  ### Complete the code so it returns the necessary 
  ### padding bytes for an ESP packet. The padding 
  ### bytes are derived from data_len the length 
  ### expressed in number of bytes of the Data 
  ### Payload 

  ##BEGIN_CODE
  #pad_len = 0 to 255 depending on data_len
  pad_len = 0
  while pad_len<255: 
    pad_len = 2+self*4
    break
  block_size = pad_len
  length = block_size - (data_len % block_size)
  Payload = data_len + length * length
  
  padding_bytes = bytes(Payload - data_len)
  

  return padding_bytes
x=pad(0,20)
print(x)
  ##END_CODE

