def check_values(emp_id,department_id,salary):
  try:
    if emp_id>0:
        print("Succesfully")

  except ValueError:
         print("employee id must be greater than 0!")

  try :
    if department_id>0:
        print("Succesfully")
  except ValueError:
        print("department id must be greater than 0!")
  try :
        if salary>0:
            print("Succesfully")
  except ValueError:
        print("salary must be greater than 0!")