#represents characters that may be confused with one another
#that is, near each other on keyboard or having a similar sound
characters = {"a": {"q", "w", "s", "z", "e", "u"}, 
            "b": {"v", "g", "h", "n"},
            "c": {"x", "d", "f", "v", "k", "s", "ck"},
            "d": {"s", "e", "r", "f", "c", "x"},
            "e": {"w", "r", "d", "s", "a", "y"},
            "f": {"d", "r", "g", "v", "c"},
            "g": {"f", "t", "h", "b", "v", "j"},
            "h": {"g", "y", "j", "n", "b"},
            "i": {"u", "o", "k", "e"},
            "j": {"u", "i", "k", "m", "n", "h", "g"},
            "k": {"i", "o", "l", "m", "j", "u", "c", "ck"},
            "l": {"o", "p", "k"},
            "m": {"n", "j", "k"},
            "n": {"b", "h", "j", "m"},
            "o": {"p", "l", "k", "i"},
            "p": {"l", "o"},
            "q": {"w","a"},
            "r": {"e","d","f","t"},
            "s": {"a","w","d", "x", "z", "c"},
            "t": {"r","f","g","y"},
            "u":{"y", "j", "i"},
            "v": {"c", "f", "g","b"},
            "w": {"q", "a", "s", "d", "e"},
            "x": {"z","s","d","c"},
            "y":{"e", "t", "h", "u"},
            "z":{"a", "s", "x"}}

#word mapped to tuple with wordStatus, abbrevStatus
wordsChecked = {}

#words user has indicated are "real" to them
personalDictionary = set()

#word ideas from https://www.gonaturalenglish.com/1000-most-common-words-in-the-english-language/
mostCommonWords = {"be","and","of","a","in","to","have","too","it",'among', 'ever','stand','bad','lose',
"I","that","for","you","he","with","on","do","say","this","they","at","but","we","his","from",'however',
"that","not","can’t","won’t","by","she","or","as","what","go","their","can","who","get","if",'member','pay',
"would","her","all","my","make","about","know","will","as","up","one","time","there",'city','almost','include',
"year","so","think","when","which","them","some","me","people","take","out","into","just","see","him",
"your","come","could","now","than","like","other","how","then","its","our","two","more","these","want",
"way","look","first","also","new","because","day","more","use","no","man","find","here","thing","give",
"many","well","only","those","tell","one","very","her","even","back","any","good","woman","through","us",
"life","child","there","work","down","may","after","should","call","world","over","school","still","try",
"in","as","last","ask","need","too","feel","three","when","state","never","become","between","high",
"really","something","most","another","much","family","own","out","leave","put","old","while","mean","on",
"keep","student","why","let","great","same","big","group","begin","seem","country","help","talk","where",
"turn","problem","every","start","hand","might","American","show","part","about",'against','place','over',
'such','again','few','case','most','week','company','where','system','each','right','program','hear','so',
'question','during','work','play','government','run','small','number','off','always','move','law','meet','car'
"like","night","live","Mr","point","believe","hold","today","bring","happen","next","without","before",
"large","all","million","must","home","under","water","room","write","mother","area","national","money",
"story","young","fact","month","different","lot","right","study","book","eye","job","word","though",
"business","issue",'side','kind','four','head','far','black','long','both','little','house','yes','after',
'since','long','provide','service','around','friend','important','father','sit','away','until','power',
'hour','game','often','yet','line','political','end','continue','set','later','community','much','name',
'five','once','white', 'least','president', 'learn','real','change','team','minute','best','several',
'idea','kid','body','information','nothing','ago','right','lead','social','understand','whether','back',
'watch','together','follow','around','parent','only','stop','face','anything','create','public','already',
'speak','others','read','level','allow','add','office','spend','door','health','person','art','sure','such',
'war','history','party','within','grow','result','open','morning','walk','reason','low','win','research',
'girl','guy','early','food','before','moment','himself','air','teacher','force','offer','enough','both',
'education','across','although','remember','foot','second','boy','maybe','toward','able','age','off',
'policy','everything','love','process','music','including','consider','appear','actually','buy','probably',
'human','wait','serve','market','die'}
'''
send – “Please send the package to my address.”
expect – “You can’t expect much from their poor service.”
home – “I can’t wait to go home!”
sense – “I did sense that something was not okay.”
build – “He is going to build his dream house.”
stay – “You can stay with me for a few weeks.”
fall – “Be careful, you might fall.”
oh – “Oh no, I left my phone at home!”
nation – “We have to act as one nation.”
plan – “What’s your plan this time?”
cut – “Don’t cut your hair.”
college – “We met in college.”
interest – “Music is an interest of mine.”
death – “Death is such a heavy topic for me.”
course – “What course did you take up in college?”
someone – “Is there someone who can go with you?”
experience – “What an exciting experience!”
behind – “I’m scared to check what’s behind that door.”
reach – “I can’t reach him, he won’t answer his phone.”
local – “This is a local business.”
kill – “Smoking can kill you.”
six – “I have six books about Psychology.”
remain – “These remain on the top shelf.”
effect – “Wow, the effect of that mascara is great!”
use – “Can I use your phone?”
yeah – “Yeah, he did call me earlier.”
suggest – “He did suggest that to me.”
class – “We were in the same English class.”
control – “Where’s the remote control?”
raise – “It’s so challenging to discipline kids these days.”
care – “I don’t care about what you think.”
perhaps – “Perhaps we can arrive at a compromise.”
little – “There’s a little bird outside my window.”
late – “I am running late for my doctor’s appointment.”
hard – “That test was so hard.”
field – “He’s over there, by the soccer field.”
else – “Is anyone else coming?”
pass – “Can we pass by the grocery store?”
former – “She was my former housemate.”
sell – “We can sell your old couch online.”
major – “It’s a major issue for the project.”
sometimes – “Sometimes I forget to turn off the porch lights.”
require – “They’ll require you to show your I.D.”
along – “Can I tag along your road trip?”
development – “This news development is really interesting.”
themselves – “They can take care of themselves.”
report – “I read her report and it was great!”
role – “She’s going to play the role of Elsa.”
better – “Your singing has gotten so much better!”
economic – “Some countries are facing an economic crisis.”
effort – “The government must make an effort to solve this.”
up – “His grades have gone up.”
decide – “Please decide where to eat.”
rate – “How would you rate the hotel’s service?”
strong – “They have strong customer service here!”
possible – “Maybe it’s possible to change their bathroom amenities.”
heart – “My heart is so full.”
drug – “She got the patent for the drug she has created to cure cancer.”
show – “Can you show me how to solve this puzzle?”
leader – “You are a wonderful leader.”
light – “Watch her face light up when you mention his name.”
voice – “Hearing his mom’s voice is all he need right now.”
wife – “My wife is away for the weekend.”
whole – “I have the whole house to myself.”
police – “The police have questioned him about the incident.”
mind – “This relaxation technique really eases my mind.”
finally – “I can finally move out from my old apartment.”
pull – “My baby niece likes to pull my hair.”
return – “I give her tickles in return.”
free – “The best things in life are free.”
military – “His dad is in the military.”
price – “This is the price you pay for lying.”
report – “Did you report this to the police?”
less – “I am praying for less stress this coming new year.”
according – “According to the weather report, it’s going to rain today.”
decision – “This is a big decision for me.”
explain – “I’ll explain everything later, I promise.”
son – “His son is so cute!”
hope – “I hope I’ll have a son one day.”
even – “Even if they’ve broken up, they still remain friends.”
develop – “That rash could develop into something more serious.”
view – “This view is amazing!”
relationship – “They’ve taken their relationship to the next level.”
carry – “Can you carry my bag for me?”
town – “This town is extremely quiet.”
road – “There’s a road that leads to the edge of the woods.”
drive – “You can’t drive there, you need to walk.”
arm – “He broke his arm during practice.”
true – “It’s true, I’m leaving the company.”
federal – “Animal abuse is now a federal felony!”
break – “Don’t break the law.”
better – “You better learn how to follow rules.”
difference – “What’s the difference between happiness and contentment?”
thank – “I forgot to thank her for the pie she sent us.”
receive – “Did you receive the pie I sent you?”
value – “I value our friendship so much.”
international  – “Their brand has gone international!”
building – “This building is so tall!”
action – “You next action is going to be critical.”
full – “My work load is so full now.”
model – “A great leader is a great model of how to do things.”
join – “He wants to join the soccer team.”
season – “Christmas is my favorite season!”
society – “Their society is holding a fund raiser.”
because – “I’m going home because my mom needs me.”
tax – “How much is the current income tax?”
director – “The director yelled ‘Cut!'”
early – “I’m too early for my appointment.”
position  – “Please position your hand properly when drawing.”
player – “That basketball player is cute.”
agree – “I agree! He is cute!”
especially – “I especially like his blue eyes.”
record  – “Can we record the minutes of this meeting, please?”
pick – “Did you pick a color theme already?”
wear  – “Is that what you’re going to wear for the party?”
paper – “You can use a special paper for your invitations.”
special – “Some special paper are even scented!”
space – “Please leave some space to write down your phone number.”
ground  – “The ground is shaking.”
form – “A new island was formed after that big earthquake.”
support  – “I need your support for this project.”
event – “We’re holding a big event tonight.”
official – “Our official wedding photos are out!”
whose  – “Whose umbrella is this?”
matter – “What does it matter anyway?”
everyone  – “Everyone thinks I stole that file.”
center – “I hate being the center of attention.”
couple – “The couple is on their honeymoon now.”
site – “This site is so big!”
end – “It’s the end of an era.”
project – “This project file is due tomorrow.”
hit  – “He hit the burglar with a bat.”
base – “All moms are their child’s home base.”
activity – “What musical activity can you suggest for my toddler?”
star – “My son can draw a star!”
table  – “I saw him draw it while he was writing on the table.”
need  – “I need to enroll him to a good preschool.”
court – “There’s a basketball court near our house.”
produce  – “Fresh farm produce is the best.”
eat – “I could eat that all day.”
American – “My sister is dating an American.”
teach – “I love to teach English lessons.”
oil  – “Could you buy me some cooking oil at the store?”
half – “Just half a liter please.”
situation – “The situation is getting out of hand.”
easy – “I thought you said this was going to be easy?”
cost – “The cost of fuel has increased!”
industry – “The fuel industry is hiking prices.”
figure – “Will our government figure out how to fix this problem?”
face  – “I can’t bear to face this horrendous traffic again and again.”
street  – “Let’s cross the street.”
image – “There’s an image of him stored inside my mind.”
itself  – “The bike itself is pretty awesome.”
phone  – “Plus, it has a phone holder.”
either – “I either walk or commute to work.”
data – “How can we simplify this data?”
cover  – “Could you cover for me during emergencies?”
quite – “I’m quite satisfied with their work.”
picture  – “Picture this: a lake, a cabin, and lots of peace and quiet.
clear – “That picture is so clear inside my head.”
practice – “Let’s practice our dance number.”
piece – “That’s a piece of cake!”
land – “Their plane is going to land soon.”
recent – “This is her most recent social media post.”
describe – “Describe yourself in one word.”
product – “This is my favorite product in their new line of cosmetics.”
doctor – “The doctor is in.”
wall – “Can you post this up on the wall?”
patient  – “The patient is in so much pain now.”
worker – “She’s a factory worker.”
news  – “I saw that on the news.”
test – “I have to pass this English test.”
movie – “Let’s watch a movie later.”
certain  – “There’s a certain kind of magic in the air now.”
north – “Santa lives up north.”
love – ” l love Christmas!”
personal  – “This letter is very personal.”
open – “Why did you open and read it?”
support – “Will you support him?”
simply – “I simply won’t tolerate bad behavior.”
third – “This is the third time you’ve lied to me.”
technology – “Write about the advantages of technology.”
catch – “Let’s catch up soon, please!”
step – “Watch your step.”
baby – “Her baby is so adorable.”
computer – “Can you turn on the computer, please?”
type  – “You need to type in your password.”
attention – “Can I have your attention, please?”
draw – “Can you draw this for me?”
film – “That film is absolutely mind-blowing.”
Republican – “He is a Republican candidate.”
tree – “That tree has been there for generations.”
source – “You are my source of strength.”
red – “I’ll wear a red dress tonight.”
nearly – “He nearly died in that accident!”
organization – “Their organization is doing great things for street kids.”
choose – “Let me choose a color.”
cause – “We have to see the cause and effect of this experiment.”
hair – “I’ll cut my hair short for a change.”
look – “Can you look at the items I bought?”
point  “What is the point of all this?
century – “We’re living in the 21st century, Mary.”
evidence – “The evidence clearly shows that he is guilty.”
window  – “I’ll buy window curtains next week.”
difficult  “Sometimes, life can be difficult.”
listen – “You have to listen to your teacher.”
soon  – “I will launch my course soon.”
culture  – “I hope they understand our culture better.”
billion  – “My target is to have 1 billion dollars in my account by the end of the year.”
chance – “Is there any chance that you can do this for me?”
brother – “My brother always have my back.”
energy  –  “Now put that energy into walking.”
period – “They covered a period of twenty years.”
course  – “Have seen my course already?”
summer – “I’ll go to the beach in summer.”
less – “Sometimes, less is more.”
realize – “I just realize that I have a meeting today.”
hundred – “I have a hundred dollars that I can lend you.”
available – “I am available to work on your project.”
plant – “Plant a seed.”
likely – “It was likely a deer trail.”
opportunity – “It was the perfect opportunity to test her theory.”
term  – “I’m sure there’s a Latin term for it.”
short  – “It was just a short stay at the hotel.”
letter – “I already passed my letter of intent.”
condition – “Do you know the condition I am in?”
choice – “I have no choice.”
place – “Let’s meet out at meeting place.”
single – “I am a single parent.”
rule – “It’s the rule of the law.”
daughter – “My daughter knows how to read now.”
administration – “I will take this up with the administration.”
south – “I am headed south.”
husband – “My husband just bought me a ring for my birthday.”
Congress – “It will be debated at the Congress.”
floor – “She is our floor manager.”
campaign – “I handled their election campaign.”
material – “She had nothing material to report.”
population – “The population of the nearest big city was growing.”
well – “I wish you well.”
call – ” I am going to call the bank.”
economy – “The economy is booming.”
medical -“She needs medical assistance.”
hospital – “I’ll take her to the nearest hospital.”
church  – “I saw you in church last Sunday.”
close -“Please close the door.”
thousand – “There are a thousand reasons to learn English!”
risk – “Taking a risk can be rewarding.”
current – “What is your current address?”
fire – “Make sure your smoke alarm works in case of fire.”
future  -“The future is full of hope.”
wrong – “That is the wrong answer.”
involve – “We need to involve the police.”
defense – “What is your defense or reason you did this?”
anyone – “Does anyone know the answer?”
increase – “Let’s increase your test score.”
security – “Some apartment buildings have security.”
bank – “I need to go to the bank to withdraw some money.”
myself – “I can clean up by myself.”
certainly – “I can certainly help clean up.”
west – “If you drive West, you will arrive in California.”
sport – “My favorite sport is soccer.”
board – “Can you see the board?”
seek – “Seek and you will find.”
per – “Lobster is $20 per pound.”
subject – “My favorite subject is English!”
officer – “Where can I find a police officer?”
private – “This is a private party.”
rest – “Let’s take a 15 minute rest.”
behavior – “This dog’s behavior is excellent.”
deal – “A used car can be a good deal.”
performance – “Your performance can be affected by your sleep.”
fight – “I don’t want to fight with you.”
throw – “Throw me the ball!”
top – “You are a top student.”
quickly – “Let’s finish reading this quickly.”
past – “In the past, my English was not as good as it is today.”
goal – “My goal is to speak English fluently.”
second – “My second goal is to increase my confidence.”
bed – “I go to bed around 10pm.”
order – “I would like to order a book.”
author – “The author of this series is world-famous.”
fill – “I need to fill (up) my gas tank.”
represent – “I represent my family.”
focus – “Turn off your phone and the TV and focus on your studies!”
foreign – “It’s great having foreign friends.”
drop – “Please don’t drop the eggs!”
plan – “Let’s make a plan.”
blood – “The hospital needs people to give blood.”
upon – “Once upon a time, a princess lived in a castle.”
agency – “Let’s contract an agency to help with marketing.”
push – “The door says ‘push,’ not ‘pull.'”
nature – “I love walking in nature!”
color – “My favorite color is blue.”
no – “‘No’ is one of the shortest complete sentences.”
recently – “I cleaned the bathroom most recently, so I think it’s your turn this time.”
store – “I’m going to the store to buy some bread.”
reduce – “Reduce, reuse, and recycle are the ways to help the environment.”
sound – “I like the sound of wind chimes.”
note – “Please take notes during the lesson.”
fine – “I feel fine.”
before – “Before the movie, let’s buy popcorn!”
near – “Near, far, wherever you are, I do believe that the heart goes on.”
movement – “The environmental movement is an international movement.”
page – “Please turn to page 62.”
enter – “You can enter the building on the left.”
share – “Let me share my idea.”
than – “Ice cream has more calories than water.”
common – “Most people can find something in common with each other.”
poor – “We had a poor harvest this year because it was so dry.”
other  – “This pen doesn’t work, try the other one.”
natural – “This cleaner is natural, there aren’t any chemicals in it.”
race – “We watched the car race on TV.”
concern – “Thank you for your concern, but I’m fine.”
series – “What is your favorite TV series?”
significant – “His job earns a significant amount of money.”
similar – “These earrings don’t match, but they are similar.”
hot – “Don’t touch the stove, it’s still hot.”
language – “Learning a new language is fun.”
each – “Put a flower in each vase.”
usually – “I usually shop at the corner store.”
response – “I didn’t expect his response to come so soon.”
dead – “My phone is dead, let me charge it.”
rise – “The sun will rise at 7:00 a.m.”
animal – “What kind of animal is that?”
factor – “Heredity is a factor in your overall health.”
decade – “I’ve lived in this city for over a decade.”
article – “Did you read that newspaper article?”
shoot – “He wants to shoot arrows at the target.”
east – “Drive east for three miles.”
save – “I save all my cans for recycling.”
seven – “There are seven slices of pie left.”
artist – “Taylor Swift is a recording artist.”
away – “I wish that mosquito would go away.”
scene – “He painted a colorful street scene.”
stock – “That shop has a good stock of postcards.”
career – “Retail sales is a good career for some people.”
despite – “Despite the rain, we will still have the picnic.”
central – “There is good shopping in central London.”
eight – “That recipe takes eight cups of flour.”
thus – “We haven’t had any problems thus far.”
treatment – “I will propose a treatment plan for your injury.”
beyond – “The town is just beyond those mountains.”
happy – “Kittens make me happy.”
exactly – “Use exactly one teaspoon of salt in that recipe.”
protect – “A coat will protect you from the cold weather.”
approach – “The cat slowly approached the bird.”
lie – “Teach your children not to lie.”
size – “What size is that shirt?
dog – “Do you think a dog is a good pet?”
fund – “I have a savings fund for college.”
serious – “She is so serious, she never laughs.”
occur – “Strange things occur in that empty house.”
media – “That issue has been discussed in the media.”
ready – “Are you ready to leave for work?”
sign – “That store needs a bigger sign.”
thought – “I’ll have to give it some thought.”
list – “I made a list of things to do.”
individual – “You can buy an individual or group membership.”
simple – “The appliance comes with simple instructions.”
quality – “I paid a little more for quality shoes.”
pressure – “There is no pressure to finish right now.”
accept – “Will you accept my credit card?”
answer – “Give me your answer by noon tomorrow.”
hard – “That test was very hard.”
resource – “The library has many online resources.”
identify – “I can’t identify that plant.”
left – “The door is on your left as you approach.”
meeting – “We’ll have a staff meeting after lunch.”
determine – “Eye color is genetically determined.”
prepare – “I’ll prepare breakfast tomorrow.”
disease – “Face masks help prevent disease.”
whatever – “Choose whatever flavor you like the best.”
success – “Failure is the back door to success.”
argue – “It’s not a good idea to argue with your boss.”
cup – “Would you like a cup of coffee?”
particularly – “It’s not particularly hot outside, just warm.”
amount – “It take a large amount of food to feed an elephant.”
ability – “He has the ability to explain things well.”
staff – “There are five people on staff here.”
recognize – “Do you recognize the person in this photo?”
indicate – “Her reply indicated that she understood.”
character – “You can trust people of good character.”
growth – “The company has seen strong growth this quarter.”
loss – “The farmer suffered heavy losses after the storm.”
degree – “Set the oven to 300 degrees.”
wonder – “I wonder if the Bulls will win the game.”
attack – “The army will attack at dawn.”
herself – “She bought herself a new coat.”
region – “What internet services are in your region?”
television – “I don’t watch much television.”
box – “I packed my dishes in a strong box.”
TV – “There is a good movie on TV tonight.”
training – “The company will pay for your training.”
pretty – “That is a pretty dress.”
trade – “The stock market traded lower today.”
deal – “I got a good deal at the store.”
election – “Who do you think will win the election?”
everybody – “Everybody likes ice cream.”
physical – “Keep a physical distance of six feet.”
lay – “Lay the baby in her crib, please.”
general – “My general impression of the restaurant was good.”
feeling – “I have a good feeling about this.”
standard – “The standard fee is $10.00.”
bill – “The electrician will send me a bill.”
message – “You have a text message on your phone.”
fail – “I fail to see what is so funny about that.”
outside – “The cat goes outside sometimes.”
arrive – “When will your plane arrive?”
analysis – “I’ll give you my analysis when I’ve seen everything.”
benefit – “There are many health benefits to quinoa.”
name – “What’s your name?”
sex – “Do you know the sex of your baby yet?”
forward – “Move the car forward a few feet.”
lawyer – “My lawyer helped me write a will.”
present – “If everyone is present, the meeting can begin.”
section – “What section of the stadium are you sitting in?”
environmental – “Environmental issues are in the news.”
glass – “Glass is much heavier than plastic.”
answer – “Could you answer a question for me?”
skill – “His best skill is woodworking.”
sister – “My sister lives close to me.”
PM – “The movie starts at 7:30 PM.”
professor – “Dr. Smith is my favorite professor.”
operation – “The mining operation employs thousands of people.”
financial – “I keep my accounts at my financial institution.”
crime – “The police fight crime.”
stage – “A caterpillar is the larval stage of a butterfly.”
ok – “Would it be ok to eat out tonight?”
compare – “We should compare cars before we buy one.”
authority – “City authorities make the local laws.”
miss – “I miss you, when will I see you again?”
design – “We need to design a new logo.”
sort – “Let’s sort these beads according to color.”
one – “I only have one cat.”
act – “I’ll act on your information today.”
ten – “The baby counted her ten toes.”
knowledge – “Do you have the knowledge to fix that?”
gun – “Gun ownership is a controversial topic.”
station – “There is a train station close to my house.”
blue – “My favorite color is blue.”
state – “After the accident I was in a state of shock.”
strategy – “Our new corporate strategy is written here.”
little – “I prefer little cars.”
clearly – “The instructions were clearly written.”
discuss – “We’ll discuss that at the meeting.”
indeed – “Your mother does indeed have hearing loss.”
force – “It takes a lot of force to open that door.”
truth – “Please tell me the truth.”
song – “That’s a beautiful song.”
example – “I need an example of that grammar point, please.”
democratic – “Does Australia have a democratic government?”
check – “Please check my work to be sure it’s correct.”
environment – “We live in a healthy environment.”
leg – “The boy broke his leg.”
dark – “Turn on the light, it’s dark in here.”
public – “Masks must be worn in public places.”
various – “That rug comes in various shades of gray.”
rather – “Would you rather have a hamburger than a hot dog?”
laugh – “That movie always makes me laugh.”
guess – “If you don’t know, just guess.”
executive – “The company’s executives are paid well.”
set – “Set the glass on the table, please.”
study – “He needs to study for the test.”
prove – “The employee proved his worth.”
hang – “Please hang your coat on the hook.”
entire – “He ate the entire meal in 10 minutes.”
rock – “There are decorative rocks in the garden.”
design – “The windows don’t open by design.”
enough – “Have you had enough coffee?”
forget – “Don’t forget to stop at the store.”
since – “She hasn’t eaten since yesterday.”
claim – “I made an insurance claim for my car accident.”
note – “Leave me a note if you’re going to be late.”
remove – “Remove the cookies from the oven.”
manager – “The manager will look at your application.”
help – “Could you help me move this table?”
close – “Close the door, please.”
sound – “The dog did not make a sound.”
enjoy – “I enjoy soda.”
network – “Band is the name of our internet network.”
legal – “The legal documents need to be signed.”
religious – “She is very religious, she attends church weekly.”
cold – “My feet are cold.”
form – “Please fill out this application form.”
final – “The divorce was final last month.”
main – “The main problem is a lack of money.”
science – “He studies health science at the university.”
green – “The grass is green.”
memory – “He has a good memory.”
card – “They sent me a card for my birthday.”
above – “Look on the shelf above the sink.”
seat – “That’s a comfortable seat.”
cell – “Your body is made of millions of cells.”
establish – “They established their business in 1942.”
nice – “That’s a very nice car.”
trial – “They are employing her on a trial basis.”
expert – “Matt is an IT expert.”
that – “Did you see that movie?”
spring – “Spring is the most beautiful season.”
firm – “Her ‘no” was very firm, she won’t change her mind.”
Democrat – “The Democrats control the Senate.”
radio – “I listen to the radio in the car.”
visit – “We visited the museum today.”
management – “That store has good management.”
care – “She cares for her mother at home.”
avoid – “You should avoid poison ivy.”
imagine – “Can you imagine if pigs could fly?”
tonight – “Would you like to go out tonight?”
huge – “That truck is huge!”
ball – “He threw the ball to the dog.”
no – “I said ‘no,’ please don’t ask again.”
close – “Close the window, please.”
finish – “Did you finish your homework?”
yourself – “You gave yourself a haircut?”
talk – “He talks a lot.”
theory – “In theory, that’s a good plan.”
impact – “The drought had a big impact on the crops.”
respond – “He hasn’t responded to my text yet.”
statement – “The police chief gave a statement to the media.”
maintain – “Exercise helps you maintain a healthy weight.”
charge – “I need to charge my phone.”
popular – “That’s a popular restaurant.”
traditional – “They serve traditional Italian food there.”
onto – “Jump onto the boat and we’ll go fishing.”
reveal – “Washing off the dirt revealed the boy’s skinned knee.”
direction – “What direction is the city from here?”
weapon – “No weapons are allowed in government buildings.”
employee – “That store only has three employees.”
cultural – “There is cultural significance to those old ruins.”
contain – “The carton contains a dozen egges.”
peace – “World leaders gathered for peace talks.”
head – “My head hurts.”
control – “Keep control of the car.”
base – “The glass has a heavy base so it won’t fall over.”
pain – “I have chest pain.”
apply – “Maria applied for the job.”
play – “The children play at the park.”
measure – “Measure twice, cut once.”
wide – “The doorway was very wide.”
shake – “Don’t shake the can of soda.”
fly – “We can fly to France next year.”
interview – “My job interview went well.”
manage – “Did you manage to find the keys?”
chair – “The table has six matching chairs.”
fish – “I don’t enjoy eating fish.”
particular – “That particular style looks good on you.”
camera – “I use the camera on my phone.”
structure – “The building’s structure is solid.”
politics – “Mitch is very active in politics.”
perform – “The singer will perform tonight.”
bit – “It rained a little bit last night.”
weight – “Keep track of your pet’s weight.”
suddenly – “The storm came up suddenly.”
discover – “You’ll discover treasures at that thrift store.”
candidate – “There are ten candidates for the position.”
top – “The flag flies on the top of that building.”
production – “Factory production has improved over the summer.”
treat – “Give yourself a treat for a job well done.”
trip – “We are taking a trip to Florida in January.”
evening – “I’m staying home this evening.”
affect – “My bank account will affect how much I can buy.”
inside – “The cat stays inside.”
conference – “There will be expert presenters at the conference.”
unit – “A foot is a unit of measure.”
best – “Those are the best glasses to buy.”
style – “My dress is out of style.”
adult – “Adults pay full price, but children are free.”
worry – “Don’t worry about tomorrow.”
range – My doctor offered me a range of options.
mention – “Can you mention me in your story?”
rather – “Rather than focusing on the bad things, let’s be grateful for the good things.”
far – “I don’t want to move far from my family.”
deep – “That poem about life is deep.”
front – “Please face front.”
edge – “Please do not stand so close to the edge of the cliff.”
individual – “These potato chips are in an individual serving size package.”
specific – “Could you be more specific?”
writer – “You are a good writer.”
trouble – “Stay out of trouble.”
necessary – “It is necessary to sleep.”
throughout – “Throughout my life I have always enjoyed reading.”
challenge – “I challenge you to do better.”
fear – “Do you have any fears?”
shoulder – “You do not have to shoulder all the work on your own.”
institution – “Have you attended any institution of higher learning?”
middle – “I am a middle child with one older brother and one younger sister.”
sea – “I want to sail the seven seas.”
dream – “I have a dream.”
bar – “A bar is a place where alcohol is served.”
beautiful – “You are beautiful.”
property – “Do you own property, like a house?”
instead – “Instead of eating cake I will have fruit.”
improve – “I am always looking for ways to improve.”
stuff – “When I moved, I realized I have a lot of stuff!”
claim'''
