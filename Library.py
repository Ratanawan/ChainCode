student = { 1 : {'user_name' : 'WANN', 'password' : '111'},
            2 : {'user_name' : 'SOTHEA', 'password' : '222'},
            3 : {'user_name' : 'LYNAN', 'password' : '333'},
            4 : {'user_name' : 'SENGHAK', 'password' : '444'},
            5 : {'user_name' : 'PANHA', 'password' : '555'},
            6 : {'user_name' : 'OUDOM', 'password' : '666'}
          }

book = { 1 : 'Harry Potter and the Soccerer stone',
         2 : 'Harry Potter and the Chamber of Secret',
         3 : 'Harry Potter and the Prisoner of Azkaban',
         4 : 'Harry Potter and the Goblet Fire',
         5 : 'Harry Potter and the Order of Phoenix',
         6 : 'Harry Potter and the Half Blood Prince',
         7 : 'Harry Potter and the Deathly Hallow',
         8 : 'In order to live',
         9 : 'Romeo and Juliet',
         10 : 'Data and Network Communication',
         11 : 'Network Security',
         12 : 'Learning Web Design',
         13 : 'C program',
         14 : 'Understanding Human Communication',
         15 : 'Business English',
         16 : 'Java',
         17 : 'Scala',
         18 : 'DBMS',
         19 : 'IT Literacy',
         20 : 'Black Head'
       }

print("WELCOME TO KIT LIBRARY!\n\nPlease input User name and Password: ")

user_name = input(str('Username: '))
password = input(str('Password: '))

user_name = user_name.upper()

#Validation

for i in range (1, len(student)+1):
    #Validate the Username
    if user_name == student[i]['user_name']:

        #Validate the password
        if password == student[i]['password']:
            print('You are %s. Welcome back' %user_name)

            #print the list of book in library
            print('\nThis are the list of books in our library: ')

            for key,values in book.items():
                print(key, ' : ', values)

            #Student borrow the book
            listOfBookNum = []

            n = int(input('\nHow many book do you want to borrow?: '))
            if n > 5:
                boolean = True
            else:
                boolean = False
                
            while boolean is True:
                print('\n***You can borrow only 5 books at a time***')
                n = int(input('\nHow many book do you want to borrow?: '))
                if n <= 5:
                    boolean = False
            else:
                print('you want to borrow %s books' %n)

                print('\nInput the number of the book that you want to borrow: ')

                for j in range(1,n+1):
                    num = int(input())
                    listOfBookNum.append(num)

                StudentBorrowed = {}
                StudentBorrowed.update({student[i]['user_name'] : listOfBookNum})

                print('You have borrowed %s book(s) which are the following: ' %n)

                for k in range(0, n):
                    print(listOfBookNum[k], ' : ', book.get(listOfBookNum[k]))

                print('\n__________Thank you for using our library__________') 
                break
        else:
            print('Incorrect password')
            break
    elif i == len(student) and user_name != student[i]['user_name']:
        print('Invalid Username')
    else:
        continue
        




    




