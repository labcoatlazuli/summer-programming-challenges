while True:
    ask for a username
    try 
        opening a file called userdata.txt in read mode, assign to file object user_data
        set a list called user_data_list to every single line in user_data
        remove newline characters from user_data_lsit
        for every single element in user_data_list:
            if the index of the element is even then append it to a list called username_list
            else append it to a list called password_list
        if the username they entered is in username_list
            set a variable called table_password to the corresponding password of the username entered
        else
            tell the user that their username was not found
            continue to the beginning of the loop
    except if the file cannot be found
        tell the user that userdata.txt cannot be found in the working directory and that the program will exit
        exit the program
    
    ask for their old password, set to a variable called old_password
    if table_password from userdata.txt does not match old_password
        tell the user that they did not enter the right password
        continue to beginning of loop
    
    set a list called easy_words to 123456, password, and the username
    set a variable called trust_rating to 0 as integer
    ask the user for a new password, set to a variable called new_password
    check whether the password is in the easy_words list
    if it is then say that your password is too common, or it is the same as their username
        continue to the beginning of the loop
    
    if the length of their new password is more than 7 and it is not completely upper or lowercase
        ask the user for their new password again
        if it matches the first time they entered it
            tell the user that their password has now been changed
        
            set the relevant password in password_list to new_password
            open a file called userdata.txt in write mode as a file object called user_data
            for count in a list of sequential numbers starting from zero to the length of username_list
                write in the file the element of username_list at index count and a newline character
                write in the file the element of password_list at index count and a newline character
            flush the write buffer to make sure that all of it gets written to the file
            
            if the length of new_password is less than 10
                add 1 to trust_rating
            else if the length of new_password is less than 12
                add 2 to trust_rating
            else
                add 3 to trust_rating
            
            if new_password has special characters
                add 2 to trust_rating
            if trust_rating is less than 2
                tell the user that their password is weak
            else if trust_rating is less than 4
                tell the user that their password is medium strong
            else
                tell the user that their password is very secure
                
            break out of the loop
        else
            tell the user that their new password does not match the first time they entered it
            continue to the beginning of the loop
    else
        tell the user that their password needs to be at least 8 characters long and must have 
