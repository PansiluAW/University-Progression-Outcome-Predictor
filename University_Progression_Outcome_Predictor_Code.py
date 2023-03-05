# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210021 (IIT) / w19127880 (UoW)
# Date: 05/04/2022
#---------------------------------------------------------------------------------------------

#functions
def complete_main(repeat_option):
    "this is for the main program with the horizontal histogram."
    main(repeat_option)    #callout main() function
    
    if repeat_option != "1": #display data processed in the main() function in a horizontal histogram
        print("------------------------------------------------------------------------------\nHorizontal Histogram\nProgress",progress_count,"\t:","*"*progress_count,"\nTrailer",trailer_count,"\t:","*"*trailer_count,"\nRetriever",retriever_count,"\t:","*"*retriever_count,"\nExclude",exclude_count,"\t:","*"*exclude_count,"\n")
        print(progress_count+trailer_count+retriever_count+exclude_count,"outcome(s) in total.\n------------------------------------------------------------------------------")
       
def main(repeat_option):# "repeat_option" variable as an argument for choosing between student version and staff version
    "this is for the main program."
    #access global variables
    global pass_credits
    global defer_credits
    global fail_credits
    global progress
    global trailer
    global retriever
    global exclude
    global progress_count
    global trailer_count
    global retriever_count
    global exclude_count
    global progress_list
    global trailer_list
    global retriever_list
    global exclude_list
    #create variables
    pass_credits_inp = 0
    defer_credits_inp = 0
    fail_credits_inp = 0
    data = ()
    range_error_message = "Out of range!!. Please try again.\n"

    while True:     #get values from the user, loop until user gives integer inputs by error handling
        #check validity of the values inputted by the user and process accordingly
        try:
            pass_credits_inp = (int(input("Please enter the credits at pass : ")))
            if not(pass_credits_inp%20 == 0 and 0<=pass_credits_inp<=120):
                print(range_error_message)
                continue
            defer_credits_inp = (int(input("Please enter the credits at defer : ")))
            if not(defer_credits_inp%20 == 0 and 0<=defer_credits_inp<=120):
                print(range_error_message)
                continue
            fail_credits_inp = (int(input("Please enter the credits at fail : ")))
            if not(fail_credits_inp%20 == 0 and 0<=fail_credits_inp<=120):
                print(range_error_message)
                continue
            
        except ValueError:
            print("Integer required !!. Please try again.\n") #print-out the appropriate error message for invalid inputs
            continue
        
        else:
            if (pass_credits_inp+defer_credits_inp+fail_credits_inp) == 120:        #check if the total is equal to 120 and process accordingly
                data = (pass_credits_inp,defer_credits_inp,fail_credits_inp)
                if data == progress:                 #check progression outcomes according to the inputted values and process accordingly
                    progress_count += 1
                    progress_list.append(data)
                    print("Progress")
                elif data in trailer:
                    trailer_count += 1
                    trailer_list.append(data)
                    print("Progress (module trailer)")
                elif data in retriever:
                    retriever_count += 1
                    retriever_list.append(data)
                    print("Module retriever")
                elif data in exclude:
                    exclude_count += 1
                    exclude_list.append(data)
                    print("Exclude")
            else:
                print("\nTotal incorrect !!. Please try again.\n")
                continue
        if repeat_option == "2":          #repeat process according to user preference
            repeat = str(input("\nWould you like to enter another set of data ? \nEnter 'y' for yes or 'q' to quit and view results : "))
            if repeat.lower() ==  "y":
                continue
            elif repeat.lower() ==  "q":
                break
            else:
                print("Invalid input!!. Proceeded to quit the program.") #print-out the appropriate error message for invalid inputs
                break
        else:
            break
def vertical_histogram(repeat_option):
    "this is for displaying the vertical histogram."
    main(repeat_option)     #call main(function)
    
    #create varibales and assign values
    count1 = progress_count
    count2 = trailer_count
    count3 = retriever_count
    count4 = exclude_count
    white_space = "             "
    #display vertical histogram labels and data
    print("\nProgress",progress_count,"| Trailer",trailer_count,"| Retriever",retriever_count,"| Excluded",exclude_count)
    for count in range (0,max(progress_count,trailer_count,retriever_count,exclude_count)):
        print()
        if count1!=0:
            print("   *",end= white_space)
            count1 -= 1
        else:
            print("    ",end= white_space)
            
        if count2!=0:
            print("*",end= white_space)
            count2 -= 1
        else:
            print(" ",end= white_space)
            
        if count3!=0:
            print("*",end= white_space)
            count3 -= 1
        else:
            print(" ",end= white_space)
            
        if count4!=0:
            print("*",end= white_space)
            count4 -= 1
        else:
            print(" ",end= white_space)
    print("\n\n",(str(progress_count+trailer_count+retriever_count+exclude_count)+" outcome(s) in total").center(78,"-"),"\n")
    
def main_with_listed_histogram(repeat_option):
    "This is for displaying the data inputted that categorized into their relevant outcome progression category"
    #accessing global variables
    global progress_list
    global trailer_list
    global retriever_list
    global exclude_list

    complete_main(repeat_option)     #calling out the complete_main() function
    
    #display data after looping for the maximum cycles that it needs to display all data
    if repeat_option == "1": #for displaying the only result in the student version in a listed histogram.
        print()
        print("Result".center(28,"_"),"\n")
        
    for count in range(len(progress_list)):
        print("Progress - ",str(progress_list[count]).strip("()"))
    for count in range(len(trailer_list)):
        print("Progress (Module Trailer) - ",str(trailer_list[count]).strip("()"))
    for count in range(len(retriever_list)):
        print("Module Retriever - ",str(retriever_list[count]).strip("()"))
    for count in range(len(exclude_list)):
        print("Exclude - ",str(exclude_list[count]).strip("()"))

def main_with_saving_data(repeat_option):
    "this is to store processed data that were categorized into progression outcomes into text file and retrieve"
    #accessing gloabl variables
    global progress_list
    global trailer_list
    global retriever_list
    global exclude_list
    complete_main(repeat_option)     #calling out the complete_main() function
    file = open("savedata.txt","w") #save data to a text file
    #save data in the apropriate format for relevent progression outcomes
    for count in range(len(progress_list)):
        file.write("Progress - "+str(progress_list[count]).strip("()")+"\n")
    for count in range(len(trailer_list)):
        file.write("Progress (Module Trailer) - "+str(trailer_list[count]).strip("()")+"\n")
    for count in range(len(retriever_list)):
        file.write("Module Retriever - "+str(retriever_list[count]).strip("()")+"\n")
    for count in range(len(exclude_list)):
        file.write("Exclude - "+str(exclude_list[count]).strip("()")+"\n")
    file.close()

def retrieve_data():
    "this is to retrieve data from the text file"
    file = open("savedata.txt","r")     #open file "savedata.txt" fro retrieving previously stored data
    
    print("DATA SAVED".center(78," "))
    print("-"*78)
    for line in file:   #loop through each line saved to display
        print(line.rstrip("\n"))

while True:    
    #create variables
    repeat_option = ""
    rerun_program = ""
    pass_credits = []
    defer_credits = []
    fail_credits = []
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0
    progress_list = []
    trailer_list = []
    retriever_list = []
    exclude_list = []
    #values of each progression outcome assigned into seperate variables
    progress = (120,0,0)
    trailer = ((100,20,0),(100,0,20))
    retriever = ((80,40,0),(80,20,20),(80,0,40),(60,60,0),(60,40,20),(60,20,40),(60,0,60),(40,80,0),(40,60,20),(40,40,40),(40,20,60),(20,100,0),(20,80,20),(20,60,40),(20,40,60),(0,120,0),(0,100,20),(0,80,40),(0,60,60))
    exclude = ((40,0,80),(20,20,80),(20,0,100),(0,40,80),(0,20,100),(0,0,120))

    print("Select one option to proceed ;\n\t1 ~ Part 1 - Main Version.\n\t2 ~ Part 2 - Vertical Histogram.\n\t3 ~ Part 3 - List/Tuple/Directory .\n\t4 ~ Part 4 - Text File.")     #display menu select the required part of the program to approach
    
    #get options from the user
    option = str(input("\n\n    Enter option (1 to 4),\n    >>>> ")) #gets input for choosing menu options
    repeat_option = str(input("\n    Please select your prefered version... \n\t1.Student Version.\n\t2.Staff Version (for multiple students' data inputs).\n\n\tEnter option (1 or 2)\n\t>>>> ")) #gets option for choosing between student version and staff version

    if repeat_option == "1" or repeat_option == "2":
        if repeat_option == "1" and option != "":
            print("\n","Student Version".center(25,"_"),"\n")
        elif repeat_option == "1" and option != "":
            print("\n","Staff Version".center(25,"_"),"\n")
        #process according to the user choice
        if option == "1":
            complete_main(repeat_option)
        elif option == "2":
            vertical_histogram(repeat_option)
        elif option == "3":
            main_with_listed_histogram(repeat_option)
        elif option == "4":
            main_with_saving_data(repeat_option)
            retrieve_data()
        else:
            print("Invalid input!!. Please re-run to try again.") #print-out the appropriate error message for invalid inputs
        rerun_program = input("\nDo you want to rerun the university progression prediction program ? ('y' for yes / 'n' for no) : ")
        if rerun_program.lower() == "y":
            continue
        elif rerun_program.lower() == "n":
            print("_"*42)
            print("\n",".Thank you for using the program.".center(40,"_"))
            break
        else:
            print("Invalid input!!.Program proceeded to quit option.") #print-out the appropriate error message for invalid inputs
            print("_"*42)
            print("\n",".Thank you for using the program.".center(40,"_")) #printout end message of the program after proceeded to quit.
            break
    else:
        print("Invalid Inputs!!.") #print-out the appropriate error message for invalid inputs
