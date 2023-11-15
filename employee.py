# Let's start!

#  OOP introduction

"""
class Employee:
    name = "No Name"
    dept =  "No Department"

def getName(self):
    return self.name

def getDept(self):
    return self.dept

def setName(self, xname):
    self.name = xname
    return

def setDept(self, xdept):
    self.dept = xdept
    return
"""

"""
class Test:

    def __init__(self, arg1 = 6.2):
        
        self.a = arg1


b = Test("Bobby")
c = Test()

print(f"b = {b.a}, c = {c.a}")

"""

# this code is without any validation an if you put inappropiate data type it'll crash


"""
class Employee:
    _name = ''
    _dept = ''
    departments = {'ACC':'Accounts', 'ADM':'Administration', 'ENG' : 'Engineering', 'MTC': 'Maintenance'}

    def __init__(self, name, dept):
        self.setName(name)
        self.setDept(dept)

    def setName(self, name):
        self._name = name

    def setDept(self, dept):
        self._dept = dept

    def getName(self):
        return self._name

    def getDept(self):
        return self._dept
    
# The application program

myDep = 'ACC'
myEmp = Employee('Walter ', myDep)

myName = myEmp.getName()
myDept = myEmp.getDept()
myDeptFull = myEmp.departments[myDept]

print (f'{myName} is in {myDeptFull} - Code {myDept}')
       
myEmp.setName('Freddy')
myEmp.setDept('ENG')
              
print (f'{myEmp.getName()} in {myEmp.getDept()} - {myEmp.departments[myEmp.getDept()]}')

"""


# this code is WITH validation an if you put inappropiate data type it should not crash)

"""
class Employee: 
    _name = "Invalid name" 
    _dept = "Invalid Dept" 
    _ind = False 
    _creationErr = False 
    departments = {'ACC':'Accounts', 'ADM':'Administration', 'ENG':'Engineering', 'MTC':'Maintenance'} 
     
    def __init__(self, name, dept, ind = False): 
         
         self.setName(name) 
         self.setDept(dept) 
         self.setInd (ind) 
         if self._creationErr: 
             print ('Error occurred.  Employee not created') 
                       
 
    def setName (self, name): 
      errFlg = False  
      errMsg = 'Arg1: Name required - A string starting with an alpha' 
      if not name: 
         errFlg = True 
      else: 
        if type(name) != str: 
          errFlg = True 
        else: 
          nameA = name.strip() 
          if not nameA[0].isalpha():             
            errFlg = True         
  
        if errFlg == True: 
          self._creationErr = True 
          print(errMsg) 
        else:                
          self._name = nameA 
           
    def setDept(self, dept): 
      errFlg = False  
 
      if not dept: 
        errMsg = 'Arg2 A valid Department code is required' 
        errFlg = True 
      else: 
        if type (dept) != str: 
          errMsg =  'Department must be a string' 
          errFlg = True 
        else: 
            deptKey = dept.strip().upper() 
            if not deptKey in self.departments: 
              errMsg = 'Not a valid department' 
              errFlg = True 
               
      if errFlg == True: 
        self._creationErr = True 
        print (errMsg) 
      else:             
        self._dept = deptKey 
         
    def setInd (self, ind): 
        if not ind: 
            indA=False 
        else: 
            indA=True 
        self._ind = indA 
 

    def getName(self): 
        return self._name 
           
    def getDept(self): 
        return self._dept  
 
    def getInd(self): 
        return self._ind  
 

# Application program 
 
myDep = '  adm  '    
myEmp = Employee(' Walter  ',myDep, True) 
 
# Here I access the object variables directly 
print (f'''{myEmp._name} in {myEmp._dept} - {myEmp.departments[myEmp._dept]} ind = {myEmp._ind}''') 
 
# Use the setters on an existing object 
myEmp.setName("Freddy") 
myEmp.setDept('mtc') 
myEmp.setInd(0) 
 
# Here I use the getters 
print (f'''{myEmp.getName()} in {myEmp.getDept()} - {myEmp.departments[myEmp.getDept()]} Induction = {myEmp.getInd()}''')

"""


# Happy coding!