from db import create_table
from employee_repostery import EmployeeRepository
from department_statistics import DepartmentStatistics

create_table()
repo = EmployeeRepository()
stats = DepartmentStatistics()

repo.insert_data(1, "Kamal Həsənov",     1350, 20)
repo.insert_data(2, "Aysu Quliyeva",      320, 30)
repo.insert_data(3, "Eldar Məmmədli",     780, 10)
repo.insert_data(4, "Leyla Kərimova",     460, 20)
repo.insert_data(5, "Samir Əlizadə",     2100, 10)
repo.insert_data(6, "Nərmin Hüseynli",    950, 30)
repo.insert_data(7, "Təbriz Rzayev",      410, 20)
repo.insert_data(8, "Səbinə Əliyeva",    1600, 10)
repo.insert_data(9, "Murad Qasımov",      290, 30)
repo.insert_data(10, "Aygün Abdullayeva", 1200, 20)
repo.insert_data(11, "Rəşid Əhmədli",    1750, 10)
repo.insert_data(12, "Günay Məlikova",    380, 30)
repo.insert_data(13, "Orxan İbrahimov",   840, 20)
repo.insert_data(14, "Sevda Səfərova",    470, 10)
repo.insert_data(15, "Vüsal Nəcəfli",     260, 30)

repo.show_all_employees()

repo.show_low_salary_descending()

stats.show_charts()