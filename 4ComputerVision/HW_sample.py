#------------------------------------------------------------------------------
"""
Created on Tue Feb 15 13:44:51 2022
"""
#------------------------------------------------------------------------------
# SUBMODULES
def d_xor(a, b):    # XOR (no signed bit) operator output will be (length_b - 1)                                         
    result = []
    for i in range(1, len(b)):                                    
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def mod2div(divident, divisor):                            # modulo-2 division
    pick = len(divisor)
    tmp  = divident[0 : len(divisor)]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = d_xor(divisor, tmp) + divident[pick]     # '+' means concatenate
        else:
            tmp = d_xor('0'*pick, tmp) + divident[pick]    # '+' means concatenate
        pick = pick + 1
    if tmp[0] == '1':
        tmp = d_xor(divisor, tmp)
    else:
        tmp = d_xor('0'*pick, tmp)
    remainder = tmp
    return remainder
#------------------------------------------------------------------------------ 
# TOP-MODULES
def TOP_encode(data, poly):                                       # crc encode
    l_poly         = len(poly)
    appended_data  = data + '0'*(l_poly-1)                        # concatenate
    remainder      = mod2div(appended_data, poly) 
    crccode        = remainder                 
    codeword       = data + remainder                             # concatenate
    return codeword, crccode                    # return code-word and crc-code

def TOP_check(codeword, poly):                                    # crc check
    remainder = mod2div(codeword, poly)
    return remainder                                         
#------------------------------------------------------------------------------
# TESTBENCHS
def bin2hexa(n):
    num     = int(n, 2)                                 # convert binary to int
    hex_num = format(num, 'x')                     # convert int to hexadecimal       
    return(hex_num)

def hex_to_int(inputs):
    return int(inputs,16)

def int_to_bin(inputs):
    getbinary   = lambda x, n: format(x, 'b').zfill(n)
    output      = getbinary(inputs,16)
    return output

def test_xor():
    print('Testing XOR operator...\n')
    a = '1001'
    b = '1100'
    r = d_xor(a, b)
    print('Result:', r)
    return r

def test_mod2div():
    divident  = '100100000'
    divisor   = '1101'
    remainder = mod2div(divident, divisor)
    print('Result:', remainder)

def testbench1():
    print('Generating for 0x07 poly...\n')
    getbinary         = lambda x, n: format(x, 'b').zfill(n)
    poly              = "100000111"                                        #0x07
    data              = 4
    bin_data          = getbinary(data,16)
    hex_data          = bin2hexa(bin_data)
    enc_dw, enc_crc   = TOP_encode(bin_data, poly)
    enc_hex           = bin2hexa(enc_crc)
    print('-----------------------------')
    print('Poly is:              ', bin2hexa(poly))
    print('Data hex is:          ', bin2hexa(bin_data))
    print('Binary string is:     ', bin_data)
    print('CRC cncode in bin is: ', enc_crc)
    print('CRC encode in hex is: ', enc_hex)        

def testbench2():
    print('Generating for 0x07 poly...\n')
    getbinary   = lambda x, n: format(x, 'b').zfill(n)
    poly        = "100000111"                                             #0x07
    with open('crc_result_0x07.txt','w') as f:
        for data in range(0, 65536):                            #Full 0000~ffff
            print('\n calculating for ', data)
            bin_data          = getbinary(data,16)
            hex_data          = bin2hexa(bin_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(hex_data)
            f.write(', ')
            f.write(enc_hex)
            f.write('\n')
  
def testbench3():
    print('Generating for 0x1021 poly...\n')
    getbinary   = lambda x, n: format(x, 'b').zfill(n)
    poly        = "10001000000100001"                                     #0x1021
    with open('crc_result_0x1021.txt','w') as f:
        for data in range(0, 65536):                               #for 0000~ffff 
            print('\n calculating for ', data)
            bin_data          = getbinary(data,16)
            hex_data          = bin2hexa(bin_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(hex_data)
            f.write(', ')
            f.write(enc_hex)
            f.write('\n')

def testbench4():
    print('Generating for 0x04C11DB7 poly...\n')
    getbinary   = lambda x, n: format(x, 'b').zfill(n)
    poly        = "100000100110000010001110110110111"                  #0x04C11DB7
    with open('crc_result_0x04C11DB7.txt','w') as f:
        for data in range(0, 65536):                                #for 0000~ffff  
            print('\n calculating for ', data)
            bin_data          = getbinary(data,16)
            hex_data          = bin2hexa(bin_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(hex_data)
            f.write(', ')
            f.write(enc_hex)
            f.write('\n')

def testbench5():
    poly        = "100000111"                  #0x07
    number_list = open('crc_input.txt','r') 
    with open('crc_output_0x07.txt','w') as f:
        for line in number_list:
            hex_data = line.strip()
            print('\n calculating for ', hex_data)
            int_data          = hex_to_int(hex_data)
            bin_data          = int_to_bin(int_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(enc_hex)
            f.write('\n')
        number_list.close()

def testbench6():
    poly        = "10001000000100001"                  #0x1021
    number_list = open('crc_input.txt','r') 
    with open('crc_output_0x1021.txt','w') as f:
        for line in number_list:
            hex_data = line.strip()
            print('\n calculating for ', hex_data)
            int_data          = hex_to_int(hex_data)
            bin_data          = int_to_bin(int_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(enc_hex)
            f.write('\n')
        number_list.close()

def testbench7():
    poly        = "100000100110000010001110110110111"                  #0x04C11DB7
    number_list = open('crc_input.txt','r') 
    with open('crc_output_0x04C11DB7.txt','w') as f:
        for line in number_list:
            hex_data = line.strip()
            print('\n calculating for ', hex_data)
            int_data          = hex_to_int(hex_data)
            bin_data          = int_to_bin(int_data)
            enc_dw, enc_crc   = TOP_encode(bin_data, poly)
            enc_hex           = bin2hexa(enc_crc)
            f.write(enc_hex)
            f.write('\n')
        number_list.close()                
#------------------------------------------------------------------------------
# MAIN FUNCTIONS
if __name__ == "__main__":
    #test_xor()
    #test_mod2div()
    #testbench1()
    #testbench2()
    #testbench3()
    #testbench4()
    testbench5()
    testbench6()
    testbench7()
#------------------------------------------------------------------------------   
