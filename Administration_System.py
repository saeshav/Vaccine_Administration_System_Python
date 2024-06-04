#SAESHAV SUBASH
#TP060888
# vaccine_code=['AF','BV','CZ','DM','EC']
vaccine_centers= ['VC1','VC2']


class newpatientregistration:
    def __init__(self):
        f = open("patients.txt", "r")
        data = f.read()
        if len(data) == 0:
            self.patient_id = 1
        else:
            self.patient_id = len(data.split('###'))
        f.close()

    def register(self):
        # patient name entry
        name= False
        while name == False:
            try:
                patient_name = input(f"Enter Patient Name: ")
                if not all(x.isalpha() or x.isspace() for x in patient_name):
                    raise ValueError
            except ValueError:
                print("Enter Alphabets Only!")
                continue
            else:
                name=True



        # patient vaccine center entry
        center = False
        while center == False:
            try:
                patient_vaccine_center = int(input(f"Enter Vaccine Center Name:\n1 : {vaccine_centers[0]} \n2 : {vaccine_centers[1]}\n"))
                if patient_vaccine_center <= 0 or patient_vaccine_center > 2:
                    raise ValueError
            except ValueError:
                print("Invalid Input, Choose the Vaccine center From 1 to 2.")
                continue
            else:
                center=True

            # patient age entry
            # I have considered the maximum age of person as 150
            age = False
            while age == False:
                try:
                    patient_age = int(input(f"Enter patient Age:[>=12 and <=150]"))
                    if patient_age <= 11 or patient_age >= 151:
                        raise ValueError
                except ValueError:
                    print("Invalid Input, Choose the age from 12 to 150.")
                    continue
                else:
                    age = True




            #patient available vaccines entry
            def available_vaccines(age):
                vaccine_code=[]
                if age>=12:
                    vaccine_code.append('AF')
                    vaccine_code.append('DM')
                if age >=18:
                    vaccine_code.append('BV')
                    vaccine_code.append('EC')
                if age>=12 and age<=45:
                    vaccine_code.append('CZ')
                return vaccine_code

            vaccine_code=available_vaccines(patient_age)

            vaccine_selection = False
            while vaccine_selection == False:
                try:
                    print("Choose From Available Vaccine As Below:")
                    for i in range(len(vaccine_code)):
                        print(f"{i} : {vaccine_code[i]}")
                    patient_vaccine_code = int(input())
                    if patient_vaccine_code < 0 or patient_vaccine_code > len(vaccine_code)-1:
                        raise ValueError
                except ValueError:
                    print(f"Invalid Input, Choose from 0 to {len(vaccine_code)-1}")
                    continue
                else:
                    vaccine_selection = True





            #patient contact number entry
            #i have considered the length of phone number as 10
            contact_number = False
            while contact_number == False:
                try:
                    patient_contact_number = int(input("Enter the Patient Contact Number(Start with 60):"))
                    if len(str(patient_contact_number)) != 11:
                        raise ValueError
                except ValueError:
                    print(f"Invalid Input, Contact Number Must be of length 11 and Start with 60")
                    continue
                else:
                    contact_number = True


            #patient email address entry
            email_number = False
            while email_number == False:
                try:
                    patient_email_number = input("Enter the Patient Email (only gmail) :")
                    if "@gmail.com" not in patient_email_number:
                        patient_email_number=patient_email_number+"@gmail.com"
                except ValueError:
                    print(f"Invalid Input")
                    continue
                else:
                    email_number = True

#complete patient record that needs to write in patients.txt
            patient_record =[self.patient_id,patient_name,vaccine_centers[patient_vaccine_center-1],patient_age,vaccine_code[patient_vaccine_code],patient_contact_number,patient_email_number]

#appending the patients.txt file

            f = open("patients.txt", "a")
            for i in range(len(patient_record)):
                f.write(str(patient_record[i]))
                if i!= len(patient_record)-1:
                    f.write("--")

            f.write("###")
            f.write("\n")
            f.close()

            f = open("vaccination.txt", "a")
            f.write(str(patient_record[0])+"--"+"D1Not"+"--"+"D2Not")
            f.write("###")
            f.close()

            print("Patient Get Successfully Registered With The Following Data: ")
            print(patient_record)





class vaccinationadministration:
    def __init__(self):
        print("")

    def vaccine_admin(self):

        # patient id entry
        def read_patient_record(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            patient_record = data.split('###')
            patient_record.pop()
            if len(patient_record) >= int(id) and not (int(id) <= 0):
                return False
            return True


        id = False
        while id == False:
            try:
                patient_id = input("Enter the Patient ID:")
                if read_patient_record(patient_id) == True:
                    raise ValueError
            except ValueError:
                print(f"Invalid ID, Patient With ID {patient_id} Does Not Exist")
                continue
            else:
                id = True


        #read dose number

        def ec_dose_checker(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            all_patients=data.split("###")
            return all_patients[int(id)-1].split("--")[4]=="EC"

        def interval_between_doses(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            all_patients = data.split("###")
            if all_patients[int(id) - 1].split("--")[4] == "EC":
                return("You Only Need 1 Dose, Your Doses are Complete.")
            elif all_patients[int(id) - 1].split("--")[4] == "AF":
                return ("You Need 1 More Dose, You Need To Come After 14 Days or 2 Weeks.")
            elif all_patients[int(id) - 1].split("--")[4] == "BV" or all_patients[int(id) - 1].split("--")[4] == "CZ":
                return ("You Need 1 More Dose, You Need To Come After 21 Days or 3 Weeks.")
            else:
                return ("You Need 1 More Dose, You Need To Come After 28 Days or 4 Weeks.")



        def patient_remaining_doses(id):
            f = open("vaccination.txt", "r")
            data = f.read()
            f.close()
            doses = []
            if len(data)==0:
                doses=['D1','D2']
                return doses
            else:
                patient_vaccine_record = data.split('###')
                patient_vaccine_record.pop()
                for i in range(len(patient_vaccine_record)):
                    doses_record = patient_vaccine_record[i].split("--")
                    if(int(doses_record[0]) == int(id)):
                        if doses_record[1] != "D1":
                            doses.append('D1')
                        if doses_record[2] != "D2":
                            doses.append('D2')
                        return doses

            doses =['D1','D2']
            return doses

        dose = False
        patient_taken_all_doses=False
        while dose == False:
            remaining_doses = patient_remaining_doses(patient_id)
            if len(remaining_doses) ==0:
                print("Patient Has Taken All Doses")
                patient_taken_all_doses=True
                dose=True


            elif ec_dose_checker(patient_id) == True:
                try:
                    if "D1" in remaining_doses:
                        print("Choose From Patient Remaining Doses :")
                        print(f"0 : {remaining_doses[0]}")
                        patient_dose_number = int(input(""))
                        if patient_dose_number !=0:
                            raise ValueError
                    else:
                        print("Patient Has Taken All the Doses")
                        patient_taken_all_doses=True
                        dose=True

                except ValueError:
                    print(f"Invalid Dose Number, Valid Dose Numbers is 0 ")
                    continue
                else:
                    dose = True


            else:
                try:
                    print("Choose From Patient Remaining Doses :")
                    for i in range(len(remaining_doses)):
                        print(f"{i} : {remaining_doses[i]}")
                    patient_dose_number = int(input(""))
                    if len(remaining_doses) ==2 and patient_dose_number == 0:
                        print(interval_between_doses(patient_id))

                    if patient_dose_number >= len(remaining_doses) or patient_dose_number < 0 or (len(remaining_doses) ==2 and patient_dose_number==1):
                        raise ValueError
                except ValueError:
                    if len(remaining_doses) == 2 and patient_dose_number == 1 :
                        print("You Need to Complete Dose1 First")
                    else:
                        print(f"Invalid Dose Number, Valid Dose Numbers Are From 0 to {len(remaining_doses) - 1} ")
                    continue
                else:
                    dose = True

        complete_vaccine_record=[patient_id]
        print("Patient Doses Get Updated Successfully")

        if patient_taken_all_doses == False:
            if (remaining_doses[patient_dose_number] == "D1"):
                complete_vaccine_record.append("D1")
                complete_vaccine_record.append("D2Not")
            if (remaining_doses[patient_dose_number] == "D2"):
                complete_vaccine_record.append("D1")
                complete_vaccine_record.append("D2")

            # search the vaccination.txt if patient does not exist then append the record otherwise update the record of doses

            f = open("vaccination.txt", "r")
            data = f.read()
            f.close()
            updated_doses_record = []
            record_found = False
            all_patients_doses_record = data.split("###")
            all_patients_doses_record.pop()
            for i in range(len(all_patients_doses_record)):
                patient_dose_record = all_patients_doses_record[i].split("--")

                if (int(patient_dose_record[0]) == int(patient_id)):
                    record_found = True
                    new_record = str(complete_vaccine_record[0]) + "--" + complete_vaccine_record[1] + "--" + \
                                 complete_vaccine_record[2]
                    updated_doses_record.append(new_record)
                else:
                    updated_doses_record.append(all_patients_doses_record[i])

            # append the record if not found
            if record_found == False:
                f = open("vaccination.txt", "a")
                for i in range(len(complete_vaccine_record)):
                    f.write(str(complete_vaccine_record[i]))
                    if i != len(complete_vaccine_record) - 1:
                        f.write("--")
                f.write("###")
                f.close()
            elif record_found == True:
                f = open("vaccination.txt", "w")
                for i in range(len(updated_doses_record)):
                    f.write(updated_doses_record[i])
                    f.write("###")
                f.close()





class searchthepatient:
    def __init__(self):
        print("")

    def search(self):
        # patient id entry
        def search_patient_record(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            patient_record = data.split('###')
            patient_record.pop()
            if len(patient_record) >= int(id) and not (int(id) <= 0):
                return False
            return True

        id = False
        while id == False:
            try:
                patient_id = input("Enter the Patient ID:")
                if search_patient_record(patient_id) == True:
                    raise ValueError
            except ValueError:
                print(f"Invalid ID, Patient With ID {patient_id} Does Not Exist")
                continue
            else:
                id = True

        def patient_by_id(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            all_patients = data.split("###")
            return all_patients[int(id) - 1]

        def vaccine_by_id(id):
            f = open("vaccination.txt", "r")
            data = f.read()
            f.close()
            all_patients_vaccination = data.split("###")
            all_patients_vaccination.pop()
            for i in range(len(all_patients_vaccination)):
                individual_patient_record = all_patients_vaccination[i].split("--")
                if int(individual_patient_record[0]) == int(id):
                    return individual_patient_record
            return "not found"

        patient_data=patient_by_id(patient_id)
        vaccine_data=vaccine_by_id(patient_id)
        print("-------------------------------")
        print("Record of Patient is as Below:")
        print("-------------------------------")
        patient_data=patient_data.split("--")
        print(f"Patient ID:{patient_data[0]}\nPatient Name:{patient_data[1]}\nPatient Vaccine Center:{patient_data[2]}\nPatient Age:{patient_data[3]}\nPatient Selected Vaccine:{patient_data[4]}")
        print(f"Patient Phone Number:{patient_data[5]}\nPatient Email:{patient_data[6]}\n")

        print("-------------------------------")
        print("Patient Vaccine Record is as Below:")
        print("-------------------------------")
        if patient_data[4] == "EC":
            if vaccine_data[1]=="D1":
                print(f"Vaccine Dose Status:Completed")
            else:
                print(f"Vaccine Dose Status:Not Completed")
        else:
            first_dose_status= "Completed" if vaccine_data[1]=="D1" else "Not Completed"
            second_dose_status = "Completed" if vaccine_data[2] == "D2" else "Not Completed"
            print(f"First Vaccine Dose Status:{first_dose_status}\nSecond Vaccine Dose Status:{second_dose_status}")




class statisticofcenter:
    def __init__(self):
        print("")

    def stat(self):
        def patients_per_center():
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            all_patients = data.split("###")
            all_patients.pop()
            center_stats=[0,0]
            for i in range(len(all_patients)):
                individual_patients=all_patients[i].split("--")
                if(individual_patients[2] == "VC1"):
                    center_stats[0]=center_stats[0]+1
                else:
                    center_stats[1]=center_stats[1]+1
            return center_stats

        def ec_dose_checker(id):
            f = open("patients.txt", "r")
            data = f.read()
            f.close()
            all_patients=data.split("###")
            return all_patients[int(id)-1].split("--")[4] == "EC"

        def patients_waiting_per_doses():
            f = open("vaccination.txt", "r")
            data = f.read()
            f.close()
            all_patients = data.split("###")
            all_patients.pop()
            vaccine_centers_stats = [0, 0 , 0]
            for i in range(len(all_patients)):
                individual_patients=all_patients[i].split("--")
                print (individual_patients[0])
                if ec_dose_checker(individual_patients[0]) == True:
                    if individual_patients[1] == "D1":
                        vaccine_centers_stats[2]=vaccine_centers_stats[2]+1
                    else:
                        vaccine_centers_stats[0]=vaccine_centers_stats[0]+1
                else:
                    if individual_patients[1] == "D1" and individual_patients[2] == "D2":
                        vaccine_centers_stats[2]= vaccine_centers_stats[2]+1
                    else:
                        if individual_patients[1] == "D1" and individual_patients[2] !="D2":
                            vaccine_centers_stats[1] =vaccine_centers_stats[1]+1
                        elif individual_patients[1] != "D1" and individual_patients[2] != "D1":
                            vaccine_centers_stats[0]=vaccine_centers_stats[0]+1


            return vaccine_centers_stats

        center_stats=patients_per_center()
        vaccine_stats=patients_waiting_per_doses()
        print("----------------------------")
        print("Vaccine Center Statistics: ")
        print("----------------------------")
        print(f"Patients Get Registered in Vaccine Centre 1 is as Follows:{center_stats[0]}")
        print(f"Patients Get Registered in Vaccine Centre 2 is as Follows:{center_stats[1]}")

        print("----------------------------")
        print("Waiting Patient Stats Per Doses: ")
        print("----------------------------")
        print(f"Patients Waiting For First Dose are :{vaccine_stats[0]}")
        print(f"Patients Waiting For Second Dose are :{vaccine_stats[1]}")
        print(f"Patients Completed their Vaccine are :{vaccine_stats[2]}")





def callrespectivefunction(number):
    if number == 1:
        newpatient = newpatientregistration()
        newpatient.register()

    elif number == 2:
        vacc_adm = vaccinationadministration()
        vacc_adm.vaccine_admin()

    elif number == 3:
        search_patient = searchthepatient()
        search_patient.search()

    elif number == 4:
        statistics = statisticofcenter()
        statistics.stat()


mainloop = True
while mainloop:
    print(f"------------------------------\nWelcome to Vaccination Center:\n------------------------------\n")
    print(f"Please Select One of the Options Below:")
    print(
        f"1 : New Patient Registration\n2 : Vaccine Administration\n3 : Search For Patient \n4 : Statistical Record Of Patients\n5 : Exit The Program ")
    try:
        number = int(input(f"========================================"))
        if number <= 0 or number > 5:
            raise ValueError
    except ValueError:
        print("Invalid Input, Enter the Number From 1 to 5.")
        continue

    if number == 5:
        mainloop = False
    else:
        callrespectivefunction(number)



