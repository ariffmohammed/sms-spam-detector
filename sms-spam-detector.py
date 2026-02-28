import re
from sklearn.linear_model import LogisticRegression

messages = [
    ("ham", "Go until jurong point crazy Available only in bugis n great world la e buffet"),
    ("spam", "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005 Text FA to 87121"),
    ("ham", "Nah I don't think he goes to usf he lives around here though"),
    ("spam", "FreeMsg Hey there darling its been 3 weeks now and no word back Id like some fun"),
    ("ham", "Even my brother is not like to speak with me They treat me like aids patent"),
    ("spam", "WINNER As a valued network customer you have been selected to receive a 900 prize reward"),
    ("spam", "Had your mobile 11 months or more U R entitled to Update to the latest colour mobiles"),
    ("ham", "Im gonna be home soon and i dont want to talk about this stuff anymore tonight"),
    ("spam", "SIX chances to win CASH From 100 to 20000 pounds txt CSH11 and send to 87575"),
    ("spam", "URGENT You have won a 1 week FREE membership in our 100000 Prize Jackpot"),
    ("ham", "Ive been searching for the right words to thank you for this breather"),
    ("ham", "I HAVE A DATE ON SUNDAY WITH WILL"),
    ("spam", "XXXMobileMovieClub To use your credit click the WAP link in the next txt message"),
    ("ham", "Oh k im watching here"),
    ("spam", "England v Macedonia dont miss the goals Txt ur national team to 87077"),
    ("ham", "Is that seriously how you spell his name"),
    ("ham", "Im going to try for 2 months ha ha only joking"),
    ("ham", "Just forced myself to eat a slice Im really not hungry tho This sucks"),
    ("ham", "Lol your always so convincing"),
    ("spam", "Thanks for your subscription to Ringtone UK your mobile will be charged 5 per month"),
    ("ham", "Yup Ok i go home look at the timings then i msg you again"),
    ("ham", "Oops Ill let you know when my roommates done"),
    ("spam", "FREE WINNER URGENT claim prize reward cash mobile call now txt winner selected"),
    ("spam", "Sunshine Quiz Wkly Q Win a top Sony DVD player if u know which country the Algarve is in Txt ansr to 82277"),
("spam", "Want 2 get laid tonight Want real Dogging locations sent direct 2 ur mob Join the UK largest Dogging Network bt Txting GRAVEL to 69888"),
("ham", "I only haf msn"),
("ham", "He is there You call and meet him"),
("ham", "No no I will check all rooms before activities"),
("spam", "You'll not rcv any more msgs from the chat svc For FREE Hardcore services text GO to 69988"),
("ham", "Got c I lazy to type I forgot u in lect I saw a pouch but like not v nice"),
("ham", "K text me when you're on the way"),
("ham", "Sir Waiting for your mail"),
("ham", "A swt thought Nver get tired of doing little things 4 lovable persons coz somtimes those little things occupy d biggest part in their Hearts"),
("ham", "I know you are Can you pls open the back"),
("ham", "Yes see ya not on the dot"),
("ham", "Whats the staff name who is taking class for us"),
("spam", "FreeMsg Why haven't you replied to my text I'm Randy sexy female and live local Luv to hear from u"),
("ham", "Ummma will call after check in our life will begin from qatar so pls pray very hard"),
("ham", "Sindu got job in birla soft"),
("ham", "Yup i thk cine is better cos no need 2 go down 2 plaza mah"),
("ham", "You are everywhere dirt on the floor the windows even on my shirt"),
("ham", "I'm leaving my house now"),
("ham", "Hello my love what are you doing did you get to that interview today"),
("spam", "Customer service announcement You have a New Years delivery waiting Please call 07046744435 now to arrange delivery"),
("spam", "You are a winner U have been specially selected 2 receive 1000 cash or a 4 star holiday speak to a live operator 2 claim"),
("ham", "Keep yourself safe for me because I need you and I miss you already"),
("ham", "New car and house for my parents i have only new job in hand"),
("ham", "I'm so in love with you I'm excited each day i spend with you"),
("spam", "PLS STOP bootydelious is inviting you to be her friend Reply YES or NO"),
("spam", "BangBabes Ur order is on the way U SHOULD receive a Service Msg 2 download UR content"),
("spam", "URGENT We are trying to contact you Last weekends draw shows that you have won a 900 prize GUARANTEED Call 09061701939"),
("ham", "Hi frnd which is best way to avoid missunderstding wit our beloved ones"),
("ham", "Great escape I fancy the bridge but needs her lager See you tomo"),
("ham", "Sir I need AXIS BANK account no and bank address"),
("ham", "What time you coming down later"),
("ham", "Well i'm gonna finish my bath now Have a good fine night"),
("ham", "Let me know when you've got the money so carlos can make the call"),
("ham", "U still going to the mall"),
("ham", "Text her if she doesnt reply let me know"),
("ham", "Lol no u can trust me"),

]

all_words=set()
for label,msg1 in messages:
    words1=msg1.lower().split()
    all_words.update(words1)
all_words=list(all_words)

def convert_features(msg2):
    words2=msg2.lower().split()
    features=[]
    for word in all_words:
        features.append(1 if word in words2 else 0)
    return features 

x=[convert_features(msg3) for label,msg3 in messages]
y=[1 if label=="spam" else 0 for label,msg3 in messages]

model = LogisticRegression()
model.fit(x, y)
 
def predict(msg4):
    features=convert_features(msg4)
    result = model.predict([features])[0]
    return "SPAM" if result == 1 else "NOT SPAM"

while True:
    msg5=input("enter message")
    print(predict(msg5))