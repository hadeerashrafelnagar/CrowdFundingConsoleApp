# Crowd-Funding console app

'''Crowdfunding is the practice of funding a project or venture by raising small
amounts of money from a large number of people, typically via the Internet.
Crowdfunding is a form of crowdsourcing and alternative finance. In 2015,
over US$34 billion was raised worldwide by crowdfunding.'''

# The aim of the project: Create a console app to start fundraise projects.

# projects part

import datetime

# helper functions


# function for project name validation

def namevalidation():
    projectname = input("enter your project name : ").strip().lower()
    while True:
        if projectname.isalpha():
            break
        else:
            print("enter your project name without spaces or digits")
            projectname = input("enter your project name : ").strip().lower()
    return projectname

# function for project description validation

def descvalidation():
    projectdescription = input("enter project decription : ").strip().lower()
    while True:
        if projectdescription.isalpha():
            break
        elif projectdescription == " ":
            print("cannot be empty")
            projectdescription = input(
                "enter project decription : ").strip().lower()
        else:
            print("enter project decription without symbols or number , just use ','")
            projectdescription = input(
                "enter project decription : ").strip().lower()
    return projectdescription

# function for project total target validation

def targetnumvalidation():
    while True:
        target = int(input("please enter your total target : "))
        if target >= 1000:
            break
        else:
            print("please enter target number above 1000")
            target = input("please enter your total target : ")
    return target

# function for project start and end date validation

def datevalidation():
    while True:
        try:
            projectstartDate = input(
                "enter project start date in 'dd-mm-yy' format : ").split('-')
            projectendDate = input(
                "enter project end date in 'dd-mm-yy' format : ").split('-')
            projectstartDate = datetime.datetime(int(projectstartDate[2]), int(
                projectstartDate[1]), int(projectstartDate[0]))
            try:
                projectendDate = datetime.datetime(int(projectendDate[2]), int(
                    projectendDate[1]), int(projectendDate[0]))
            except:
                print("input date is not valid...")
                break
        except:
            print("input date is not valid...")
            break
        else:
            if projectstartDate < projectendDate:
                return [projectstartDate, projectendDate]
            else:
                print("input date is not valid...")
                break
    return [projectstartDate, projectendDate]

# function for project editing fields validation

def fieldvalidation(id, line):
    editedline = []
    fields = ["name", "description",
              "target", "startdate", "enddate"]
    editedfield = input(
        "enter the field name to be edited from [ 'name', 'description','target', 'startdate', 'enddate'] :").strip().lower()
    if editedfield in fields:
        if editedfield == "name":
            projectname = namevalidation()
            line[1] = projectname
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "description":
            projectdescription = descvalidation()
            line[2] = projectdescription
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "target":
            target = str(targetnumvalidation())
            line[3] = target
            editedline.append(line)
            print("editing field")
            return editedline[0]
        elif editedfield == "startdate" or editedfield == "enddate":
            projectstartDate = str(datevalidation()[0])
            projectendDate = str(datevalidation()[1])
            line[4] = projectstartDate
            line[7] = projectendDate
            editedline.append(line)
            print("editing field")
            return editedline[0]
    else:
        print("no available field")

# main functions

# function creating a project

def createproject(id):

    projectname = namevalidation()

    projectdescription = descvalidation()

    target = targetnumvalidation()

    projectstartDate = datevalidation()[0]

    projectendDate = datevalidation()[1]

    print("creating project")

    print(
        f" project name : {projectname} \n project description : {projectdescription} \n project total target : {target} \n project start date : {projectstartDate} \n project end date : {projectendDate} ")

    with open("projects.txt", 'a') as projectsfile:
        projectsfile.writelines(
            [f"{id}:{projectname}:{projectdescription}:{target}:{projectstartDate}:{projectendDate} \n"]
        )

# function deleteing a project

def deleteproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input(
            "enter your project name to be deleted : ").strip().lower()
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    print("deleting project")
                else:
                    restfile += line    
            else:
                print("you don't have any projects to be deleted ")
                restfile += line    
                break
        return restfile

# function viewing projects

def viewproject():
    projectsfile = open("projects.txt", 'r')
    for line in projectsfile:
        print(line)


# function edit a project

def editproject(id):
    while True:
        projectsfile = open("projects.txt", 'r')
        restfile = ""
        projectname = input(
            "enter your project name to be edited : ").strip().lower()
        for line in projectsfile.readlines():
            if id in line:
                if line.split(":")[1] == projectname:
                    editedline = fieldvalidation(id, line.split(":"))
                    editedline = ":".join(editedline)
                    restfile += editedline
                    print("editing file")
                else:
                    restfile += line
            else:
                print("you don't have any projects to be edited ")
                restfile += line
        return restfile

# function to handle all the above

def projects(id):
    while True:
        choice = int(input(
            "for create projects enter 1       or       for edit projects enter 2       or       for delete projects enter 3       or       for view projects enter 4       or       for exit 5  : "))
        try:
            choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5
        except:
            print("something went wrong")
        else:
            if choice == 1:
                try:
                    createproject(id)
                except:
                    print("something went wrong")
            elif choice == 2:
                try:
                    edit = editproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(edit)
            elif choice == 3:
                try:
                    delete = deleteproject(id)
                except:
                    print("something went wrong")
                else:
                    with open("projects.txt", 'w') as projectsfile:
                        projectsfile.writelines(delete)
            elif choice == 4:
                print("viewing projects")
                try:
                    viewproject()
                except:
                    print("something went wrong")
            elif choice == 5:
                print("ok bye bye , hope to see you soon")
                break
            else:
                print("invalid choice")
