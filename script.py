from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import re
import csv
import sys


#employees = ['test@test.com', 'test@mail.com', 'email@test.com', 'test@tester.com', 'tested@test.com']

breached_accounts = {}


def checkpwn(emails_file):


    with open(emails_list_file, 'rt') as emails:
        csv_reader = csv.reader(emails)

        next(csv_reader) # skip the heading

        for line in csv_reader:
#           print(line[1])
            employee = line[1]


            #print(employees.index(employee))

            driver = webdriver.Firefox()

            driver.get('https://monitor.firefox.com')

            time.sleep(2)

            email_field = driver.find_element_by_id("scan-email")

            email_field.send_keys(employee)

            button = driver.find_element_by_xpath("/html/body/main/section/div/form/div[2]/input")

            button.click()

            time.sleep(2)

            breach_number = driver.find_element_by_xpath("/html/body/main/div[1]/div/h2/span")

            breach_number = breach_number.get_attribute('innerHTML')

            index = line[0]


            if int(breach_number) > 0:
                breaches_title = driver.find_elements_by_class_name("breach-title")

                breaches_value = driver.find_elements_by_class_name("breach-value")

                breached_accounts[index] = {}
                breached_accounts[index]['Email'] = employee
                breached_accounts[index]['Appeared'] =  breach_number

                breached_accounts[index]['Breaches'] = []

                for breach_title in breaches_title:
                    title = breach_title.get_attribute('innerHTML')
                    breached_accounts[index]['Breaches'].append(title)
                    #print(breach_title.get_attribute('innerHTML'))


                breach_date = breaches_value[0].get_attribute('innerHTML')

                breached_accounts[index]['Date'] = breach_date

                compromised_values = breaches_value[1].get_attribute('innerHTML')

                breached_accounts[index]['Compromised'] = []

                compromised_datas = compromised_values.split(",")

                for compromised in compromised_datas:

                    breached_accounts[index]['Compromised'].append(compromised)




            driver.quit()




header = ['id', 'email', 'appeared', 'breaches', 'date', 'compromised']

def create_breached_csv(output_file):


    with open(output_file, 'wt') as f:

        csv_writer = csv.writer(f)

        csv_writer.writerow(header) # write header

        for ba, ba_info in breached_accounts.items():

            row = []

            # append id
            row.append(ba)

            # append email
            row.append(ba_info['Email'])

            # append appeared
            row.append(ba_info['Appeared'])


            # append breaches

            breaches_list = ba_info['Breaches']

            #print(str(breaches_list)[1:-1])

            breaches_list = str(breaches_list)[1:-1]

            row.append(breaches_list)


            # append date
            row.append(ba_info['Date'])

            # append compromised

            compromised_lists = ba_info['Compromised']

            compromised_lists = str(compromised_lists)[1:-1]

            row.append(compromised_lists)

            csv_writer.writerow(row)

    print("Breached accounts details have been saved to : ", output_file)
    
 


if len(sys.argv) == 2:

    emails_list_file = sys.argv[1]

    checkpwn(emails_list_file)

    output_file = 'breached_accounts.csv'

    create_breached_csv(output_file)

elif len(sys.argv) == 3:

    emails_list_file = sys.argv[1]

    checkpwn(emails_list_file)

    output_file = sys.argv[2]

    create_breached_csv(output_file)


else:

    print("Please run the script with input csv file path and the optional output csv file path as arguments")

    print("python3 script.py emails_list.csv breached_accounts.csv")






#print(breached_accounts)

#print(">>")

#for ba, ba_info in breached_accounts.items():
#    print("Item number>>> ", ba)

#    for key in ba_info:
#        print(key + ': ', ba_info[key])


        

#        for key in ba_info:

            #print(ba_info[key])

#            row.append(ba_info[key])

#            if key == 'Breaches':
                #print(ba_info[key])

                #print("Hello")

 #               breaches_list = ba_info[key]

#                for breach_list in breaches_list:

                    #print(breach_list)
 #                   row.append(breach_list)

#            else:

 #               row.append(ba_info[key])

            #print(key)

