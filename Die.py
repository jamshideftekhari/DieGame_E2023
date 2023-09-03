# import random class for generating random numbers
import random
# Die class which inheritate from object class
class Die(object):
    # constructor method, will be called for each instance of Die class
    def __init__(self):
        self.FaceValue = 0   #FaceValue is Die attribute which initialised here in init method. 
    
    # roll method generate a value of facevalue using randint() method in random class 
    def Roll(self):
        self.FaceValue = random.randint(1,6)

    # Get face value return the generated random number
    def GetFaceValue(self):
        return self.FaceValue    
 
 # Test the class   
if __name__ == "__main__":
    # create a instance of Die class
    d = Die()
    # call roll method to generate a random number
    d.Roll()
    # print the generated number
    print(d.GetFaceValue())