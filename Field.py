import json
class Field():
    def __init__(self, fieldType, fieldMove):
        self.FieldType = fieldType
        self.FieldMove = fieldMove

    
    def GetFieldType(self):
        return self.FieldType
    
    def GetFieldMove(self):
        return self.FieldMove
    
    def __str__(self) -> str:
        return f" {self.FieldType} {self.FieldMove}"
    
if __name__ == "__main__":
    field = Field("N", 5)
    print(field)
    print(field.GetFieldType())
    print(field.__str__())
    print(str(field))
    print(field)
    print(json.dumps(field.__dict__))   