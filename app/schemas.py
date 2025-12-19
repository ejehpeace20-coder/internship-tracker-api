from pydantic import BaseModel

class InternshipBase(BaseModel):
    company: str
    role: str
    status: str


class InternshipCreate(InternshipBase):
    pass


class InternshipResponse(InternshipBase):
    id: int

    class Config:
        orm_mode = True
