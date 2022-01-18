import datetime

#  function for controlling the data in txt file
def user_info(ussnm, pssd): 
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()

#  function for controlling sign-up
def signup():
    print("\n--------- New User Registration --------\n")
    username = input("Please enter your username : ")
    username = str(username)
    password = input("Please create a password : ")
    password = str(password)
    user_info(username, password)
    print("Signup Completed. Proceed to login")
    login()

#  function for controlling login
def login():
    print("\n--------- User Login --------\n")
    user_nm = input("Enter the username here : ")
    user_nm = str(user_nm)

    #same password while signup
    pass_wrd = input(("Enter Password : "))+'\n'
    pass_wrd = str(pass_wrd)
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')

        #read file for the entered password
        k = f_.readlines(0)[0]
        f_.close()

        #checking if the entered password is correct
        if pass_wrd == k :
            print("\n-------- Action Menu -------\n")
            print("1--VIEW DATA \n2--ADD TASK \n3--UPDATE TASK \n4--VIEW TASK STATUS\n")
            

            #storing the input from the above menu in 'a'
            a = int(input("select an action : "))
            if a == 1:
                view_data(usernm)
            elif a == 2:
                task_add(usernm)
            elif a == 3:
                update_task(usernm)
            elif a == 4:
                view_task_status(usernm)
            else :print("Wrong input")
        else :
            print("------- incorrect details -------")
            login()

    except Exception as e:
        print(e)
        login()

#function to view data of user
def view_data(username) :
    ff = open(username, 'r')     #opening the file with user data
    print(ff.read())          #reading the file with user data
    ff.close()             #closing the file with user data
    login()


#function to add tasks to a user
def task_add(username) :
    print("Enter the number of tasks u want to add : ")
    j = int(input())
    f1 = open(username, 'a')

    for i in range(1, j+1):
        task = input("Enter the task details : ")
        deadline = input("Enter the deadline : ")
        pp = "TASK "+str(i)+' :'
        qq = "TARGET "+str(i)+" :"
         
        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(deadline)
        f1.write('\n')
        print("press 'spacebar to stop adding tasks and save' or press 'enter' : ")
        l = input()
        if l == ' ':
            break
    
    f1.close()
    login()
        
#function to update the tasks for a user
def update_task(username):
    username = username+" task.txt"
    print("Please enter the completed task : ")
    task_completed = input()
    print("Please enter the pending task : ")
    task_pending = input()
    print("Please enter the ongoing task : ")
    task_ongoing = input()
    
    #writing the updated information on the txt file
    fw = open(username, 'a')
    dt = str(datetime.datetime.now())

    fw.write(dt)
    fw.write("Completed task : ")
    fw.write(task_completed)
    fw.write("\nPending task : \n")
    fw.write(task_pending)
    fw.write("\nOngoing task : \n")
    fw.write(task_ongoing)
    print("------- Tasks Updated successfully --------")
    login()


#function to view task status
def view_task_status(username):
    ussnm = username+" task.txt"
    m = open(ussnm, 'r')
    print(m.read(ussnm))
    m.close()
    login()


# main function for controlling login and sign-up
if __name__ == '__main__':
    print("WELCOME TO MY TASK MANAGER")
    print("are you a new user")
    a = int(input("Type 1 for YES and 0 for NO :: "))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input!")