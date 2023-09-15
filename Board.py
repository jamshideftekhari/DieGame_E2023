from Field import Field
class Board():
    def __init__(self):
        self.fields = {}
        self.field={}

    def addFieldObject(self, fieldNumber, fieldType, fieldMove):
        self.fields[fieldNumber] = Field(fieldType, fieldMove)

    def addField(self, fieldNumber, fieldType, fieldMove):
        self.fields[fieldNumber] = {"fieldType": fieldType, "fieldMove": fieldMove}

    def getField(self, fieldNumber):
        return self.fields[fieldNumber]

    def __str__(self) -> str:
        return f" {self.fields}"

if __name__ == "__main__":
    b = Board()
    b.addField(1, "N", 5)
    b.addField(2, "N", 5)
    b.addField(3, "N", 5)

    f = {"fieldType": "N", "fieldMove": 5}
    b.addField(4, f["fieldType"], f["fieldMove"])

    print(b)                