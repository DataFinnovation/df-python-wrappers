'''

'''

def subdict(dict_in, sub_keys):
    out_dict = {}
    for k in sub_keys:
        if k in dict_in:
            out_dict[k] = dict_in[k]
    return out_dict

# eof
