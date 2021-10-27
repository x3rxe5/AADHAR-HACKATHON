
from typing import Optional
from typing import Optional
from src.schemas.schema import CreateAddress


def parse_address(res:CreateAddress) -> dict:
    parser_dict = dict(res)
    address_list = list()
    address_set = set()
    for address in parser_dict:
        address_list.append(address)
        address_set.add(parser_dict[address])
    # print(address_list)
    print(address_set)
    return res