from googletrans import Translator
from typing import Optional

from pydantic import errors
from src.schemas.schema import CreateAddress
from src.logic.language_dict import LANGUAGES
from src.errors.Error import InvalidLanguageException

def parse_address(res:CreateAddress,lang:Optional[str]=None):
    try:
        parser_dict = dict(res)   
        res_dict = main_logic(parser_dict)
        final_dict = dict()
        if lang != None:
            try:
                result_dict = dict(parse_address_local(res_dict,lang))
                final_dict = {
                    "english":res_dict,
                    LANGUAGES[lang]:result_dict
                }
            except Exception:
                raise InvalidLanguageException
        else:
            final_dict = {
                "english":res_dict,
            }
        
        return final_dict
    except InvalidLanguageException:
        return{
            "error":"Invalid Language error"            
        }

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

def parse_address_local(res_dict:dict,lang:str) -> dict:
    try:
        translator = Translator()
        result_dict = dict()
        for key in res_dict:
            if isinstance(res_dict[key],str):
                try:
                    result_dict[key] = (translator.translate(res_dict[key], src='en', dest=lang)).text
                except Exception:
                    raise InvalidLanguageException
            else:
                result_dict[key] = res_dict[key] 
        
        return result_dict
    except InvalidLanguageException:
        return{
            "error":"Invalid Language error"            
        }