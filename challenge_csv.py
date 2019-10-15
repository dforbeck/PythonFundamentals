#Goal: collect all events of unauthorized traffic over the network

# # import csv module
import csv

# # name and open the employee and access CSV files
# # create a csv reader object and print

# #Sample
# # with open('employees.csv') as employees_csv:
# #     csv_emp_reader = csv.DictReader(employees_csv)
#     # for employee in csv_emp_reader:
#     #     print(employee['id'], employee['first_name'] ,employee['last_name'], employee['email'], employee['ip_address'])

with open('access_list.csv') as access_csv, open('employees.csv') as employees_csv:
    csv_access_reader = csv.DictReader(access_csv)
    csv_emp_reader = csv.DictReader(employees_csv)

    both = {a[0] for a in csv_access_reader} and {a[4] for a in csv_emp_reader}
    for access in csv_access_reader:
        if access[0] not in both:
            print(access)


