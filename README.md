# EmailPwnCheckerbot
Automated python selenium script for checking if the given list of mail ids, have appeared in any data breaches.


> The python script, automates the process of checking for email id's appearing in data breaches, by visiting the firefox monitor site and entering in every email id in the given csv file and checking for breaches, if breach is found, the bot creates a new csv file with list and details of all breached email ids.

---

> Clone or Download the project, and switch to the directory and create a python environment.
> Then run the command `pip install -r requirements.txt` to download the needed packages.
> Also check the selenium documentation page to ensure, your system has the needed browser driver.

> The script takes in one required argument of file path to the csv file containing the list of email id's.
> Also takes in another optional argument of file path towards an output csv file to be generated.

> The bot is run by : `python3 script.py emails_list.csv` 
> The above command only contains single argument that of the input file, the script will read through every email in the file and will do the checking.
> Ones the check is completed the script will generate a new default csv file.

> To pass in the output file `python3 script.py emails_list.csv breached_accounts.csv`
> The above command contains two arguments, the input file and the output file. 
> After the check if completed the bot will generate a new csv file in the mentioned file path the details of all breached emails.

> If no commands are provided `python3 script.py`
> The script will end with a print statement stating to add the neccessary arguments.

---

> This is a personal project i came up with while learning python selenium web automation. The automation is done based on my own workflow and environment i work in. You are free to go ahead and look through the repo and make changes according to your workflow.
