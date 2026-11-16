from pydantic import BaseModel , field_validator, constr, conint
from typing import Optional
data = '{"name":"kishore","mark":26}'

class valid(BaseModel):
    name : constr(min_length=1)
    Age : Optional[int] =None
    mark : conint(gt=25) | None = None


   

user= valid.model_validate_json(data)
#op = user.model_dump_json()

print(user)
