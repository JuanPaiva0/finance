from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str | None = None

class CategoryOut(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)