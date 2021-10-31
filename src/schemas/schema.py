from pydantic import BaseModel

class CreateAddress(BaseModel):
    house:str
    street:str
    area:str
    landmark:str
    city:str
    pincode:int
    sub_district:str
    district:str
    state:str
    
    # def __str__(self) -> str:
    #     return super().__str__(self)