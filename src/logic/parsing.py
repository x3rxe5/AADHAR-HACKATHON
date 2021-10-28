
from typing import Optional
from typing import Optional
from src.schemas.schema import CreateAddress


def parse_address(res:CreateAddress) -> dict:
    parser_dict = dict(res)
    print("This is parsed dictionary -> ",parser_dict)
    res_dict = main_logic(parser_dict)
    return res_dict

# main logic implementation for parsing and combine the address
def main_logic(input_dict:dict) -> dict:
    values = set(list(input_dict.values()))
    output_dict = {}    
    for v in values:        
        res = [k for k, z in input_dict.items() if z == v]
        if len(res) > 1:
            output_dict['/'.join(res)] = v
        else:
            output_dict[res[0]] = v
    return output_dict