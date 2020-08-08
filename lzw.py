

in_str = "ABBABBBABBA"
#in_str = "AAA" 
in_str = "TOBEORNOTTOBEORTOBEORNOT"

#every time a code is output a code is added to the dictionary
def compress(in_str):
    code_dict = dict()
    for i in range(256):
        code_dict[chr(i)] = i

    next_code = 257
    curr_str = ""
    rtn_codes = []

    for i in range(len(in_str)):
        curr_str += in_str[i]
        #print(curr_str)
        if curr_str not in code_dict:
            curr_code = code_dict[curr_str[:-1]]
            print("Append code: %d for: %s"%(curr_code, curr_str[:-1]))
            rtn_codes.append(curr_code)
            code_dict[curr_str] = next_code
            next_code += 1
            curr_str = curr_str[-1]

    rtn_codes.append(code_dict[curr_str])

    return rtn_codes

r = compress(in_str)
print("Compress results: %s"%(str(r)))

#every time a code is output a code is added to the dictionary
#every time a code is added to the dictionary a code list is reset?
def decompress(code_list):
    code_dict = dict()
    for i in range(256):
        code_dict[i] = chr(i)

    next_code = 257
    tmp_code_list = []

    for code in code_list:
        tmp_code_list.append(code)
        if len(tmp_code_list) > 1:
            code_dict[next_code] = tmp_code_list
            tmp_code_list = tmp_code_list[-1:]
            print("Code: %i Trans: %s tmp_code_list: %s"%(next_code, str(code_dict[next_code]), str(tmp_code_list)))
            next_code += 1
            

def decompress(code_list):
    code_dict = dict()
    for i in range(256):
        code_dict[i] = chr(i)

    next_code = 257

    rtn = ""
    for i in range(1,len(code_list)):
        rtn += code_dict[code_list[i-1]]
    
        if code_list[i] in code_dict:     
            n_str = code_dict[code_list[i-1]] + code_dict[code_list[i]][0]
        else:
            #this is the trick case of LZW where the code is based on a repeat
            #of the previous code
            n_str = code_dict[code_list[i-1]] + code_dict[code_list[i-1]][0]
            
        code_dict[next_code] = n_str
        print("Code: %i Value: %s"%(next_code, n_str))
        next_code += 1

    rtn += code_dict[code_list[-1]]
    return rtn

        


print("Decompress...")
print(decompress(r))


        
    
