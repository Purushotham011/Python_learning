#if his basic salary is less than Rs. 1500, then HRA=10% of basic salary and DA=90% of basic salary.If his salary is either equal to or above Rs.1500,then HRA =Rs500 and DA = 98% of basic salary.If the employee's salary is input through the keyboard write a program to find his gross salary using functions

def gs(basic_salary):
    if basic_salary<1500:

        HRA=basic_salary*0.1
        DA=basic_salary*0.9
    else:
        HRA=500
        DA=basic_salary*0.98
    gross_sal= basic_salary+HRA+DA
    return gross_sal

x=int(input("Enter your Basic salary : Rs.")) 
print(f"Gross Salary : Rs.{gs(x)}")