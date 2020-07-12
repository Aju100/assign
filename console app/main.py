import sys
class students():
    name:str
    age:int
    student_id:int
    address:str
    phone_number:str
    registerDate:str
    courses_in_withprice={}
    courses_and_price = {
    'Fullstack Js':20000,
    'Python and Django':20000,
    }
    # function to save a student information into a file
    def save(self):
        file = open('student_info.txt','a')
        file.write(self.name+',')
        file.write(str(self.age)+',')
        file.write(self.address+',')
        file.write(self.student_id+',')
        file.write(self.phone_number+',')
        file.write(self.registerDate+',')
        no_of_course = self.courses_in_withprice.keys()
        temp_course_fees = 0
        for _ in no_of_course:
            temp_course_fees = self.courses_in_withprice.get(_)
            file.write(_+',')
            file.write(temp_course_fees+',')

        file.write('\n')
        file.close()

def add_new_student():
    print('Enter Student Credentials: ')
    temp_obj = students()
    temp_name = input("Enter Name: ")
    temp_obj.name = temp_name
    temp_age = input("Enter Age: ")
    temp_obj.age = temp_age
    temp_registerdate = input("Enter registration date: ")
    temp_obj.registerDate = temp_registerdate
    temp_address = input("Enter address:")
    temp_obj.address = temp_address
    temp_student_id = input("Enter ID: ")
    temp_obj.student_id = temp_student_id
    temp_phone_no = input("Enter your Phone number: ")
    temp_obj.phone_number = temp_phone_no

    print("Enter the number of course :")
    temp_decision = input("Enter: ")
    for _ in range(0,int(temp_decision)):
        temp_course_name = input("Enter course name: ")
        temp_course_price = input("enter course fees:")
        temp_obj.courses_in_withprice[temp_course_name] = str(temp_course_price)

    print("Are u sure to make this ?")
    print("Yes or No")
    temp_decision = input("Enter: ")
    if(temp_decision.lower()=='yes'):
        temp_obj.save()
        print("Success")
        return temp_obj
    else:
        print("Entry process is terminated")
        return 0

def read_previous_students():
    file = open("student_info.txt","r")
    student_list = []

    for _ in file.readlines():
        temp_str = _
        student_list.append(temp_str)
        temp_str = 0

    file.close()
    return student_list

def students_search(students_list,actual_name):
    for _ in students_list:
        if(_.name == actual_name):
            print('---------------------------------------------')
            print('Name: '+_.name)
            print('Age:'+_.age)
            print('registration date'+_.registerDate)
            print('address'+_.address)
            print('student no'+_.phone_number)
            print('---------------------------------------------')
            print('\n')
    return 0

def students_complete_information(students_list):
    for _ in students_list:
        print('--------------------------------------------------')
        print('Name: '+_.name)
        print('Age: '+_.age)
        print('Registration Date: '+_.registerDate)
        print('Address :'+_.address)
        print('Phone Number: '+_.phone_number)
        print('---------------------------------------------')
    return 0

def recreating_student_Object(students_info):
    temp_list=[]
    obj_list=[]
    temp_obj:object

    for _ in students_info:
        temp_list=_.split(",")
        temp_obj=students()
        temp_obj.name=temp_list[0]
        temp_obj.age=temp_list[1]
        temp_obj.address=temp_list[2]
        temp_obj.registerDate=temp_list[3]
        temp_obj.phone_number=temp_list[5]
        obj_list.append(temp_obj)

    return obj_list

def cancel_student(student_list,std_name):
    list_index=0
    k=0
    std_temp_list=[]
    for _ in student_list:
        if(_.name==std_name):
            break
        list_index=list_index+1

    #print((student_list[0].name))
    file=open('student_info.txt','w')
    for _ in range(0,len(student_list)):

        if(j!=list_index):
            file.write(student_list[_].name+',')
            file.write(str(student_list[_].age)+',')
            file.write(student_list[_].address+',')
            file.write(student_list[_].registerDate+',')
            file.write(student_list[_].phone_number+',')
            file.write('\n')


    filename.close()
    return  0

def update_student_info(student_list,std_name):
    list_index=0
    k=0
    std_temp_list=[]
    for _ in student_list:
        if(_.name==std_name):
            #Enter Data
            print("Enter 1)Change Name \n 2)Change Age \n 3)Change Entry Date \n 4)Change Fathername \n 5)Change Address \n 6)Change Phone No \n 7)Change Parent Phone no \n 8)Update Course")
            temp_decision_2=input("Enter: ")
            print('Enter Student Credentials: ')
            #temp_obj=students()

            if(temp_decision_2=='1'):
                temp_name=input("Enter Name: ")
                _.name=temp_name
            elif(temp_decision_2=='2'):
                temp_age=input("Enter Age: ")
                _.age=temp_age
            elif(temp_decision_2=='3'):
                temp_entry=input("Enter Entry Date Of Student in MM/DD/YY Format : ")
                _.entry=temp_entry
            elif(temp_decision_2=='4'):
                temp_father_name=input("Enter Father Name: ")
                _.father_name=temp_father_name
            elif(temp_decision_2=='5'):
                temp_address=input("Enter adderss: ")
                _.address=temp_address
            elif(temp_decision_2=='6'):
                temp_phone_no=input("Enter Student Phone No: ")
                _.personal_phone_no=temp_phone_no
            elif(temp_decision_2=='7'):
                temp_parent_phone_no=input("Enter Parent Phone No: ")
                _.parent_phone_no=temp_parent_phone_no

            elif(temp_decision_2=='8'):
                print("Enter Number Of Course To Enter: ")
                temp_decision=input("Enter: ")
                for _ in range(0,int(temp_decision)):
                    temp_course_name=input("Enter Course Name :")
                    temp_course_price=input("Enter Course Fees: ")
                    _.courses_in_withprice[temp_course_name]=str(temp_course_price)

        #list_index=list_index+1

    #print((student_list[0].name))
    filename=open('student_info.txt','w')
    for _ in range(0,len(student_list)):
        filename.write(student_list[_].name+',')
        filename.write(str(student_list[_].age)+',')
        filename.write(student_list[_].address+',')
        filename.write(student_list[_].registerDate+',')
    #    filename.write(student_list[j].father_name+',')
    #    filename.write(student_list[j].personal_phone_no+',')
        filename.write(student_list[_].phone_number+',')
        filename.write('\n')
    filename.close()
    return 0

students_list=read_previous_students()
#obj_list=edit_info_student(students_list)
obj_list=recreating_student_Object(students_list)



# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white

def banner():
    print("""%s
.___ __      __     _____                     .___
|   /  \    /  \   /  _  \   ____ _____     __| _/____   _____ ___.__.
|   \   \/\/   /  /  /_\  \_/ ___\\__  \   / __ |/ __ \ /     <   |  |
|   |\        /  /    |    \  \___ / __ \_/ /_/ \  ___/|  Y Y  \___  |
|___| \__/\  /   \____|__  /\___  >____  /\____ |\___  >__|_|  / ____|
           \/            \/     \/     \/      \/    \/      \/\/%s%s
           # Coded by Aju Tamang
           """%(R,W,Y))

banner()

def main():
    for i in range(0,6):
        print(' Select Option:\n 1) Register \n 2) View Students Complete Details \n 3) Search student by Name\n 4) Cancel registration\n 5) Update Info')
        temp_decision = input("\n Enter any option:")
        if(temp_decision=='1'):
            temp_obj=add_new_student()
        #elif(temp_obj=='2'):
        #    complete_info_student(obj_list)
        elif(temp_decision=='2'):
            students_complete_information(obj_list)
        elif(temp_decision=='3'):
            temp_name=input('Enter Name to Search Student: ')
            students_search(obj_list,temp_name)
        elif(temp_decision=='4'):
            temp_name=input('Enter Name to Cancel Student: ')
            cancel_student(obj_list,temp_name)
        elif(temp_decision=='5'):
            temp_name=input('Enter Name to Update student: ')
            update_student_info(obj_list,temp_name)
        else:
            print("No Such Fucntionality Yet")
        students_list=read_previous_students()
        obj_list=recreating_student_Object(students_list)
        print('\n')
        print('#####################################################')
        print('\n')
        print("""\
    ~~~ Thank You for using IW Academy!
                       ~ \033[1;94m@Aju Tamang\033[0m
        """)

if __name__ == '__main__':
    main()
