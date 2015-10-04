# coding=utf8
#!/usr/bin/python


class Employee:
  empCnt = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCnt += 1

  def displayCount(self):
    print "Total employee %d" % Employee.empCnt

  def displayEmployee(self):
    print "Name: ", self.name, ", Salary: ", self.salary

emp = Employee("allen", "22")
emp.displayCount()
emp.displayEmployee()

# add,
# setattr
# getattr
# hasattr
emp.xxxx = "yyyy"
print emp.xxxx
print getattr(emp, "xxxx")
print hasattr(emp, "name")
setattr(emp, "wife", "xiaofeng")
print getattr(emp, "wife")
print emp.wife
del emp.wife


# 内置类属性
print Employee.__bases__
print Employee.__doc__
print Employee.__dict__
print Employee.__module__
