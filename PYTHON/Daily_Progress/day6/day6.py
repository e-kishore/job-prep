from pydantic import BaseModel , field_validator , model_validator 
class validate(BaseModel):
        age:int = 18
        name:str = None

        @field_validator('age')
        def agevalidation(cls,age):
                if age<18:
                        raise ValueError("age must be above 18")
                return age

data = validate(name="",age = "19")
print(data)


class password(BaseModel):
        passw:str
        repass:str

        @model_validator(mode='after')
        def passmatch(self,cls):
            if self.passw != self.repass:
                   raise ValueError("password does not match")
            return self
user = password(passw="kishore",repass ="kishore")

print(user)


