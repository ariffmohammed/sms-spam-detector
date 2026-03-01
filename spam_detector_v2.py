from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

messages = [
    ("ham", "Go until jurong point crazy available only in bugis and great world buffet"),
    ("spam", "Free entry in a weekly competition to win FA Cup final tickets text FA to 87121"),
    ("ham", "I don't think he goes to USF he lives around here though"),
    ("spam", "FreeMsg hey there darling it has been 3 weeks now and no word back I would like some fun"),
    ("ham", "Even my brother does not like to speak with me they treat me badly"),
    ("spam", "Winner as a valued network customer you have been selected to receive a 900 prize reward"),
    ("spam", "Had your mobile 11 months or more you are entitled to update to the latest colour mobile with camera for free"),
    ("ham", "I am gonna be home soon and I don't want to talk about this stuff anymore tonight"),
    ("spam", "Six chances to win cash from 100 to 20000 pounds text CSH11 and send to 87575"),
    ("spam", "Urgent you have won a 1 week free membership in our 100000 prize jackpot"),
    ("ham", "I have been searching for the right words to thank you for this breather"),
    ("ham", "I have a date on Sunday with Will"),
    ("spam", "XXXMobileMovieClub to use your credit click the WAP link in the next text message"),
    ("ham", "Oh okay I am watching here"),
    ("spam", "England v Macedonia don't miss the goals text your national team to 87077"),
    ("ham", "Is that seriously how you spell his name"),
    ("ham", "I am going to try for 2 months just joking"),
    ("ham", "Just forced myself to eat a slice I am really not hungry this sucks"),
    ("ham", "Lol you are always so convincing"),
    ("spam", "Thanks for your subscription to Ringtone UK your mobile will be charged 5 per month"),
    ("ham", "Okay I will go home look at the timings then message you again"),
    ("ham", "Oops I will let you know when my roommate is done"),
    ("spam", "Free winner urgent claim prize reward cash mobile call now text winner selected"),
    ("spam", "Sunshine quiz win a top Sony DVD player if you know which country the Algarve is in text answer to 82277"),
    ("spam", "Want to get laid tonight want real locations sent direct to your mobile text GRAVEL to 69888"),
    ("ham", "I only have MSN"),
    ("ham", "He is there you call and meet him"),
    ("ham", "No I will check all rooms before activities"),
    ("spam", "You will not receive any more messages from the chat service for free hardcore services text GO to 69988"),
    ("ham", "I am lazy to type I forgot you in lecture I saw a pouch but it was not very nice"),
    ("ham", "Text me when you are on the way"),
    ("ham", "Sir waiting for your mail"),
    ("ham", "A sweet thought never get tired of doing little things for lovable people because sometimes those little things occupy the biggest part of their hearts"),
    ("ham", "I know you are can you please open the back"),
    ("ham", "Yes see you not exactly on time"),
    ("ham", "What is the staff name who is taking class for us"),
    ("spam", "FreeMsg why haven't you replied to my text I am Randy sexy female and live local love to hear from you"),
    ("ham", "Will call after check in our life will begin from Qatar so please pray very hard"),
    ("ham", "Sindu got a job at Birla Soft"),
    ("ham", "I think the cinema is better because no need to go down to the plaza"),
    ("ham", "You are everywhere on the floor the windows even on my shirt"),
    ("ham", "I am leaving my house now"),
    ("ham", "Hello my love what are you doing did you get to that interview today"),
    ("spam", "Customer service announcement you have a delivery waiting please call 07046744435 now to arrange delivery"),
    ("spam", "You are a winner you have been specially selected to receive 1000 cash or a 4 star holiday speak to a live operator to claim"),
    ("ham", "Keep yourself safe for me because I need you and I miss you already"),
    ("ham", "New car and house for my parents I only have a new job in hand"),
    ("ham", "I am so in love with you I am excited each day I spend with you"),
    ("spam", "Please stop this user is inviting you to be her friend reply YES or NO"),
    ("spam", "Your order is on the way you should receive a service message to download your content"),
    ("spam", "Urgent we are trying to contact you last weekend draw shows you have won a 900 prize guaranteed call 09061701939"),
    ("ham", "Hi friend what is the best way to avoid misunderstanding with our loved ones"),
    ("ham", "Great escape I fancy the bridge see you tomorrow"),
    ("ham", "Sir I need the bank account number and bank address"),
    ("ham", "What time are you coming down later"),
    ("ham", "I am going to finish my bath now have a good night"),
    ("ham", "Let me know when you have got the money so Carlos can make the call"),
    ("ham", "Are you still going to the mall"),
    ("ham", "Text her if she does not reply let me know"),
    ("ham", "Lol no you can trust me"),
]

labels = [label for label, msg in messages]
texts = [msg for label, msg in messages]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = [1 if label == "spam" else 0 for label in labels]

model = LogisticRegression()
model.fit(X, y)

def predict(msg):
    x = vectorizer.transform([msg])
    result = model.predict(x)[0]
    return "SPAM" if result == 1 else "NOT SPAM"

while True:
    user_input = input("Enter a message: ")
    print(predict(user_input))
