import pyttsx3  # python text to speech library
import pywhatkit  # python library to play videos
import datetime  # python library for date and time and alarm
import wikipedia  # python library to search the wikipedia
import pyjokes  # python library for jokes
import cv2  # python library for using your webcam/camera
import subprocess  # python library to open apps/files
import webbrowser  # python library to open links on the web
import PyPDF2  # python library for pdfs
import random  # python library to select random things from a group
import mysql.connector as sqlator  # python library to connect mysql to python
import getpass  # python library to hide whatever you type

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 300)
engine.setProperty('volume', 200)


def talk(code):  # this function allows Kenta to speak to you
    engine.say(code)
    engine.runAndWait()


# connection with mySQL
con = sqlator.connect(host='localhost', user='root', password='1234', database='login')
talk('Do you want to login, register or change password .')
l_r = input('Do you want to login, register or change password :- ')
l_r = l_r.lower()
# registration of new entry to mySQL
if 'register' in l_r:
    talk('You chose Register')
    print('You chose register. ')
    cursor = con.cursor()
    talk('Enter your username')
    name = input('Enter the username :- ')
    talk('Enter the email id')
    mail = input('Enter your email id :- ')
    talk('Enter the password')
    password = getpass.getpass('Enter your password :- ')
    talk('Please confirm your password')
    conf_password = getpass.getpass('Please confirm your Password :- ')
    sqlform = "Insert into register values (%s,%s,%s,%s) "
    users = [(name, mail, password, conf_password)]
    if password == conf_password:
        try:
            cursor = con.cursor()
            cursor.executemany(sqlform, users)
            con.commit()
            print('You have successfully registered. You can now login by rerunning the program.')
            talk('You have successfully registered. You can now login by rerunning the program.')
            print('--------' * 15)
            talk('A project by Prathamesh Lakhotiya')
            print(' ~~ Prathamesh L \n D.A.V Public School')
            quit()
        except sqlator.IntegrityError:
            print('It seems that the email id that you have entered has already been registered. Please try again with a different email id ')
            talk('It seems that the email id that you have entered has already been registered. Please try again with a different email id ')
            print('--------' * 15)
            talk('A project by Prathamesh Lakhotiya')
            print(' ~~ Prathamesh L \n D.A.V Public School')
            quit()
    else:
        talk('The confirmed password does not match the password entered. Please try again .')
        print('The confirmed password does not match the password entered. Please try again .')
        print('--------' * 15)
        talk('A project by Prathamesh Lakhotiya')
        print(' ~~ Prathamesh L \n D.A.V Public School')
        quit()
# changing of password in existing table in mySQL
elif 'change password' in l_r:
    talk('You Chose Change Password')
    print('You chose Change Password.')
    cursor = con.cursor()
    talk('Enter your Username ')
    name = input('Enter the username :- ')
    talk('Enter the current Password ')
    Passwd = getpass.getpass('Enter the current password :- ')
    talk('Enter the email id')
    mail = input('Enter your email id :- ')
    talk('Enter the new password.')
    nPasswd = getpass.getpass('Enter the new password :- ')
    talk('Please confirm the new password')
    confPasswd = getpass.getpass('Please confirm the new password :- ')
    users = [(name, mail, nPasswd, confPasswd)]
    cursor.execute('SELECT Password from register ;')
    result = cursor.fetchall()
    x = (Passwd,)
    if x not in result:
        talk('The current Password that you have entered does not match the username. Please try again by correcting the details')
        print('The current Password that you have entered does not match the username ')
        print('--------' * 15)
        talk('A project by Prathamesh Lakhotiya')
        print(' ~~ Prathamesh L \n D.A.V Public School')
        quit()
    else:
        if nPasswd == confPasswd:
            form = 'DELETE FROM REGISTER WHERE username = '
            n_form = form + "'" + name + "'"
            cursor.execute(n_form)
            sqlform = "Insert into register values (%s,%s,%s,%s) "
            cursor.executemany(sqlform, users)
            con.commit()
            talk('Your Password has been successfully changed. You can now login with your new password by rerunning the program.')
            print('Your Password has been successfully changed ')
            talk('A project by Prathamesh Lakhotiya')
            print(' ~~ Prathamesh L \n D.A.V Public School')
            print('--------' * 15)
            quit()
        else:
            talk('The confirmed password does not match the password entered. Please try again .')
            print('The confirmed password does not match the password entered. Please try again .')
            talk('A project by Prathamesh Lakhotiya')
            print(' ~~ Prathamesh L \n D.A.V Public School')
            print('--------' * 15)
            quit()
# Crosschecking values from mySQL
elif 'login' in l_r:
    talk('You chose Login')
    print('You chose Login.')
    cursor = con.cursor()
    talk('Enter your Username ')
    name = input('Enter the username :- ')
    talk('Enter the password ')
    Passwd = getpass.getpass('Enter the password :- ')
    cursor.execute("SELECT username, Password from register")
    result = cursor.fetchall()
    x = (name, Passwd)
    if x in result:
        print(" =============================================== Hello", name,
              "!! ================================================")
        talk('Hello' + name)
        talk('I am your personal assistant Kenta ')
        print("")
        print(" My name is Kenta,You can do the following by using me .......")
        print("\n\t 1.PLAY A SONG  \t 2.SEARCH ON GOOGLE \n\t 3.KNOW THE TIME  \t 4.KNOW MORE ABOUT SOMEBODY OR SOMETHING "
            " \n\t 5.SET AN ALARM \t 6.CLICK A PICTURE \n\t 7.USE WHATSAPP   \t 8.HEAR A JOKE  "
            "  \n\t 9.PLAY A GAME \t\t 10.KNOW THE WEATHER \n\t 11.KNOW THE NEWS \t 12.OPEN VARIOUS APPLICATIONS")
        print("\n (YOU MUST ADD KENTA AT THE BEGINNING OF EVERY COMMAND Eg :- Kenta google I.P)")
        print("\n ============================================ Welcome To My Tools ==============================================")
        talk("Welcome to my tools")
        talk('To know more just type Kenta Help')
        print('\t\t\t\t\t TO KNOW MORE JUST TYPE KENTA HELP')
        talk('What can I do for you .')
        print("")

        # input command for Kenta
        def take_command():
            command = input("Enter Your Command For Me (Enter Kenta at the start of every command) :- ")
            command = command.lower()
            if 'kenta' in command:
                command = command.replace('kenta', '')
            else:
                talk('Please check the command again and make sure Kenta is there at the beginning and try again  ')
                print('Please check the command again and make sure Kenta is there at the beginning and try again.')
                print('--------' * 15)
                quit()
            return command


        def run_kenta():
            command = take_command()
            if 'mini royale' in command:
                talk('Opening Mini Royale 2 game on the web')
                webbrowser.open_new('https://miniroyale2.io/')
                print('--------' * 15)

            elif 'subway surfers' in command:
                talk('Opening Subway Surfers game on the web')
                webbrowser.open_new('https://poki.com/en/g/subway-surfers')
                print('--------' * 15)

            elif 'temple run' in command:
                talk('Opening Temple Run game on the web')
                webbrowser.open_new('https://poki.com/en/g/temple-run-2')
                print('--------' * 15)

            elif 'venge.io' in command:
                talk('Opening Venge.io game on the web ')
                webbrowser.open_new('https://venge.io/')
                print('--------' * 15)

            elif 'slither.io' in command:
                talk('Opening slither.io on the web')
                webbrowser.open_new('http://slither.io/')
                print('--------' * 15)

            elif 'agar.io' in command:
                talk('Opening Agar.io game on the web ')
                webbrowser.open_new('https://agar.io/')
                print('--------' * 15)

            elif 'paper.io' in command:
                talk('Opening Paper.io game on the web ')
                webbrowser.open_new('https://paper-io.com/?referer=paper.io&channel=11')
                print('--------' * 15)

            elif 'dark room' in command:
                talk('Opening dark room game on the web ')
                webbrowser.open_new('https://adarkroom.doublespeakgames.com/')
                print('--------' * 15)

            elif 'zombs royale' in command:
                talk('Opening Zombs Royale game on the web')
                webbrowser.open_new('https://zombsroyale.io/')
                print('--------' * 15)

            elif 'flight simulator' in command:
                talk('Opening flight simulator game on the web ')
                webbrowser.open_new('https://www.agame.com/game/boeing-flight-simulator')
                print('--------' * 15)
            # play games via Kenta
            if 'game' in command:
                talk('You can Choose one of the following games')
                print("\n\t 1.Mini Royale 2  \t\t 2.Subway Surfers  \n\t 3.Temple Run   \t\t 4.Venge.io "
                      " \n\t 5.Slither.io \t\t\t 6.Agar.io  \n\t 7.Paper.io \t\t\t 8.A Dark Room "
                      "\n\t 9.Krunker.io \t\t\t 10.Flight Simulator \n\t 11.Rock-Paper-Scissors")
                g = input('Which game do you want to play :- ')
                g = g.lower()
                if 'mini royale' in g or '1' in g:
                    talk('Opening Mini Royale 2 game on the web')
                    webbrowser.open_new('https://miniroyale2.io/')
                    print('--------' * 15)
                elif 'subway surfers' in g or '2' in g:
                    talk('Opening Subway Surfers game on the web')
                    webbrowser.open_new('https://poki.com/en/g/subway-surfers')
                    print('--------' * 15)
                elif 'temple run' in g or '3' in g:
                    talk('Opening Temple Run game on the web')
                    webbrowser.open_new('https://poki.com/en/g/temple-run-2')
                    print('--------' * 15)
                elif 'venge.io' in g or '4' in g:
                    talk('Opening Venge.io game on the web ')
                    webbrowser.open_new('https://venge.io/')
                    print('--------' * 15)
                elif 'slither.io' in g or '5' in g:
                    talk('Opening slither.io on the web')
                    webbrowser.open_new('http://slither.io/')
                    print('--------' * 15)
                elif 'agar.io' in g or '6' in g:
                    talk('Opening Agar.io game on the web ')
                    webbrowser.open_new('https://agar.io/')
                    print('--------' * 15)
                elif 'paper.io' in g or '7' in g:
                    talk('Opening Paper.io game on the web ')
                    webbrowser.open_new('https://paper-io.com/?referer=paper.io&channel=11')
                    print('--------' * 15)
                elif 'dark room' in g or '8' in g:
                    talk('Opening dark room game on the web ')
                    webbrowser.open_new('https://adarkroom.doublespeakgames.com/')
                    print('--------' * 15)
                elif 'krunker.io' in g or '9' in g:
                    talk('Opening Krunker.io game on the web')
                    webbrowser.open_new('https://krunker.io/')
                    print('--------' * 15)
                elif 'flight simulator' in g or '10' in g:
                    talk('Opening flight simulator game on the web ')
                    webbrowser.open_new('https://www.agame.com/game/boeing-flight-simulator')
                    print('--------' * 15)
                elif 'rock-paper-scissors' in g or 'rock paper scissors' in g or '11' in g:
                    talk('Please choose Rock, Paper, or Scissors')
                    y = input('Choose Rock/Paper/Scissors :- ')
                    y = y.lower()
                    if y == 'rock' or y == 'paper' or y == 'scissor':
                        i = ['rock', 'paper', 'scissor']
                        choose = random.choice(i)
                        talk('I choose ' + choose)
                        print('I choose ' + choose)
                        if y == 'rock' and choose == 'rock':
                            talk('Its a tie')
                            print('ITS A TIE ')
                        elif y == 'rock' and choose == 'paper':
                            talk('You lose')
                            print('YOU LOSE')
                        elif y == 'rock' and choose == 'scissor':
                            talk('You Win')
                            print('YOU WIN ')
                        elif y == 'scissors' and choose == 'paper':
                            talk('You win')
                            print('YOU WIN')
                        elif y == 'scissors' and choose == 'scissor':
                            talk('Its a tie')
                            print('ITS A TIE')
                        elif y == 'scissors' and choose == 'rock':
                            talk('You Lose')
                            print('YOU LOSE')
                        elif y == 'paper' and choose == 'rock':
                            talk('You Win')
                            print('YOU WIN')
                        elif y == 'paper' and choose == 'scissor':
                            talk('You Lose')
                            print('YOU LOSE ')
                        elif y == 'paper' and choose == 'paper':
                            talk('Its a tie')
                            print('ITS A TIE')
                        print('--------' * 15)
                    else:
                        talk('Please try again by inputting a valid command')
                        print('--------' * 15)
                else:
                    talk('Please select a game from the above eleven games.')
                    print('Please select a game from the above 11 games.')
                    print('--------' * 15)

            elif 'who are you' in command:
                talk('I am none other than your personal assistant Kenta')
                print('I am none other than your personal assistant Kenta')
                print('--------' * 15)

            elif 'what can you do' in command:
                talk("There's a lot I can do. Some of them include opening applications, playing a game, setting an alarm. I can also tell you the news and weather. To know more just type kenta help")
                print("There's a lot I can do. Some of them include opening applications, playing a game, setting an alarm. I can also tell you the news and weather. To know more just type kenta help")
                print('--------' * 15)

            elif 'rock-paper-scissors' in command or 'rock paper scissors' in command:
                talk('Please choose Rock, Paper, or Scissors')
                y = input('Choose Rock/Paper/Scissors :- ')
                y = y.lower()
                if y == 'rock' or y == 'paper' or y == 'scissor':
                    i = ['rock', 'paper', 'scissor']
                    choose = random.choice(i)
                    talk('I choose ' + choose)
                    print('I choose ' + choose)
                    if y == 'rock' and choose == 'rock':
                        talk('Its a tie')
                        print('ITS A TIE ')
                    elif y == 'rock' and choose == 'paper':
                        talk('You lose')
                        print('YOU LOSE')
                    elif y == 'rock' and choose == 'scissor':
                        talk('You Win')
                        print('YOU WIN ')
                    elif y == 'scissors' and choose == 'paper':
                        talk('You win')
                        print('YOU WIN')
                    elif y == 'scissors' and choose == 'scissor':
                        talk('Its a tie')
                        print('ITS A TIE')
                    elif y == 'scissors' and choose == 'rock':
                        talk('You Lose')
                        print('YOU LOSE')
                    elif y == 'paper' and choose == 'rock':
                        talk('You Win')
                        print('YOU WIN')
                    elif y == 'paper' and choose == 'scissor':
                        talk('You Lose')
                        print('YOU LOSE ')
                    elif y == 'paper' and choose == 'paper':
                        talk('Its a tie')
                        print('ITS A TIE')
                    print('--------' * 15)
                else:
                    talk('Please try again by inputting a valid command')
                    print('--------' * 15)
            # open calculator
            elif 'calculator' in command:
                talk('Searching For Calculator among all applications')
                try:
                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                    talk('opening calculator')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open notepad
            elif 'notepad' in command:
                talk('Searching for notepad among all applications')
                try:
                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                    talk('opening notepad')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open word
            elif 'open word' in command or 'microsoft word' in command or 'ms word' in command:
                talk('Searching for Microsoft word among all applications')
                try:
                    subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
                    talk('opening microsoft word')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open ppt
            elif 'ppt' in command or 'powerpoint' in command:
                talk('Searching for Powerpoint among all applications')
                try:
                    subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE')
                    talk('opening PPT')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open discord
            elif 'discord' in command:
                talk('Searching for discord among all applications')
                try:
                    subprocess.Popen('C:\\Users\\lakhotia\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe')
                    talk('opening Discord')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open telegram
            elif 'telegram' in command or 'tg' in command:
                talk('Searching for telegram among all applications')
                try:
                    subprocess.Popen('C:\\Users\\lakhotia\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')
                    talk('opening Telegram')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open Microsoft Teams
            elif 'teams' in command or 'ms teams' in command or 'microsoft teams' in command:
                talk('Searching for Microsoft teams  among all applications')
                try:
                    subprocess.Popen('C:\\Users\\lakhotia\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe')
                    talk('opening MS TEAMS')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open zoom
            elif 'zoom' in command:
                talk('Searching for zoom among all applications')
                try:
                    subprocess.Popen('C:\\Users\\lakhotia\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
                    talk('opening Zoom')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open paint
            elif 'paint' in command or 'microsoft paint' in command or 'ms paint' in command:
                talk('Searching for Microsoft paint among all applications')
                try:
                    subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
                    talk('Opening microsoft paint')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open microsoft excel
            elif 'excel' in command:
                talk('Searching for Microsoft excel among all applications')
                try:
                    subprocess.Popen('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
                    talk('opening Microsoft Excel')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open spotify
            elif 'spotify' in command:
                talk('Searching for spotify among all applications ')
                try:
                    subprocess.Popen('C:\\Users\\lakhotia\\AppData\\Roaming\\Spotify\\Spotify.exe')
                    talk('Opening Spotify ')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # open instagram
            elif 'instagram' in command or 'ig' in command:
                talk('opening instagram')
                webbrowser.open_new('https://www.instagram.com/')
                print('--------' * 15)
            # open whatsapp (on web)
            elif 'open whatsapp' in command:
                talk('Searching for Whatsapp among all applications')
                try:
                    subprocess.Popen('C:\\whatsapp.exe')
                    talk('Opening Whatsapp')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application. So, opening whatsapp on the web ')
                    print('Could not find the specified application. So, opening whatsapp on the web')
                    webbrowser.open_new('https://web.whatsapp.com/')
                    print('--------' * 15)
            # open  facebook (on web)
            elif 'facebook' in command or 'fb' in command:
                talk('Searching for Facebook among all applications')
                try:
                    subprocess.Popen('C:\\facebook.exe')
                    talk('Opening Facebook')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . So, opening Facebook on the web ')
                    print('Could not find the specified application . So, opening Facebook on the web')
                    webbrowser.open_new('https://www.facebook.com/')
                    print('--------' * 15)
            # open youtube
            elif 'youtube' in command or 'yt' in command:
                talk('opening Youtube on the web')
                webbrowser.open_new('https://www.youtube.com/')
                print('--------' * 15)
            # open gmail
            elif 'gmail' in command or 'open my mails' in command:
                talk('opening Gmail on the web')
                webbrowser.open_new('https://mail.google.com/')
                print('--------' * 15)
            # open twitter
            elif 'twitter' in command:
                talk('opening Twitter on the web')
                webbrowser.open_new('https://www.twitter.com/')
                print('--------' * 15)
            # open google chrome
            elif 'open google' in command or 'open chrome' in command:
                talk('Searching for google chrome among all applications')
                try:
                    subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                    talk('Opening google chrome')
                    print('--------' * 15)
                except FileNotFoundError:
                    talk('Could not find the specified application . Please check that the application is installed and try again ')
                    print('Could not find the specified application . Please check that the application is installed and try again ')
                    print('--------' * 15)
            # play song on YouTube
            elif 'play' in command:
                song = command.replace('play', '')
                talk('Playing ' + song)
                pywhatkit.playonyt(song)
                print('--------' * 15)
            # play song on YouTube
            elif 'sing' in command:
                song = command.replace('sing', '')
                talk('Playing ' + song + 'on youtube')
                pywhatkit.playonyt(song)
                print('--------' * 15)
            # tell the current time
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('The current time is ' + time)
                talk('The current time is ' + time)
                print('--------' * 15)
            # know about someone or something
            elif 'tell me about ' in command:
                wikipedia.set_lang('En')
                person = command.replace('tell me about ', '')
                try:
                    info = wikipedia.summary(person, sentences=2)
                    p = wikipedia.page(person)
                    talk(info)
                    print(info)
                    talk('for more information click on the following link ')
                    print(p.url)
                    print('--------' * 15)
                except wikipedia.exceptions.DisambiguationError:
                    talk('Could not extract information from the web over here, so opening information on google')
                    base_url = 'https://en.wikipedia.org/wiki/'
                    url = base_url + person
                    webbrowser.open_new(url)
                    print('--------' * 15)
                except wikipedia.exceptions.PageError:
                    talk('Could not extract information from the web over here, so opening information on google')
                    base_url = 'https://en.wikipedia.org/wiki/'
                    url = base_url + person
                    webbrowser.open_new(url)
                    print('--------' * 15)
            # know about a person
            elif 'who is' in command:
                wikipedia.set_lang('En')
                person = command.replace('who is ', '')
                try:
                    info = wikipedia.summary(person, sentences=2)
                    p = wikipedia.page(person)
                    talk(info)
                    print(info)
                    talk('for more information click on the following link ')
                    print(p.url)
                    print('--------' * 15)
                except wikipedia.exceptions.DisambiguationError:
                    talk('Could not extract information from the web over here, so opening information on google')
                    base_url = 'https://en.wikipedia.org/wiki/'
                    url = base_url + person
                    webbrowser.open_new(url)
                    print('--------' * 15)
                except wikipedia.exceptions.PageError:
                    talk('Could not extract information from the web over here, so opening information on google')
                    base_url = 'https://en.wikipedia.org/wiki/'
                    url = base_url + person
                    webbrowser.open_new(url)
                    print('--------' * 15)

            # set an alarm
            elif 'alarm' in command:
                talk('Enter Alarm Hour in 24 hour format')
                alarmhour = int(input('Enter Alarm Hour in 24 hour format :- '))
                if 0 < alarmhour < 24:
                    talk('Enter Alarm Minute')
                    alarmmin = int(input("Enter Alarm Minute :-"))
                    if 0 < alarmmin < 60:
                        talk('Enter the song for alarm')
                        song = input('Enter the song for alarm :- ')
                        talk('Alarm has been set')
                        print('Alarm has been set')
                        while True:
                            if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
                                pywhatkit.playonyt(song)
                                break
                            else:
                                pass
                    else:
                        talk('Alarm minute out of range , Please try again ')
                        print('--------' * 15)
                else:
                    talk('Alarm hour out of range , Please try again ')
                    print('--------' * 15)
            # click a picture
            elif 'click a picture' in command:
                cam = cv2.VideoCapture(0)
                cv2.namedWindow('Capturing your photo')
                while True:
                    ret, frame = cam.read()
                    if not ret:
                        talk('No Camera Detected ')
                        print('No camera is detected.')
                        break
                    else:
                        pass
                    cv2.imshow('Capturing your photo', frame)
                    img_name = 'photo.png'
                    cv2.imwrite(img_name, frame)
                    talk('Photo is taken ')
                    print('Photo is taken')
                    break
                cam.release()
                cv2.destroyAllWindows()
            # message someone via whatsapp directly
            elif 'whatsapp' in command:
                try:
                    talk('Do you want to message to a person or in a group')
                    h = input('Do you want to message to a person or in a group :- ')
                    h = h.lower()
                    if 'person' in h:
                        talk('Enter the whatsapp number to whom the message is to be sent with country code at beginning')
                        z = input('Enter the whatsapp number to whom the message is to be sent (with country code at beginning):- ')
                        talk('Enter the message')
                        msg = input('Enter the message :- ')
                        talk('Enter the hour ( 24 hour format)')
                        hour = int(input('Enter the hour (24hr format) :- '))
                        talk("Enter the minute")
                        minute = int(input("Enter the minute :- "))
                        pywhatkit.sendwhatmsg(z, msg, hour, minute)
                        print('--------' * 15)
                    elif 'group' in h:
                        talk('Enter the group id')
                        s = (input('Enter the group id :- '))
                        talk('Enter the message')
                        d = (input('Enter the message :- '))
                        talk('Enter the hour (24hr format)')
                        hour = int(input('Enter the hour (24hr format) :- '))
                        talk("Enter the minute")
                        minute = int(input("Enter the minute :- "))
                        pywhatkit.sendwhatmsg_to_group(s, d, hour, minute)
                        print('--------' * 15)
                except pywhatkit.mainfunctions.CallTimeException:
                    talk('An Unknown Error occurred please check your internet connection and try again ')
                    print('--------' * 15)
            # tells a joke
            elif 'joke' in command:
                joke = pyjokes.get_joke()
                print(joke)
                talk(joke)
                print('--------' * 15)
            # tells the weather
            elif 'weather at' in command:
                url = 'https://www.google.com/search?q='
                location1 = command.replace('weather at', '')
                location2 = location1.replace('tell me', '')
                location3 = location2.replace('what is', '')
                location = location3.replace('the', '')
                s = 'Weather at ' + location
                final_url = url + s
                talk('Showing the weather in google')
                webbrowser.open_new(final_url)
                print('--------' * 15)
            # tells the weather
            elif 'weather' in command:
                url = 'https://www.google.com/search?q='
                talk('Please Enter the location ')
                location = input('Enter the location :- ')
                s = 'Weather at ' + location
                final_url = url + s
                talk('Showing the weather at ' + location)
                webbrowser.open_new(final_url)
                print('--------' * 15)

            elif 'international news' in command:
                talk('Opening International News ')
                webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'national news' in command:
                talk('Opening national news ')
                webbrowser.open_new('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'business news' in command:
                talk('Opening Business news')
                webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'technology news' in command:
                talk('Opening Technological News ')
                webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'entertainment news' in command:
                talk('Opening Entertainment news ')
                webbrowser.open_new('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'health news' in command:
                talk(' Opening health news ')
                webbrowser.open_new('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'sports news' in command:
                talk('opening Sports News ')
                webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'local news' in command:
                talk('Opening Local News ')
                webbrowser.open_new('https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREUxZVRKeGVnc0tDUzl0THpBeE5Ya3ljU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREUxZVRKeEtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)

            elif 'science news' in command:
                talk('opening science news ')
                webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                print('--------' * 15)
            # opens the news
            elif 'news' in command:
                talk('Which type of news do you want to hear :- ')
                print("\n\t 1.NATIONAL NEWS  \t 2.INTERNATIONAL NEWS  \n\t 3.SPORTS NEWS   \t 4.ENTERTAINMENT NEWS  "
                      " \n\t 5.SCIENCE NEWS \t 6.BUSINESS NEWS  \n\t 7.TECHNOLOGY NEWS \t 8.HEALTH NEWS \n\t 9.LOCAL NEWS")
                n = input('Which type of news do you want to hear ? :-')
                n = n.lower()
                if 'international' in n or '1' in n:
                    talk('Opening International News ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'national' in n or '2' in n:
                    talk('Opening national news ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'technology' in n or '7' in n:
                    talk('Opening Technological News ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'entertainment' in n or '4' in n:
                    talk('Opening Entertainment news ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'sports' in n or '3' in n:
                    talk('Opening Sports news ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'science' in n or '5' in n:
                    talk('Opening Science News')
                    webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'business' in n or '6' in n:
                    talk('Opening Business news')
                    webbrowser.open_new('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'health' in n or '8' in n:
                    talk('Opening Health news')
                    webbrowser.open_new('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                elif 'local' in n or '9' in n:
                    talk('opening local news ')
                    webbrowser.open_new('https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREUxZVRKeGVnc0tDUzl0THpBeE5Ya3ljU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREUxZVRKeEtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')
                    print('--------' * 15)
                else:
                    talk('select a valid option from the ones given above. Please try again')
                    print('Select a valid option from the ones given above. Please try again')
                    print('--------' * 15)
            # tells a story
            elif 'story' in command:
                num = str(random.randint(1, 10))
                b = 'Short_story' + num + '.pdf'
                book = open(b, 'rb')
                reader = PyPDF2.PdfFileReader(book)
                pages = reader.numPages
                talk('Here is a story for you .')
                for num in range(0, pages):
                    page = reader.getPage(num)
                    text = page.extractText()
                    talk(text)
                    num += 1
                print('--------' * 15)
            # opens various applications
            elif 'open' in command:
                command = command.replace('open', '')
                talk('Searching for' + command + 'among all applications.')
                talk('No such application found ')
                talk('PLease enter an installed application and try again')
                print('PLease enter an installed application and try again')
                print('--------' * 15)
            # searches on the web
            elif 'google' in command:
                query = command.replace('google', '')
                talk("Here's what I found on the web")
                pywhatkit.search(query)
                print('--------' * 15)
            # searches on the web
            elif 'search' in command:
                query = command.replace('search', '')
                talk("Here's what I found on the web")
                pywhatkit.search(query)
                print('--------' * 15)
            # searches on the web
            elif 'what' in command:
                query = command.replace('what', '')
                talk("Here's what I found on the web")
                pywhatkit.search(query)
                print('--------' * 15)
            # changes password
            elif 'change password' in command:
                talk('You Chose Change Password')
                print('You chose Change Password.')
                cursor1 = con.cursor()
                talk('Enter your Username ')
                name1 = input('Enter the username :- ')
                talk('Enter the current Password ')
                Passwd1 = getpass.getpass('Enter the current password :- ')
                talk('Enter the email id')
                mail1 = input('Enter your email id :- ')
                talk('Enter the new password.')
                nPasswd1 = getpass.getpass('Enter the new password :- ')
                talk('Please confirm the new password')
                confPasswd1 = getpass.getpass('Confirm the new password :- ')
                users1 = [(name1, mail1, nPasswd1, confPasswd1)]
                cursor1.execute('SELECT Password from register ;')
                result1 = cursor1.fetchall()
                x1 = (Passwd1,)
                if x1 not in result1:
                    talk('The current Password that you have entered does not match the username. Please try again by correcting the details')
                    print('The current Password that you have entered does not match the username ')
                    talk('A project by Prathamesh Lakhotiya')
                    print(' ~~ Prathamesh L \n D.A.V Public School')
                    print('--------' * 15)
                    quit()
                else:
                    if nPasswd1 == confPasswd1:
                        form1 = 'DELETE FROM REGISTER WHERE username = '
                        n_form1 = form1 + "'" + name1 + "'"
                        cursor1.execute(n_form1)
                        sqlform1 = "Insert into register values (%s,%s,%s,%s) "
                        cursor1.executemany(sqlform1, users1)
                        con.commit()
                        talk('Your Password has been successfully changed. You can now login with your new password by rerunning the program.')
                        print('Your Password has been successfully changed ')
                        talk('A project by Prathamesh Lakhotiya')
                        print(' ~~ Prathamesh L \n D.A.V Public School')
                        print('--------' * 15)
                        quit()
                    else:
                        talk('The confirmed password does not match the password entered. Please try again .')
                        print('The confirmed password does not match the password entered. Please try again .')
                        talk('A project by Prathamesh Lakhotiya')
                        print(' ~~ Prathamesh L \n D.A.V Public School')
                        print('--------' * 15)
                        quit()
            # ends the program
            elif 'end' in command or 'stop' in command or 'quit' in command:
                talk('Thanks for using me. Hope to meet you soon ')
                print('Thanks for using me. Hope to meet you soon')
                talk('A project by Prathamesh Lakhotiya')
                print(' ~~ Prathamesh L \n D.A.V Public School')
                print('--------' * 15)
                quit()

            elif 'help' in command:
                talk('The list of valid commands with the syntax is as follows .')
                print(" 1. Kenta play a game \n 2. Kenta play <game name> \n 3. Kenta open <application name> \n 4. Kenta use <application name> \n "
                    "5. Kenta What is the time \n 6. Kenta tell me more about <someone/something> \n 7. Kenta who is <someone> \n "
                    "8. Kenta set an alarm \n 9. Kenta click a picture \n 10. Kenta tell me a joke \n 11. Kenta whats the weather at <location> \n"
                    " 12. Kenta play <song> \n 13. Kenta tell me a story \n 14. Kenta tell me the news \n 15. Kenta tell me <type of news>.")
                print("")
                talk('There are many more commands , but those are for you to explore ')
                print('There are many more commands , but those are for you to explore.')
                print('--------' * 15)

            else:
                talk("Sorry I'm not sure what you said . You can use the help statement to know my functions in a better way.")
                print("Sorry I'm not sure what you said . You can use the help statement to know my functions in a better way.  ")
                print('--------' * 15)

        while True:
            run_kenta()
    else:
        talk('The username and password do not match. Please try again ')
        print('The username and password do not match. Please try again')
        talk('A project by Prathamesh Lakhotiya')
        print(' ~~ Prathamesh L \n D.A.V Public School')
        print('--------' * 15)
        quit()
else:
    talk('Please enter a valid command. You can either login, register or change your password .')
    print('Please enter a valid command. You can either login, register or change your password')
    talk('A project by Prathamesh Lakhotiya')
    print(' ~~ Prathamesh L \n D.A.V Public School')
    print('--------' * 15)
    quit()
