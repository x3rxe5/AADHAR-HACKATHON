from pydantic import BaseModel

class CreateAddress(BaseModel):
    house:str
    street:str
    area:str
    landmark:str
    village:str
    pincode:int
    sub_district:str
    district:str
    state:str
    
