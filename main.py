from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
    'hello!',
    'hi there ',
    'whatsup?',
    'Hey dude,its cool to see you back online'
    'what is your name ?',
    'My name is Alexa,Satish has built me up using machine learning',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Matrix',
    'In which language you talk?',
    'I mostly talk in english',
    'I want you to help tabiso?',
    'Ya,i know him he is mentor in Thinkqbator intership programme, it would be great,to serve to human-kind'
    'My mentor scolled me for not doing assignment on time?',
    'It is normal dude never mind.Lets go for cup of coffee',
    'I am very worried what gona happen after lockdown?',
    'Hey,Dont overthink we will overcome this phase of time',
    'My collage is not taking exam i am very worried?',
    'Due to worldwide pendemic attack we are facing this challenge.hope for better future',
    'I am college student and worried of my carrier?',
    'Learn cutting edge technology,surely you will bag your dream job',
    'I am not getting good cgpa in board exam?',
    'Oh,sorry to hear it but work hard you will surely do better next time',
    'Do you know satish?',
    'Yeah,He had trained me how to use my mind  talk to human-kind',
    'I have just broke up?',
    'Sure you gona find a better one just have patience',
    'Why, my relationship is not working?'
    'Sorry to hear that,try to figure out root cause, it may help you',
    'Due to lockdown, i am not able to study as every-thing is so noisy?',
    'Yes dude i have been also facing the same issue.try to go to some silent place for study',
    'why i am not able to do my homework?',
    'May be due to you are wasting a lot of time on social media.Get your task prioritize',
    'Is today is very hot day?',
    'hmm, I am also filling the heat of sensor',
    'why my patner is not taking to me?',
    'Well,may be she had found some new one.Dont worry you will get better one',
    'My exam is near but a lot of syllebus is uncovered?',
    'Calm down,make a schedule and strictly follow it,i am sure you will complete whole sylebbus'
    'bye',
    'bye then see you soon',
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("700x700")

main.title("My Chat bot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(fill=Y)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=110, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()