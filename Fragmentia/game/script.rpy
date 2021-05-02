$ bl_game = False
#default BestEnd = 0

label start: 
    
    #$ bl_game = False
    #default BestEnd = 0
    
    #window hide 
    #nvl clear 
    
    #Do an ear ringing sound that fades out as the screen goes from white to the room?
    
    scene black with slowf
    
    play music "audio/music/Kevin_MacLeod_-_Clean_Soul.mp3"
    #play music "audio/music/M01 Stars.ogg"
    
    play environment "audio/background/Car driving.ogg" fadein 2.0
    
    scene sky016 with slowd
    
    
    #"«бла-бла»"
    
    #play music "audio/music/Kevin_MacLeod_-_Clean_Soul.mp3"
    #play music "audio/music/M01 Stars.ogg"
    
    #play environment "audio/background/Car driving.ogg" fadein 2.0
    
    #"I stare out of the window, the sky somewhat beautiful tonight."
    
    #"I lean my elbow on the door and stare out of the window."
    
    #scene black with slowd
    
    #centered "My parents are arguing again. I asked them where we're going but they wouldn't say." with slowd
    

    
    t"I rest my head against the window; the vibrations allow for a wave of comfort as I gaze into the stars." with slowd
    
    #t"The window's vibrations allow for a wave of comfort as I gaze into the stars."
    #l
    
    
    t"The view is beautiful, the night sky bereft of clouds."
    
    
    t"There's just something about the stars; they appear so timeless, so still."
    
    
    t"But in the bigger picture that's far from the truth. They're individual solar systems orbiting our galaxy too. "
    
    t"As for timeless, many stars have deceased by the time their light has reached Earth." 
    
    t"Will I echo beyond my death in such a way?" 
    
    nvl clear 
    
    t"It makes me wonder where life is taking me." 
    
    #t"I'm like a cog in the smaller picture, controlled by the force of the lever."
    t"I'm a cog in the smaller picture, coerced by momentum."
    #mentioning moved by other cogs?
    
    
    #t"I'm like a miniature cog in my own smaller picture, controlled by the flow of the one who turns the lever."
    
    
    stop music fadeout 3.0
    
    
    #pause 2.0
    
    #t"A jarring screech sinks my heart into my stomach..."     #with dissolve
    #pause 1.5
    window hide 
    nvl clear 
    
    centered "A jarring screech sinks my heart into my stomach..." with dissolve
    
    #"My heart drops to my stomach as I hear an approaching screech, my body clenches tight to itself in anticipaion."
    
    stop environment fadeout 2.6
    play sound "audio/sfx/Crash.mp3"
    
    show text "My body clenches to itself in anticipation." at truecenter with dissolve
    pause 1.0
    hide text with dissolve
    
    #"My heart drops to my stomach as I hear an approaching screech, my body clenches tight to itself in anticipaion. {p=2.0)"
    
    scene black
    show blood
    
    
    play environment "audio/sfx/Ear Ringing Sound Effect.mp3" fadein 4.1
    scene white with wd
    #play music "audio/music/Anxiety.mp3" fadein 2.0
    stop environment fadeout 2.0
    stop sound fadeout 2.0
    play music "audio/music/Awkward Meeting.mp3" fadein 2.5
    
    "Blinding light stings my eyes."
    
    wv"\"Doctor, he's stirring!\""
    
    #"I feel a presence, it grows so close that I can feel their breath on my cheek."
    
    #"Scrambling footsteps surround me."
    
    #"I'm surrounded by the sound of scrambling footsteps."
    
    
    "Footsteps scramble around me."
    
    scene hospital10_day with slowd
    
    
    
    #"Managing a squint, my gaze flitters along a line of foreign faces, coming to rest on the one closest."     
    "I manage a squint." 
    
    "My gaze flitters along a line of foreign faces, coming to rest on the one closest."     
    
    #dd"\"It's a relief to see you awake, and so soon.\""
    
    dd"\"Can you tell me your name?\""
    
    "My name? My name..." 
                        
    "Where am I?!"
    
    #"I rise to a surge of panic, but crippling agony rips a cry from my throat and wrestles me into submission."
    #"I rise to a surge of panic, but the movement rips a scream of agony from my throat and wrestles me into submission."
    "Seized by panic, I rise; the movement rips a groan of agony from my throat and wrestles me into submission."
    #Ripping a scream of agony from my throat.
    
    "My lungs collapse to the pain of every breath."
    
    "I. Can't. Breathe!"
    
    #My hands search my throat. 
    
    #"Dark dread shoots up my spine. My body trembles as the world seems to fade into the backdrop."
    #"Dark dread shoots up my spine. My trembling body and screaming mind drown out the world around me."
    #My mind screaming, drowning the world out. 
    #"Dark dread shoots up my spine. My body trembles, swirling darkness enshrouds my mind as the world fades away."
    #"Panic shoots up my spine. My trembling body rocks the bed; a dark dread enshrouds the world around me."
    #A dark dread enshrouds my mind as the world fades away."
    
    # swirling darkness enshrouds my mind as I begin to fade
    
    #"I gasp to push down the rising panic, but it tenfolds." 
    #"I gasp for air but it gets stuck in my throat."    
    "I gasp for air and choke, reaching out to the doctor with curling fingers; he gestures orders to his colleagues."
    
    
    #"I reach out to the doctor with curling fingers; he gestures orders to his colleagues."
    
    dd"\"He's going into shock!\""
    
    #"The world around me consumed by dread."
    "Dread consumes the world around me."
    
    #"Am I dead?"
    
    #"No, I can't be. I'm in too much pain. "
    
    #stop music fadeout 2.0
    
    #lapse 2??? You have forgotten what the doctors have spoken about.
    #Don't recognise a man who barges in, yet he adresses you as Peter and claims he's your uncle. You'll forget about doctors and when he asks about your memory and you're dumbfounded, he's relieved.
    #Keep this scene for introducing the uncle. NEEDS WORK
    scene hospital10_evening with slowf
    #Will you forget the initial meeting with the doctors? Well, at leas forget them. Then you have to play amnesia to the uncle. 
    "When I wake, the doctor from earlier is examining me."
    
    "It would feel intrusive but for his drawn eyes and worried frown."
    
    "Knowing I'm awake, he leans closer."
    
    #dd"\"I'm glad to see you're awake, and so soon. Can you tell me who you are?\""
    dd"\"Are you OK?\""
    
    mm"\"Who... are you?\""
    
    "My voice strained and dislocated; it hurts to breathe too deep."
    
    dg "\"I'm Doctor Gerald. I'm glad to see you're awake, and so soon.\""
    
    dg "\"Can you tell me your name?\""
    
    #mm "\"...\""
    
    #"My... name? It stirs up anxiety; I know the definition, but... why don't I know my name?"
    "My... {i}name...?{/i}"
    
    mm "\"I... can't.\""
    
    "He pulls a clipboard from the side and scribbles frantically."
    
    dg "\"Do you remember what happened?\""
    
    "I can only shake my head. His frown tightens."
    
    dg "\"You were in a terrible car collision.\""
    
    "He takes a deep breath, as if performing a rehersal."
    
    dg "\"I sincerely regret to inform you...\""
    
    "His features fall and his gaze rests on the ground."
    #"His features fall along with his gaze."
    
    dg"\"...Your parents are dead.\""
    
    #dg "\"I offer my sincerest condolences.\""
    
    #"There's no impact. Though, I know there should be."# And not because it sounded so rehearsed."
    
    "His delivery suggests impact, but I have nothing."
    
    #My family... gone. 
    "I turn from his grave expression and lift up my gown."
    
    #"My ribs swollen; bruises descend down my side, ranging from hues of bright blue to deep purple."
    #"Bruises descend from my breast to my waist; hues ranging from bright blue to deep purple."
    "Bruises descend my ribcage, hues ranging from bright blue to deep purple."
    
    "My left leg enveloped in a thick cast."
    
    mm "\"What's my... name?\""
        
    #"My leg is in excruciating pain and every breath makes my ribs feel like they'll shatter if I were to breathe too deep."
    
    #"I lift up my gown and take in the sight for the first time. My ribs swollen, bruises descend down my side; ranging from hues of bright blue to deep purple." #patches
    
    #"Amidst awaiting the results and my uncle, I wonder which will arrive first. The only thoughts I have to try and take my mind from the pain."
    
    
    #bang
    "A man bursts into the room with a panicked expression."
    
    q"\"Peter!\""
    
    "His erratic entrance drawn to a stupor as he takes in the sight of me."
    
    "It takes a moment to realise he's addressing me.{w} My... name...{w} {i}Peter.{/i}"
    
    #p"\"Are you... my uncle?\""
    
    #"His face contorts with his nod."
    
    
    
    p"\"W-who... are you?\""
    
    q"\"It's me, your Uncle Benjiro.\"" 
    
    #"He lurches forward, his hand searching the inside of his jacket." #fingers curling around his jacket." #hands patting his jacket. 
    #"He lurches forward. His hand clutching the hem of his jacket."
    "He lurches forward, hand fumbling inside his jacket."
    
    
    b"\"Do you not recognise me?\"" 
    
    #b"\"Are you OK? They've told me that you've lost your memories, but I didn't believe them. Do you remember anything?\""
    #"He continues before giving me chance to respond."
    "He continues before I have the chance to respond."
    #"His words pour forth like a torrent."
    
    b"\"Are you OK? I...\""
    
    "His voice cracks. He musters a breath and masters himself."
    
    b"\"After hearing the news... I'm just glad you're OK.\""
    
    p"\"It hurts... so much. I can't... remember anything.\"" 
    
    "Relief washes over his features; his fingers caress my cheek." 
    
    b"\"I'm just glad you're OK...\""
    
    b"\"I'm always here for you. My home is yours when you're fit to leave.\""
    
    #p"\"But... he said I lost my family.\""
    
    #b"\"Don't worry, I'm your family. I'll always be here for you.\""
    
    "His reassurance makes me feel a little better, but only because of how lost I feel."
    
    dg "\"I'm sorry to spoil the reunion, but it could take months, even years before he's ready.\""
    
    dg "\"It appears Peter is suffering from some form of amnesia.\""
    
    
    
    
    
    
    
    
    stop music fadeout 2.0
    
    scene black with slowf
    
    centered "Nine months later." with dissolve #pass
    
    #play music "audio/music/bensound-november.mp3"
    
    play music "audio/music/myuu - Prey -Reprise-.mp3" fadein 3.0
    
    scene room_living14_day with slowf
    
    
    
    "I wake up everyday, nothing to rise for."
    
    "I manoeuvre my slouch towards the TV, knocking over a few empty cans as I locate the remote."
    
    "The drab titles protest with snippets of picture and audio."
    
    "Nothing. Nothing until the end of channels."
    
    #"I sigh, resting my gaze on the monotonous ceiling."
    
    "I rest my gaze on the ceiling and sigh."
    
    tv"\"Another bank robbery has taken place, this time in the city of Bristol.\""
    
    "It grabs my interest." 
    
    #"That's our local city. My uncle sometimes goes for our groceries and provisions."
    #"That's our local city, my uncle visits once a week for groceries and provisions."
    "That's our local city; my uncle shops there."
    
    tv"\"Authorities haven't confirmed whether it's a succession to the—\""
    
    b"\"Bored?\""
    
    "His voice rips my attention from the broadcast. How long has he been stood there?"
    
    #"He's scanning the mess that envelops my vicinity. I already know what's coming next."
    
    "He scans the surrounding mess. {i}Here we go.{/i}"
    
    b"\"How do you live like this?\""
    
    "{i}I don't. I exist like this.{/i}"
    
    b"\"What did I tell you to do yesterday?\""
    
    p"\"To clean up, but I couldn't sleep last night.\""
    
    "He points a furrowed brow that seems to say, \"{i}can you ever?{/i}\""
    
    b"\"I specified in the morning.\""
    
    p"\"I'll clean up later, OK?\""
    
    b"\"You realise you're due to start school in a week, right?\""
    
    #Make an argument about his work and drinking?
    #"I wince as he examines his watch."
    #"The examination of his watch draws a wince from me."
    "He inspects his watch, drawing a wince from me."
    
    #b"\"You're still waking up mid-afternoon and doing nothing.\"" 
    
    b"\"It's half-one in the afternoon for Christ's sake.\""
    
    #"I know it's a jab because he thinks that I haven't left the house in weeks." 
    #"But unbeknownst to him, I've been going out to the park late at night. When there's no people around."
    #"Although, last week when he was out I went to the park late in the night. When it was quiet, when no people were around."
    
    p"\"Aren't you at work today?\""
    
    "Annoyance drips into my tone. He sighs, kneading his temples."
    
    b"\"No, it's Saturday.\""
    
    
    p"\"Oh.\""
    
    "I shrug; it's not unusual for me to lose track of the day."
    #I'm expecting that to be the end of that
    #"I feign interest on the TV but he places himself on the couch next to me." but I couldn't care less." 
    "I feign interest in the report, hoping he'll leave."
    
    "But he places himself on the couch next to me."
    #"But he places himself next to me on the couch."
    
    
    #"So close that I have to shuffle over due to a slight odour of alcohol. Has he been drinking?"
    
    "I shuffle to the arm due to the odour of stale alcohol and remnant perfume." 
    
    "Come to think of it, I didn't hear him return last night—he must've been out all night drinking again." 
    
    #"I'd forgotten he returns from working away today."
    
    #"Come to think of it, I don't recall him returning last night." 
    #press to the arm I have to shuffle over 
    
    b"\"Peter, we need to talk.\""
    
    #"My fingers instinctively curl into the cushion. The first topic that springs to mind is my parents."
    
    "My fingers flex into the cushion."# arm." 
    
    #"The first topic springing to mind: my parents." 
    
    p"\"About... my...?\""
    
    "He's mentioned so little; their deaths have been a looming shadow."
    
    "I wasn't even able to attend their funeral in my first month in hospital..."
    
    b"\"No.\""
    #This is something I've withheld.
    #"A flat dismissal."
    "He dismisses it again. A taboo subject."
    
    b"\"You're no longer going to attend a local school or live here with me.\""
    
    #"He continues despite my shock."
    "I gasp, but he continues."
    
    b"\"I've arranged for you to move into a boarding school up north.\""
    
    "My stomach sinks." #; it's like he's shattered something inside me." 
    
    "Not only did he lie about the school..." #show
    
    p"\"But... you said you'd be here for me.\""
    
    p"\"You should've told me. Why didn't I get a say in this?\""
    
    "He graces my shoulder with a few awkward pats."
    
    b"\"I'm afraid I have too much work. I'll be unable to care for you.\""
    
    
    #"He says it so matter-of-factly, it's clear that I have little choice in the matter."
    
    #"\"Not like you did anyway,\" I refrain from relaying."
    
    "{i}Not like you cared anyway.{/}"
    
    #independently
    p"\"I can motivate myself and attend school here.\""
    #you didn't even tell me? 
    b"\"Then you'll be fine living on your own in dorms, right?\""
    
    "It's annoying that he's right, that I can't find a legitimate reason..."
    
    #b"\"It'll be better for you to meet new people, y'know. It'll do you no good to continue living like you are.\""
    b"\"It'll be better for you to get out into the world and meet new people, y'know.\""
    
    b"\"It'll do you no good to continue living like this.\""
    
    "That only serves to piss me off further. He suggested that I take the remainder of the school year off."
    
    #"As mad as I am at him, as much as I want to disagree, I know deep down that he's right."
    
    p"\"I can still do that here, though.\""
    
    b"\"No, you can't.\"" # I won't allow it.\""
    
    "His tone suggest it's his way. {i}It's always his way.{/i}"
    
    p"\"You're such an arsehole; I can't believe I trusted you.\""
    
    #p"\"You're such an asshole, I can't believe I trusted you.\""
    
    "A sharp regret strikes before the words leave my lips."
    #finish rolling off my tongue."
    #had finished
    "He shoots to his feet."
    
    b"\"Believe me, this is the best thing for you. {w}The best thing for me.\"" 
    
    "His words slice in a seething calm."
    
    #"I'm speechless, too startled to respond. Either way, it's clear I have little say in the matter."
    
    
    
    b"\"So get yourself packed and ready, you'll be leaving next week.\""
    
    "His glare flitting between me and my mess."
    
    b"\"Clean this shit up.\""
    
    b"\"I'm going to bed.\""
    
    stop music fadeout 3.0
    
    #Maybe the uncle didn't directly kill your parents, but he knew who did and knew that they had to die, 
    #He appreciated that you had no memories, as he could keep you alive. 
    
    #Hiraeth, a word from the neighboring country, Wales. It means to miss a home that you can never return to or maybe it never was to begin with. 
    #An apt word for the constant longing, even at my uncle's house I never felt truly at home. I know I won't find it where I'm going, either. 
    
    #I watch as the buildings and traffic rush past the window, leaving behind the fields and streams of the countryside. It seems to mark a shift, 
    
    play environment "audio/background/trainsound.ogg" fadein 4.0 
    
    #I find myself on the train late as I woke up far too late. 
    scene train with longf
    
    #mention the anxiety of being in a vehicle, which you did tbh.
    
    #"The rhythmic rotations of the train tracks seems to build anxiety, each rotation inflates it like a balloon."
    
    #p"\"I'm heading into my new life.\""
    #"I murmur to myself to see if the realisation will set in. {w}It doesn't."
    #"I can't seem to feel much of anything, not past this underlying unease. But that's always been there. "
    #"Still, this is a chance I would often dream of when languishing on that couch."
    #"A chance to start living, a chance to make friends. A chance to find me."
    #"But even though I left on somewhat good terms with my uncle, it's tainted by his words."
    #"Best thing for him?{w} To get rid of me?"
    #"Though, I don't blame him. I've been nothing but a burden."
    
    "There are a few people scattered across the seats. I'm just thankful they're out of view."
    
    #"My book's lay open on my lap, the words left begging. My mind too distant to read."
    "My book's lying across my lap—the words left begging. My mind too distant to read."
    
    "Every rotation inflates my anxiety like a balloon."
    
    "They say be careful what you wish for."
    
    #"I wished to get off that couch. To do something with my time. To... meet new people."
    #"I wished to get off that couch. To do something with my time, to... make friends."
    #"I wished to get off that couch. To do something with my time, to... start a new life."
    #"I wished to get off that couch. I wished to meet people, to do something with my time, to... start a new life."
    
    "I wished to get off that couch." 
    
    "I wished to meet people." 
    
    "I wished to do something more with my time."
    
    "I wished... {w} {i}I could start a new life.{/i}"
    
    "Yet, here I am, dreading the opportunity."
    
    "Though I left on good terms with my uncle, his words fester."
    
    "Best thing for him...{w} {i}to get rid of me?{/i}"
    
    "I don't blame him. I've been nothing but a burden."
    
    
    #"The chime signals the next stop. People flood into the train,  
    
    #"Life soon catches up, time soon passes by. I find myself on the dreaded train journey."
    #"With little else to do, I rest my head against the window. The vibrations are peculiarly pleasant."
    
    #"With little else to do, I rest my head against the window hoping to salvage solace."
    "I press my cheek to the window, the vibrations offer solace." # temporary
    
    
    #"The vibrations are pleasant. Like a long lost feeling." 
    
    #"Nostalgia?{w} No, it can't be."
    
    "But buildings and traffic now rush past the window, having left behind the fields and streams of the countryside." 
    
    "It marks a shift; I'm already losing what little I'd come to know."
    
    "Somehow, it all seems so familiar."
    #"It seems to mark a shift; I'm already losing what little I had come to know."
    
    #"Hiraeth. A word from my neighboring country, Wales." 
    
    #"A homesickness for a home that you can never return to, or that never existed to begin with; nostalgia, yearning and grief for the lost places of your past."
    
    #"I can't help but feel that I'm the personification of that word." 
    
    #"Even at my uncle's house I never felt truly at home and I know that it doesn't await, either."
    
    
    #Black screen here?
    
    "..." #with slowd
    
    #"A examination of my phone reveals there's three hours left of the train journey."
    #"I examine my phone..." #and estimate the remaining time of the journey..." 
    
    #"I check the time on my phone."
    
    #"Three hours left to stew in my thoughts."
    
    "The time on my phone reveals three more hours left of this journey."
    
    "{i}The joy.{i}"
    
    stop environment fadeout 3.0
    
    
    #City scene
    
    play environment "audio/background/Rain.ogg" fadein 3.0
    #play environment2 "audio/background/city.mp3" fadein 3.0
    #play music "audio/music/bensound-tomorrow.mp3" fadein 3.0
    play music "audio/music/bensound-betterdays.mp3" fadein 3.0
    #play music "audio/music/Aiden track.mp3" fadein 3.0
    
    scene residentroad004_night_light_rain with longf
        
    
    #station bg
    
    "I'm greeted by a smog of car fumes and cigarette smoke."
    
    #"I'm surrounded by offenders, who share the small shelter at the entrance of the train station."
    "The offenders surround me, sharing the small shelter at the entrance."
    
    "The downpour has people scrambling to their taxis. I yearn for a prompt arrival as they pull off."
    
    "But I was forced to travel by train from the hospital, after having a panic attack in my uncle's car."
    
    "The image of the backseat sinks into my stomach and bile rises to my throat."
    #from the backseat 
    
    
    #play environment3 "audio/sfx/Ear Ringing Sound Effect.mp3" fadein 4.0
    #play environment4 "audio/sfx/heartbeat.mp3" fadein 4.0
    #scene residentroad004_night_light_rain2 with longd
    #scene residentroad004_night_light_rain with slowd
    #stop environment3 fadeout 2.0
    #stop environment4 fadeout 2.0
    
    #"Just thinking about being on the back seat brings a lump to my throat."
    #"Just thinking of the back seat brings bile to my throat."
    #bring bile
    #"I choke it back and shake the thought, pulling the makeshift directions from my pocket."
    "I swallow the lump and shake the thought, pulling the makeshift directions from my pocket."
    #swallow lump?
    "I travelled the journey via Duudle Maps, recording street names as I scrolled through."
    
    "The end result is a list of street names and little sense of direction—the map's images taken in daylight."
    
    "I shoulder my duffle bag and extend the handle on my suitcase. The wheels protest in my wake..."
    # on hind wheels
    #"Rain rolls down my forehead and drips from my chin. The growing pollution fails to sate my lungs' appetite for air."
    
    #"I'm greeted by a miasma comprised of traffic fumes and cigarette smoke as I exit the station." 
    
    #"I'm surrounded by offenders. Heavy traffic on the roads and smokers sharing the small shelter at the entrance of the train station." 
    
    #"The downpour has people scrambling to their destinations, almost as chaotic as the traffic."
    
    #"I'm usually somewhat fond of the rain, but I wouldn't class this as an ideal scenario."
    
    #"I take what I convinced myself were adequate directions from my pocket." 
    
    #"Kicking myself for only writing down a list of street names and convincing myself that I'd remember the way from doing the journey on Goodle maps. "
    
    #"I travelled the journey via Duudle maps, writing down the street names as I progressed."
    
    #"The images in street view were all compiled in the day, too. Leaving me all the more stranded."
    
    #"I ready myself. Thankful that I at least remember to turn right from the station."
    
    #"I heave my duffle bag over my shoulder and grip the handle to my suitcase, which begins to noisily protest on its hind wheels."
    
    #"With little else to go off, I shoulder my duffle bag and extend the handle on my suitcase; its hind wheels protesting in my wake."
    play environment2 "audio/background/city.mp3" fadein 3.0
    scene street003_night_light_rain with longf
    
    #"The city is intimidating, information overload after living like a hermit for the past year."
    
    #"The city is intimidating, sensory overload after living like a hermit."
    
    
    "Though I've seen it a thousand times on TV, I feel lost and insignificant immersed within the metropolis."
    
    #"It almost feels... unreal."
    
    
    
    #"Faceless buildings tower up into the grey-painted sky, adorned in advertisements and posters embellished by model faces applying mascara, couples frolicking on the grass on a hot summer's afternoon and gritty alpha males emerging from explosions." 
    #"Commercial buildings rise into the grey-painted sky, adorned by advertisements; I note the model faces applying mascara, blissful couples frolicking in the sun, and gritty alpha-males emerging from explosions."
    "Commercial buildings rise into the grey-painted sky, adorned with advertisements; model faces apply mascara, blissful couples frolic in the sun, and gritty alpha-males emerge from explosions."
    
    #"And my uncle has told me that I don't live in the real world."
    
    #"Neon signs allure my eyes to numerous entrances, they seem to swallow the bustling people."# Refuges from the rain."
    
    #"When my gaze descends, the neon signs allure my eyes to numerous entrances; they seem to swallow the bustling people."# Refuges from the rain."
    
    "When my gaze descends, neon lights attract my eyes to numerous entrances." 
    
    "They seem to swallow the bustling people."
    
    #"Neon signs above numerous entrances allure the eyes, which seem to swallow the bustle of people."
    
    #I've seen it a thousand times on TV, but I'm semblant within the scene. 
    
    
    
    
    #"They're much like the buildings I've seen a thousand times on TV, but I feel so small and insignificant actually being amongst them and the people."
    
    #"The bustle of people in the door ways, the traffic mostly inwards to seek shelter from the rain."
    
    #"I couldn't deny that's one appeal to why I like the rain."
    
    scene street001_night_light_rain with longf
    
    #"At least the rush of people has dissipated, but It's mostly just condensed into safe spaces."
    
    "When I observe people, I realise how alone I really am."
    #"When I observe people, it makes me realise how alone I've really been."
    
    "Smokers pour from bars and pubs, sharing banter and laughter."
    #haughty
    "Couples walk by, sharing the shelter of their umbrellas. "
    
    "And others share the refuge of the bus stops; their faces gloomy and impatient, merging into the scene."
    
    #"I share only the rain's embrace." 
    
    #"I only share the rain's embrace." 
    
    
    #"I feel as though they're all watching, judging me. Their gazes weighing down on me."
    
    #"I walk alone, feeling alien in the scene." #I share incessant 
    
    "I stop to switch the weight on my shoulder. I feel their stares." #demurring 
    
    #"Their gazes a burden; as heavy, if not heavier than my luggage." 
    #"Their gazes a burden, as heavy—if not heavier—than my luggage."
    "Their gazes a burden, as heavy as—if not heavier than—my luggage."
    
    #"Their thoughts; they think that I'm weird. They know that I'm different."
    
    #arriving at school scene 
    
    play environment "audio/background/Rain.ogg"
    stop environment2 fadeout 3.0
    #play music "audio/music/bensound-tomorrow.mp3"
    stop music fadeout 3.5
    
    scene school_out003_night_light_rain with slowf
    
    #"I approach the school complex, thankfully underestimating my makeshift directions and... my memory."
    "I approach the school complex, thankful to underestimate my makeshift directions."
    
    #"Though, the main building acts as a beacon from the outskirts of the city."
    
    #"As I'm switching the duffle bag to my other shoulder for the umpteenth time, a guard approaches."
    "As I stop to rotate my luggage again, a weathered man approaches in a guards uniform." 
    

    # a guard approaches."
    # what feels the fifth 
    
    "His smile wrinkles to his eyes lined with age."
    
    #"The greying guard approaches the gate as I draw near."
    
    g"\"New arrival, I see.\""
    
    #His voice as withered as he is."
    
    p"\"Yeah...\""
    
    "Rain trickles from the rim of his guard's cap." #lopsided guard's peaked 
    
    g"\"Welcome to SunnyVale.\""
    
    ##
    "It extracts a wry smile as I wipe rain from my brow."
    #"It extracts a wry smile as I wipe my sleeve across my brow."
    
    g"\"What's your name?\""
    
    p"\"Peter Enning.\""
    
    #"He swipes a pen across his device, punctuating with a final stab."  
    "He swipes a pen across his device and punctuates with a final stab." 
    
    g"\"I'll take you to reception.\""
    
    "I gather my belongings and prepare to follow."
    
    #"He contacts another guard to relieve him of the gate before leading the way.{w} Slowly."
    "He contacts another guard to relieve him of the gate. {w}Who arrives before we're even ten feet into the grounds..."
    
    scene school_out009_night_light_rain with slowd
    
    "My shoulder screams for him to hurry..."
    
    stop environment2 fadeout 3.0
    stop environment fadeout 3.0
    stop music fadeout 3.0
    
    #You meet a guard at the front gate who escorts you to the main building. Then they find out that they're unable to make you a key card without the knowhow.
    #Luckily, they'll find somebody who can and escort me to my room. 
    
    #school scene 
    
    scene school_in001_night_light with slowf
    
    g"\"I'll go and find Cheryl for you. I won't be a moment.\""
    
    "I stare after him, following his trail of glistening raindrops."
    
    "The word \"slug\" springs to mind."
    #"\"Slug\" springs to mind."
    
    # in his wake
    "When he turns the corner, I'm left to the room."
    
    "Pamphlets and notices adorn the back wall, leading to the kiosk with no receptionist; seats situated around the two large pillars through the centre."
    
    #"I take a seat, grateful to rest my luggage and knead the knots in my aching shoulders."
    
    "I rest my luggage and slump myself along a row of seats, kneading the knots from my aching shoulders."
    #seizing the opportunity to 
    "The TV displays pictures of students. They perform tasks that don't merit their candid smiles."
    
    "I mean, who smiles whilst studying?"
    
    #"I mean, in what world do people smile when they study?"
    
    #"I'm soon distracted by doubtful shouting in the back, which accounts for the apologetic expression when he re-emerges."
    
    "I'm distracted by shouting in the back; he re-emerges with an apologetic smile." #which accounts for the apologetic expression when he re-emerges."
    
    "I rise to my feet, trying to impede his view of the damp stain across the chairs."
    
    g"\"I'm ever so sorry. You've just missed the lady who operates the machine for your card-key.\""
    
    "I sigh despite myself." 
    
    "It's my fault. I was supposed to catch the train by noon but I was still asleep."
    
    #"Despite myself, my sigh is audible."
    #"Despite myself, I manifest a sigh."
    #"I sigh despite myself."
    
    #"Useless.{w} Like me."
    
    #"Despite myself, I sigh audibly."
    
    p"\"Card-key?\""
    
    g"\"They're a staple of the school. They allow for access and identification, effectively replacing the bog-standard uniform.\""
    
    "Great. So not only am I stuck here, I have nowhere to stay."
    
    "I'll admit—even in the circumstances—I'm relieved I don't have to conform to a uniform."
    #It would feel like a lie. 
    "I'd appear like everybody else, despite knowing I'm... {i}different.{/i}"
    
    #"They have lives; they have dreams; they have... memories."
    
    "{i}They have lives... dreams... {w}memories...{/i}"
    
    p"\"Oh.\""
    
    "He takes in my sunken features and offers a smile."
    
    g"\"Don't worry, I won't leave you to die in here.\""
    
    "He draws a smile from me, which I'm quick to extinguish."
    
    g"\"I'll contact Cheryl. I'm sure she hasn't gone too far.\""
    
    p"\"Thank you.\""
    
    
    scene hospital03_day with slowf
    
    "Cheryl saved the day. Well, my night in this case."
    
    "Not only did she create my ID badge (that also functions as my card-key), she printed an information package for me, too."
    
    "I come to a stop outside room 117. My... {i}home{/i} for the foreseeable future."
    
    "I place my card in range of the lock, a confirming green light grants my entry." #Which grants my entry with a green light."
    
    
    #room scene
    
    
    
    scene room_boy16_night_dark with slowd
    
    #"I'm greeted by a room so impersonal, you'd think it was expecting me. "
    
    "I'm greeted by a room so impersonal, you'd think it was expecting me. "
    #nondescript
    #"But even if I take a jab, I can't deny that I'm grateful to be here. I'm physically and mentally exhausted. "
    
    play sound "audio/sfx/switch.mp3"
    scene room_boy16_night_light 
    
    #"The lamp does it no justice either."
    
    "I rest my luggage by the door and flick the lamp on."#The lamp does no justice either."
    
    "Bleak beige walls, ugly mismatching fabrics and longing storage space."
    
    "Chips and scratches blemish the wooden surfaces, testimonial to the character they once adorned." #Showing they were once adorned with character."
    
    "Now they're stripped and left bearing scars..." #{w}{i}Like me.{/i} "
    
    #"{i}Like me.{/i}"
    
    "I strip from my soaking clothes and throw them in the corner, deciding on a hot shower to drive out the cold settling into my bones."
    
    "I put my suitcase in the wardrobe—where it'll remain for a while, I'm sure—and get myself ready for said shower." #, I'm sure
    
    #    "My soaken clothing soon finds itself as a heap in the corner and my suitcase in the wardrobe." 
    
    #"Where it'll likely remain for a while."
    
    #"My dufflebag is soon ransacked and I'm finally ready for a shower."
    
    #"I ransack my duffle bag and ready myself for a shower."
    
    
    
    
    
    
    
    
    scene room_bath01_night_light with slowf
    
    "I'm struck by wry amusement to find the bathroom is more homely than my room. "
    
    #"I'm drawn to the full body mirror."
    
    "I approach the shower, but the mirror stops me in my tracks."
    
    #"A stranger stares back, I struggle to associate the image as me."
    "The reflection stares back. I struggle to associate the image as me."
    #my lips purse as I associate it as me. 
    #the pursing lips register it as me. 
    "But those haggard blue eyes... {w}{i}they're mine.{/i}" 
    
    #"I've commentated for so long, I'd almost forgotten I partake."
    #"I've only known myself as this voice in my mind."
    
    "My hair short and dishevelled, descending to my chin that yields a meagre sum of whiskers." #(Jennifer will call them peach hairs.)
    #descending
    "I rip my gaze away and turn the water on, avoiding the image in the mirror as it warms..."
    
    #I can't bear to stare into his empty eyes. 
    
    
    
    
    
    
    scene room_boy16_night_light with slowf
    
    "I add to the pile in the corner and slump onto the bed."# {w}My bed..."
    
    "My phone unable to provide distraction. It's filled with games that now lack my interest."
    
    #"I lie back on the bed and rummage through my phone for something to do."
    
    #"But it's mostly filled with overplayed games that now lack my interest."
    
    "Hmm... I wonder if Destiny's online, it's been a while."
    
    "Damn, that's right. I haven't connected to the wi-fi."
    
    #"My phone is filled with overplayed games that lack my interest."

    
    #I take the time to wash myself seems as I didn't have a shower after yesterday
    
    
    #"I shove my suitcase into the wardrobe, knowing that it will probably remain that way for a while."
    
    #"It evokes the first smile I've had for a while."
    
    #"Even though it's not exactly a good thing, it's nice to know some things don't change."
    
    #"Either way, I had better try and get some sleep. I have my first day in class tomorrow."
    
    
    #flick light off
    
    "Either way, I'd better get some sleep."
    
    play sound "audio/sfx/switch.mp3"
    scene room_boy16_night_dark
    
    "I flick the lamp off and get into bed."
    
    "My first day tomorrow..."
    
    "The mention causes my mind to explode with possibilities." 
    
    "{i}Will I ever make friends? {w}Is it even possible to start a new life?{/i}"
    
    "I shuffle in the sheets, failing to find comfort."
    
    #"What will they think of me? What if they ask about my past?"
    
    
    #"I shuffle restlessly in the sheets."
    
    "I settle on my back in the end, staring into the dark, foreign ceiling."
    
    #"The rain's stopped. The silence is violent."
    
    #"I rest my head back on the pillow, staring into the dark, foreign ceiling."
    
    #"I close my eyes, wishing that was all it took to find sleep."
    
    #"I stare into the dark, foreign ceiling."
    
    #"It's a shock to the system being surrounded by so much unfamiliarity, in this new environment, and having to be up tomorrow. Monday morning."
    
    #"For the start of my new routine. The start of my new life. Somehow knowing that I have to be up makes it more difficult to sleep."
    
    #"But of course, the rain has stopped now. The sound relaxes me, it helps me sleep."
    
    play music "audio/music/Wounded piano.ogg"
    #play music "audio/music/Wounded.mp3"
    #play environment "audio/sfx/heartbeat.mp3"
    
    #t"My thoughts are overbearing; I've always had distractions to hide behind. "
    
    t"The rain's stopped, leaving me shrouded in violent silence. Unrelenting darkness." with slowd
    
    t"Gravity weighs on my aching limbs. Every breath contests the weight of my chest."
    
    t"Aware of every heartbeat. Every beat breeds anxiety, but every beat is necessary."
    #Every heartbeat 
    
    #My heart beating against the mattress
    #Aware of every heartbeat.
    #t"Aware of every heartbeat. Every thump feeds the gnawing anxiety. "
    
    #t"No distraction."
    #t"Dissociative amnesia."
    t"{i}Dissociative amnesia.{/i} {w}Not caused by physical trauma, but repressed emotional trauma."
    
    #t"Face-to-face with the feelings I've avoided for so long. Free-falling. Nothing to hold on to, nothing to ground me."
    t"Face-to-face with it, after avoiding it for so long. I Free-fall into questions; nothing to latch on to, nothing to ground me."
    
    #t"Hiding from myself. Hiding from what I want."
    t"Not knowing who I am, or what I want."
    
    #t"But you can't fail if you don't try; I'm too scared to live, too scared to die."
    
    window hide 
    nvl clear
    
    #play a stomach growl sound. 
    play sound "audio/sfx/switch.mp3"
    #scene room_boy16_night_light 
    #stop environment fadeout 2.0
    #"My stomach grumbles, protesting like a worker threatening to strike."
    
    #play environment3 "audio/sfx/Ear Ringing Sound Effect.mp3" fadein 3.0
    play environment4 "audio/sfx/heartbeat.mp3" fadein 3.0
    scene room_boy16_night_light2
    scene room_boy16_night_light with longd
    #stop environment3 fadeout 2.0
    stop environment4 fadeout 2.0
    
    
    
    #"I rise to my racing thoughts. Flicking the lamp on and pacing my room in an attempt to calm them."
    "I rise and flick the lamp on, pacing to tame my racing thoughts."
    
    
    #"I pace the room. 
    "Hollow groans erupt from my stomach."
    #, akin to a worker on the verge of strike
    #"The words my therapist reiterated in the hospital: you need to eat properly to help stave your anxiety."
    "It conjures the words of my therapist at the hospital: {i}eating properly can stave your anxiety.{/i}"
    
    #"My stomach protests, akin to a worker on the verge of strike."
    
    #"The rumble in my stomach breaks me from my brooding."
    
    "I'm not sure if I'd eaten breakfast this... "
    
    stop music fadeout 3.0
    
    "...Afternoon."
    
    "It gives me an objective, something to focus on."
    
    #"I grab my bag of food from the ransacked dufflebag." 
    
    #"Despite my attempt to be quiet, the door's creek is elongated."
    
    #"I grab my bag of food from the ransacked dufflebag."
    
    #"..."
    
    "I grab my bag and head to the hall."
    
    stop music fadeout 3.0
    
    scene hospital03_night_dark with fastf
    
    #"I find myself creeping down the cold corridor." 
    
    "I shiver in the cold air that greets me and creep towards the kitchen."
    
    "Waking up people I'm about to spend the year with—at this time—wouldn't be the ideal first impression."
    
    #"I notice the kitchen light is still on, should I have turned it off earlier?"
    
    
    scene room_kitchen06_night_light with fastf
    
    "I freeze in the doorway when met by the back of a girl at the central counter."
    
    #"I freeze in the doorway; 
    
    "Soft, rhythmic scratching hangs in the air, the only reminder that time's still in effect."
    
    #toaster sound. 
    play sound "audio/sfx/Toaster-sound-effect.mp3"
    play music "audio/music/bensound-enigmatic.mp3" fadein 1.0
    
    
    "I jump to the springing toaster, slamming my bag against the door frame." 
    
    
    #play music "audio/music/bensound-enigmatic.mp3"
    
    show S 2YAnxious_Open at PC1
    
    #show S cshock
    
    "She spins; our gazes collide."
    
    "Startled into action, I initiate a greeting."
    
    p"\"H-hey... I'm Peter. I've—\""
    
    #show S cHBH with slowd
    
    show S 1AAnxious_Flat at PC1 with slowd
    
    "She glimpses my crotch area wide-eyed and turns away."
    #evident dismay
    "Comprehension sends a flush creeping up my cheeks." 
    
    "{i}My boxers...{/i}"
    
    p"\"Uh...\""
    
    #"She wrenches the pad from the counter and clutches it by her leg. Her knuckles whiten around the spine." #split?
    #Her fingers flex around the spine, knuckles turning pale."
    "She wrenches the pad from the counter and clutches it by her leg, knuckles whitening around the spine."
    
    show S 2DSad_Flat at PC1 with medd
    show S 2AAnxious_Flat at PC1 with medd
    
    
    "She poises herself, as if measuring her escape."
    
    hide S 1AAnxious_Flat with slowd
    
    #"I move out of the doorway and she bolts as though being released from a snare."
    
    #"By the time I've moved from the doorway, she's bolted through."
    "I move from the doorway and she bolts through."
    
    #"I grab
    
    #"The toast left erect in the toaster,"
    
    #"I notice the pan on the stove bubbling over."
    
    "Her toast left protruding from the toaster."
    
    #"I begin to call after her."
    
    p"\"Hey, wait! Your...\""
    
    #"As I call after her, realisation stomps on my tongue."
    "Realisation stomps on my tongue."
    
    #"Unless I want the rest of my new neighbors to see me in my boxers, I'd better hush."
    "Unless I want the rest of my new neighbors to see me in my boxers too..."
    
    #"And there's no way I'm guessing which room at this time."
    "I didn't see which door she went in, either. And I'm not prepared to test my luck."
    
    "I prepare my food and head back to my room."
    
    stop music fadeout 3.0
    
    scene room_boy16_night_light with fastf
    
    "I set my plate on the side table and slide into bed, flailing in the sheets and wringing them to my lips." 
    
    #"I flail in the sheets and wring them to my chin." 
    #"I flail in the sheets and wring them to my lips." 
    
    p"\"How could I be so stupid?\""
    
    #"I clench the quilt and wring it to my chin. How could I be so stupid?"
    
    "Mentioning ideal first impressions—{i}that wasn't one.{/i}"
    
    #"I'm not living at my uncle's now. I can't continue to mope around in my boxers."
    "I'm not living at my uncle's now. I can't keep moping around in my boxers."
    
    "Now she's going to think I'm a weirdo." 
    
    "I hear a door creek and the rhythmic pitter-patter of footsteps along the corridor."
    
    #"It makes me want to go and apologise, but I can't bring myself to face her after that."
    "I urge to apologise, but I can't bring myself to face her after that."
    
    #"I nibble my sandwich to appease my groaning stomach."
    
    "My stomach whines, so I nibble on my sandwich to appease it."
    
    "1:07am. It's going to be a long night..."
    
    #"Knowing I have to be up tomorrow—Monday morning—for the start of my routine; well, it makes it hard to sleep."
    
    #faux pas 
    
    
    #Wake up before your alarm and can't sleep? This is when you have ypur first shower? And you look into the mirror?
    scene black with longd
    play sound "audio/sfx/Alarm.mp3" fadein 0.8
    #play music "audio/music/Peter's track reverb.ogg" fadein 3.0 
    #morning
    
    #Morning light
    "My alarm rips away the sanctity of sleep." #Attempts to silence it requires me to open my eyes
    stop sound fadeout 1.0
    scene room_boy16_day with slowf
    
    "I'm forced to open my eyes in my attempts to silence it."
    
    "I groan and stretch my tender limbs. Yesterday's travel did a number on me."
    
    "Despite the rising urge to set a snooze, I peel myself from the sheets."
    
    "I scramble through my duffle bag for clothes and my rolled up school bag." #thankful to find a map of campus in the information booklet Cheryl printed."
    
    #"Now thankful that Cheryl gave me a map along with my card-key."
    
    "I'm thankful to find a map of campus in the information booklet Cheryl printed."
    
    #Can't believe I packed my pencil case in my suitcase. 
    #I'm scared to open it. There's so much packed in there, it will devastate my room
    #assuming I won't organise or clean up. Which I probably won't. 
    
    #I clench the quilt and wring it to my chin 
    
    
    
    
    
    
    
                  
    scene school05_day with slowf
    
    
    #corridor
    
    #"I've missed 'rush hour' at least, as it appears most students are already in their respective classrooms." 
    
    #"Despite being on the verge of late, there's still a score of people scurrying along the hallway. Eking out every last bit of freedom before the bell rings."
    
    "My stomach curdles with every step, as if death itself was waiting beyond that door."
    
    "Well, that's what this primordial anxiety would have me believe."
    
    "It has me considering whether to skip class today." 
    
    "I could turn back—"
    
    #play sound "sbell.mp3"
    
    "I jump to the sound of the bell. I hear a few people laughing behind me and assume it's my startlement." 
    
    "I nerve myself and enter."
    
    scene school02_day with fastf
    
    #classroom
    
    #"As I enter the room, a plump, greying lady pauses mid-sentence and turns to me."
    
    "A plump, greying lady rises from the front desk and turns to me."
    
    m "\"Just in time...\"" 
    
    "Her voice deep and raspy for a woman; she casts an ominous glare that accentuates her chiseled frown." 
    
    #"She casts an ominous glare that accentuates her chiseled frown."
    #before looking me up and down." 
    "I get the feeling I've just escaped a prison sentence."
    #mention student whispers? 
    m "\"As I was saying, we have a new student. If you would like to introduce yourself.\""
    
    #"After spending so much time with minimal social interaction, finding myself the centre of attention in a classroom full of strangers isn't anything less than intimidating."
    
    #"An expecting silence falls over the classroom, almost crushing me under it's weight as all eyes pinpoint on me."
    
    "An expectant silence falls over the room, crushing air from my lungs."
    #crushing the air from my lungs?
    
    #"I avoid eye contact by focusing on a poster at the back. I brush my fingers across my clammy palms."
    #"I avoid eye contact by focusing on the posters at the back, brushing my fingers across my clammy palms."
    "I focus on the posters at the back to avoid eye contact and brush my fingers along my clammy palms."
    
    p "\"Hey. The n-names... Peter.\""
    
    "I feel my voice catch and stutter so I take a deep breath in an attempt to calm myself."
    
    p "\"I-I'm from a small village outside of Bristol; I moved to the school yesterday.\"" 
    
    p"\"I... hope that I can get along with everybody.\""
    #Have Jennifer mock him for this^^
    
    "I feel desperate after adding the last part, but I can kick myself later."
    
    #Mention that this is on the outskirts of my city?
    #"Everybody seems satisfied with what little I could muster on the spot at least. I begin to question what I was so worried about."
    
    m "\"Tell us about yourself?\""
    
    "The question stumps me." 
    
    "The posters exclaiming, \"The Art Club Needs You!\" and \"The Sunnyvale Synchronized Swimming Team!\" aren't helping either."
    
    "Could I... lie?{w} Probably shouldn't."
    
    #"Apart from the Mrs Brown it seems, and this is a question that I really was worried about..."
    #I really didn't want to answer.
    #"I really don't know what I did before... and after, I haven't done much but browse the web and watch all types of television. My world viewpoint being my couch."
    
    "I catch glimpses of Impatient faces and force out a response." # makeshift 
    
    p "\"I like to watch... TV, I guess?\""
    
    #"The room falls into a brief silence before a few stifled laughs turn to snickers and ripple across the classroom, I feel my face begin to flush. "
    
    "Snickers ripple across the classroom. A flush climbs my cheeks."
    
    "I'm given a disapproving frown from Mrs Brown."

    #m "\"That's not something you should consider as a hobby. I want to see you getting yourself involved in some of the school's clubs and activities.\""
    
    m "\"Sit yourself down. The seat at the back there.\""
    
    p "\"Yes, Miss.\""
    
    
    #Have a calss mingle? As there are a few new people, I was just late. 
    #Jennifer could pick up on your accent and ask about it.
    #Danielle is Jennifer's friend from the previous year. 
    
    
    "I take my seat in the far corner, hyper-aware of people glancing and whispering amongst themselves."
    
    "I hear laughter and illogical self-conscious reasoning takes over."
    
    "They're talking about me. {i}Is it my hair? My clothes? My... introduction?{/i}"
    
    m"\"Quiet!\""
    
    "Silence ensues after her roar."
    
    m"\"As you all know, this is your final year...\""
    
    "Mrs Brown proceeds to drone about future opportunities, but my mind is miles away."
    
    "I don't even know who I was, so how can I decide who I want to become?"#?
        
    #classroom scene with Jen and Danielle? They will call you over for the group intro. (Pamphlets asking what you want to do in life and shit of that nature.)
    #This will cause uneasy moments where Peter may even lie to avoid telling them about his loss of memory. 
    #stop mjusic fadeout 2.0
    "I'm ripped from my thoughts when she says we'll be splitting into groups; anxiety reawakens in my stomach."
    #curdles
    "Everybody's forming groups, I don't know anyone."
    
    #Morning light
    
    #"I... don't know anybody."
    
    #"Suddenly a high-pitched voice calls out."
    
    #show Jennifer and then slide her over to reveal Danielle
    
    play music "audio/music/bensound-tenderness.mp3" fadein 4.0
    
    #show J mwave with slowd
    
    show J 1YHappy_OpenSmile at PM1 with slowd
    
    
    
    q"\"Yoo-hoo~! New guy!\""
    
    
    "A girl waves in my direction." 
    
    hide J 1YHappy_OpenSmile with slowd
    show J 1YHappy_OpenSmile at PM1 with fastd 
    
    "I scan the wall behind me and turn back to her."
    
    
    p"\"Me?\""
                                      
    q"\"Who else?\""
    
    
    #"My anxiety wanes into ambivalent relief when I turn to the source: a girl waving me over."
    #beckoning
    
    show J 2YHappy_Smile at PCR1
    show D 1YSerious_Flat at PCL1
    with slowd
    
    
    "I shuffle my table and chair over, adding to the tumult of screeches."
    
    #"I realise the girl next to her is her friend."
    
    j"\"Nice to meet you! I'm Jennifer and this is Danielle.\""
    show J 2CHappy_OpenSmile with fastd
    
    
    "She takes my hand in both of hers and flails my aching arm. Danielle spares me a glance."
    
    show J 2YHappy_Smile with slowd
    
    p"\"I'm Peter.\""
    
    j"\"We know. You just said so at the front, silly!\""
    
    "{i}Then why'd she call me new guy?{/i}"
    
    "Mrs Brown places three booklets on my desk and I hand them out. Without thanks from Danielle, I note." 
    
    show D 2YSerious_Flat with slowd
    
    "They pull out pens and leave me stranded. My stationary still in my suitcase..."
    
    "Danielle is already writing, but Jennifer catches my helpless expression."
    
    j"\"You OK?\""
    #j"\"You OK?\""
    
    p"\"I, er... forgot my pen.\""
    
    #"A worrying grin perches itself on her lips."
    "The grin pulling on her lips leaves me unsettled."
    
    j"\"I've got just the one!\""
    
    "She rummages through her pencil case with a chuckle."
    
    "She hands me a pink pen, complete with a bright pink tassel."
    
    j"\"It suits you!\""
    
    "I cast a searching glance to Danielle, who presents me with no other option."
    
    p"\"Thanks...\""
    
    "The title: Goals and Ambitions.{w} Gee, lucky me."
    
    #the title an antithesis of myself (goals and ambitions) (Future/past/goals/dreams/weaknesses)
    
    
    
    m"\"If you would all like to fill in your forms. Remember that this is your final year.\""
    
    #"First and final, in my case."
    
    "Jennifer perks up with excitement."
    
    #"I'm grateful that she carries on before giving us chance to answer."
    
    show J 3CHappy_OpenSmile with slowd
    
    
    j"\"I'm gonna swim in the Olympics!\""
    #\"I'm gonna... oh, I know! 
    #olympic swimmer
    #"Her voice twinges in a moment of disbelief."
    
    #"She looks to Danielle, a look that asks for a bail out. Which is blanked."
    
    #"It seems so whimsical."
    
    show J 2YHappy_Smile with slowd
    
    j"\"What are you guys putting down?\""
    
    "She looks to Danielle for an answer, which she blanks."
    
    #d"\"You know what I want to be.\""
    
    "Then to me..."
    
    p"\"E-erm... I'm not sure.\""
    
    
    #show D cER at left with fastd
    #show D cnormal at left with fastd
    
    "Danielle rolls her eyes. The first emotive gesture I've seen from her."
    
    j"\"Didn't you do anythin' at your old school?\""
    
    p"\"N-no...\""
    
    j"\"So all you did is watch TV? That's so lazy!\""
    
    "The words like a punch to the gut, echoes of my uncle."
    
    #show D 2YManic_Frown with fastd
    #show D 2YSerious_Flat with medd
    
    j"\"You should totally come swimming with me! If that's not your thing, then Danielle—\""
    
    #Make Jennifer joke about being something? No, it's written, link it to something. 
    
    "An inconspicuous elbow cuts her off mid-sentence; Jennifer's lack of reaction implies it's a common occurrence."
    
    "I'm left bemused."
    
    p "\"What... was that about?\""
    
    show D 1Closed_Open with slowd
    
    d "\"Nothing. Just write down what you want, both of you.\""
    
    show D 2YSerious_Frown with slowd
    
    "Have I made a blunder? Should I have greeted her properly or something?"
    
    "She's spared me a glance; her first words blunt and deflective."
    
    "Jennifer seems oblivious to her venom." #, and her apparent dislike of me."
    
    stop music fadeout 3.0
    
    show J 2YHappy_Pout with slowd
    
    j"\"What crawled up your arse and died?\""
    
    "Maybe not."
    
    d"\"I'm trying to concentrate.\""
    
    show J 2YHappy_Smile with slowd
    
    j"\"...\""
    #"We set to work on the questions."
    
    "Jennifer starts on her questions, I follow suit."
    
    "How would you describe yourself?"
    
    "Well, I can leave that blank."
    #This will catch up and the teacher will ask why after school? This could also lead to seeing the psychiatrist
    "What are your strengths...?"
    
    #"Followed by pages of further questions that turn my stomach."
    
    "Followed by three more pages that turn my stomach."
    
    #a question about what his goals are for this year. 
    
    scene school02_day with fastf
    
    #"The bell breaks me from my zombified state. Mrs Brown gives the go ahead for lunch."
    
    "I've finished most of the questions, despite them being hard to answer."
    
    "But unease rises at the thought of killing time over dinner."
    
    "Maybe I'll head back to my room."
    
    "Or maybe—" # I could ask
    
    play music "audio/music/On My Way.mp3" fadein 3.0
    
    #show J cnormal at right with slowd
    
    #show D cAC at left with slowd
    
    show J 2YHappy_Smile at PCR1
    show D 1YSerious_Flat at PCL1
    with slowd
    
    j"\"Hey, wanna have dinner with us?\""
    
    #"I'm grateful for the offer. I intended to ask but hadn't mustered the courage to do so."
    
    "As if reading my thoughts—I catch myself suppressing a smile."
    
    p"\"S-sure.\""
    
    j"\"Brought your own lunch?\""
    
    p"\"Yeah.\""
    
    j"\"Good.\""
    
    hide J 2YHappy_Smile 
    show D 1YSerious_Flat at PC1
    with slowd
    
    #"We gather our belongings and wait for Jennifer to dress herself for winter."
    
    "I glance to Danielle as we wait for Jennifer to shuffle through her bag and begin applying a top up of makeup."
    
    #"Her apparel looks professional. Her eyes flicker in thought, but her face remains expressionless."
    "She's prim and proper; she's the closest to resembling a \"proper\" student. Her eyes flicker in thought, but her face remains expressionless."
    
    #Description of Danielle here — also mention about it getting cold but not being winter
    
    #"When her gaze is returned I rest mine on the floor, willing Jennifer to hurry."
    #"She returns her gaze and I rest mine on the floor, willing Jennifer to hurry."
    "When her gaze returns I rest mine on the floor, willing Jennifer to hurry."
    
    "What's taking her so long..."
    
    "..."
    
    show J 2YHappy_Smile at PCR1
    show JX Bag at PCR1
    show D 1YSerious_Flat at PCL1
    with slowd
    
    j"\"You guys ready?\""
    
    show D 1Closed_Flat with slowd
    
    d"\"We were waiting for you.\""
    
    #j"\"Let's go!\"" 
    
    #All now obsolete...
    
    #have her sprite pop back fully dressed
    
    #d"\"Winter solstice isn't for another three months, y'know.\""
    
    #"It wrings a chuckle from me, with similar thoughts crossing my mind."
    
    #j"\"You're the one always telling me that I need to pre-prepare. I can't win.\"" #Danielle was talking about food
    #j"\"You're always telling me to pre-prepare. I can't win!\"" #Danielle was talking about food
    
    #"Though it makes little sense, she grins at Danielle's grimace and leads the way."
    #Have Jen exit right and then transition
    
    
    
    hide J cnormalc with moveoutright 
    
    scene school_out004_day with fastf
    
    show J 2YHappy_Smile at PMR1
    show JX Bag at PMR1
    show D 1YSerious_Flat at PML1
    with slowd
    
    "They lead me out of a side door, with a few benches and the car park in view."
    
    
    show J 2YHappy_Smile at PCR1
    show JX Bag at PCR1
    show D 1YSerious_Flat at PCL1
    with slowd
    
    "Each taking a seat on the benches situated together, leaving me with a quick choice of who to sit next to."
    
    #"Jennifer it is. Danielle doesn't seem too fond of me."
    
    "I choose Jennifer, who turns to me with a smile."
    
    j"\"So, Peter, you're gonna come swimming with me, right?\""
    
    p"\"E-erm... I guess I could try it.\""
    
    j"\"Really? Yay!\""
    
    "She sticks her tongue out at Danielle."
    
    j"\"See, people do like swimming.\""
    
    d"\"Yeah. People who have nothing else to do.\""
    
    "Ouch."
    
    "Jennifer isn't offended in the slightest."
    
    j"\"Aw, don't be so mean! He's just moved here.\""
    
    "She says after calling me lazy earlier."
    
    #j"\"Peter?\""
    "She looks to me for a response."
    
    "I shrug and extract my pre-prepared lunch: ham and cheese sandwiches."
    
    #"I retreat from the conversation, extracting my pre-prepared lunch: ham and cheese sandwiches."
    #happy to drop the topic
    "Thankfully, they drop the topic."
    
    "An aroma wafts from Jennifer's lunchbox; I find myself peering over for a better view."
    
    "She notices and catches my gaze."
    
    j"\"Like what you smell?\""
    
    p"\"Y-yeah...\""
    
    "She lifts out a wrap and displays it in her palm."
    
    j"\"My chicken wraps are fit for a god. I have my own secret recipe.\""
    
    d"\"They're not that good.\""
    
    j"\"Hush, you can't cook.\""
    
    d"\"Don't need to be a chef to know a good steak.\""
    
    "Danielle makes a fair point, but..."
    
    p"\"I must say the smell's amazing.\""
    
    j"\"Maybe you'll be privileged enough to try them someday.\""
    
    "She gives a wink and gulps down a hefty chunk."
    
    "We eat in silence..."
    
    scene school_out004_day with fastf
    
    show J 2YHappy_Smile at PCR1
    show JX Bag at PCR1
    show D 1YSerious_Flat at PCL1
    with slowd
    
    "...it lingers beyond the packing away of our lunches."
    
    #"I notice them playing on their phones, motivating me to fiddle on my own."
    "They play on their phones, motivating me to fiddle on my own."
    
    j"\"Don't talk much, do you?\""
    
    "Jennifer first to break the silence, prompting me to ask something on my mind."
    
    p"\"Not really...\"" 
    
    p"\"But I need the wi-fi code, do you know where I can get it?\""
    
    d"\"I have it saved as a picture.\""
    
    "She hands me her phone and I connect."
    #enter the awkward code.
    p"\"Thanks.\""
    
    "I offer a smile as I hand it back, which isn't returned." #reciprocated."
    
    d"\"It's OK.\""
    
    j"\"You got FaceAP?\""
    #Whatsface
    p"\"No.\""
    
    j"\"Get it and add me!\""
    
    "Caught up in excitement, she snatches my phone. {w}Guess I have no choice."
    
    play sound "audio/sfx/short vibrate.mp3"
    
    "I notice her phone buzz as she fiddles with mine, but she doesn't react to it."
    
    j"\"Make an account, I downloaded it for you.\"" 
    
    #I also saved my number.\""
    
    #"Wait, what? Her... number?"
    #she adds everyone to her contacts
    
    #"I begin to register my e-mail but the bell rings."
    #"I'm clawed away from creating my account by the bell signaling the end of lunch."
    
    "I'm interrupted from account creation by the bell signaling the end of lunch."
    
    "We grab our bags and head up."
    
    
    
    
    
    
    
    scene school02_day with fastf
    
    "As we make our way back, my impression of Jennifer being gregarious is fortified by numerous waves and greetings in the halls."
    
    "I'm glad she called me over. This is a start; I'm happy to meet new people—even if Danielle hasn't taken to me."
    
    stop music fadeout 4.0
    
    m "\"Peter, I would like to speak to you after class.\""
    
    "But my straying thoughts are stolen by Mrs Brown."
    
    j"\"Ooh, you're in trouble!\""
    
    #"Jennifer murmurs in my ear as she walks past."
    "Jennifer gives a teasing whisper as she walks by."
    
    "After making our way to our desks, we're instructed to reorganise."
    
    "Jennifer sheds her extra layer as I drag my table back into position."
    
    "Mrs Brown starts the first lesson of the day: maths." 
    
    "She scribbles equations down on the whiteboard; students put their hands up to answer."
    
    "I can't focus on the lecture at hand. The lack of sleep has done a number on my concentration."
    
    "I've also spent so much time watching TV shows, documentaries and reading books, my concentration lapses without adequate stimulation."
    #
    #my concentration tends to lapse without anything interesting happening."
    "And they always skip the boring parts in the stories..."
    
    
    
    
    
    
    
    scene school02_day with fastf
    
    "The bell signals the end of the day. My first day."
    
    #"It went better than imagined. To think I'd almost skipped class."
    "It went better than I'd imagined. To think I'd considered skipping class."
    
    "Students rush to the door. Jennifer stops and waves before she leaves."
    #I notice Jennifer leaving who in turn notices me."
    
    show J 1YHappy_OpenSmile at PMR1 with slowd
    
    j"\"Bye, Peter! See you tomorrow.\""
    
    p"\"See ya.\""
    
    hide J 1YHappy_OpenSmile with moveoutright
    
    #"I intend to follow but Mrs Brown's raspy voice thunders in the air."
    "I intend to follow but I'm frozen by Mrs Brown's voice ripping through the air."
    #indirect summons
    m"\"Peter, where do you think you're going?\""    
    
    #"I resign and stand by her desk. She regards me in silence until we're alone."
    "I resign and make my way to her desk. She regards me in silence until we're alone."
    
    
    m"\"What are these answers?\""
    
    p"\"I... I don't know what you mean.\""
    
    m"\"You left your personal description blank for a start.\""
    
    #"She begins reading through it, much to my chagrin."
    #"She begins reading my answers from a piece of paper, to my chagrin."
    "To my chagrin, she begins reciting my answers from a piece of paper."
    
    
    m"\"Your strengths are, and I quote, '{i}making a mess and watching TV.{/i}'\""
    
    m"\"Your only weakness being '{i}memory.{/i}'\""
    
    p"\"Y-yeah...\""
    
    "She considers me, a quizzical tilt lining her brow."
    
    m"\"I've been instructed to refer you to our counsellor. But... what have you been doing?\""
    #she relays information to Mr Adams who then relays it to my uncle. 
    "Counsellor? Has my uncle told them...?" #which leads to the psychiatrist dude. Name? Mr Adwell?
    
    "She continues after my lack of an answer."
    
    m"\"I'll reprieve your answers for now. But if I find out there isn't good reason, there will be hell to pay.\""
    
    m"\"Go. The counsellor's office is down the stairs on the left-hand side.\""
    
    p"\"Yes, Miss.\""
    
    #You only spot her here? Leaving you curious about her. Sharing an awkward glance and she speeds up round the corner. 
    
    play music "audio/music/bensound-straight.mp3" fadein 3.0
    
    #scene office09_day with slowf
    scene office10_day with slowf
    #show mra cnorm with slowd
    
    #He looks barely older than a student, but his smile uncovers this deceit.
    
    "The man spins to face me in his chair, flourishing his arms in a gesture to sit down."
    
    "Despite his formal attire, he's slack with unkempt hair."
    
    a"\"Welcome, I'm Mr Adams.\""
    
    "He looks barely older than a student, but his smile uncovers this deceit."
    
    #"Though he sits by his computer, he readies a notepad."
    
    #"He's oddly energetic, yet, emits a calm air."
    
    p"\"I'm Peter.\""
    
    "His weakening smile lets me know he already knew." 
    
    "{i}What else does he know?{/i}"
    
    #He looks barely older than the students, but he wrinkled smile uncovers this deceit. 
    
    a"\"So, you think nothing of yourself, huh?\""
    
    #"I freeze to his startlingly accurate assessment."
    "I freeze. His assessment hits too close to home."
    
    "He observes my discomfort, making me realise his assessment stems further."
    
    a"\"Sorry, bad joke. But why didn't you answer the question?\""
    
    "So my uncle hasn't told them? But he must've contacted them."
    
    p"\"I... I didn't feel like answering.\""
    
    #"He nods and scribbles something in the notepad on his desk. Only now do I notice my booklet beneath it."
    #"He reminds me of the doctor as he scribbles frantically in his notepad. Only now do I notice my booklet beneath it."
    
    "His frantic scribbling reminds me of the doctor. Only now do I notice my booklet beneath his notepad."
    
    a"\"That's OK. Many people find it hard to describe themselves.\""
    
    "He slides it out, scanning through my answers with a furrowed brow; his gaze still locked as he speaks."
    
    a"\"Your uncle notified me that you may require special attention. Though, he specified it's personal to you.\""
    
    "I feel a small sense of pride from my simple deduction."
    
    "I'm glad he didn't. It was a taboo subject when I enquired."
    
    a"\"He set up weekly appointments for me to keep an eye on you.\""
    
    "On cue, his eyes rest on me." 
    #"On cue, he rests his eyes on me."
    
    p"\"I see.\""
    
    a"\"How's the move been thus far?\""
    
    "I shrug; I'm unsure myself." 
    
    "I didn't want to come here, but I can't deny it's not as bad as anticipated."
    
    "I've even made a friend, I think. When I add Jennifer on FaceAP that is."
    
    "He measures me with a scratch of his chin."
    
    a"\"I'll postpone that question, give you some time to settle in.\""
    
    a"\"We don't have time for a formal appointment today, either.\""
    
    #"He clicks his tongue as he checks his computer."
    #"He tuts rhythmically as he checks his computer."
    
    "He tuts a rhythm while checking his computer."
    
    a"\"A week today, same time.\""
    
    
    a"\"Don't forget.\""
    
    "He points to my booklet."
    
    a"\"Your {i}memory{/i} is your weakness, after all.\""
    
    "I can only offer a forced smile as I think of a segue."
    
    #Or Sarah knocks on and waits outside? 
    
    "Something strikes me."
    
    p"\"What are you going to say to Mrs Brown?\""
    
    a"\"Don't worry, I'll deal with Mrs Brown. I've heard she can come down hard on students.\""
    
    #"The last line said with a wink."
    "He gives a playful wink."
    
    play sound "audio/sfx/soft knock.mp3"
    
    p"\"Tha—\""
    
    "Gentle taps on the door interject us."
    
    a"\"Just a minute!\""
    
    a"\"I'll see you next week, Peter. I'm sure you'll settle in fine.\""
    
    "He initiates a firm shake before I leave."
    
    stop music fadeout 3.0
    scene school4_day with fastf
    
    #"It's the girl from last night..."
    
    #Maybe he looks at the answers and decides that you need to be watched more closely, which Peter isn't fond of. 
    
    #show S mnormal2 with slowd
    
    show S 2DSad_Flat at PM1
    
    "I'm frozen in the doorway. It's that girl from last night; her gaze resting on her feet."
    
    show S 1YAnxious_Open with slowd
    
    "Her eyes widen when she glances up."
    
    "Once again, I find myself an obstacle and move from the doorway." 
    
    show S 1AAnxious_Smile with medd
    hide S 1AAnxious_Smile with slowd
    
    "She offers a queasy smile and flees into Mr Adams' office."
    
    
    #"Before my brain can process words, she flees into Mr Adam's office."
    
    "I can't help but be curious. She's so... {w}mysterious."
    
    "Why was she up so late? It strikes me as weird."
    
    "Then again, I'm also weird by that standard—{i}and beyond.{/i}"
    
    
    
    
    #introduce Dean outside the dorms? 
    
    scene school_out002_day with slowf
    
    "I realise it's the first time I'm not in a rush when reaching the dorms."
    
    #"The front building looks renovated, surrounded by older buildings."
    
    "There's a small court with nets situated between the buildings; a few students are kicking the ball at an unfortunate student's rectum."
    # Where a few students are having a kick about."
    
    "The most appealing part is the view of the distant forest."
    
    play music "audio/music/bensound-funkyelement.mp3" fadein 6.0
    
    "I lean on the gate to take in the sight, but I'm distracted by the ball flying towards me."
    
    #that music you used for the jen 'battle' scene? 
    
    #show d mcall with slowd
    show De 1YRelax_WideGrin at PM1 with slowd
    
    q"\"Hey! Over here!\""
    
    #show d msmile with slowd
    
    "I slice the ball, which travels to the opposing goal."
    
    #show d csmile with slowd
    
    show De 2YRelax_OpenSmile at PC1 with slowd
    
    "He runs over, waving me to meet him half way."
    
    #q"\"That's terrible! Have you ever played football before?\""
    q"\"That's terrible! Have you ever kicked a ball?\""
    
    p"\"Can't say I have.\""
    
    #show d cnorm with slowd
    
    show De 2YDisappointed_Frown with slowd
    
    "His amusement ends with a tilt of his brow." 
    
    show De 2YDisappointed_Smirk with slowd
    
    "I meet his extended hand; his shake a firm tug."
    
    
    D"\"I'm Dean. When'd you move in?\""
    
    #p"\"I'm Peter, just yesterday.\""
    p"\"Peter, yesterday.\""
    
    D"\"Explains why I ain't seen ya before.\""
    
    #show d csmile with slowd
    
    show De 2YDisappointed_OpenSmile with slowd
    
    D"\"Wanna play?\""
    
    
    "I glance to my leg; my shin was shattered in the crash. There's a metal rod in it to this day."
    
    "I don't fancy having the ball blasted at my arse, either." #for one
    
    p"\"I... I really shouldn't.\""
    
    
    D"\"Why not?\""
    
    show De 1YDisappointed_Smirk with slowd
    
    
    D"\"Come on! We need one more for even teams.\""
    
    "I don't feel comfortable explaining why and I can't think of a lie."
    
    #"I don't fancy having the ball blasted at my arse, either."
    
    #D"\"Why not? Come on! We need one more for even teams.\""
    
    #"I don't feel comfortable explaining why and I can't think of a lie."
    
    
    
    p"\"Erm...\""
    
    show De 2YDisappointed_Smirk with slowd
    
    D"\"Come on!\"" 
    
    
    #"He yanks my arm."
    
    "He slaps my shoulder."
    
    D"\"It'll be too cold to play soon.\""
    
    "Maybe I can avoid a sore bottom if it's a normal game."
    
    p"\"OK...\""
    
    "I fold, accepting against my wishes."
    
    hide De 1YDisappointed_Smirk with slowd
    
    "They begin arguing about who's team I should be on. I don't think I set a good impression with my first kick."
    
    #Have them say that you should be on Dean's team as he recruited you. 
    
    "Finally, we set up into two teams of four and begin the game."
    
    stop music fadeout 3.0
    scene school_out002_evening with longd
    
    "I'm exhausted. I excuse myself and sit on the sidelines."
    
    "One thing I've learnt from this: I'm terrible at football."
    
    show De 1YDisappointed_Frown at PC1 with slowd
    
    D"\"Done already?\""
    
    p"\"Yeah. I'm going to head in. It was nice meeting you.\""
    
    D"\"You can't leave now!\""
    
    p"\"I have to go. Stuff to do.\""
    
    show De 2YDisappointed_Frown with slowd
    
    "He regards me for a moment. To be honest, I didn't convince myself."
    #I doubt I'd have convinced myself."
    
    D"\"Oh, OK. Peace, man.\""
    
    "But he can't anticipate how listless I am—yet." 
    
    #hide d cnorm with slowd
    scene hospital03_day with slowf
    
    "I make my way inside to avoid further questions."
    
    
    
    
    
    scene room_boy16_evening with slowf 
    
    "I fall face-first onto my bed, heaving for air."
    
    "I avoided the ball at all costs and I'm still tired. Thankfully, my leg doesn't seem to be aching,"
    
    "My lungs calm. I roll over and draw my phone, opening the app and tapping a message to Destiny." # some kind of gaming chat app
    
    t"L0stc4us3: Hey, long time no speak."
    
    play sound "audio/sfx/short vibrate.mp3"
    
    "A running joke we had that's for real this time."
    
    #vibration sound
    
    "To my surprise, her reply is instantaneous."
    
    #"By the time I've put my phone aside it vibrates."
    
    t"x-Destiny-x: Hey."
    
    t"L0stc4us3: I've just moved into a new school."
    
    t"x-Destiny-x: Really? Which school?"
    
    #"She was never one for conversation, so I'm glad she's making the effort."
    
    "I'm glad she's making the effort. She was never one for conversation."
    
    "So I find myself keying in my location to a stranger."
    
    #"It seems weird telling a stranger where I'm staying, but I find myself keying it in."
    
    t"L0stc4us3: Sunnyvale Academy."
    
    #Maybe end it there??
    
    #t"x-Destiny-x: You lie."
    
    #t"L0stc4us3: Why would I lie?"
    
    #t"x-Destiny-x: Nevermind."
    
    window hide 
    nvl clear 
    
    "..."
    
    #Any one of these students could be Destiny. 
    
    #"Well, that's the end of that."
    
    "But with that, the conversation comes to an end."
    
    #"We met on a game. She referred to me as \"noob\" and introduced me to a clan to get me started."
    
    "We met on an online game." 
    
    "She referred to me as \"noob\" and introduced me to a clan to get me started."
    
    #"We met on a forum, both with an interest in casual gaming."
    
    #"We messaged each other in game—the topic being games."
    #"We messaged each other when we played—the topic: games."
    #We only ever spoke whilst gaming—the topic being the game in hand.
    "Yeah. I didn't know her."
    
    #"We only ever spoke while playing games—even then, the topic would be the game in hand."
    
    "I decide to sign up for FaceAP."
    
    "After signing up and fiddling on the app, I realise it's boring with no friends."
    
    "A Search for Jennifer is futile without her second name."
    
    "Seized by a yawn, I stretch and lie back across the sheets."
    
    "The events of today reel back through my mind."
    
    "It's exhausting meeting new people, taking in new scenery and information." 
    
    #"I can't deny I feel better for it, though."
    "But I can't deny the sense of accomplishment." #, though.
    
    "My heavy lids descend over my eyes." 
    
    scene black with slowd
    
    "I lack the will to protest."
    #volition
    
    
    scene room_boy16_night_dark with slowf 
    
    "I wake with a start, brushing sleep from my eyelashes."
    
    "What time is it?"
    
    "My phone's blinding light merges into 11:34pm."
    
    #"My eyes strain at my phone's light. It's a few seconds before they adjust to see 11:34pm."
    
    #"Inspection of my phone reveals it's 11:34pm."
    
    #"Damn, my sleep schedule is in shambles."
    "Damn. Somehow, I've made my sleep pattern worse."
    
    "Still no message from Destiny. Not that I expected one..."
    
    "My stomach groans." 
    
    "Once again, I haven't eaten."
    
    "My limbs protest as I hoist myself from the sheets." 
    
    "I'm way too unfit."
    
    #"I'd like to blame it on the atrophy of being stuck in a hospital bed for three months. But I haven't done anything since."
    "I'd like to say it's the atrophy from being stuck in a hospital bed for three months, but I haven't done much since."
    
    "I navigate my way to the door with my phone's light."
    
    
    
    
    
    #sarah introduction
    
    scene hospital03_night_dark with fastf
    
    "And once again find myself on this corridor at stupid o'clock." 
    
    "This isn't normal, but at least I'm dressed."
    #"This isn't normal, but at least I'm appropiately dressed this time."
    
    #"I find myself creeping down the corridor, again. This isn't normal. But at least I'm appropiately dressed this time."
    
    "The kitchen light is on again..."
    
    
    
    
    
    
    
    
    scene room_kitchen06_night_light with fastf
    
    show S 2YAnxious_Open at PC1 with slowd
    
    "I'm not surprised to see her. This time though, she notices me from the get-go."
    
    #"Her eyes widen like saucers at my appearance."
    
    p"\"I'm sorry about last night!\"" 
    
    "Words spill from my lips."
    
    #p"\"I...{w} I hadn't thought it through.\""
    p"\"I...{w} I didn't expect anybody to be in here...\"" #XD
    
    play music "audio/music/Kevin_MacLeod_-_Dream_Culture.mp3" fadein 3.0
    show S 1AAnxious_Smile with slowd
    
    
    #"This extracts a smile from her. Although it's forced, it relieves tension."
    "It extracts a smile from her." 
    
    "Although it's forced, it relieves tension. I seize the boost."
    
    #p"\"I'm Peter. I didn't catch your name last time 'round.\""
    p"\"I didn't catch your name last time 'round.\""
    
    "I'm taking no prisoners. I at least have to find out her name." #Though she's uncomfortable, 
    
    show S 2AAnxious_Smile with slowd
    
    "She shuffles as if she's about to bolt again, but manages to master herself." 
    
    s"\"I... I'm Sarah.\""
    
    p"\"It's nice to meet you, Sarah. I'm Peter.\""
    
    show S 2YAnxious_Smile with slowd
    
    s"\"How could I... forget?\""
    
    "By partaking in a traumatic car crash."
    
    "..."
    
    #"I'm not sure."
    
    p"\"Anyway, I've been having sleeping troubles, so thought I'd make a brew. D'you want one?\"" 
    
    #"I say, flicking the kettle on." 
    
    "She doesn't bolt when I move from the door way." 
    
    "Instead, she accepts my offer with a nod."
    
    p"\"How do you like it?\""
    
    s"\"T-tea two.\""
    
    p"\"Me too.\""
    
    "With nothing left to say, we sink into silence."
    #it feels so awkward
    
    "I stare at the static kettle, willing it to boil."
    
    show S 1AAnxious_Smile with slowd
    
    s"\"A...\""
    
    "She breaks the silence, but doesn't continue."
    
    p"\"Huh?\""
    
    s"\"A... watched kettle never boils.\""
    
    p"\"You can say that again.\""
    
    "She reciprocates my strained chuckle."
    
    #"When the kettle boils, I grab two clean enough looking cups and prepare our tea."
    #"I prepare the cups and the kettle clicks."
    "I prepare each of our cups with a teabag and two sugars."
    
    "The kettle clicks on cue."
    
    #mention two sugars? 
    
    #"I set down her cup next to her plate of toast, positioning myself over the counter." #remaining
    "I position myself over the counter and place her cup next to her plate of toast."
    
    "She leans away, as if touching me would contaminate her."
    
    p"\"So, what're you working on?\""
    
    show S 1DSad_Flat with slowd
    
    "I tap the pad, achieving the opposite of my desired effect—relieving tension."
    #reaction, evoking
    s"\"It's... it's just my art work.\""
    
    #"It's as if my presence is a mild form of torture."
    
    #p"\"Can I take a look?\""
    p"\"Sounds interesting, can I see something?\""
    
    show S 2DSad_Flat with slowd
    
    "She squirms at the question; it makes me feel like an interrogator."
    #You'd think I'd asked her to sell her soul."
    
    "I'm about to let it slide but for her sharp nod. She finishes off her toast and flicks the pad open."
    
    #s"\"T-this is what I've... been working on.\""
    s"\"T-this... is something I've been working on.\""
    
    #"Murky images dance on the page as I make out the image."
    "It takes a moment for the murky shading and outlines to consolidate into a picture."
    
    #"There are two facing silhouettes surrounded by thick smoke."
    "Two facing silhouettes are wreathed by thick smoke."
    
    #"Galaxies and nebulas swirl within the silhouettes."
    "Galaxies and nebulae swirl within them with a pleasant juxtaposition."
    
    ##old
    #"Upon closer inspection, it looks like two silhouettes—each filled with stars and galaxies—wreathed in smog."
    #"Two facing silhouettes filled with stars and galaxies, surrounded by thick smoke."
    
    #"The detail is impressive, the constellations are on point."
    
    #"I notice smoke leaks into the male-like silhouette's mouth, wreathing nearby galaxies."
    "I notice smoke leaks into the male-like silhouette's mouth and wreathes nearby galaxies."
    
    p "\"This is good. Will you show me when you've finished?\""
    
    show S 1AAnxious_Smile with slowd
    
    "She remains silent, with an expression and nod that seem to say anything but yes."
    
    p"\"I mean, you don't have to if you don't want to. I like it, though.\"" #I genuinely like it, though.\""
    
    show S 1YCalm_Smile with slowd
    
    "I'm surprised by the genuine smile tugging on her lips."
    
    "She finishes her tea in a swill and rises, taking her notepad in arms."
    
    s"\"T-thank you for the tea. But... I must get to bed.\""
    
    p"\"You're welcome. I should do the same.\""
    
    "I say that, but I haven't prepared my food yet."
    
    stop music fadeout 3.0
    hide S 1YCalm_Smile with slowd
    
    #"I finish off my drink, and attempt to say goodnight but she's already left the room.
    #"By the time I've finished my tea, she's already left."
    "She leaves as I finish off my tea." # the time I finish off mine."
    
    "She didn't say whether she'd show me, either."
    
    "I make a sandwich and head back to my room."
    
    scene room_boy16_night_dark with slowf 
    
    "It's midnight. I'm not tired; I have nothing to do." #I have nothing to do. I'm not tired." 
    
    "How I hate myself right now..."
    
    scene room_boy16_day with longd
    
    "Morning comes. I haven't slept a wink."
    
    #"It's going to be a long day. I'm dreading the thought."
    
    "I head out for a shower, in hopes it will wake me up for the day." #perk me up
    
    
    
    
    scene school02_day with slowf
    
    "I'm... early. I don't think I've ever been early." 
    
    "Maybe as a sperm. I can't imagine I'd win without a head start."
    
    #"The classroom like a gloopy mass of stagnant time."
    #"The classroom is like an alternate dimension where time stagnates."
    
    "I flop my forehead on my clenched fists, wondering how Im going to make it through today."
    
    #"My stomach free-falling as I wonder how I'll make it through today."
    
    
    "I perk up when I hear Jennifer enter the room." 
    
    show J 2YHappy_Flat at PMR1 with fastd
    hide J 2YHappy_Flat with slowd
    
    "I glance over, but I'm quick to rest my gaze back into my laced fingers."
    
    "I wonder if she'll speak to me again."
    
    play music "audio/music/bensound-memories.mp3" fadein 4.0
    show J 1YHappy_OpenSmile at PMR1 with slowd
    
    j"\"Hey, Peter!\""
    
    
    "I turn back to her, unable to defeat the smile pulling on my lips."
    
    p"\"Hey.\""
    
    #show J 2CHappy_Smile at PC1 with slowd
    show J 2YHappy_Smile at PC1 with slowd
    
    "She parades over, with far too much energy this early in the morning. {w}Or any time, for that matter."
    
    #show J 2YHappy_Smile at PC1 with slowd
    
    j"\"You look better today.\""# You seemed down yesterday.\""
    
    "It takes me off guard. Did I look that bad yesterday?"
    #"Her frank words take me off guard. Did I look that bad yesterday?"
    
    #"I take a moment to formulate my response."
    
    #p"\"Oh. I didn't sleep well.\""
    p"\"Oh. I hadn't slept well.\""
    
    
    #"Or at all last night."
    #Or at all today."
    "{i}Or at all since midnight.{/i}"
    
    show J 3YHappy_OpenSmile at PC1 with slowd
    
    j"\"That's no excuse! You have to be ready for every day.\""
    
    
    "She draws her fists in an aggressive stance, jabbing the air."
    
    
    p"\"Easy to say when morning's like caffeine to you.\""
    
    show J 3YUpturned_Grin at PCC1 with slowd
    
    #"She leans over."
    
    #show J cfist3 with slowd
    
    #Change this poo dialogue. 
    
    j"\"They say life's a bitch. I'll kick her ass!\""
    
    
    "Waving her fist as if I was the aggressor."
    
    j"\"Which means morning's nothing. It resides under my boot.\""
    
    show J 2YHappy_Smile at PC1 with slowd
    
    "She extracts a chuckle from me." 
    
    
    #p"\"I'll bear that in mind. I wouldn't wanna be life's bitch or anything.\""
    #WTF? XD custard
    # Open smile sprite
    
    p"\"I wouldn't wanna be life.\""
    
    j"\"No, you wouldn't. That's why you should come swimming!\""
    
    show J 2YHappy_OpenSmile at PC1 with slowd
    
    "She takes on a proud pose."
    
    j"\"I've already been this morning.\""
    
    p"\"I'm not going in the morning.\""
    
    "I'm putting my foot down there, at least."
    
    show J 2YHappy_Smile at PC1 with slowd
    
    #j"\"I have a meeting today, but you could come with me tomorrow, after school?\""
    j"\"I have practice today. You could come, tomorrow, after school?\""
    
    p"\"Maybe.\""
    
    "Mrs Brown storms into the room."
    
    j"\"You will!\""
    
    #"Jennifer gives a wink before making her way back to her chair."
    "Jennifer flashes a wink and makes her way back to her chair."
    
    
    hide J 2YHappy_Smile with slowd
    
    "Her whisper left hanging in the air."
    
    "Why does she want me to join her?"
    
    "I don't even know if I can swim."
    
    #Jennifer: It's like training a child. 
    
    #"Maybe today won't be so bad, after all." 
    
    stop music fadeout 3.5
    
    
    scene school02_day with fastf
    
    #"Who was I kidding? I keep drifting off. Startling myself awake in fear of Mrs Brown's wrath."
    
    "I keep drifting off and startling myself awake in fear of Mrs Brown's wrath."
    
    "Every time I try to focus on the work, the writing blurs across the page."
    
    #"I watch the clock tick time away, each second longer than the last." 
    
    #"I force myself to look away, in fear of time stagnating completely."
    
    "I watch the clock tick time away, each second longer than the last..." 
    
    "I force myself to look away, in fear of time stagnating completely."
    
    
    scene room_boy16_day with slowf
    
    "When I make it back to my room I feel re-energised, after falling asleep all day. {w}Typical."
    
    #"I should try and stay awake if I want to get my sleeping pattern back on track."
    "But it works in my favour. I shouldn't sleep until later if I want to get my sleep schedule back on track."
    
    #"Though... it was never on track."
    "{i}If it was ever on track.{/i}"
    
    scene room_boy16_evening with slowd
    
    #"I kill time reading my book, but I catch myself yawning."
    
    "I kill time reading my book, but I catch myself yawning and my eyes closing."
    
    "I put it down and think of ways to keep myself awake."
    
    "My gaze comes to rest on my ransacked duffle bag."
    
    "Hmm...{w} no."
    
    "Then my wardrobe."
    
    "Let's be real, that's not going to happen."
    
    "I pick up my phone and find myself messaging Destiny again."
    
    
    
    t"L0stc4us3: Hey, long time no speak." with slowd
    
    play sound "audio/sfx/short vibrate.mp3"
    #play destiny's music?
    
    "As I lay it down, it vibrates." with slowd
    #"I lay it down as it vibrates."
    #"I'm about to lay down my phone but the response is just as fast."
    
    t"x-Destiny-x: Stop messaging or I'll call the police."
    
    "Wait, what? Is she joking?"
    
    t"L0stc4us3: Why would you call the police?"
    
    t"x-Destiny-x: Because you know which school I attend. I'm calling the police."
    
    "What the—she lives here?"
    
    t"L0stc4us3: Wait, stop! I swear I've moved to Sunnyvale."
    
    window hide
    nvl clear
    
    "I wait, but the response is futile."
    
    "Is she really ringing the police?"
    
    "I send her my number, along with an invitation to ring me."
    
    "I rest my phone on the table and wonder whether that was a stupid decision."
    
    "What are the chances?" 
    
    "A stranger I used to speak to on the internet happens to go to the same school."
    
    play environment "audio/sfx/ring vibrate.mp3"
    
    "My phone startles me. I watch it dance across the side table. "
    
    "Unknown number, I brace myself and answer."
    
    stop environment fadeout 0.3
    #beep sound
    
    j"\"Heeeeeeeya, Peter!\""
    
    "Her greeting leaves me rubbing my ear."
    #"Jennifer's voice pierces my eardrum." 
    
    "Wait, Jennifer is..."
    
    p"\"Destiny?\""
    
    j"\"Yes, it's destiny that we swim tomorrow.\""
    
    p"\"No, I'm asking if you're Destiny?\""
    
    #j"\"I may kick life's arse, but I'm not destiny.\""
    j"\"I know I'm amazing but I'm not destiny.\""
    
    "Is she being cryptic?"
    
    "No, she can't be. Destiny doesn't know my real name."
    
    p"\"How did you get my number?\""
    
    j"\"Well...\""
    
    "Out of all of this, I'm most surprised to hear her voice fall sheepish."
    
    #"Even for Jennifer, she seems hesitant."
    
    #j"\"I one belled myself from your phone at lunch yesterday.\""
    j"\"I called myself from your phone at lunch yesterday.\""
    
    #"Her cheeky giggle fills the line."
    "She giggles down the line."
    
    j"\"I'm sorry. I should've asked you.\"" 
    
    j"\"But you did say you'd come swimming with me...\"" #; so I put it on myself to obtain your number.\""
    #procure
    #her words
    #"Why am I not surprised? I find myself chuckling."
    #"What am I not surprised? A laugh escapes in resignation."
    # escapes in
    "I laugh in resignation." #at her torrent."
    
    p"\"It's OK.\""
    
    play sound "audio/sfx/short vibrate.mp3"
    
    "My phone vibrates."
    
    p"\"I've just received a message.\""
    
    j"\"You can get to it, right after you agree to come swimming.\""
    
    p"\"I said I would, didn't I? You said so yourself.\""
    
    j"\"That's what I like to hear. Ba-bye~!\""
    
    #"Before I have a chance to reply, the dial tone ensues."
    
    p"\"Bye.\""
    
    #"My reply lost to the dial tone."
    "My reply lost to the end call tone."
    
    
    #"I'd wonder why she wants me to come swimming, but 
    "Why does she want me to come?"
    
    "I'm not sure, but my mind is soon back on Destiny."
    
    #"One down, the rest of the school to go."
    
    "I check my phone to find a missed call and a message:" 
    
    "\"It's Destiny. If you've really moved here, meet me on the roof in twenty minutes.\""
    
    "Wait... which roof?" 
    
    "I message her as much, but there's no reply."
    
    "Well, I have twenty minutes to find it and something to keep me awake, I guess."
    
    "The roof..."
    
    "Oh, that's right! My map."
    
    #"I scan over it but there's no mention of any roofs..."
    "I scan over it, but it doesn't cover the rooftops..."
    
    scene school_out009_evening with slowf
    
    "I make my way to the main building."
    
    "I was hoping to ask somebody for directions but the grounds are empty."
    
    scene school_out008_evening with slowd
    
    "I find a nook and follow it out of curiosity. I have nothing else to go off."
    
    scene school_out010_evening with slowd
    
    "Dumb luck is on my side." 
    
    "These steps surely lead to the roof, but the sign on the pillar states, \"Authorised Personnel Only.\""
    
    "Maybe it's best that I didn't ask anyone."
    
    "I scan the area. {w}Nobody."
    
    "I find myself climbing the steps, looking over my shoulder to make sure no one is privy."
    
    scene school_out011_evening with slowd
    
    "The roof is vacant." 
    
    "I'm not surprised, this place has seen better days."
    
    "Why would she want to meet me here? This doesn't seem like a safe place to meet a stranger."
    
    "..."
    
    "It's been twenty minutes, she should be here." 
    
    t"I get restless and pace the roof, looking out through the fence." with slowd
    
    t"It's like I'm on the divide between two worlds. The human world one way, the natural world the other."
    
    t"The evening breeze whistles through the fence, drawing my attention back to the city."
    #"I leer over the city, 
    t"It's like one giant organism from up here; humans like cells and streets like veins."
    
    t"The buildings like organs I add as an after thought, just to complete the comparison."
    
    t"As for me, I'm a foreign cell trying to adapt to this new biosystem. {w}Trapped in the belly of the beast... "
    #maladaptive 
    #q"\"I can't believe it's you.\""
    
    window hide 
    nvl clear 
    
    q"\"It is you...\"" with slowd
    
    "A familiar voice grabs my attention..."
    
    #"It's..."
    
    play music "audio/music/bensound-thejazzpiano.mp3" fadein 2.0
    
    show D 1YSerious_Flat at PM1 with slowd 
    
    p"\"Danielle?\""
    
    "I'm frozen by her analyzing gaze. It's as if she's tearing me apart and reconstructing me in her mind."
    
    show D 1YSerious_Flat at PC1 with slowd
    
    d"\"You're the only new student in my class.\""
    
    d"\"Lost Cause.\""
    
    d"\"Explains why you don't know what to do with your life.\""
    #d"\"That's why you don't know what to do with your life.\""
    
    "Ouch. She doesn't miss the opportunity."
    
    "I'm left tongue-tied. I can't deny it."
    
    #"Out of all people..."
    
    d"\"Have you played Smackdivision's new MMORPG, Magnum Dilon?\""
    
    "Prompted by the unexpected question, my brain lurches a response."
    # my brain turns and forces out words
    p"\"I... can't say I have.\""
    
    "{i}How many times am I going to say that...?{/i}"
    
    d"\"It's good. It runs on the Ethereal engine.\""
    
    "That engine rings a bell..."
    
    p"\"Wait, didn't you start creating your own game?\""
    
    show D 1YSerious_Grit with slowd
    
    d"\"I did.\""
    
    #"It's strange to see Danielle looking... ashamed? Well, anything other than impassive for that matter."
    #"Her shoulders drop; I'm surprised to see her looking... ashamed? Well, anything other than impassive for that matter."
    
    "Her tone stifled through her gritted teeth."
    
    d"\"But I gave up on that. It was a terrible idea.\""
    
    p"\"That sucks, I was on the shortlist. Have you started something new?\""
    
    show D 1YSerious_Flat at PC1 with slowd
    
    "Her eyes narrow."# with fierce determination."
    
    d"\"I have. I'm going to complete it this time.\""
    
    #show D cnormal with slowd
    
    d"\"Don't tell Jennifer about this, OK.\""
    
    p"\"Why not?\""
    
    #d"\"Because she'll tell everybody.\""
    
    d"\"Because she'll annoy me to no end.\""
    
    #d"\"She knows I play a few games, but I don't want the rest of the school to know how much time I really spend playing games.\""
    
    "I'm stunned; she was so cold yesterday." 
    
    "Now I already know something about her that Jennifer doesn't."
    
    #"Though, she interjected Jennifer before she could speak in class. So Jennifer must know something I don't." —- save this for later custard :p 
    
    p"\"Your secret's safe with me.\""
    
    #"My word choice pulls a scowl from her." 
    
    "It pulls a scowl from her."
    
    #"So it's a secret?"
    
    d"\"Good.\""
    
    "Unease strikes at the thought of holding it over her."
    
    "The setting sun recedes. A yawn seizes me." #A yawn escapes my lips."   #, I let out a yawn."
    
    
    #A yawn escapes from my lips.
    
    d"\"Yes, I must get going. I altered my schedule to meet you here.\""
    
    "Schedule? Beyond school? My stomach falls at the thought."
    
    p"\"Erm, thanks.\""
    
    d"\"What for?\""
    
    p"\"For not ringing the police, I guess?\""
    
    show D 2YSerious_Relaxed with slowd
    
    "A smirk tugs on her lips."
    #"Is that a smile tugging on her lips?"
    
    d"\"That's OK. Bye.\""
    
    
    stop music fadeout 3.0
    hide D 2YSerious_Relaxed with slowd
    
    "She turns on her heel and marches to the steps."
    
    
    p"\"I'll see you tomorrow...\""
    
    "My words left to scatter in the wind."
    
    #It reminds me of the pain when I spoke with broken ribs. 
    #Her voice dislocated, it's like it pains her to speak. I can't help recall my forced speech in the hospital. 
    #
    
    
    
    
    
    
    
    
    
    
    scene room_boy16_day with longf
    
    
    #"I awake before my alarm. Even though I've slept for twelve hours, I feel sluggish."
    
    "I wake before my alarm. Despite twelve hours of sleep, I'm fighting to stay awake."
    
    
    #Despite sleeping for twelve hours, I feel sluggish."    
    "I kick off my quilt and the cold drives me from my pit."
    #"I slide out of bed and begin preparing myself for the day."          
    
    
    #"My morning stretch is disturbed by a thought: Jennifer wants me to join her for a swim today."    
    #"A thought disturbs my morning stretch: Jennifer wants me to join her for a swim today."
    #"That's right, Jennifer wants me to join her for a swim."
    
    "A thought disturbs me as I dress: Jennifer wants me to swim today."
    
    #"Really though, swimming leaves me with an uneasy feeling. It's something I should've avoided."
    
    "I roll up my trouser leg to reveal the scar tissue." 
    
    "Two hairless spots of bright pink located above my ankle and below my kneecap, marking the incisions of the metal rod and screws."
    
    #"It's not that I'm ashamed of how it looks; I'm avoiding questions I'd rather not answer."
    "I'm not ashamed of how it looks; I'd rather avoid questions I don't want to answer."
    
    #skip to the end of class? 
    scene school05_day with slowf
    
    "I'm... early, again."
    
    "There are a few people conversing in the classroom, so I wait outside."
    
    "I'm distracted by footsteps approaching from behind."
    
    #play music "audio/music/bensound-thejazzpiano.mp3" fadein 2.5
    
    #play music "audio/music/bensound-thejazzpiano.mp3" fadein 2.0   
    show D 1YSerious_Flat at PC1 with slowd
    
    #"It's Danielle."
    
    d"\"Hey.\""
    
    p"\"Hey...\""
    
    "She fixes me with an expectant stare."
    
    p"\"I.. er...\""
    
    "...Don't know what to say."
    
    "She takes a glimpse to each side."
    
    d"\"Don't you play anything anymore?\""
    
    p"\"No...\""
    
    #"I haven't played anything in months." 
    "When I think about it, not since we stopped talking."
    
    p"\"Not since Clubseal.\""
    
    d"\"I haven't played it since we did.\""
    
    p"\"Yeah... me either—\""
    
    #stop music fadeout 3.0
    
    #show D cnormal at left with move
    
    show D 1YSerious_Flat at PCL1 with move
    
    show J 1YHappy_OpenSmile at PMR1 with slowd
    
    #show J mwavecs at right with slowd
    
    j"\"Hey, guys!\""
    
    #show J cnormalc at right with slowd
    
    "Jennifer waves from the end of the corridor and parades over."
    
    show J 2YHappy_Smile at PCR1 with slowd
    
    "Our conversation shunned at her arrival."
    #"Her presence shuns out conversation."
    
    "As far as Jennifer knows, I've exchanged a few words with Danielle."
    
    "I get the impression Danielle wants to keep it that way."
    
    p"\"Hey.\""
    
    j"\"We're going swimming after school, you should join us!\""
    
    "She pokes Danielle in the side, pulling a grimace from her."
    
    d"\"No, thanks.\""
    
    j"\"That's OK, we're still going.\""
    
    #"She nudges me with her shoulder. A reminder I'm yet to expose my scars."
    #It seems I can't forget I'm yet to expose my scars.
    
    "She nudges me with her shoulder. Another reminder I'll be exposing my scars."
    
    "Danielle inspects her phone."
    
    d"\"Class is starting.\""
    
    "We head inside and ready ourselves for class."
    
    #stop music fadeout 2.5
    
    #time pass intil end of school?
    
    
    scene school02_day with slowf
    
    "The end of school dawns, the prospect of swimming ever daunting."
    
    show J 2YHappy_Smile at PMR1 with fastd
    hide J 2YHappy_Smile with slowd
    
    "The moment the bell rings, I spy Jennifer lurking in my peripheral." #approaching 
    
    play music "audio/music/bensound-memories.mp3" fadein 4.0
    show J 2YHappy_Smile at PC1 with slowd
    
    "She springs and lands by my desk, drawing a few glances from our exiting classmates."
    
    j"\"Ready?\""
    
    #Name Jennifer Autumn; she has the hair of the trees and eyes of the leaves. 
    #jen t-shirt
    
    p"\"I guess so.\""
    
    hide J 2YHappy_Smile with slowd
    
    "She's already off, it takes me a few keen strides to catch up with her."
    
    #show J mnormal
    scene school05_day with slowd
    
    show J 2YHappy_Smile at PC1
    
    j"\"So, how're you finding it here?\"" #at a new school
    
    p"\"It's... not so bad.\""
    
    "I think that's a fair assessment." 
    
    "I'm not sure why I had myself so worked up about coming here. Although, it's easier said in hindsight."
    
    "She laughs."
    #corridor
    j"\"You don't seem too happy about it, leave something behind?\""
    
    
    scene school_in003_day with slowd
    
    show J 2YUpturned_Smile at PC1
    
    j"\"Or someone, maybe?\"" 
    
    j"\"Come on, you can tell little old me~!\""
    
    "She probes my expression."
    
    p"\"N-no, nothing...\""
    
    "Can you leave nothing behind?" 
    
    "Well, there was something I left: my existence. Which might as well have been nothing."
    
    "I shake my head of the reminder." 
    
    #show J mnormal with slowd
    
    show J 2YHappy_Smile at PC1 with slowd
    
    #"Her curious exitement is sapped away, sensing my apprehension around the subject—we fall into a strange silence."
    
    "My apprehension saps away her curious excitement—we fall into silence."
    
    #"It's strange because she's anxious; 
    "She keeps twitching as if she's about to say something and withdraws." 
    
    #changing area
    scene school12_day with slowd
    
    show J 2YHappy_Smile at PC1
    
    "When we reach the changing rooms, she breaks the silence."
    
    j"\"So, are you any good at dancing?\""
    
    #"Her question met by my lifted brow."
    #"I meet her question with my lifted brow."
    #"I meet her question with a lifted brow."
    "My brow lifts to her question."
    
    p"\"No, why would I be?\""
    
    
    j"\"I'm just messing with you!\""
    
    show J 2YHappy_OpenSmile at PC1
    
    "She grips my wrist and pulls me."
    
    j"\"Come on, let's get changed!\""
    
    
    #"She takes hold of my hand and urges m
    
    "Wait, {i}together?{/i} {w}I catch my tongue and ride it out."
    
    
    #Have Jennifer's sprite move forward and pull into darkness.
    
    #scene black with slowd
    
    #I catch my tongue and ride it out. 
    
    
    
    #hide j magape
    #scene school10_day with slowf
    
    #j"\"The male changing rooms are through there.\""
    
    #p"\"Thanks.\""
    
    stop music fadeout 3.0
    scene school12_day with slowf
    
    "I get myself changed but Jennifer's still in there. What's taking her so long?"
    
    "I decide to head out on my own."
    
    #pool
    
    scene school15_day with slowd
    
    "I've never been swimming before, but... here it goes."
    
    
    #splash
    #psychedelic
    play sound "audio/sfx/Splash.mp3"
    p "\"Argh!\"" 
    #Cold! 
    "My breath rushes from my lungs, I'm quick to climb out."
    #"The water cold enough to take my breath away, I rush to the side and climb out. That was quite a wake up call."
    
    #"The afternoon breeze brushes over my back, hypersensitive due to the layer of water enveloping it."
    "The afternoon breeze pulls a shiver from me." #I shake off the water."
    
    "I glance around, hoping nobody was privy."
    
    #play music "audio/music/bensound-psychedelic.mp3" fadein 3.0
    
    #"A snicker from behind me makes my head one-eighty, our eyes connect."     
    
    play music "audio/music/bensound-enigmatic.mp3" fadein 4.0
    #show J mnormals with slowd
    
    "My head spins to a snicker from behind; our eyes connect."
    
    #show J msmiles with slowd
    
    
    "I lower my head and she bursts into a fit of laughter."
    
    j"\"Haha~! You're such a girl!\""
    
    "I have to admit, it's emasculating to be called a girl—by a girl I've met a handful of times." 
    
    #"Having been caught of guard, I take a moment to compose myself."
    #"Unchecked ego bubbles from my lips."
    
    
    p "\"It's cold! I'd like to see you jump in there.\""
    
    "Having now taken in the sight of her, I find myself taken back by her scantily-clad body."
    
    #show J mnormals with slowd
    
    j "\"Watch me!\""
    
    "She says it with an air of confidence that makes me want to eat my words."
    
    play sound "audio/sfx/Splash.mp3"
    hide J mnormals with slowd
    
    #splash
    
    #stop music fadeout 3.0
    
    "I find myself swallowing them when she dives into the pool, resurfacing on the other end with a devilish grin." 
    
    
    "I'd be lying if I said I wasn't impressed."
    
    #"She climbs out, with little attempt to catch her breath."
    
    #show J mnormals with slowd
    
    #"She strides over, still sporting her grin."         
    "She climbs out and strides over, sporting a grin."
    
    
    j "\"Go on, I bet you can't reach half way.\""
    
    #play music "audio/music/bensound-extremeaction.mp3" fadein 5.0
    
    #"What have I managed to get myself into?" 
    "What have I gotten myself into?" 
    
    "I'm not sure, but my pride isn't about to let me back down." 
    stop music fadeout 3.0
    hide J mnormals with slowd
    
    #"I stand at the edge of the pool, readying myself with a deep breath."
    "I ready myself at the edge of the pool and take a deep breath."
    
    play sound "audio/sfx/Splash2.mp3"
    play environment "audio/background/underwater.ogg" fadein 4.0
    scene underwater with slowd
    
    "I dive in, flailing my arms and legs. I find it's counterproductive as I've almost come to a standstill on a few occasions." 
    
    "I feel my breath coming to an end, despite taking the largest breath I could muster." 
    
    "I just have to make it half way, but I can't determine my location through my obscured vision."
    
    #play music "audio/music/Anxiety.mp3"
    
    "I inhale a mouthful of water, plunging panic down my throat."
    #"I inhale a mouthful of water; panic plunges down my throat."
    
    "Can't. Breathe!"
    
    #"I flitter to the surface and gasp for air."
    "I thrash to the surface and gasp for air."
    
    #"My survival instincts kick in and panic ensues, causing me to flitter to the surface and gasp for air." 
    #"I gasp and swallow 
    
    stop environment fadeout 2.5
    stop music fadeout 2.5
    #scene school15_day with slowd
    play environment4 "audio/sfx/heartbeat.mp3" fadein 3.0
    scene school15_day2 with longd
    scene school15_day with longd
    stop environment4 fadeout 2.0
    
    "An image of reaching out to the doctor flashes through my mind."
    
    #"I rest my torso on the side of the pool, my heart pounding against the ground." 
    "I rest my torso over the edge of the pool, heart pounding against the ground." 
    #play heartbeat over this scene!?!?!? Or a short burst again after exiting the pool? 
    #"I've only managed to make it a third of the way, leaving me ashamed as she approaches."
    
    
    #"She approaches and waits for me to gather myself."
    "She approaches as I cough and spit out water."
     
    # gape sprite in swimsuit here
    
    j"\"Are you OK?\""
    
    #show J mnormals with slowd
    
    "I compose myself and crane my neck towards her."
    
    p"\"Yeah... I'm fine.\""
    
    #j "\"See, I told you!\"" 
    
    "I take a deep breath and rise without her help."
    
    "I've made it about a third of the way, but I can't care."
    
    
    
    play music "audio/music/bensound-memories.mp3" fadein 6.0
    
    
    "Her concern melts into a grin."
    
    #j"\"But...\""
    
    #j"\"Can I ask you a question?\""
    j"\"Can I ask somethin'?\""
    
    p "\"...You just did.\""
    
    #"The vestigial adrenaline manifests in sarcasm."
    "The residing adrenaline results in a jibe."
    
    #"The adrenaline leaves me snappy."
    #feeling
    "She makes a movement as if she's going to jab my arm, but retracts her hand."
    
    j"\"Silly! Anyway, have you swam before?\""
    
    p "\"I... haven't. How'd you know?\""
    
    j "\"Well, you'd know that the pool would be cold for a start.\""
    
    p "\"Guess I can't argue with that...\""
    
    j "\"You shouldn't flail your arms and legs, either. Get into a controlled rhythm or you'll waste valuable energy and oxygen.\""
    
    p "\"Thanks for the tip.\"" 
    
    p "\"What's with your swimsuit by the way? I haven't seen one like it before.\""
    
    #show J mvforv with slowd
    
    j "\"This is my outfit for the synchronised swimming team!\""
    
    #"Shooting her arms in a V."
    
    #"She shoots her arms into a V, I imagine for vendetta."
    "She shoots her arms into a V. I imagine for vendetta, against my sanity."
    
    #show J mnormals with slowd
    
    j "\"It's best for me to train in this as I'll have to perform in it.\""
    
    j "\"Anyway, I have my routine to attend to. You should find a rhythm and go from there.\""
    
    p "\"Thanks, I'll give it a go.\""
    
    hide J mnormals with slowd
    
    "This time I brace myself for the cold, easing myself into the pool and finding a relaxed rhythm." 
    
    #"I find my new methodical movements more efficient; my speed has increased and I exert less energy." 
    
    "My new methodical movements more efficient; my speed has increased and I exert less energy."     
    
    "After a few measured lengths, I pick up the pace and find myself feeling... liberated?"
    
    "Well I did, until I overexerted myself. My breath's ragged and my leg drags like lead."
    
    #You need to do the "it shouldn't hurt to drink a cup of tea" scene.
    
    "I climb out and sit on the edge. My weight shifted to my right buttock, allowing my left leg to rest." 
    
    "I proceed to rub my leg, pressing points to inspect the damage. It's nothing major, I've put too much strain on it."
    
    t"Content it's nothing to worry about, I find myself captivated by Jennifer; who's going about her routine." with slowd
    
    #"Her body elegant, every movement carefully choreographed as she glides from one end of the pool to the other."
    t"Her body is elegant. She glides from one end of the pool to the other as if every movement was choreographed."
    
    
    
    t"The top half of her body submerges and her legs straighten out into the air; she performs a running like motion before flipping and resurfacing."
    #I find myself mesmerized as t
    
    #"She wipes the water from her eyes and spots me watching from the sidelines." 
    t"She wipes her eyes and spots me watching on the sideline."
    
    window hide 
    nvl clear 
    
    "I avert my gaze." with slowd #Though it's obvious I was watching, I don't want to give the wrong impression."
    
    j"\"It's OK. You can watch!\""
    
    "Her presumptuous statement—with my previous line of thought—brings a burning to my cheeks." # rise in
    
    "She swims over, her expression growing curious."
    
    #I can't help but find it a little misleading. I turn away to hide the burning in my cheeks as she swims over."
    
    #j"\"Hey, are you OK? You're sitting a little funny, and your face is red.\""
    j"\"Are you OK?\""
    
    p"\"Yeah! I'm fine, I'm fine...\""
    
    "It's a knee-jerk response." 
    
    "There's no way I can tell her about the metal rod in my leg, or the impurity of my thoughts."
    #She measures me for a moment,
    
    "She measures my unnatural position and expression."
    
    "A questioning tilt lines her brow."
    
    j"\"Are you about to fart?\""
    
    p"\"No!\""
    
    "She giggles at my reaction."
    
    j"\"I'm done for today, you ready to head in?\""
    
    p"\"Sure.\""
    
    "Happy to drop the subject, I rise with a wince. She misses it as she climbs out."
    
    #"She doesn't seem convinced; I can see her trying to examine my submurged leg."
    
    #"I'm unsure how she didn't notice in the first place, it's the most obvious scar on my body."
    
    #"I wince as I stand up, fortunate that Jennifer misses it as she climbs out of the pool. I take a deep breath to suppress the pain."
    
    #show J mnormals with slowd
    
    j"\"So, how'd you find it?\""
    
    p"\"Huh?\""
    
    #show J msmiles with slowd
    
    j"\"Swimming!\""
    
    #show J mnormals with slowd
    
    p"\"Oh. A lot better after your advice, thanks.\""
    
    #"I notice she does glance a few times at the scarring on my leg, but she doesn't say anything about it."
    
    stop music fadeout 3.0
    
    "I notice her glance at the scarring on my leg, but she doesn't say anything."
    
    "It's the most obvious scar on my body. I'm surprised she didn't notice earlier."
    
    "We share a few moments in silence before heading in."
    
    #(Time pass, now dressed)
    
    #changing room
    
    
    scene school12_day with slowd
    
    "She's taking longer than last time. Though, I'm not exactly sure why I'm waiting."
    
    #show J mnormalc with slowd
    
    show J 2YHappy_Smile at PC1 with slowd
    
    j"\"So, you'll come again?\""
    
    p"\"Maybe.\""
    
    j"\"You will...\""
    
    "She whispers and makes her way through the main doors."
    
    hide J 2YHappy_Smile with slowd
    
    "I'm curious why she still wants me to come."
    
    "But it's nice knowing she wants me to."
    # feels good
    
    
    
    
    #Sarah next? "Shouldn't hurt to drink a cup of tea" and asking her about the art club. 
    
    
    scene room_kitchen06_day with longf
    
    "I'm approaching my first weekend. My first week of school."
    #conquered my first week in school. 
    "I'm beginning to feel this won't be so bad." 
    
    "Though, my food is dwindling."
    
    "I'll be fine for tonight, but I should head out tomorrow and survey the area."
    
    "Content with my conclusion, I rinse my dish and rest it to dry."
    
    scene hospital03_day with slowd
    
    #show S mshock with slowd
    
    show S 2YAnxious_Open at PM1 with slowd
    
    "As I exit the kitchen, Sarah appears through the far door."
    
    #She keeps glancing at door 119? :p 
    
    p"\"Hey, Sarah.\""
    
    s"\"Hey...\""
    
    show S 2AAnxious_Flat at PC1 with slowd
    
    "I approach her and realise I have nothing to say."
    
    p"\"So... what're you doing?\""
    
    s"\"Nothing...\""
    
    "She glimpses to room 119."
    
    p"\"I see...\""
    
    "She's not making this easy."
    
    p"\"I was wondering...\""
    
    p"\"If you'd help me with the local area? I need to do some shopping.\"" #, I'm running low on food
    
    "I watch the conflict play out across her face."
    
    show S 2YAnxious_Smile with slowd
    
    s"\"S-sure.\""
    
    "She doesn't seem sure. I'm beginning to question whether she's capable of saying no."
    
    s"\"I just need to... get my things.\""
    
    p"\"Me too.\""
    
    scene hospital03_day with slowf
    
    #slowf
    "I head into my room to grab my bag and wallet."
    
    show S 1AAnxious_Flat at PC1 with slowd
    
    
    
    "Sarah emerges not long after. So 119 is her room."
    
    p"\"Ready?\""
    
    show S 1AAnxious_Smile at PC1 with slowd
    
    s"\"Y-yeah...\""
    
    #"I set the pace and she follows reluctantly."
    "I set the pace and she trails."
    
    
    #outside of dorms
    
    scene school_out002_day with slowd
    
    "She falls in step as we exit the building, pinning her eyes on the ground." #her eyes pinned to the floor." 
    
    "The silence deafening."
    
    #main building
    
    scene school_out009_day with slowd
    
    #show S cnormal at left with move
    
    #show J mwavec2 at right with slowd
    
    show S 2ACalm_Flat at PCL1 
    show J 1YHappy_OpenSmile at PMR1 
    with slowd
    
    "Speaking of deafening..."
    
    j"\"Hey, Peter! Cara!\""
    
    #toaster music
    show J 2YHappy_Smile at PCR1
    show S 1AAnxious_Flat 
    with slowd
    
    "Jennifer strides towards us. Sarah shrinks to her presence."
    
    play music "audio/music/bensound-enigmatic.mp3" fadein 2.0
    
    #"Wait..." 
    
    "I glance behind us and shoot her a raised brow." #confused look."
    
    p"\"Cara?\""
    
    #"An awkward silence lingers as I look from girl to girl.."
    
    #p"\"Who's Cara?\""
    
    #"..."
    
    p"\"...You mean Sarah?\""
    
    "A hint of red rises in Jennifer's cheeks."
    
    show SX Blush at PCL1 with slowd
    
    "I turn to Sarah; her head bowed and cheeks ablaze."
    
    j"\"Oh my gosh, I'm so sorry!\""
    
    j"\"I thought you said Cara when we first met! You remind me of someone I used to know...\""
    
    "I have to stifle a laugh at the situation."
    
    "But now we're stood in this awkward triangle, I feel responsible for Sarah's discomfort."    
    
    #"One option comes to mind: bail."
    
    p"\"We need to get going. Right, Sarah?\""
    
    "Sarah's gaze fixes on the gate. I've made the right choice."
    
    show J 1YHappy_OpenSmile with slowd
    
    j"\"Yeah, me too. See ya around, guys!\""
    
    p"\"Later.\""
    
    s"\"B-bye.\""
    
    hide J cwavec with moveoutright
    show S 1AAnxious_Flat at PC1 with move
    
    "Is she so shy she'd let someone call her by the wrong name?"
    
    "It's an amusing thought, but it's cute."
    
    stop music fadeout 2.0
    
    #entrance
    
    #play music "audio/music/Wisps of Whorls.mp3" fadein 3.0
    
    scene school_out003_day with slowd
    
    
    "I'm grateful for our saunter, my leg is still aching from swimming."
    
    show S 2ACalm_Smile at PC1 with slowd
    
    "Sarah's silent." #staring into the trees by the entrance."
    
    "I watch her curiosity sweep from the birds in the trees down to insects in the bushes."
    
    "She's always uneasy, yet unassuming."
    
    "It's conflicting, I don't know whether to be anxious or relaxed myself."
    
    #city
    #sounds
    
    play environment "audio/background/city2.mp3" fadein 3.0
    scene street001_day with slowd
    
    show S 1AAnxious_Flat at PC1
    
    "She shrinks in the city. I imagine she's as intimidated by it as me."
    
    "Her eyes flicker at people walking past, as if they were potential assailants."
    
    #"I imagine she's as intimidated by it as I am."
    
    #"Maybe I should say something."
    
    #"I search my mind for a topic, the poster in class comes to mind."
    
    #Our silence adds to the unease. 
    "Our silence unsettling; I search for a topic, the poster in class comes to mind."
    #sprite
    p"\"So... are you in the art club?\""
    
    show S 1YAnxious_Smile with slowd
    
    s"\"N-no, I just like to... draw.\""
    
    show S 1AAnxious_Flat with slowd
    
    "Her reluctance palpable. Maybe she wants to join but she's too shy?"
    
    "Damn, I can't think of anything to say."
    
    "It makes me feel bad, for what feels like {i}using{/i} her as a guide."
    
    #shop
    
    stop environment fadeout 2.0
    #play environment2 "audio/background/shopping.ogg" fadein 2.0
    scene shop01_day with slowf
    show S 2ACalm_Smile at PC1
    
    #sprite
    s"\"Here we are.\""
    
    p"\"Thanks. What're you getting?\"" #Are you getting anything in particular
    show S 1AAnxious_Smile with slowd
    s"\"I don't... need anything.\""
    
    p"\"Really? I feel bad for dragging you out now...\""
    
    #play music "audio/music/Wisps of Whorls.mp3" fadein 3.0
    #play music "audio/music/Kevin_MacLeod_-_Dream_Culture.mp3" fadein 3.0
    show S 1YAnxious_Smile with slowd
    s"\"It's OK.\""
    "Her smile and tone genuine enough to put me at ease."
    
    "Still, I can't help wonder: does she feel a responsibility to help me or does she feel inclined because she's afraid to say no?"
    hide S cNsmile with slowd
    #"She browses the aisles, her fingers twining in here sleeves."
    t"She leads me down the aisles, twisting her fingers in her sleeves." with slowd
    
    t"She brings her sleeve to her lips and stares into the shelves." 
    
    
    t"It's as if she's disconnecting herself from her surroundings rather than browsing."
    
    #"Though she stares into the shelves, it's as if she's disconnecting herself from her surroundings rather than browsing."
    #than looking for anything in particular."
    
    t"She just avoids a passing man, offering an apology he doesn't acknowledge." 
    
    window hide
    nvl clear
    
    s"\"S-sorry...\"" with slowd
    
    "Sarah doesn't strike me as someone who's used to being acknowledged." 
    
    "I think she'd prefer to merge into the background."
    
    "Like a picture..."
    
    "I intercept her and lead the way, picking up groceries as we progress."
    
    #"Sarah decides to grab a few things. I note she has two loaves of bread among them."
    
    "Sarah decides to grab a few loaves and some butter."
    
    "At least it wasn't a complete waste of time for her."
    
    "We make our way to the checkout. The cashier scans through my items."
    
    #"I hand over my items and the cashier scans through them."
    
    C"\"That's nineteen pounds and ninety-one pence, please.\""
    #£19.91
    "Damn, spent more than I thought."
    
    "I shell over the cash and he hands me my change and receipt."
    
    p"\"Thanks.\""
    
    #"The bags jolt my arm as he hands them to me."
    #"The weight of the bags lowers my arm."
    
    "My arms jolt to the weight of my bags."
    
    #"He hands me my bags and my arms jolt to the weight." # of the bags
    
    show S 2YAnxious_Smile at PM1 with slowd
    
    "I rest them aside and wait for Sarah."
    
    #"He scans her items."
    
    C"\"That's three pounds and ninety-six pence, please.\""
    
    show S 2YCalm_Open with slowd
    
    "She fumbles to both pay him and receive the bag." 
    
    "I echo the cashier's smile."
    
    #"I can only smile as I watch."
    
    #"The man smiles at her and gives thanks." 
    
    show S 2YAnxious_Smile at PC1 with slowd
    "She takes her bag and approaches with a wavering smile." #smile wavering on her lips
    
    #"She approaches with a wavering smile."
    show S 2AAnxious_Smile with slowd
    
    s"\"Are you...\""
    
    p"\"Ready? Yeah, let's go.\""
    
    stop music fadeout 3.0
    play environment "audio/background/city2.mp3" fadein 4.0
    scene shop006_evening with slowf
    "The setting sun greets us."
    
    #stop environment2 fadeout 2.0
    scene street001_evening with slowd
    
    "Sarah lingers behind me."
    
    "I attempt to pick up the \"conversation\" from earlier."
    
    p"\"So... have you considered joining the art club?\""
    
    s"\"No...\""
    
    "But I'm shot down faster than last time."
    
    #stop music fadeout 3.0
    
    "This whole trip feels like a disaster."
    
    "I thought she'd open up a little, but it's stressed her out."
    
    "These bags are reawakening the ache in my arms, too..."
    
    stop environment fadeout 2.0
    
    
    #back at halls
    
    scene hospital03_day with slowf
    #sprite
    #"I watch her shoulders relax when we make it back."
    #"Her shoulders ease when we make it back."
    "Her shoulders fall slack when we make it back."
    
    "We head into the kitchen to deposit our goods."
    
    scene room_kitchen06_evening with slowd
    
    "She's packed away her things. I've still got two bags left."
    
    show S 2AAnxious_Smile at PC1 with slowd
    
    s"\"Bye.\""
    
    p"\"Thanks, I appreciate it. See you later.\""
    
    show S 2YAnxious_Smile with slowd
    
    s"\"You're welcome.\""
    hide S 2YAnxious_Smile with slowd
    "She fights a smile and heads back to her room." #wrestles
    
    "I don't know what to think. She's an enigma."
    
    #Mention recovering limbs from swimming? Xd 
    
    
    
    
    
    
    #Curiosity is the wick in the candle of learning.
    
    
    
    #Danielle's Day off:
    
    scene room_boy16_day with longf
    
    #"I want to lounge in bed, I can see myself not moving today."
    
    "I spend the morning playing any game of interest from the Appmarket."
    
    #"I can see myself squandering the day away in bed." 
    "I can see myself squandering another Saturday." #in bed 
    
    "But after my productive week, it'd be a shame to revert so soon."
    
    "With little else in mind, I decide to explore the campus."
    
    "I might check out the art room, there seems to be a music room too."
    
    #Look for the art room or go gaming with Danielle as a choice??? :o
    
    # How far should I go? I should introduce some new bgs
    #on that corridor?
    
    play music "audio/music/bensound-thejazzpiano.mp3" fadein 6.0
    scene school_in004_day with slowf
    show D 2YGentle_Flat at PC1
    "I almost bump into Danielle as I turn the corner."
    
    #"She probes my expression."
    
    p"\"Hey. What are you up to?\""
    
    "Her expression shifts from a lifted brow to an easy smile."
    
    d"\"I'm going to the staffroom.\""
    
    p"\"What, why? You in trouble or something?\""
    
    
    show D 2Closed_Flat with slowd
    d"\"No.\""
    
    "She sighs in exasperation."
    
    show D 2YGentle_Flat with slowd
    
    d"\"They let me use the computer room on weekends.\"" 
    
    d"\"My laptop is laggy...\"" #lags when I play Magnum Dilon.\""
    
    "A drop of frustration mars her tone."
    #Her chin rests in her palm. Her gaze explores the clouds. 
    #posters scattered on the back wall.
    p"\"Oh, I see.\""
    
    d"\"Want to join me? There's always a few free.\""
    
    #"She's approached me a few times since we spoke on the rooftop, but Jennifer has cut us short."
    
    "I can't deny that I'm curious." 
    
    "She's seemed eager to talk to me; Jennifer has cut us short a few times."
    
    p"\"Sure.\""
    
    "She turns on her heel and leads the way."
    
    #staffroom
    scene Computer_Room with slowf
    
    "After visiting the staffroom, they let us in. It seems some of the teachers use the computer room on weekends too."
    
    "The teachers give greetings to Danielle, who only nods in return."
    
    T"\"So, are you going to introduce us?\""
    
    #show D cnormal with slowd
    
    d"\"He's joining me.\""
    
    
    "She strides past, making her way to her goal."
    
    stop music fadeout 1.5
    
    #T"\"I see.\""
    
    "Guess I'll introduce myself then."
    
    p"\"Hey, I'm Peter. I moved in last week.\""
    
    "Another teacher turns in his chair, realisation glinting in his eye."
    
    
    q"\"Peter. Nice to meet you, Peter.\""
    
    "I reach his extended hand; he shakes and pulls me in."
    
    mb"\"I'm new here, too. I'm Mr Brent.\""
    
    p"\"Nice to meet you.\""
    
    mb"\"I thought I should introduce myself. It's hard being the new guy, wouldn't you say?\""
    
    p"\"I guess so.\""
    
    #"He releases me and turns back in his chair." #a grey coat swings from the back of his chair? 
    
    "He turns back in his chair, grey coat swinging from the back."
    
    "I wait, expecting something more—it doesn't come." #A grey coat just settles on the back of his chair."
    
    #p"\"Thanks.\""
    
    #We don't have thrusters yet. It's easy to do alone once you get them.
    
    "Well, that was weird."
    
    #"I follow Danielle to the far computers."
    "I follow Danielle to the far computers who meets me with a lifted brow."
    
    show D 1YSerious_Flat at PC1 with slowd
    
    d"\"Do you know him?\""
    
    p"\"No, why?\""
    
    d"\"He started two weeks ago.\"" 
    
    d"\"I haven't heard him say more than a few words to anybody on his own accord.\"" #He's quiet. 
    
    "I shrug it off."
    
    "I doubt I would've heard more than a sentence or two from Danielle if she wasn't Destiny."
    
    
    
    
    
    
    
    
    
    
    
    
    p"\"Anyway, you should show me that game.\""
    
    p"\"What was it again? Magnum... something.\""
    
    show D 1Closed_Flat at PC1 with slowd
    
    d"\"Magnum Dilon.\""
    
    hide D 1Closed_Flat with slowd
    
    "We settle down on a computer each."
    
    
    
    d"\"OK, give me a few minutes, I'll get you a code.\""
    
    p"\"A code?\""
    
    d"\"So you can play.\""
    
    "She proceeds and I take the opportunity to read up on the game."
    
    
    
    #hide D cnormal with slowd
    
    
    #"Humanity has consumed the majority of the world's resources. People left to starve throughout kingdoms across the world, not deemed worthy of survival. Every country fought for a stake in the resouces, until four remain. The four remaining factions: Viktos who favour the axe, Namrosian that favour the sword, , each surviving until the end times with their unique weapon enhancements and abilities." with slowd
    
    t"Humanity has consumed the majority of the world's resources. People left to starve throughout kingdoms across the world, not deemed worthy of survival. Every country fought for a stake in the resouces, until four remained." with slowd
    
    t"The four remaining races each developed technologies to form super soldiers. Each faction with a part to play in what the people rumour to be \"the end times of Earth.\""
    
    window hide 
    nvl clear
    
    "My eyes come to rest on the price tag. I could afford it and its subscription fee, but it would be a dent in my funds." with slowd
    
    p"\"Damn, this game isn't cheap.\""
    
    show D 1YSerious_Flat at PC1 with slowd
    
    d"\"It's OK. Type this in.\""
    
    "She motions to her screen. I lean back to find a serial number."
    
    p"\"Wait, you bought an account for me?\""
    
    show D 1YSerious_Relaxed with slowd
    
    d"\"No, I have ways.\""
    
    p"\"That seems...\""
    
    d"\"Don't question a freebie.\""
    
    
    p"\"OK, OK. Read out the code.\""
    
    show D 1YSerious_Flat at PC1 with slowd
    
    "She reads it aloud and I type it in."
    
    d"\"That's my friend's account. Go to his level 37 Viktese Warrior.\""
    
    p"\"OK...\""
    
    d"\"I'll go on my level 29 Namrosian soldier and still beat you.\""
    
    "I forgot how competative she was."
    
    hide D 1YSerious_Flat at PC1 with slowd
    
    #"She sends an invite and the timer counts down."
    "I accept her invitation and the timer counts down."
    
    #centered "3... 2... 1..."
    
    "3... 2... 1..."
    
    #play epic?
    
    play music "audio/music/bensound-epic.mp3" 
    #play music "audio/music/piano snip Kevin_MacLeod_-_Crossing_the_Divide.ogg"  #L0L
    #play music "audio/music/myuu - It_s Not Over Yet cut intro.ogg"  #L0L
    
    #map image here?
    
    t"Fight!"
    
    t"We're summoned to Forest Fortress." 
    
    t"Small outposts are scattered through the trees, hidden by thick foliage." 
    
    t"Rope bridges run through the canopy."
    
    t"Basics first, I find the attack button and slash through the air with my futuristic battleaxe."
    #My axe thrusts through the air. 
    t"Damn, the movement is slow, there must be someway..."
    
    nvl clear 
    
    t"I press through the controls and my character boosts through the air."
    
    
    t"This will take some getting used to."
    
    #t"I spot a movement in the canopy. She must be on the rope bridges."
    t"I spot movement in the canopy above." #She must be on the rope bridges."
    
    t"I try to spot her with the awkward camera rotation." 
    
    t"When I catch a glimpse, it's too late—she buries her sword in my back."
    #her sword slams through my back."
    
    window hide 
    nvl clear 
    
    stop music fadeout 4.0
    
    "\"x-Destiny-x is the victor\" slams onto the screen, cracking the make-believe lense."
    
    
    
    "I hear her chuckling behind me."
    
    show D 1YSerious_Flat at PC1 with slowd
    
    d"\"I see you're still a noob.\""
    
    p"\"That's cheating. I don't know the controls yet.\""
    
    d"\"Ignorance of law excuses no one.\""
    
    p"\"I don't see how that applies here.\""
    
    d"\"Do I really need to lecture you about how tough the world is?\""
    
    p"\"It's just a game.\""
    
    d"\"Then you shouldn't be upset about losing, right?\""
    
    p"\"I'm not!\""
    
    show D 1YSerious_Smirk with slowd
    
    "A few teachers glance over; her lips curl into a smirk."
    
    d"\"Again?\""
    
    "I sigh in resignation."
    
    
    p"\"After I've looked up the controls.\""
    
    scene Computer_Room with slowf
    #reset scene
    "No use. She's too good."
    
    "I can't look at her, that smirk will annoy me."
    
    p"\"Again.\""
    
    "She says nothing, but the counter ticks down..."
    
    scene Computer_Room with slowf
    #scene reset
    
    "She plucks me out of the air with her sword and slams me into the ground. Dead.{w} Again."
    
    "I'm sure it's 11-0 to her."
    
    p"\"I'm done.\""
    
    
    show D 1YSerious_Flat at PC1 with slowd
    
    d"\"...\""
    
    p"\"...\""
    
    d"\"I should probably head back. It was fun.\""
    
    p"\"Yeah, for you I bet.\""
    
    play music "audio/music/bensound-thejazzpiano.mp3" fadein 3.0
    
    show D 1YSerious_Smirk at PC1 with slowd
    
    #"Her smirk is released."# smirk from her."
    "She releases her smirk."
    
    d"\"You played me longer than most. It can't have been that bad.\""
    
    p"\"I have a good mind to never play you again.\""
    
    d"\"That's because you're a noob.\""
    
    "I can only laugh in the face of defeat."
    #"She extracts a defeated laugh."
    
    p"\"Bye, Danielle. I'll see you around.\""
    
    d"\"Bye.\""
    
    hide D 1YSerious_Smirk with slowd
    
    "I look back and she's still on the computer, despite her words."
    
    "Damn, I wanted to beat her. Still, I head out with a lazy smile."
    #She works on her game there, too? With a cloud drive she can save it where she goes. Mr brent will use this for access to her files later on?
    stop music fadeout 2.5
    
    scene school_in004_evening with slowf
    
    "Ah, that's right... I forgot to check out the art room." 
    
    "Maybe another day..."
    
    #"I head back to my room."
    
    #lead into dream scene. 
    
    scene room_boy16_evening with slowf
    
    
    #"With nothing to do, I think back over the week."
    
    "Looks like an early night is on the cards, I couldn't imagine that a week ago."
    
    "But here I am, adapting to my new life, meeting people and making... acquaintances."
    
    "I can't say I've paid much attention in class. Though, I can say the work is harder than the basics in hospital."
    
    "I'm also adapting to this room, this environment." 
    
    "This... {w}{i}new life.{/i}"
    
    #"A smile rests on my lips."
    
    #"For the first time, I'm looking forward to life."
    
    #"I think it's time I put the past behind me."
    
    #"With a peaceful mind, sleep comes easy."
    
    "My shoulders sink into the sheets, every breath feels lighter."
    
    "My mind calm."
    
    #scene room_boy16_night_dark with slowd
    scene black with slowd
    
    "I close my eyes, basking in relaxation." #to savour the moment of serenity."
    
    #"..."
    
    "Sleep caresses my consciousness. I fall into its grasp." #sweet grasp
    #"Sleep comes easy."
    
    play music "audio/music/Drone in D.mp3"
    
    centered "..." with slowd #I slip into another world or I fall in its grasp here?
    
    t"I slip into another world.{w} {i}I've been here before.{/i}" with slowd
    
    t"A watchtower looms on the hill next to a quaint village, lifeless streets and desolate buildings veiled by the gloom of its shadow."
    # casts a shadow over a quaint village."
    #t"The watchtower casts its shadow over the lifeless streets and desolate buildings a quaint village."
    
    #t"Lifeless streets and desolate buildings veiled by the gloom of its shadow."
    
    t"Nostalgia washes over me."
    
    t"This place... it's fuelled by dry ink and scattered pages." #missing pages.
    #t"This place is fuelled by dry ink and scattered pages." #missing pages.
    
    t"My body carries me the same route, skipping the same parts of the journey: past the dilapidated church and tavern."
    
    nvl clear 
    
    t"To the centre of town. Without fail." with slowd
    
    t"A wooden shack rests in the middle, glowing through its crevices."
    
    #t"I jitter towards it, like a moth drawn to its angelic light." 
    
    t"I shimmer towards it, like a moth drawn to its angelic light."
    
    #emits an angelic light
    #t"I'm like a moth drawn to its angelic light."
    
    show ghost angels with slowd
    
    centered "On cue, the door creaks open to reveal two angels." #white phosphorus? 
    
    #window hide 
    
    #t"They were always pleasant, inviting me into their home with offers of food and love."
    #t"They greet me with the smell of heavenly food and open arms."
    
    t"They greet me with open arms. A heavenly aroma wafts from the bubbling pans." with slowd
    
    t"When I enter, the female angel wraps me in her embrace."
    
    #t"In a place I belong."
    
    hide ghost angels wiyh slowd
    
    centered"I close my eyes, trying to savour the feeling of being in her arms..." with slowd #What feeling? Peace, joy, belonging? 
    
    nvl clear 
    
    stop music fadeout 1.0
    
    centered"That's odd..." with slowd 
    
    play music "audio/music/Wounded Strings.ogg" fadein 2.3
    
    #t"The smell of burning rubber invades my nostrils." with slowd #The feeling shifts into nervous curiosity." 
    t"The scents of hot iron and burning rubber coil in my nostrils." with slowd 
    
    #The smell of burning rubber coils in my nostrils. Shrill screams permeate the air. 
    
    t"She pushes me to arms length and digs her fingers into my shoulders."
    
    t"Her shrill scream permeates the air." 
    
    show ghost angel scream with slowd
    show ghost angel scream2 with slowd
    
    t"My eyes open to her twisted features, they melt from her face." #the frame of
    
    t"She convulses and hauls me to the ground."
    
    
    #show ghost angel scream2 with slowd
    
    #play environment4 "audio/sfx/heartbeat.mp3" fadein 3.0
    
    #scene room_boy16_night_dark  blur
    hide ghost angel scream2
    scene room_boy16_night_dark with fastd
    
    #stop environment4 fadeout 2.0
    
    
    
    
    window hide 
    nvl clear 
    
    #wake up
    
    "I wake on impact, gasping for breath."
    #"I wake on impact, gasping for breath. The scream rings in my ears."
    
    #"I landing on the floor and convulsing under intense panic."
    "Cold sweat wreathes my skin. Dried tears stain my cheeks." #My skin wreathed in cold sweat
    
    "I rush out of bed but my legs buckle. "
    
    #"Though the ground finds me, my stomach is in freefall."
    "Though the ground finds me, my stomach remains in vertigo."
    
    "I flail on the floor, groping the fabric of the carpet and the panel on the desk." 
    
    "Panic wells into my heart..."
    
    #"Unable to ground myself..." #for anything to ground myself."
    
    
    scene room_boy16_evening  with slowd
    
    "The brunt of the anxiety passes, but embers reside in my stomach. "
    
    "I fear they'll reignite."
    
    #"I have to focus on something, anything..."
    
    "The more I try not to think about it, the more it festers."
    
    stop music fadeout 2.3
    
    "Try not to think of a pink elephant and you shall."
    
    "..."
    
    play music "audio/music/myuu - Nebula.mp3" fadein 3.0
    scene room_boy16_day  with longd
    
    #"When I calm down, I try to look at it from an objective perspective." #I wipe the dried tears from my cheeks."
    #Now that the feelings have subsided, 
    #"I try to look at it from an objective perspecive." 
    
    #"I realise it's paradoxical, considering it's a subjective dream."
    #"But
    "That dream was once a comfort for me." 

    "That house, those angels... were where I found peace. But it usually ended in her arms."
    
    "It's all so vague. I can't help think they're a subconscious portrayal of my parents." #parallel 
    
    "She shares the same curly hair as my mother."
    
    #"Though, I never seemed to pat attention to the male angel."
    
    "Maybe that hut was parallel to the life I once had."
    
    "A light in the darkness."
    
    "A light that was taken away."
    
    #"Thoughts that take me for the rest of the day..."
    "Thoughts that lay burden on the rest of the day..."
    #
    
    
    
    
    
    #in class? Or thinking the next day?
    
    scene school02_day with longf
    
    #"I'm glad I had yesterday to recover; I doubt I'd have attended class otherwise."
    #"I'm glad I had yesterday to recover; I wouldn't be in class otherwise."
    
    #"Her screams still echo through the corridors of my mind."
    
    #"The world's receded an inch. Everything feels so far away." #seems 
    "My mind's receded an inch. Everything feels so far away." 
    
    "I'm not sure I'd have made it to class today without a day to recover."
    
    "The question lingers whether I should claim sickness to escape."
    
    "Students flood into the room—Jennifer conspicuous among them."
    
    #"Her... personality isn't something I want to deal with right now."
    "But right now, I don't feel like dealing with her... {i}personality.{/i}"
    
    #"Of course, she approaches, eye contact extracts a reflexive smile."
    
    "Of course, she approaches. Eye contact extracts a reflexive smile from me."
    
    show J 1YHappy_OpenSmile at PM1 with slowd
    
    j"\"Hey, Peter!\""
    
    show J 2YHappy_Smile at PC1 with slowd
    
    "But her glee grinds through me."
    #grates
    p"\"Hey.\""
    
    "I can't surpass a hollow tone."
    
    #"A bitter anger drips into my tone."
    
    show J 2YHappy_Flat with slowd
    
    j"\"Are you OK?\""
    
    
    "Confusion tilts her features. She reaches out but her fingers hover over my arm."

    #She reaches out but doesn't touch me."
    #
    
    p"\"Yeah.\""
    
    show J 2YSad_Flat with slowd
    
    "The word slithers off my tongue."
    
    "What should I say? No?"
    
    "Should I spill my problems to a girl I've spoken to a handful of times?"
    
    #She looks uneasy. Wounded.
    #I have no answer for her."
    
    "We're locked in an uneasy silence."
    
    "Mrs Brown enters and marches to her desk."
    
    j"\"...\""
    
    "Jennifer bites her bottom lip and returns to her chair."
    
    hide J cworried with slowd
    
    
    "She looked... worried."
    
    #"Is my mood so easy to read?"
    "Damn, she's been kind to me." 
    
    "And I brush her off for talking to me. Through no fault of her own, no less."
    
    "If she hadn't called me over on my first day, I wouldn't have had the confidence to approach anyone..."
    
    #"What if she stops talking to me?"
    
    #"I'll have to speak to her later."
    
    #"I knew I shouldn't have come in today..."
    
    stop music fadeout 3.0
    
    scene school02_day with slowf
    
    "I'm allowed to leave early for my appointment."
    
    scene school05_day with slowf
    
    "I should speak to Jennifer. She seemed concerned earlier." 
    
    #"I left for my room at dinner, I needed some time to think."
    "I left for my room at dinner, needing time to think."
    
    
    #"Her and Danielle seemed busy doing their own things at dinner so I left for my room."
    
    #"I needed some time to think."
    
    
    
    #mention feeling more confident after talking to Jennifer and Danielle.
    
    
    #stop music fadeout 3.0
    
    
    #mr adams' office
    play music "audio/music/bensound-straight.mp3" fadein 3.0
    #scene office09_day with slowf
    #show mra cnorm with slowd
    
    scene office10_day with slowf
    
    a"\"Welcome back, Peter.\""
    #I sit down
    "He says with the same exaggerated flourish. I take the seat."
    
    #p"\"Thanks.\""
    
    a"\"So, let's start where we left off: how's your stay at Sunnyvale?\""
    
    p"\"It's... going OK, I guess.\""
    
    #p"\"I've met a few people; I've improved my practicality; I've motivated myself to attend school.\""
    "I've met a few people; I've improved my practicality; I've motivated myself to attend school."
    
    "It's a start, {i}right?{/i}"
    
    "Putting everything into perspective lifts my mood."
    
    "It's just a dream, but the feelings it evokes..." 
    #"It's a dream, yet, the feelings it evokes... they're real"
    
    #"I can't let it control my life."
    
    "He observes my brooding. It's subtle, almost... non-intrusive."
    
    a"\"Can I ask the nature of your uncle's reference?\""
    
    p"\"I... I don't want to talk about it.\""
    
    #a"\"That's OK, you don't have to.\""
    
    a"\"You don't have to tell me what the problem is, but I could help you with the symptoms.\""
    
    "What, so you can figure out what's wrong with me? Like I'm some puzzle to be solved."
    
    
    "He takes my silence as a means to question."
    
    
    
    
    a"\"Are you eating well?\""
    
    p"\"I'm doing OK.\""
    
    "I fidget as I relay my answer."
    
    #"My fingers lace as I relay my answer."
    
    a"\"What about sleep?\""
    
    p"\"My pattern is a little messed up, but I haven't missed class.\""
    
    a"\"Elaborate on 'messed up.'\""
    
    #p"\"I... have been going to bed late.\""
    #p"\"I... often have late nights and—\""
    p"\"I... often have late—\""
    
    "I cut myself off."
    #"I'm quickto amend myself."
    #"I forget to mention for a while."
    
    #p"\"I also fell asleep early on tuesday and ended up pulling an all nighter to get my sleep back on track\""
    p"\"Let's just say I've had a few problems, but I'm adapting.\""
    
    a"\"Good. Be sure to get yourself into a routine.\""
    
    a"\"Your circadian rhythm regulates your mood.\""
    
    #a"\"Staying in routine is important for mental health.\""
    
    #"Explains why I'm fucked up."
    
    a"\"I have some questions regarding your general mental health.\""
    
    a"\"If you can just answer between one and five—one being not at all, five being consistently.\""
    
    "..."
    
    stop music fadeout 3.0
    #scene office09_day with slowf
    scene office10_day with slowf
    
    #show mra cnorm with slowd
    
    "We run through a tedious list of questions. I relay answers he wants to hear."
    
    a"\"Have you had any suicidal thoughts in the past week?\""
    
    "I reel back to his question."
    
    p"\"One.\""
    
    #"I'm being truthful."
    
    a"\"I wish I didn't have to ask, but it's a problem that's overlooked.\""
    
    "His voice growing solemn with every word."
    
    #"I can't say the thought hasn't crossed my mind before."
    
    "I can't say the thought has never crossed my mind."
    
    #"He smiles, I assume he's about to lighten the subject."
    
    "He takes a breath and moves on."
    
    
    a"\"Speaking of sleep earlier, any unsettling dreams in the past week?\""
    #a"\"Any unsettling dreams in the past week?\""
    
    "A cold flush descends over my face." #sweeps across my face #descends to my cheeks
    
    p"\"Two...\""
    
    "I avert my gaze. The scratching of his pen hastens."
    
    "{i}Why didn't I just say one?{/i}"
    
    a"\"Thank you for your answers.\""
    
    #"I avert my gaze."
    #"The scratching of his pen hastens"
    
    
    
    #a"\"Peter, is something wrong?\""
    
    #"His pen picks up the pace."
    #"I hear his pen pick up its pace."
    #"The rhythm of his pen's scratching hastens."
    
    #"Why'd he have to ask that... picking the scab of my fresh wound."
    #"He's seen right through me... I take a moment to master myself."
    
    
    #p"\"I'm fine.\""
    
    
    "I shrug."
    
    #"I reassure him by looking him in the eye."
    #"I look into his eyes, 
    
    #a"\"\""
    play music "audio/music/bensound-straight.mp3" fadein 6.0
    
    #p"\"My main problems are that I can't sleep or I don't want to wake up.\""
    p"\"My main problems are that I don't want to sleep and I don't want to wake up.\""
    
    "We share a chuckle." #knowing it's a lie."
    #"We both chuckle. The lightening air releases from my skin."
    
    a"\"Yeah, like the rest of us.\""
    
    "His response fuels my smile. I can't pinpoint why."
    
    p"\"Is that everything, can I go?\""
    
    #a"\"You may leave if you wish.\""
    
    a"\"You're free to leave.\""
    
    #"I rise to my feet, but his voice reaches out. I hesitate to shake his outstretched hand."
    
    #"As I rise to my feet and his hand reaches out. I hesitate to shake it."
    
    "His hand reaches out as I rise; I hesitate to shake it."
    
    a"\"Look, Peter... I'm here if you need anything, OK?\""
    
    "He places his other hand on the back of mine."
    
    a"\"Take your time... But I can't help if you don't tell me.\""
    
    #"Despite myself, His solemn gesture touches me."
    
    #"This time, I offer to shake his hand."
    
    p"\"Thanks...\""
    
    "He claps the back of my hand and releases me."
    
    a"\"Take care of yourself, Peter.\""
    
    p"\"Bye.\""
    
    a"\"I'll see you next week.\""
    
    #hide mra cnorm with slowd
    
    "I turn in a jumble of thoughts."
    
    "Is it that easy? Could I tell him my problems and they'll disappear?"
    
    #show mra cnorm with slowd
    
    "I glimpse to him one last time before leaving. He smiles and waves me off."
    
    
    
    stop music fadeout 3.0
    
    scene school4_day with fastf
    #corridor
    
    "No, of course it's not that easy."
    
    "He insists like I have a problem to confess." 
    
    "I can't deny I have several to myself—it just annoys me." #It just annoyed me."
    #Though, I can't deny I have several to myself. It just annoys me.
    "I'm not about to commit suicide."
    
    "And the fact he's paid to pry into my life..." 
    
    #"The thought leaves a slimy weight in my stomach."
    "The thought leaves a slimy weight swinging in my stomach."
    
    #"Just like my uncle, it's only a duty to care for me."
    "{i}It's only a duty to care for me...{/i}"
    
    scene room_boy16_day with slowf
    
    "I don't know what to think; my weekend started well and ended in disaster."
    
    "{i}That dream...{/i}"
    
    #"Everything was so real."
    
    "They say it's rare to have olfactory dreams, but the smells were so vivid."
    
    "And the angel's scream still echoes through the corridors of my mind."
    
    #"Why were the emotions so real?"
    
    "All I know is, I don't want to be alone anymore."
    
    "I want to find that feeling of the angel's embrace."
    
    #knocks
    play sound "audio/sfx/soft knock.mp3"
    
    "A few gentle raps pull me from my daze."
    
    "Who the—"
    
    #option?
    
    #music!
    
    "I open the door to find a fidgeting Sarah with her hands behind her back."
    
    play music "audio/music/Kevin_MacLeod_-_Dream_Culture.mp3" fadein 5.0
    
    #hallway
    scene hospital03_day with slowd
    show S 2DSad_Flat at PC1
    
    "I step out and close the door to shield my mess."
    
    p"\"Hey, Sarah…\""
    
    "She looks down to her shoes and twists her toe on the floor."
    
    s"\"H-hey…\""
    
    p"\"Is everything OK?\""
    
    #s"\"H-hey…\""
    show S 2YAnxious_Smile at PC1 with slowd
    
    "She meets my gaze with a sweet smile."
    
    s"\"I… I've finished.\""
    
    "She pulls her pad from behind her back. It takes me a moment to register."
    
    #"She hands me the pad and her smile echoes on my lips." #I echo her genuine smile."
    
    "I echo her smile and latch onto the pad."
    
    show S 2AAnxious_Sad with slowd
    
    "Her countenance unsure when it leaves her finger tips..."
    
    #"I stare into her picture."
    #"It's still two silhouettes surrounded by smoke. The detail is now perfected."
    #"When I look at it now it brings my parents to mind, evoking a set of curious emotions."
    "It now brings my parents to mind, evoking a sense of melancholy." #set of curious emotions
    
    "But the aesthetics are pleasing, every detail perfected. I've always had a thing for space." #, every detail perfected
    #Glaxies and nebulas swirl in the silhouettes.
    p"\"Wow. Really, this is good.\""
    
    show S 2YAnxious_Smile with slowd
    
    s"\"Thank you.\""
    
    
    
    p"\"Have you shown anybody else?\""
    
    show S 1AAnxious_Flat with slowd
    
    s"\"N-no...\""
    
    p"\"You should.\"" #I see. Well, 
    
    s"\"I...\"" 
    
    show S 1AAnxious_Smile with slowd
    
    s"\"...I'll think about it.\""
    
    hide S 1AAnxious_Smile with slowd
    
    #"She turns and makes her way to her door."
    
    "I return her pad and she rushes for her room."
    
    p"\"Wait, Sarah...\""
    
    show S 1YAnxious_Open at PM1 with slowd
    
    s"\"Hm?\""
    
    p"\"I'll see you around.\""
    
    show S 1DSad_Smile with slowd
    
    s"\"Bye.\""
    
    hide S 1DSad_Smile with slowd
    stop music fadeout 3.0
    
    "I watch her hide behind her door."
    
    "She... approached me."
    
    scene room_boy16_day with slowd
    
    #"She only showed me because I asked."
    
    #"If I didn't catch her with her pad at stupid o'clock, I wonder if it would've been left unseen by anybody but herself."
    "If I didn't catch her with her pad at stupid o'clock, would it've been left unseen by the world?"
    
    "It's a depressing prospect."
    
    nvl clear 
    
    t"That picture... the passion it portrayed. Though I don't understand her reasons, it moved me for my own." with slowd
    
    t"What do I want? I've been living a listless life since the accident."
    
    t"I've often wondered who I was back then. I often wonder if there's anything left of who I was."
    
    t"Besides memories, what makes a person who they are?"
    
    #t"Appearance? Thought patterns? Interests? {w}I don't know..."
    t"Appearance? Thought patterns? Interests? {w}{i}Memories...?{/i}"
    
    t"Everyone seems to have some kind of goal or a hobby. The more I think about it, the more alienated I feel."
    
    #window hide 
    nvl clear 
    
    "My uncle's right about one thing: I can't keep living—no, existing like this." with slowd
    
    t"I have a fresh start. I can be whoever I want to be.{w} Or remain {i}nobody...{/i}" with slowd #at all
    
    t"It's like I can't resist taking a jab at myself."
    
    t"I should be positive about this."
    
    t"This move has been a forced restart.{w} And not the first, I might add."
    
    t"But sometimes things happen that are out of our control."
    
    t"I guess it's how you react that ultimately decides the outcome."
    
    window hide 
    nvl clear 
    
    "I've been anything but positive up until this point, in either case." with slowd
    
    #"And my parents, they'd want me to find happiness."
    
    "I have to change."
    
    "But... where do I start?"
    
    
    scene school02_day with longf
    
    "I'm feeling positive today."
    
    "A good night's sleep can work wonders."
    
    "Jennifer enters. This time, I wave first."
    
    play music "audio/music/bensound-memories.mp3" fadein 5.0
    
    show J 1YHappy_Smile at PM1 with slowd
    
    "She approaches with a curious smile."
    #"Her expressions drops with curiosity."
    
    show J 2YHappy_Smile at PC1 with slowd
    
    j"\"Hey, Peter!\""
    
    "She searches my expression, clearly discouraged from yesterday."
    
    "I reassure her with a smile."
    
    p"\"Hey.\""
    
    #show J cnormal with slowd
    
    "I'm met by her grin."
    
    j"\"You really do look better today.\""
    
    p"\"Thanks, I do try.\""
    
    "She waves away my comment."
    
    j"\"Was somethin' wrong?\""
    
    p"\"No. I'm fine, really.\""
    
    j"\"I bet you're not sleeping well again.\""
    
    
    #j"\"You need to toughen up!\""
    
    show J 2YUpturned_Smile with slowd
    
    
    j"\"You need to toughen up!\""
    
    "She plants her fist on my shoulder."
    #"Her fist plants on my shoulder." #her fist on my shoulder."
    
    
    p"\"Ow.\""
    
    "I rub my arm, more out of shock than anything." #It just feels like a natural reaction." # to the minimal pain
    
    show J 2YUpturned_Pout with slowd
    
    j"\"That didn't hurt!\""
    
    #"I rub harder; a grin pulls on my lips."
    
    "I rub harder, grin pulling on my lips."
    
    #p"\"I might never be able to swim again after that.\""
    #p"\"I'm not sure I can ever swim again after such abuse.\""
    
    p"\"Not sure I'll ever be able to swim again.\""
    
    "I tilt my head back in dramatic fashion."
    
    #"I feel stupid at first but her giggle reassures me."
    
    show J 3YUpturned_Grin with slowd
    
    j"\"I'll give you something to to \"ow\" about!\""
    
    p"\"I'm joking!\""
    
    #j"\"You're such a drama queen!\""
    
    #"She giggles but her features drop into a solemn visage."
    
    show J 2YSad_Smile with slowd
    
    
    "Her features fall solemn."
    
    #solemn/pleading XD 
    
    j"\"But about swimming... would you come again?\""
    
    "She's actually asking me; she looks serious too..." #I feel put on the spot..."
    
    #"Should I?"
    menu: 
        
        "Play it off":
            jump Jen1y
            
        "Pass":
            jump Jen1n
        
    label Jen1y:
        
        "I keel over my desk in feigned agony and snicker through my teeth." #grit my teeth to hide my smile."
        
        p"\"I really don't think I can.\""
        
        show J 3YUpturned_Grin with slowd
        
        "She waves her fist by my face."
        
        #j"\"I'll give you something to cry about if you don't!\""
        j"\"If you don't stop being a drama queen, I'll make sure you never swim again!\""
        
        "I reel back into my seat with my hands up."
        
        p"\"OK, OK! I'll come.\""
        
        show J 1CHappy_Smile with slowd
        
        #"Her smile beams, echoeing on my lips."
        "Her beaming smile reflects on my lips."
        
        j"\"I'll catch you at the end of class and we'll go together!\""
        
        p"\"Sure thing.\""
        
        #j"\"See you then~!\""
        
        hide J 1CHappy_Smile with slowd
        
        "She turns with a flourish and heads for her seat."
        
        "{i}What have I gotten myself into?{/i}" 
        
        "I'm not sure, but my smile doesn't falter." #but this smile isn't faltering.
        
        #stop music fadeout 2.0
        scene school02_day with slowf
        show J 2CHappy_Smile at PC1 with slowd
        
        "Jennifer arrives at my desk in sync with the bell."
        
        j"\"Let's go!\""
        
        p"\"I didn't bring my shorts.\""
        
        show J 2YHappy_Smile with slowd
        
        j"\"Go and get them. Hurry!\""
        
        #scene black with slowd
        #Peter's room
        scene room_boy16_day with slowd
        
        
        "I rush back to my room and grab my bag."
        
        scene school12_day with slowd
        
        #show J mnormals with slowd
        
        "Jennifer's waiting for me in her swimsuit."
        
        "She shoots a glance at my bag."
        
        j"\"You're looking a little light.\""
        
        p"\"Huh?\""
        
        "I open my bag and give her a view."
        
        
        j"\"Looks like you forgot something.\""
        
        
        "I rummage through my bag non the wiser."
        
        j"\"What gets wet as it dries?\""
        
        p"\"...\""
        
        j"\"...\""
        
        p"\"No idea.\""
        
        
        j"\"A towel, silly!\""
        
        #show J mtongues with slowd
        
        "She thrusts her tongue at me."
        
        #show J mnormals with slowd
        
        #my palm connects with my forehead. 
        
        "{i}Damn.{/i} I used it to have a shower."
        
        #"How on Earth did I forget a towel?"
        
        p"\"Ah... I'll go and get one.\""
        
        j"\"You can use mine after me.\""
        
        p"\"Are you sure?\""
        
        show J mGGCs with slowd
        
        #"She points to the changing rooms."
        
        j"\"The lesson's started. Go get changed!\""
        
        
        
        #j"\"The lesson's started.\""
        
        #"She points to the changing rooms."
        
        #j"\"Go get changed!\""
        
        #"She points to the changing rooms."
        
        "That's right... she had a lesson this time last week."
        
        #stop music fadeout 3.5
        
        
        scene school15_day with slowf
        
        show J mnormals with slowd
        
        "We're greeted by a lesson in progress."
        
        #"Couples are performing moves in the pool and the others huddle around the instructor."
        
        #"Couples are scattered across the pool performing out of synch choreography."
        
        "Male-female duos are scattered across the pool, performing out of sync choreography."
        
        "The few on the sidelines are huddled around the instructor."
        
        #choreography
        
        "A girl approaches, sharing a wave with Jennifer."
        
        show J mnormals at left with move 
        
        show c mswim at right with slowd
        
        "She pulls up and examines me."
        
        q"\"This the new blood?\""
        
        "Jennifer shoots her a furrowed glance."
        
        "My stomach drops. It all adds up." #Of course there's an ulterior motive."
        
        "It's not that I hadn't considered an ulterior motive; I just didn't want there to be."
        
        "But... why else would she talk to me?"
        
        cc"\"It's nice to meet you. I'm Casey.\""
        
        p"\"Peter.\""
        
        "They share a lifted brow at my deflated introduction."
        
        j"\"Don't worry! You'll be working with me.\"" 
        
        j"\"We might have to do extra practise, but you don't have much to learn.\""
        
        p"\"I never agreed to water dance.\""
        
        j"\"It's not water dancing; it's synchronised swimming!\""
        
        p"\"I didn't agree to that either.\""
        
        j"\"Aw.\""
        
        "Her bottom lip drops into a pout."
        
        j"\"C'mon, it'll just be one move!\""
        
        p"\"I... I'll think about it. OK?\""
        
        j"\"Yay! Come on, you can at least try it today.\""
        
        #"What choice do I have?"
        "{i}Not like I have much choice...{/i}"
        
        #"Not exactly, you've just got a few things to learn. We'll be doing the dancing."
        
        #Have Casey ask about the scars in front of Jennifer? 
        #Jennifer is uneasy around negative emotions. She tries to push them away. 
        
        show J mnormals at left with move 
        
        hide c cswim at right with slowd
        
        #teacher
        
        "We approach the rest of the team and the teacher sets his sights on me."
        
        q"\"It's nice to see a new face. Are you joining the team?\""
        
        #"I can feel Jennifer's stare boring into my cheek." #She's as invested in my answer as he is." 
        
        "Jennifer's stare bores into my cheek."
        
        p"\"No, I'm just trying it out.\""
        
        mp"\"I see. I'm Mr Palmer, welcome.\""
        
        "He looks to Jennifer."
        
        #You're late
        
        #I was waiting for Peter!
        
        #She slams her palm on my shoulder and digs her fingers in.
        
        #"He marches in front of the team and I fall in line with them."
        
        mp"\"As you can see, we're working on our duet segment again today.\"" 
        
        mp"\"Once each duo has it mastered, we'll start synchronising as a whole.\""
        
        show J mnormals at center with move 
        
        "The whole thing makes me nervous. I can barely swim, let alone dance."
        #novice swimmer
        "I'm ready to bail at any excuse, but my mind fails me."
        
        
        j"\"Don't look so worried.\""
        
        #"She gives a playful shove."
        
        "She shoves me with her shoulder."
        
        j"\"You won't have much to learn. You'll be helping me perform a few moves.\""
        
        hide J mnormals at centre with slowd
        
        "We slide into the pool."
        
        
        p"\"At least the pool isn't as cold today.\""
        
        "She turns away and presses her back against me. Her warmth tingles on my skin." #body against mine - tingling
        
        j"\"They turn on the heating for our lessons.\""
        
        #Due to the school's funding they have cleaners to clean it everyday and cameras to watch over it.
        #cameras watch over the school and the uncle could gain access to them? 
        #it's a nice juxtaposition in the cool pool.
        
        "Her fingers wrap aroud my wrists and guide my hands to her body." #pull my hands into position."
        
        j"\"You just need to hold me up.\""
        
        "I lift her by her thigh and her abdomen. They tense in my palms." #They're taut in my palms."
        
        "Her weight tenfolds as her body submerges from the water."
        
        "She keeps wriggling, trying to get into the right position."
        
        p"\"Hurry up.\""
        
        "I manage the words through the strain."
        
        j"\"Hold it.\""
        
        "My arms begin to shake under the weight. It's embarrassing." 
        
        j"\"Release.\""
        
        "I lower her back into the water in relief."
        
        show J snormals with slowd
        
        j"\"See, that wasn't so bad.\""
        
        p"\"I... guess not. But I can't hold you long out of the water.\""
        
        "Her brow lifts."
        
        j"\"Why not?\""
        
        p"\"You're heavy.\""
        
        "This earns me a swat on the shoulder."
        
        j"\"You cheeky sod!\""
        
        "I'm quick to amend my faux pas."
        
        p"\"I didn't say you were fat. Muscle has more weight.\""
        
        show J sfists with slowd
        
        "She waves her fist at me but her lips pull in the corners."
        
        j"\"Good. You better not be!\""
        
        
        "We rinse and repeat for the remainder of the lesson..."
        
        stop music fadeout 3.0
        
        scene school12_day with slowf
        
        "Everyone heads in to get changed and I'm left waiting for Jennifer."
        
        "She emerges with her towel held out; I take it and head in."
        
        #description: "We're greeted by a lesson in progress. 
        scene school12_day 
        
        show J 2YHappy_Smile at PCM1
        
        with slowf
        
        "The scents of coconut and chlorine mix in my nostrils. I catch a last whiff as I hand her towel back."
        
        #coconut fragrance
        
        p"\"Thanks.\"" 
        
        j"\"So, Peter, you should come out with us!\""
        
        p"\"Erm... I...\""
        
        "She shakes my shoulders."
        
        j"\"C'mon! You always look so down. Loosen up!\""
        
        show J 2YSad_Pout at PCM1 with slowd
        
        "She shoots a pout at me."
        
        #Jennifer arc choice
    menu: 
        
        "Cave in":
            jump Jen2y
            
        "Resist":
            jump Jen2n
        
        #(yes/no)
        
    label Jen2y:
        
        p"\"OK...\""
        
        
        
        j"\"You'll come out this weekend? Promise me.\""
        
        p"\"I said OK.\""
        
        "Geez, what do I have to do?"
        
        j"\"Pinky promise.\""
        
        p"\"What?\""
        
        j"\"We join pinkies and make the promise official.\""
        
        #"It's as if she answered my mind."
        
        
        p"\"O-OK...\""
        
        #"She holds her finger out and I wrap mine around hers."
        
        show J 2YUpturned_Grin at PCC1 with slowd
        
        "She latches onto my pinky and pulls me close."
        
        #"She grips on and pulls me closer."
        
        #p"\"...\""
        
        j"\"They used to chop off your pinky if you broke a pinky promise.\""
        
        show J 2YHappy_Smile at PC1 with slowd
        
        "She steps back simpering."
        
        j"\"So don't let me down~!\""
        
        hide J mnormalc with moveoutleft
        #hide sprite left
        
        "She turns and runs off, leaving me questioning whether there's a wolf behind her sheeplike innocence."
        
        
        
        scene black with longf
        centered "Jennifer Act 1"
        
        
        #next day
        #bedroom
        
        scene room_boy16_day with longf
        
        "My alarm tears me from sleep. But consciousness feels light today."
        
        #"I get ready with a smile. Jennifer
        
        "As I get ready, something strikes me: Jennifer wants me to hang out." 
        
        "{i}Beyond swimming.{/i}"
        
        #"I'm... looking forward to class."
        #"For the first time, I'm eager to get to class."
        #"For the first time, I'm looking forward to class."
        
        #corridor
        scene school05_day  with slowf
        
        
        "I'm fifteen minutes early. {i}A new record.{/i}"
        
        
        #"I make sure I'm early, in hopes of seeing Jennifer before the bell."
        
        j"\"Peter!\""
        
        #"Her greeting a melody in my ears; I crack a smile."
        
        #"Hearing her call my name draws a smile."
        "Her greeting draws a smile."
        
        #show J mflatc with slowd
        show J 2YSad_Pout at PCM1 with slowd
        
        #sprite
        
        "But when I turn to face her, I'm met by a pout."
        
        
        p"\"Hey, what's up?\""
        
        "{i}The table's turned.{/i}"
        
        j"\"You never added me on FaceAP!\""
        
        p"\"Ah... you're right.\""
        
        "We both whip our phones out and search for one another."
        
        p"\"There, added.\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She giggles as she accepts my request."
        
        j"\"Now you can't escape me!\""
        
        "So it's official? We're... {i}friends.{/i}" 
        
        "I flash her a grin."
        
        p"\"Maybe you should be the one concerned about escaping me.\"" #escaping from 
        #Little did I know how right I was 
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Ah, Peter. You have much to learn.\""
        
        "She pats my shoulder and heads into class grinning."
        
        hide J 2YUpturned_Grin with moveoutright
        
        "My words were hollow, but she seems to have taken it as a challenge or something."
        
        
        #classroom
        
        scene school02_day with slowf
        play sound "audio/sfx/short vibrate.mp3"
        
        #"The lesson is in full flow. I'm distracted by a vibration in my pocket."
        
        "I'm distracted by a vibration as the lesson picks up."
        
        "FaceAP wriggles with a notification. I glance to Mrs Brown before opening."
        
        t"Jenjen: How old r u? u havnt updated ur profile."
        
        "Seriously? She's looking me up in class?"
        
        "I hesitate to answer..." #But I'm not about to lie about it."
        
        t"Peter: 19."
        
        window hide 
        nvl clear
        
        ###### Do I need 19 here? Will his birthday be before or after he goes to the school? 
        
        "...Being a year older will only raise questions."
        
        #"I can see shoot a glance in my peripheral, but I pin my eyes to the front."
        
        #"She keeps shooting glances at me, but I pin my eyes to the front."
        
        "I fix my eyes on the front, distracted by Jennifer shooting glances in my peripheral."
        
        play sound "audio/sfx/short vibrate.mp3"
        
        #"A while passes before I'm distracted by another vibration." #We begin messaging when the chance presents itself."
        
        "It's not long before another vibration." #We begin messaging when the chance presents itself."
        
        t"Jenjen: So ur definitely comin out this weekend?"
        
        #How many times do I have to say? 
        
        t"Peter: I pinky promised, didn't I?"
        
        t"Jenjen: U did, remember wat will happen if u don't. ;)"
        
        #t"Peter: Does that mean I get to chop yours off if I do?"
        
        #Mrs Brown 
        
        t"Jenjen: dont tell n e 1, ok?"
        
        #t"Peter: OK..."
        
        window hide 
        nvl clear 
        
        #I decide ot to answer for my own safety, but it's not like I have anyone else to tell.
        
        "Not like I have anyone else to tell."
        
        "Still, why wouldn't she want me to tell anyone?"
        
        
        #scene bedroom
        scene room_boy16_day with longf
        #fade to weekend? :p 
        
        
        # "The weekend comes too soon."# My excitement has been waning into nervousness as our outing approaches."
        
        #"I'm stuck in purgatory. Between not knowing where we're going or when and my gnawing thoughts." #telling?
        #waiting 
        
        "A ball of unease has been expanding in my stomach all morning."
        
        #I'm stuck in purgatory. My mind too restless to keep myself busy and I'm left to wait." 
        
        #"Between not knowing what time we're going or where and my gnawing thoughts."
        #"I don't know what time we're going out or where."
        
        #"My thoughts gnaw at me."
        
        "Is there an ulterior motive here too?"
        
        "Why would a girl like her want to be friends with someone like me?"
        #What does she see in me? 
        #"I feed my insecurities until I'm paralysed by my self-disdaining venom." # Not yet, good sir. Not yet.
        
        "{i}Why would anyone?{/i}"
        
        "I checking my phone from time to time for a message or call to save me from myself."
        
        "I don't even know what time or where."
        
        "..."
        
        #vibrate
        play sound "audio/sfx/short vibrate.mp3"
        
        "{i}Finally...{/i}"
        
        t"Jenjen: we r heading into town, wanna join us?"
        
        t"Peter: OK."
        
        "Why's she acting like I didn't promise?" 
        
        "{i}This girl is something else.{/i}"
        
        t"Jenjen: meet at front gate!"
        
        window hide 
        nvl clear 
        
        #Her eyes glued to her phone. 
        
        scene school_out003_day 
        
        show J 2YSad_Pout at PM1
        
        with slowf
        
        "I arrive to find Jennifer glued to her phone."
        
        show J 2YHappy_Smile at PC1 with slowd
        
        "She notices my approach and lowers it."
        
        j"\"Hey!\""

        
        #p"\"Hey.\""
        
        #"She stares back into the screen."
        
        p"\"So, where're we going?\"" 
        
        j"\"We're gonna go get something to eat.\""
        #bensound - sexy scene XD
        #See, I told you he was funny.
        
        "She looks into her screen and sighs."
        
        j"\"We're just waiting for their slow arses.\""
        
        #"She giggles."
        #"Her head 
        #"She looks side-to-side and 
        "She peers into the grounds."
        
        
        j"\"Don't tell them I said that.\""
        
        p"\"Tell who?\""
        
        show J 2YHappy_Smile at PCR1 with move
        show De 2YRelax_Smirk at PML1 with slowd
        
        #"She looks up and I follow her gaze into the grounds. A familiar figure approaches."
        "I follow her gaze to a familiiar figure."
        
        
        #Just 
        #cream
        play music "audio/music/bensound-funkyelement.mp3" fadein 6.0
        
        show De 2YRelax_Smirk at PCL1 with slowd
        
        "It's the guy playing football outside the dorms. Dean, I think his name was."
        
        D"\"Hey, it's you!\""
        
        "Apparently, he's forgotten mine." #Don't worry, I've forgotten before. 
        
        j"\"You've met Peter?\""
        
        D"\"Yeah, he played a game of football with us.\""
        
        "An elbow connects with my ribs."
        
        j"\"I didn't realise you were so active.\""
        
        p"\"I—\""
        
        #show d cnorm with slowd
        show De 2YDisappointed_Frown with slowd
        
        
        D"\"Don't tell me he's the one swimming with you?\""
        
        j"\"Yeah!\""
        
        "She points her tongue at him and he rolls his eyes."
        
        
        D"\"So you're the poor soul.\"" 
        
        "I almost respond with a yes but catch my tongue."
        
        show J 3YUpturned_AngryPout at PC1 with medd
        show J 2YHappy_Smile at PCR1 with move
        
        j"\"Arsehole!\""
        
        "A flying fist connects with his shoulder."
        
        D"\"Did I just feel something?\""
        
        "He looks side to side in confusion."
        
        #
        "Her high-pitched growl extracts a laugh from me."
        
        show J 3YUpturned_AngryPout with slowd
        
        j"\"What're you laughin' at?\""
        
        "She turns to me brandishing her fist."
        
        stop music fadeout 3.0
        
        #show d cnorm at Position (xpos = 0.5, xanchor=0.9, ypos=1.0, yanchor=1.0) with move 
        
        #show J cnormalc at Position (xpos = 0.5, xanchor=0.5, ypos=1.3, yanchor=1.3) with move 
        
        #show c cnorma at Position (xpos = 0.5, xanchor=0.1, ypos=1.3, yanchor=1.3) with slowd 
        

        show De 2YDisappointed_Frown at PCL2 #with slowd
        show C YGentle_Sad at PC1 #with slowd
        show J 2YHappy_Smile at PCR2 #with move
        #with slowd
        with move
        
        
        #or casey says you two? :p making it awkward. :p 
        cc"\"You two.\""
        
        "Casey pulls up between them interjecting."
        
        #"Casey pulls up beside us." # and we greet her
        #"Our attention's pulled to the familiar voice."
        
        "There's a prolonged moment of silence."
        
        j"\"Let's go!\""
        
        #show casey
        
        
        #A familiar voice cuts in.
        
        #Hey, Casey."
        
        
        #Casey appears now! :p Maybe jealous from Dean and Jennifer's interaction. 
        
        ##in town
        
        play environment "audio/background/city2.mp3"
        
        scene street001_day with slowf
        
        show De 2YRelax_Smirk at PCL2 #with slowd
        show C YGentle_Smile at PC1 #with slowd
        show J 2YSad_Flat at PCR2 #with move
        with slowd
        
        "My mind wonders as Dean and Casey talk about random topics."
        
        "Something strikes me as off about the scene: Jennifer."
        
        "She's not at the forefront of the conversation. She's staring at her phone again, face expressionless."
        
        #"I draw my phone and key in a message, \"Everything OK? This must be a record amount of time that I haven't heard your voice.\""
        #"I draw my phone and key in a message, \"Everything OK? This must be record time that I haven't heard your voice.\""
        
        "I draw my phone and key in a message, \"This must be a record; I think the world might implode if you don't speak soon.\""
        
        #I think the world might implode if you don't speak soon.
        
        #vibrate sound or ding sound
        
        #show J cnormalc at Position (xpos = 0.5, xanchor=0.1, ypos=1.3, yanchor=1.3) with slowd
        
        show J 2YHappy_Smile at PCR2 with slowd
        
        "She smiles when our gazes meet."
        
        play sound "audio/sfx/short vibrate.mp3"
        
        "\"Did u miss my voice already? ;)\""
        
        "{i}Should've expected as much.{/i}"
        
        "\"Geez, you can text as fast as you can talk. God save me.\""
        
        "I'm pleased with myself for extracting another smile." 
        
        #"But as I'm beginning to wonder whether she was down about something..." #my phone vibrates."
        
        "But was something wrong? She's been—"
        
        play sound "audio/sfx/short vibrate.mp3"
        
        "\"arsehole! follow my lead.\""
        
        "This gives me a bad feeling."
        
        #show J cupturnedc at Position (xpos = 0.5, xanchor=0.1, ypos=1.3, yanchor=1.3) with slowd
        
        show J 2YUpturned_Grin at PCR2 with slowd
        
        j"\"Peter! You forgot to sign up for the team!\"" 
        
        #show c cnorma at Position (xpos = 0.5, xanchor=0.5, ypos=1.3, yanchor=1.3) with slowd
        
        "Jennifer exclaims, Casey turns with a curious expression."
        
        
        p"\"I didn't ag—\""
        
        #show J cnormalc at Position (xpos = 0.5, xanchor=0.1, ypos=1.3, yanchor=1.3) with slowd
        
        "She tugs my sleeve and starts dragging me."
        #"She's already pulling me away by my sleeve." 
        
        j"\"If you apply by three pm, then you'll be able to practice again on Tuesday!\"" #participate
        
        "She assures to shout, perpetuating my gut feeling."
        
        j"\"Later, guys!\""
        
        #show d cnorm at Position (xpos = 0.5, xanchor=0.9, ypos=1.0, yanchor=1.0) with slowd
        
        #show c cnorm at Position (xpos = 0.5, xanchor=0.5, ypos=1.3, yanchor=1.3) with slowd
        
        show De 2YDisappointed_Frown at PCL2 #with slowd
        show C YGentle_Sad at PC1 #with slowd
        with slowd
        
        "They both gawp as I'm dragged away; I can only offer a queasy smile..."
        
        #scene change
        
        stop environment fadeout 3.0
        
        scene street002_day with slowf
        
        #"She pulls me around a secluded corner and peeks around the wall."
        
        "When we're out of view she lets go and peeks around the corner."
        
        p"\"What's this about?\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        #"She turns in trumph. Smile pulling on her lips."
        #"Her pulling lips let me know she was waiting for my question."
        #"She meets my gaze with upturned eyes."
        
        j"\"All part of my ploy. Casey likes Dean, but she won't admit it.\""
        
        p"\"You're playing Cupid?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        #show J cnormalc with slowd
        
        j"\"Pretty much.\""
        
        p"\"But a ploy means it benefits you.\""
        #what if I don't join?
        
        j"\"Oh.\""
        
        #"She rests her hand on my shoulder, smile pulling on her lips."
        #"She rests her hand on my shoulder, lips pulling into a grin."
        #, lips curving into a smile
        
        play music "audio/music/bensound-memories.mp3" fadein 3.0
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        "Her hand comes to rest on my shoulder, lips pulling into a grin."
        
        j"\"It does.\""
        
        #drags
        "Her proud pose pulls a grimace from me."
        
        "Should've trusted my intuition."
                                    
        p"\"What if I don't join?\""
        
        #"Her cute voice activates."
        
        show J 2YSad_Pout at PCM1 with slowd
        
        j"\"Then you'd make a girl very sad.\""
        
        #what was that music?
        
        #play music "audio/music/bensound-extremeaction.mp3" fadein 5.0
        
        "Houston, we have a problem."
        
        "Her cute voice is activated and pout deployed."
        
        p"\"No.\""
        
        "I deflect her attack with an averted gaze but she circles around."
        
        j"\"Are you ignoring mwe?\""
        
        "I turn my body away."
        
        show J 2YSad_Pout at PCC1 with slowd
        
        "She grabs onto my arm and yanks me close, nullifying my defencive manoeuvre."
        
        j"\"Pwease?\""
        
        
        "I can't escape her coy pout or the feeling of her body pressing against mine."
        
        "She unravels me like a sweet."
        #My persistence falters. 
        #stop music fadeout 3.0 
        
        p"\"I'm only helping you perform moves, though. I'm not dancing.\""
        
        show J 2YHappy_Grin at PCM1 with slowd
        
        j"\"Yay! That's good enough for me.\""
        
        "I can't help smile."
        
        #"She never fails to draw a smile from me."
        
        p"\"I am hungry, though. Weren't we supposed to get something to eat?\""
        
        j"\"We don't have time. Come on!\""
        
        p"\"That's the whole reason we came.\""
        
        show J 2YHappy_Flat at PCM1 with slowd
        
        j"\"Yeah...\""
        
        "Her eyes swim with a passing thought."
        
        j"\"I'll make you one of my famous wraps some time to make up for it.\""
        
        p"\"They did smell good...\""
        
        show J 3YHappy_OpenSmile at PCM1 with slowd
        
        j"\"They are. Let's go!\""
        
        "She tugs my sleeve and I follow." 
        
        "{i}Would it have mattered if I'd said no?{/i}"
        
        stop environment fadeout 3.0
        
        stop music fadeout 3.0                                                                      
        
        #scene to school office? Or just go to room? 
        
        
        #I signed up in the office and then Jennifer checks her phone and says she has to go.
        
        #This will go back to Peter in his room where he thinks about Jennifer. 
        
        #Then he'll get the text asking him to come out.       
        
        #back to room
        scene room_boy16_day with longf
        
        "I signed up and Jennifer said she had to go. I can't help but think it's to do with her phone."
        
        "Who was she messaging? Or whose message was she waiting for?"
        
        "I wonder why I'm curious."
        
        "Beats me. But it beats where my mind would stray."
        
        "I smirk as today's events reel through my mind..." 
        
        "The stealth text conversation; her scheming to get Casey and Dean together; her domineering perseverance convincing me to join the club."
        
        "I want to find reasons beyond her wanting me to swim with her."
        
        "But I can't seem to allow myself..."
        
        #"I can't find reasons beyond her wanting me to swim with her."
        
        #"But it's stupid to think with the effort she puts into speaking to me everyday."
        
        #"She's concerned when she knows I'm down..."
        
        #"...I'm just glad she wants me to."
        
        #...What do I have to do to convince myself? Or am I complacent paralysed by my self-disdaining venom.
        
        #vibration
        
        play sound "audio/sfx/short vibrate.mp3"
        
        "{i}Speak of the devil.{/i}"
        
        t"Jenjen: meet us at 7 at the front gate and bring ur id!"with slowd
        
        t"Peter: What do you mean? We've already been out."
        
        
        t"Jenjen: i asked and u came. tht wasnt the pinky promise."
        
        #"Damn this girl. How didn't I see that coming?"
        
        #t"Peter: Where are we going?"
        
        t"Peter: That's not fair!"
        
        t"Jenjen: Wear something nice! ;)"
        
        window hide 
        nvl clear 
        
        #"She's seen my message but she's not responding..."
        
        #t"Peter: You used deceiving means."
        
        "Damn this girl. How didn't I see this coming?" with slowd
        
        #"Though technically, I did go out earlier and that's a legitimate argument. But I want to see her again."
        
        "I resign to having a shower and getting myself ready for tonight..."
        
        scene room_boy16_evening with slowf
        
        "I feel fresh; it's the first time I've worn these jeans." 
        
        #"Tracksuit bottoms are much comfier to lounge around in."
        
        "I hope I'm dressed smart enough. I don't know what the standards are." 
        
        "Or where we're going for that matter."
        
        
        #"I'm nervous again but with a tint of excitement."
        #"Nervousness and excitement wage an internal war."
        "Nervousness and excitement wage war in my stomach."
        
        #"Are we going to a restaurant or something?"
        
        "Thinking back on it, I had technically already been out. But… I can't deny I'm looking forward to seeing her again."
        
        #"Seven o'clock creeps. I head out early."
        
        "I end up leaving a few minutes late..."
        
        #Jennifer told them to meet us at 7:30? XD 
        
        scene school_out003_evening with slowf
        
        #can't make dress sprite...
        
        #show J mnormalc 
        
        "Jennifer's waiting alone. Weren't Dean and Casey supposed to be here?"
        #show sprite
        
        show J 1YHappy_OpenSmile at PM1 
        show JX Bag at PM1
        with slowd
        
        j"\"Peter!\""
        
        #"Her feminine feautures accentuated by her dress." 
        
        #"Wow."
        
        show J 2YHappy_Smile at PC1
        show JX Bag at PC1 
        with slowd
        
        j"\"You look nice.\""
        
        
        #"I take a moment to realise how pretty she is. Her tanned skin, her grin, those..."
        
        p"\"Thanks...\""
        
        #"My stomach flutters at the spark in those emerald eyes."
        
        
        
        
        
        #"I can't bring myself to say beautiful."
        
        #j"\"Thanks! You don't look bad yourself.\""
        
        #"Her fingers stroke my chin."
        
        show J 2YHappy_Grin at PCM1 
        show JX Bag at PCM1 
        with slowd
        
        "She strokes my chin."
        
        j"\"But you could've shaved your peach hairs.\""
        
        p"\"I… I could go and shave.\""
        
        j"\"It's fine. You suit it.\""
        
        "She flashes a wink and giggles."
        
        p"\"Thanks...\""
        
        p"\"You look nice, too.\""
        
        "She brushes off my comment."
        
        #"Heat surges into my cheeks."
        
        #"My lips tug into a smile." 
        
        #"She trips over herself."
        
        j"\"We're waiting for Casey and Dean again. I'll ring them.\""
        
        hide J 2YHappy_Grin at PCM1 
        hide JX Bag at PCM1 
        with slowd
        
        "She dials and turns away."
        
        j"\"Where are you guys?\""
        
        j"\"Hurry up!\""
        
        j"\"Alright, we'll meet you there then.\""
        
        show J 2YHappy_Smile at PC1 
        show JX Bag at PC1 
        with slowd
        
        "She slides her phone into her bag and turns back to me."
        
        j"\"We'd better get there early!\""
        
        p"\"Where are we going?\""
        
        show J 2YUpturned_Grin at PCM1 
        show JX Bag at PCM1 
        with slowd
        
        "She whispers in my ear."
        
        j"\"You'll see.\""
        
        "She claps her hands and sets off."
        
        
        play environment "audio/background/city2.mp3" fadein 4.0
        scene street001_evening with slowf
        
        t"The city glows with a vibrant tint. The sun departs, leaving maroon in its wake." with slowd
        
        t"A mixture of pleasant fragrances ride on the breeze, foods from the restaurants and perfumes of passing people."
        
        t"The streets sing with the buzz of chatter and laughter as groups of people pull off into the bars and restaurants."
        
        t"Then it hits me... we're dressed like these people."
        
        t"Wait, are we—"
        
        window hide 
        nvl clear 
        
        show J 3YAnnoyed_Pout at PCM1 
        show JX Bag at PCM1 
        with slowd
        
        j"\"Peter!\"" 
        
        "An impatient Jennifer snaps me back into reality."
        
        p"\"Huh?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Did you bring your ID?\""
        
        p"\"Oh, yeah...\""
        
        "As I retrieve it from my pocket she snatches it from my fingers."
        
        j"\"Lemme see!\""
        
        #"She snatches it from my fingers by the time I've taken it from my pocket."
        
        hide J 2YHappy_Smile with slowd
        
        "I reach out to grab it but she turns, and opens it to my picture."
        
        j"\"No way is that you!\""
        
        "I sigh in defeat."
        
        p"\"Yeah.\""
        
        j"\"Look how long your hair was!\""
        
        j"\"You look like a different person...\""
        
        "{i}I was...{/i}"
        
        p"\"...Yeah.\""
        
        show J 2DMellow_Flat at PC1 
        show JX Bag at PC1 
        with slowd
        
        "She peers closer into my passport and turns to me in confusion."
        
        j"\“I thought nineteen was a typo in class…\""
        
        "I have to change the subject and I have to know."
        
        p"\"Did you ask my age because we're going to a bar?\""
        
        show J 2YUpturned_Grin at PC1 
        show JX Bag at PCM1 
        with slowd
        
        "She grins as we stop outside a restaurant."
        
        
        j"\“Don’t be silly. How easy do you think I am?\""
        
        "Easy enough to get to a restaurant, apparently."
        
        "{i}Or am I that easy...?{/i}"
        
        "I shrug off trivialities and follow."
        
        stop environment fadeout 1.2
        
        play music "audio/music/bensound-romantic.mp3" fadein 3.0 
        
        #play music "audio/music/Melancholy.mp3" fadein 3.0 
        
        scene restaurant04_day with slowf
        
        
        "The buzz from outside follows, but music drowns the din of chatter." 
        
        "The rich aromas of tomato, cheese, and herbs hit like a wall."
        
        #"She parks her bag at a table of two and takes her coat off."
        
        "She parks her bag at a table of two and sits down."
        
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\“Uh, weren't we supposed to save seats for them?\""
        
        #j"\"They're not coming.\""
        
        #p"\"What?\""
        
        j"\"They're going to a different restaurant.\""
        
        p"\"Why?\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"I’ve already been through this!\""
        
        p"\"Dean and Casey?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Yeah!\""
        
        p"\"So you set up events and—\""
        
        #"A waiter approaches, wielding menus."
        
        "A waiter approaches and places our menus."
        
        w"\"Good evening.\""
        
        "An Italian twang lilts his accent."
        
        w"\"Welcome to Isabella Italia.\""
        
        "We give thanks."
        
        #"He places them down with immaculate symmetry."
        
        w"\“I’ll be back soon to take your orders. Don’t hesitate to hail a waiter in the meantime.\""
        
        "He glides off back into the field of tables."
        
        
        
        
        
        j"\"What ya gettin’?\""
        
        "I open the menu and find myself drowning in choice."
        
        
        
        
        
        p"\“I don’t know...\""
        
        "Everything's so expensive... not like I have much else to spend the money on."
        
        
        
        j"\"Isabella's amazing. The lasagna here is divine.\""
        
        p"\"Sounds good.\""
        
        "Jennifer signals a waiter." 
        
        w"\“Can I take your order?\""
        
        p"\“I’ll have a lasagna, please.\”"
        
        w"\"And you, signorina?\""
        
        "A grin slides up her cheek."
        
        j"\“I’ll take the carbonara.\""
        
        w"\"Certainly.\""
        
        "He writes our orders and bows."
        
        w"\"Grazie.\""
        
        "He gathers our menus and retreats."
        
        p"\“I thought lasagna was the best.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\“I can always have some of yours.\""
        
        play environment "audio/sfx/ring vibrate.mp3" fadein 0.6
        
        
        "As she flashes a wink, her phone vibrates."
        
        #"Jennifer's phone buzzes and she brings it to her ear."
        
        hide J 2YUpturned_Grin with slowd
        
        stop environment fadeout 1.2
        
        j"\"Hey!\""
        
        j"\"We're at Isabella's.\""
        
        j"\"But Peter wanted lasagna!\""
        
        p"\"Why are you telling her I—\""
        
        "She presses her finger to her lips and narrows her brow."
        
        j"\"This place is packed and we've already ordered.\""
        
        "I look around to find no table free."
        
        j"\“Isabella always works Saturday, so it’s busy.\""
        
        j"\“You guys took too long!\""
        
        j"\“We weren’t {i}{b}that{/b}{/i} early.\""
        
        j"\“I’ll see you tomorrow. Bye~!\""
        
        "I patiently await the end of the call."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\"You didn't have to throw me under the bus; I barely know them.\""
        
        j"\"It's fine! They won't hold a grudge against you.\""
        
        scene restaurant04_day with slowf
        
        "A waiter places our dishes; the smell makes my mouth water."
        
        w"\"Enjoy.\""
        
        "As I'm cutting some lasagna into manageable slices, she reaches over and forks a piece."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\“I didn't think you were serious!\""
        
        p"\“I want some of yours.\""
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        "I reach over and she deflects me with her fork. "
        
        j"\"Mine!\""
        
        #as-Salt-ted and peppered.
        
        "I lunge in again and she jolts the salt shaker at me."
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"You've just been... as{b}{i}salt{/i}{/b}ed!\""
        
        "I grab the pepper and grind it in her direction."
        
        p"\"You're getting {i}{b}pepper{/i}{/b}ed!"
        
        show J 3YAnnoyed_Flat at PCM1 with slowd
        
        j"\"Arsehole! You got it down my top.\""
        
        "People glare from adjacent tables."
        
        p"\"S-sorry...\""
        
        hide J cnormal with slowd
        
        "I place it down and fork a mouthful of food."
        
        #show J cnormal with slowd
        
        #"I retreat, opting to bide my time and wait until she's off guard."
        
        "The flavours of beef, melted cheese, and herbs explode in my mouth."
        
        p"\"Oh, wow. This really is good.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"I did say you wanted lasagna.\""
        
        "She flashes a wink and I can only chuckle."
        
        p"\"You're not wrong.\""
        
        j"\"I never am!\""
        
        "She twists spaghetti, pork, and sauce onto her fork and offers it to me."
        
        p"\"Oh, wow. The food here is amazing.\""
        
        show J 2CHappy_Smile with slowd
        
        j"\"That's why we came!\""    
        
        "We tuck into our food, but I'm curious."
        
        #p"\"So, what about Danielle, doesn't she join you?\""
        p"\"Doesn't Danielle join you?\""
        
        "I ask, knowing full well she’d rather spend her Saturdays playing Magnum Dilon."
        
        show J 2DMellow_Smile with slowd
        
        j"\"No...\""
        
        
        
        "Her reluctance arouses my curiosity."
        
        p"\"You two seemed close when I met you.\""
        
        j"\"You could say that. We were best friends in primary school.\""
        
        p"\"And now?\""
        
        #show J cflat with fastd
        #show J cnormal with slowd
        
        
        show J 2YSad_Smile with medd
        show J 2YHappy_Smile with slowd
        
        "A pensive expression washes over her face."
        
        
        j"\"We're still friends.\""
        
        "I respect her reluctance and drop it; she’s respected mine."
        
        j"\"So what about you? What about your friends?\""
        
        "Which backfires."
        
        p"\"I... I don't have any.\""
        
        show J 3YAnnoyed_Flat with slowd
        
        "I receive a shove that makes me struggle for balance."
        
        j"\"What about me?\""
        
        show J 2YSad_Pout with slowd
        
        "Her lips drop into a pout. I roll my eyes."
        
        p"\"Of course you are!\""
        
        #I deliver it with a sarcastic tone.
        
        #Good!
        
        "I can't contain my grin."
        
        
        #time
        scene restaurant04_day with slowf
        
        "The waiter collects our empty plates."
        
        w"\"Did you enjoy your meal?\""
        
        p"\"It was excellent. Thank you.\""
        
        j"\"Perfect, compliments to the chef.\""
        
        
        "He bows."
        
        w"\"Anything else I can help you with?\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Let's stay and have a drink.\""
        
        
        "The grin on her lips twists."
        
        p"\"...Alcoholic?\""
        
        #j"\"Yeah! You're old enough. What's the problem?\""
        
        j"\"Yeah! You're old enough, right?\""
        
        p"\"Err...\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        
        j"\"Don't worry, it's on me.\""
        
        scene restaurant04_day 
        
        show J 2YHappy_Smile at PCM1
        
        with slowf
        
        "The waiter returns and places down our drinks."
        
        "I choke back some of the bitter brew."
        #managing to stop my face from contorting.
        
        #"I peer around. It feels wrong for me to be drinking."
        
        #"But I don't dislike the thrill."
        
        #"I choke back some of the bitter brew."
        
        #p"\"Ugh.\""
        
        #j"\"Haha! I didn't think you'd like beer, being a girl and all.\"" #;)
        
        #edits for drink exchange?
        
        ##
        
        #"I peer around. It feels wrong for me to be drinking."
        
        #"But I don't dislike the thrill."
        
        "I take a sip of the beer and fail to manage my grimace."
        
        j"\"Drink much Peter?\""
        
        p"\"No...\""
        
        j"\"Talk much?\""
        
        p"\"If you ask me a question.\""
        
        j"\"So, any story to why you're a year older than the rest of us?\""
        
        p"\"I... was in a car crash...\""
        
        "The words slip my lips, but I somehow feel comfortable enough to say it."
        
        j"\"Is that why you have those scars on your leg?\""
        
        "{i}I knew she'd seen them.{/i} I can't deny it at this point."
        
        p"\"Yep.\""
        
        j"\"What was it like having a year off?\""
        
        p"\"...Awful.\""
        
        j"\"Well, you're here now.\""
        
        "She laughs and claps my shoulder."
        
        p"\"Yeah...\""
        
        "The word escapes with a smile."
        
        "She raises her glass and nods at my own."
        
        show J 3YHappy_OpenSmile at PCM1 with slowd
        
        j"\"To the swimming team.\""
        
        #p"\"To—\""
        
        "{i}To a new life.{/i}"
        
        #p"\"—The swimming team.\""
        
        "We clink our glasses together and finish our drinks."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"We should head back, it's getting late.\""
        
        "I check my phone to see it's 10pm. Damn, didn't realise how late it was."
        
        "We hail a waiter and pay our bill."
        
        stop music fadeout 3.0
        
        play environment "audio/background/city2.mp3" fadein 3.0
        
        scene shop006_night_light with slowf
        
        "The night's cool air a pleasant welcome. Flutters in my stomach evoke a warm flush up to my cheeks."
        
        
        "I can't be sure whether it was that drink or this girl beside me."
        
        scene street001_night_light with slowf
        
        "Jennifer bombards me with her plans for swimming."
        
        p"\"Wait, extra practise?\""
        
        j"\"Yeah! We need to get this right!\""
        
        "I can't help wonder why she's carefree enough to have a drink with such aspirations."
        
        p"\"OK, sure.\""
        
        "Her mouth opens and her features lighten in realisation."
        
        j"\"Really?\""
        
        p"\"Yeah.\""
        
        j"\"Thanks, Peter!\"" 
        
        #mention her tone here?
        
        "She latches me in a brief hug."
        
        j"\"You're the best!\""
        
        
        "I can only smile and shrug."
        
        stop environment fadeout 2.5
        
        scene school_out003_night_light with slowf
        
        
        j"\"How about Monday morning?\""
        
        "I didn't expect something so soon... but at least it's not tomorrow morning."
        
        p"\"Sure.\""
        
        "I'm left echoing her smile."
        
        scene school_out009_night_light 
        show J 2YHappy_Smile at PCM1
        with slowf
        
        j"\"Well, you'd better get yourself an early night for Monday.\""
        
        j"\"But thanks, Peter. I had fun tonight.\""
        
        p"\"Yeah, me too. I will do.\""
        
        j"\"Goodnight.\""
        
        p"\"Goodnight, Jennifer.\""
        
        "I head to my room with a grin perched on my lips."
        
        scene room_boy16_night_dark with slowf
        
        "It doesn't matter who I was; I have a new life ahead of me."
        
        
        
        
        
        #use day room throughout?
        
        scene room_boy16_evening with longf
        
        "I wake up with last night fresh in my mind."
        
        #"I feel energised after last night."
        
        "What's she doing today?"
        
        #She did say she'd see Casey today...
        
        "I could message her..."
        
        t"\"Hey Jennifer, wanna do something?\"" with slowd
        
        nvl clear
        window hide
        
        "I hold down backspace and watch the characters dissapear." with slowd
        
        "I stare into the screen until it locks black."
        
        "She did say she was going to see Casey today..."
        
        scene  room_boy16_day with slowf
        
        "I waste my energy pacing my room, doing nothing productive. You could almost say nothing's changed."
        
        "Why did she invite me out yesterday?"
        
        "Was it just for her plans to get Casey and Dean to spend time together?"
        
        "My stomach sinks and I flop back onto my bed."
        
        "I'm getting myself way too worked up."# I'm just part of her plans."
        
        #"Which in my circumstances, I can't deny I'm happy to be. But I want to be more than just a pawn."
        
        play environment "audio/sfx/ring vibrate.mp3"
        
        "{i}...Speak of the devil.{/i}"
        
        stop environment fadeout 1.0
        
        j"\"What's your room number?!\""
        
        "{i}Hello to you too.{/i}"
        
        p"\"It's one-one-seven.\""
        
        j"\“I'll be there in a minute!\""
        
        p"\"Wait—\""
        
        "Dammit, she's hung up."
        
        "{i}Shit{/i}, my room's a mess."
        
        "I kick my dirty clothes under the bed and stack up my used plates."
        
        "Despite the mess, it looks so bare..."
        
        "I take my pots to the kitchen and opt to wait outside to intercept her."
        
        scene school_out002_day 
        
        show J 1YHappy_OpenSmile at PC1
        
        with slowf
        
        j"\"Hey! Why ya waiting for me here?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\"I just thought it’d be easier...\""
        
        j"\"Oh?\""
        
        #upturned sprite
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Your room's not a mess?\""
        
        p"\"Erm... no?\""
        
        "My denial comes out like a question."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Liar! Let's go!\""
        
        "I cut my losses and follow."
        
        
        play music "audio/music/bensound-littleidea.mp3"
        scene shop01_day with slowf
        
        "She jumps on the back of the trolley and thrusts her finger towards the meat aisle."
        
        j"\"Onward!\""
        
        "Her roar draws the attention of the people who hadn't noticed yet."
        
        p"\"Stop!\""
        
        "I lower my head to hide my burning cheeks. Her grin only widens."
        
        j"\"This is no time to be embarrassed, brave knight!\""
        
        "{i}Why did I open my mouth?{/i}"
        
        p"\"Brave knight?\""
        
        j"\"Y'know, like those fantasy games. Danielle was obsessed with them!\""
        
        "{i}I can see why she's now hiding the fact.{/i}"
        
        p"\"...What are we getting?\""
        
        j"\"You don't know?!\""
        
        j"\"We're on a quest to save chickety!\""
        
        #"Why did I open my mouth?"
        
        p"\"I'll take it we're getting chicken.\""
        
        j"\"Chickety!\""
        
        "I shut my mouth and follow." #It's easier."
        
        scene shop01_day with slowf
        
        "How have {i}I{/i} ended up paying for chickety?"
        
        "{i}Chicken!{/i} This girl..."
        
        scene room_kitchen06_day 
        
        show J 2YHappy_Smile at PC1
        
        with slowf
        
        j"\"Are you positive you don't require lessons from a master chef such as myself?\""
        
        "Her arrogance draws the smile on my lips."
        
        p"\"I'm certain I'll survive, chef.\""
        
        #"{i}With you cooking it.{/i}"
        
        "With {i}you{/i} cooking it."
        
        j"\"Suit yourself.\""
        
        hide J 2YHappy_Smile with slowd
        
        "But I find myself intrigued as she sprinkles various spices into the bowl of chicken by eye, followed by a drizzle of olive oil and lemon juice."
        
        "She caresses the spices into the meat and wraps a sheet of cling film over the top."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She catches me staring when she turns, drawing the smug smile on her lips."
        
        j"\"Keep me entertained.\""
        
        p"\"Huh?\""
        
        j"\"We've gotta wait a few hours for the marinade to set into the meat.\""
        
        p"\"Well, I'll tell you about all of the things I could've eaten in that time.\""
        
        show J 3YUpturned_Pout at PCM1 with slowd
        
        "I'm met by a glare."
        
        p"\"For starters, I'd already be tucking into a ham and cheese sandwich.\""
        
        show J 3YAnnoyed_AngryPout with slowd
        
        j"\"How about I don't give you any?\""
        
        p"\"Hey, I paid for chickety!\"" #paid for chickety?  for that chicken xd
        
        show J 3YUpturned_Grin at PCM1 with slowd
        
        j"\"I'm claiming him with spice!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She lifts the clingfilm and suspends the open container of chilli powder over the bowl."
        
        p"\"You wouldn't dare.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        "Her features turn devilish."
        
        j"\"Would I not?\""
        
        #"Her features turn devilish."
        
        #"Her hand jolts and a small puff of powder descends over the bowl."
        "She jolts the container; a small puff of powder descends over the bowl."
        
        p"\"OK, OK. Please, just don't hurt Chickety!\"" # I'll be good. 
        
        "My simulated plea extracts a laugh from her."
        
        show J 2YHappy_OpenSmile at PCM1 with slowd
        
        j"\"You're so dramatic!\"" #It's clingfilmed!
        
        #"{i}Says you...{/i}"
        
        p"\"Says {i}{b}you{/b}{/i}...\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She meets me with a smug smile."
        
        #p"\"I know...\""
        
        "..."
        
        p"\"Why does it takes so long?\""
        
        j"\"Yeah... Danielle always tells me to pre-prepare.\"" 
        
        j"\"It's fine after a couple of hours, but it's recommended to leave it overnight.\"" #wait at least twenty-four
        
        #Jennifer visits Casey Custard
        
        #She said she'd visit Casey????
        
        #(cut to cooking)
        #What about the cups of tea? Really, no sugar? I'm sweet enough. ;)
        
        scene room_kitchen06_day with slowf
        
        "My interest is piqued by the aroma searing from the pan."
        
        #"I creep up behind her and peer over her shoulder for a better view."
        "I approach, trying to get a better view."
        
        show J 2YHappy_Smile at PCC1 with slowd
        
        j"\"See, not as boring as you made it out to be.\""
        
        "Her face turns to mine, mere inches away."
        
        #"The sweet scent of her perfume; her breath tickling me cheek; the way her lipbalm shines as her lips curl into a grin..."
        
        
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "I jump back startled. My reaction met by a wink."
        
        j"\"No need to be shy; the only thing I'll be eating is this chicken.\""
        
        "My thought pattern sends a warm flush creeping up my cheeks. Which only draws another laugh."
        
        j"\"Make yourself useful. You could dry the dishes with the heat in your cheeks.\""
        
        hide J 2YHappy_Smile with slowd
        
        "I resign myself to cleaning the plates I left out earlier."
        
        scene room_kitchen06_day with slowf
        
        
        "She serves them up on my freshly washed plates. I swallow my saliva several times during the process."
        
        show J 2CHappy_OpenSmile at PCM1 with slowd
        
        j"\"Bon Appétit.\""
        
        #"She raises her wrap, gesturing for me to eat my own."
        
        show J 2YHappy_Smile with slowd
        
        "She raises her wrap, we touch wraps and take a bite."
        
        "The well-cooked chicken, salad, and spices blend explode into perfection."
        
        p"\"Not gon' lie, this'ish really good.\""
        
        show J 2CHappy_Grin with slowd
        
        j"\"Pfft. What'd you expect?\""
        
        "Though she boasts with a wave of her palm, there's a gleam in her grin." 
        
        "I find it contagious as I realise her passion for food."
        
        #"She puts her heart into everything, imbuing her food with passion."
        
        stop music fadeout 2.5
        
        
        #She has to meet Casey.
        
        
        #jencustardj
        
        
        #I have to go meet with Casey.
        #Be up bright and early tomorrow! 
        
        
        #remember to say tomorrow to Casey on the phone so she can go after this.
        
        
        
        #p"\"Ah, I see. Where are we going?\""
        
        #"She leans close and whispers in my ear."
        
        # j"\"You'll see.\""
        
        #Jen custard
        
        scene black with longd
        play music "audio/music/bensound-memories.mp3" fadein 2.0
        
        scene school15_evening with slowf
        
        
        "I stretch, releasing a yawn." 
        
        p"\"Moon's still out. Great start to the day.\""
        
        show J mnormals with slowd
        
        "My tone loaded with sarcasm."
        
        j"\"I'm not going in the morning.\""
        
        "She imitates me in her high-pitched voice. I can only grimace."
        
        p"\"I'll go back to bed then.\""
        
        hide J mnormals with slowd
        
        "I turn back and she latches herself around my arm."
        
        j"\"You wouldn't just leave me like that!\""
        
        "{i}Not normally, but don't push me right now.{/i}"
        
        "I sigh and allow her to lead me to the poolside."
        
        #"But I can't say her warmth and willingness to keep me around is unpleasant."
        
        "At least her warmth and willingness to keep me around isn't unpleasant."
        
        j"\"Let's have a race!\""
        
        "{i}Her personality on the other hand...{/i}"
        
        show J msmiles with slowd
        
        #j"\"Right, we'll need to do a different warm up for this move.\""
        
        #p"\"What do you mean?\""
        
        #j"\"I said the other night that we'd need extra practise and you agreed!\""
        
        #"Her eyes narrow at me."
        
        #j"\"Are you sure you only had {i}one{/i} drink?\""
        
        #p"\"Pretty sure.\""
        
        #j"\"Let's have a race!\""
        
        
        p"\"Ugh, it's first thing in the morning.\""
        
        j"\"C'mon!\""
        
        "I'm already regretting this."
        
        p"\"You'll obviously win.\""
        
        show J mnormals with slowd
        
        j"\"But how else will you stay fit?\""
        
        p "\"I thought I {i}just{/i} had to lift you a few times.\""
        
        show J sfists with slowd
        
        j"\"What are you trying to say?\""
        
        "I can't help grin."
        
        p"\"I need weight training to lift you, not a race.\""
        
        "She digs my arm and growls."
        
        p"\"Alright, alright.\""
        
        hide J sfists with slowd
        
        "Her smile returns as I line myself up by the side of the pool."
        
        #show text "Her hands slam into my back." #at truecenter with dissolve
        
        "Her hands slam into my back." #with fastout #at truecenter with dissolve 
        #pause 1.0
        #hide text with dissolve
        
        #"Her hands slam into my back."
        
        #pause 1.2
        
        #splash/underwater XD
        
        #play environment
        
        play sound "audio/sfx/Splash2.mp3"
        play environment "audio/background/underwater.ogg" fadein 4.0
        scene underwater with longd
        stop environment fadeout 2.5
        scene school15_evening with longd
        
        p"\"You…\""
        
        "The word seethe from my lips. I mange to subdue profanities."
        
        j"\"Ahahahaha!\""
        
        "I splash water at her and she only laughs harder."
        
        #j"\"You’re cute when you’re angry.\""
        
        j"\"You’re ... cute when ... you’re angry.\""
        
        "Laughter interspersed between her words."
        
        
        "I climb out and she jumps into the pool."
        
        "{i}She's done me again...{/i}"
        
        "I cannonball into the water beside her and rush to the surface with a smile."
        
        show J snormals with slowd
        
        j"\"Why would I care? I'm already wet.\""
        
        "Her innuendo delivered with a wink."
        
        "I resign to practice and vow to get her back..."
        
        #Timeskip (next lesson)
        
        scene school15_day with longf
        
        "We're a little late but the coach just ushers us to get started."
        
        "Jennifer turns to face me with her back to the pool."
        
        show J mGGCs with slowd
        
        j"\"C'mon! We're already late.\""
        
        "{i}Now’s my chance!{/i}" #...
        
        hide J mGGCs with fastd
        
        play sound "audio/sfx/Splash.mp3"
        
        p"\"Gotcha!\""
        
        stop music fadeout 2.0
        
        q"\"Peter!\""
        
        #"The Teacher's voice makes me freeze."
        
        "{i}Shit…{/i}"
        
        q"\"Do you understand how dangerous that is?\""
        
        "He lectures me about health and safety…"
        
        #(Time skip)
        
        scene school15_day with slowf
        
        p"\"I’m sorry, Sir. It won’t happen again.\""
        
        q"\"Good.\"" #You’ve got some potential, so keep your nose clean.\""
        
        "Even after that whole lecture, all I can think is {i}worth it.{/i}"
        
        "Jennifer motions me over with a scowl, luckily she's more interested in the lesson than revenge."
        
        #time skip
        
        scene school15_day with longf
        
        play music "audio/music/bensound-memories.mp3"
        
        j"\"Peter!\""
        
        "Jennifer climbs out and waves me over."
        
        "Casey approaches as I climb out."
        
        show J mnormals at left
        
        show c mswim at right
        
        j"\"Casey!\""
        
        j"\"Good work today, guys.\""
        
        "We share a glance. Jennifer looked ready to tell me something."
        
        cc"\"It was.\""
        
        j"\"Have you convinced Dean to join yet?\""
        
        cc"\"No... I'm doing fine with Matthew.\""
        
        "She focuses on her shifting foot."
        
        cc"\"I don't think he'd ever join anyway...\""
        
        "Her voice sinks into an indescernible mumble."
        
        j"\"Don't say that! You just need to pester him!\""
        
        "Casey shrugs."
        
        j"\"It worked on Peter.\""
        
        p"\"Hey! I joined from my own volition, thanks.\""
        
        j"\"Vol—?\""
        
        p"\"From my own free will!\""
        
        show J msmiles with slowd
        
        j"\"But I planted the seed.\""
        
        "The whole thing just gives me mixed feelings." 
        
        "I enoy spending time with Jennifer, but it only seems to confirm my doubt when she says something like that."
        
        j"\"Let's get changed!\""
        
        show school12_day with slowd
        
        #changing rooms
        
        "Casey leads them into the girl's changing rooms. Jennifer points to her eye, to me, and then to her wrist before following."
        
        stop music fadeout 3.2
        
        "I decipher it as, {i}see you later!{/i}"
        
        #kitchen
        
        scene room_kitchen06_day with longf
        
        "As the kettle clicks, banging in the hallway draws me to the doorway."
        
        scene hospital03_day with slowd
        
        p"\"Jennifer?\""
        
        play music "audio/music/bensound-memories.mp3" fadein 2.0
        
        "She forces me back into the kitchen."
        
        scene room_kitchen06_day with slowd
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Good timing! You even boiled the kettle!\""
        
        p"\"How many sugars?\""
        
        j"\"None, I'm sweet enough.\""
        
        "She flashes a wink."
        
        p"\"But seriously?\""
        
        show J 3YUpturned_Pout at PCM1 with slowd
        
        j"\"Hey, I'm serious! No sugars.\""
        
        #"I grin."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "I grin as I place her brew beside her."
        
        p"\"Oh.\""
        
        "I stretch my aching arms and take a sip of my own."
        
        p"\"Y'know, it shouldn't hurt to drink a cup of tea.\""
        
        show J 2YHappy_Grin at PCM1 with slowd
        
        j"\"I'm a good weight, I see.\""
        
        #time skip XD
        
        scene room_boy16_day with slowf
        
        "She invites herself in."
        
        "Her eyes scan across my room." 
        
        "It makes me feel self-conscious about it still being bare in nature."
        
        "And the fact my clothes are still peeking from under my bed from the other day..."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"So this is your room?\""
        
        p"\"Yep.\""
        
        j"\"Ready to leave so soon?\""
        
        p"\"Nope...\""
        
        "She opens my wardrobe to my chagrin."
        
        p"\"Hey!\""
        
        show J 2YUpturned_Flat at PCM1 with slowd
        
        j"\"You haven't even unpacked your suitcase?!\""
        
        "I shut the door and usher her away."
        
        p"\"It's fine, I'll sort it out later.\""
        
        show J 3YUpturned_Pout at PCM1 with slowd
        
        j"\"You've been here for three weeks!\""
        
        p"\"Then another day won't matter.\""
        
        show J 2YSad_Pout at PCM1 with slowd
        
        j"\"I know you're not going to do it tomorrow.\""
        
        p"\"It's fine the way it is, just leave it.\""
        
        j"\"I've already seen it now. I can't let it go...\""
        
        "Her pout wins out in the end."
        
        p"\"Fine...\""
        
        #time skip XD
        
        scene room_boy16_day with slowf
        
        "As I'm hanging up my T-shirts, she starts packing away my underwear."
        
        p"\"Stop! What are you doing?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"It's washed, right?\""
        
        p"\"Yeah, of course. It's just weird!\"" #italicise just or weird? 
        
        p"\"How would you feel if I came into your room and started packing away your underwear?\""
        
        show J 2CHappy_OpenSmile at PCM1 with slowd
        
        "She bursts into laughter."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Wouldn't happen. They'd be where they should be.\""
        
        # fist sprite
        show J 3YUpturned_Pout at PCM1 with slowd
        
        j"\"If I caught you snooping through my drawers on the otherhand...\""
        
        p"\"Wouldn't happen. What do you take me for?\""
        
        show J 2YSad_Smile at PCM1 with slowd
        show J 2YHappy_Smile at PCM1 with fastd
        
        "To my surprise, a pensive expression washes over her face."
        
        j"\"Y'know, I'm not sure with you sometimes. You're not a perv, though.\""
        
        #"Her pensive tone leaves me in thought."
        
        "It takes a moment to reaise its not an insult."
        
        p"\"Good. Do my T-shirts instead.\""
        
        hide J 2YHappy_Smile with slowd
        
        "I usher her to where I left off on my T-shirts."
        
        p"\"Why did you come anyway?\""
        
        show J 2YHappy_OpenSmile at PCM1 with slowd
        
        j"\"I almost forgot! We need to plan Casey's Birthday!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\"I'm not good at planning.\""
        
        j"\"I can see that.\""
        
        "..."
        
        p"\"When is it?\""
        
        j"\"It's on Thursday, but we can plan something for the weekend.\""
        
        p"\"Why the weekend?\""
        
        j"\"It's her eighteenth birthday. So she'll legally be able to drink.\""
        
        p"\"You want us to go and get drunk?\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"No, I want Dean and Casey to have a few drinks together.\""
        
        #p"\"I'll take it we're not going then.\""
        
        p"\"Then what do you want me to do?\""
        
        #I want you to ring me and pretend you're lost. 
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        #j"\"Exactly! But, I need you to do me a favour.\""
        
        #p"\"What's that?\""
        
        j"\"You to ring me and pretend you're lost. I'll meet you near Stop-Shop and we'll leave them to get together.\""
        
        #j"\"You need to ring me and pretend you're lost. I'll meet you near Stop-Shop and we'll leave them to get together.\""
        
        #p"\"To get together?\""
        
        #j"\"Yeah, I've been asking Casey to ask Dean, but she won't.\""
        
        p"\"Then what are {i}we{/i} going to do?\""
        
        j"\"I thought we could get some grilled chicken from Pepper's. It's amazing~!\""
        
        "I release a grin and shrug. {i}How can I say no?{/i}"
        
        p"\"Sounds good.\""
        
        j"\"Then it's settled!\""
        
        show J 2YHappy_Smile at PC1 with slowd
        
        "She lays down my T-shirt mid-sentence and rises."
        
        p"\"You can't just leave this half done. You started it!\""
        
        j"\"I've given you a head start. I'm sure you can handle the rest.\""
        
        show J 2YHappy_Grin at PC1 with slowd
        
        "She offers an exaggerated grin as she leaves."
        
        j"\"Ba-bye~!\""
        
        stop music fadeout 2.0
        
        hide J 2YHappy_Grin with slowd
        
        "..."
        
        "It's the kick up the arse I needed, but I still can't help but feel annoyed."
        
        # town bikes scene
        
        scene street002_evening with longf
        
        "I rang Jennifer ten minutes ago. What's taking her so long?" #She's taking her sweet time.
        
        "I whip out my phone and begin a message."
        
        show J 1YHappy_OpenSmile at PC1 with slowd
        
        j"\"Peter!\""
        
        "{i}Finally.{/i}"
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"What's up? You've got a face like a slapped arse.\""
        
        "She pinches my cheek and I push her hand away."
        
        p"\"You took ages and I haven't eaten yet.\""
        
        show J 2CHappy_OpenSmile at PCM1 with slowd
        
        j"\"Pepper's will be worth it!\""
        
        "She tugs on my sleeve and I follow."
        
        #Long Rd
        
        play environment "audio/background/city2.mp3" fadein 3.0
        
        scene street001_evening 
        
        
        show C YSad_Smile at PM1 #with slowd
        show J 2YHappy_Flat at PCR2 #with move
        show De 2YDisappointed_Frown at PML1 #with slowd
        with slowd
        
        
        #show c mnorma at Position (xpos = 0.5, xanchor=0.1, ypos=1.3, yanchor=1.3)
        
        #show J cnormalc at Position (xpos = 0.5, xanchor=0.9, ypos=1.0, yanchor=1.0) 
        
        #show d mnorm 
        
        
        
        
        "As we pull out onto Long Rd, Dean and Casey are waiting."
        
        "{i}Surely they've followed her...{/i}"
        
        #show C YSad_Smile at PC1 #with slowd
        
        show C YSad_Smile at PC1
        show J 2YHappy_Flat at PCR2 
        show De 2YDisappointed_Frown at PCL2 
        with move
        
        cc"\"Hey, guys. Where are you going?\""
        
        "Casey's expression insinuates she knows the ruse."           
        
        j"\"Hey, we were gonna get some food on the way.\""
        
        cc"\"Don't you usually do that at the end of the night?\""
        
        j"\"Always good to prepare for the night.\""
        
        #"There's an awkward yet jovial air coming from both girls." 
        
        #There's an awkward 
        

        show C YSad_Smile at PML1
        show J 2YHappy_Flat at PMR1 
        show De 2YDisappointed_Frown at PC1 
        #with slowd
        with move
        
        
        "Dean approaches me."
        
        D"\"Plannin' t' leave?\""
        
        "I'll just have to roll with it."
        
        #p"\"Oh, no. I had gotten lost and I haven't eaten yet.\""
        p"\"Oh, nah. Still new around here and haven't eaten yet.\""
        
        "He snorts and smiles."
        
        D"\"Whatever. Let's get a drink.\""
        
        hide C YSad_Smile 
        hide J 2YHappy_Flat 
        with slowd
        
        D"\"Catch up, ladies.\""
        
        #hide  c mnorma at right with fastd
        
        #hide J cnormalc at left with fastd
        
        "They pay no notice and I head off with Dean."
        
        show De 2YRelax_Smirk at PC1 with slowd
        
        D"\"Gettin' along alright with Jenny, aren't ya?\""
        
        p"\"Jenny?\""
        
        D"\"Yeah. She hates that nickname.\""
        
        "I take a mental note to store it in my arsenal."
        
        D"\"So you're helpin' her out with the team?\""
        
        p"\"Yeah. She's helped me with the move and... meeting people.\""
        
        "A gasp escapes my lips as his hand crashes into my back." #gasp?????
        
        D"\"It's just here.\""
        
        # Bar scene
        
        stop environment fadeout 2.5
        
        play music "audio/music/Lounge Bar - Background Instrumental Music - Royalty Free.mp3" fadein 3.0
        
        #play environment "audio/background/bar.ogg" fadein 2.0
        
        scene Bar with slowd
        
        "The smell of alcohol and perfume sit on the air. It reminds me of my uncle."
        
        "He pulls up a chair at the bar and I sit beside him."
        
        show De 2YRelax_Frown at PC1 with slowd
        
        D"\"Two Burgs.\""
        
        B "\"You lads got ID?\""
        #"A silence hangs between us as the bartender pulls the drinks."
        
        "Somehow, I {i}knew{/i} I'd need it tonight."
        
        "We show our IDs and he pulls our pints."
        
        D"\"Cheers.\""
        
        "He holds up his glass and I meet it with mine."
        
        p"\"Cheers.\""
        
        #"The bittner drink washes down my neck."
        #"I grimace and stomach the bitter brew."
        
        "I struggle to contain my grimace after we drink."
        
        show De 2YRelax_Smirk at PC1 with slowd
        
        D"\"She growin' on ya?\""
        
        
        "I shrug."
        
        p"\"Yeah, I guess.\""
        
        show De 2YDisappointed_Frown at PC1 with slowd
        
        D"\"She's a good'n.\""
        
        "His eyes rest on his drink and his lips fall flat."
        
        #"His eyes rest on his drink and his lips pull into a smile."
        
        
        "A meaty hand slams on Dean's shoulder."
        
        show De 1YStern_OpenSmile with slowd
        
        D"\"Ryan! How's it goin'?\""
        
        show De 1YStern_Smirk with slowd
        
        "He ignores Dean's question and scans me head-to-toe with a stern gaze."
        
        ry"\"Ryan.\""
        
        "He offers a shake and crushes my hand."
        
        p"\"Peter.\""
        
        ry"\"Good t' meet ya.\""
        
        p"\"You too.\""
        
        "He loses interest and focuses back on Dean."
        
        ry"\"Why you stopped weight liftin'? It's borin' without ya.\""
        
        D"\"I don't have time. I'm two As away from a scholarship.\""
        
        "Damn, I didn't pin Dean down to have such good grades."
        
        ry"\"Don't have time? You're in a bar.\""
        
        D"\"It's Casey's birthday.\""
        
        ry"\"You gon' get with her or what?\""
        
        "He shoots a glance at me."
        
        show De 2YStern_Frown with slowd
        
        D"\"We're friends.\""
        
        ry"\"I need to get back to Amber, anyway. Later.\""
        
        p"\"Later.\""
        
        D"\"Don't be getting yourself expelled.\""
        
        "Ryan grins and walks away." 
        #"We say later and dean ushers in."
        
        show De 2YStern_Frown at PCM1 with slowd
        
        "Dean leans towards me."
        
        D"\"He's a cool guy, but—\""
        
        "He scans for Ryan to be sure he's out of earshot."
        
        D"\"—I wouldn't want to get on the wrong side of him. Just stay away from his sister, Rachel.\""
        
        p"\"I don't even know wh—\""
        
        j"\"Dean! Peter!\""
        
        "We opt to find a table."
        
        #time skip
        
        #"Having decided more drinks are needed, Dean follows Jennifer to bar. They share banter I can't decipher."
        
        scene Bar 
        
        show De 2YRelax_Smirk at PCL1
        
        show C YGentle_Grin at PCR1
        
        with slowf
        
        "We make our way to the last free table and Jennifer heads for the bar; Dean’s eyes follow."
        
        D"\"Need a hand?\""
        
        j"\"Sure.\""
        
        hide De 2YRelax_Smirk with moveoutleft
        
        show C YSad_Smile at PC1 with move
        
        "They make their way to the bar with our eyes in tow."
        
        #hide c csmile with fastd
        
        #nvl
        
        t"Dean leans his mouth into her ear; Jennifer laughs and slaps his arm." with slowd
        
        t"It stirs up discomfort.  I enjoy her playful nature, but... she's like this with {i}everyone?{/i}"
        
        #window clear
        #hide nvl
        
        window hide
        nvl clear
        
        show C YGentle_Smile at PC1 with move
        
        cc"\"You like Jennifer, don't you.\"" with slowd
        
        "My mouth opens but my brain freezes."
        
        cc"\"It's OK, I won't tell her.\""
        
        show C YGentle_Smile at PC1 with slowd
        
        "She looks in their direction but her eyes fall to the table."
        
        show C YSad_Sad at PC1 with slowd
        
        cc"\"She won't notice anyway.\""
        
        "Venom laces her tone."
        
        p"\"What do you mean?\""
        
        show C YSad_Sad at PC1 with slowd
        #show CX Shadow at PC1 with slowd
        
        cc"\"Before you came, she'd bail from outings with personal issues, and now she's going out with you instead.\""
        
        cc"\"Every time she sets up events, it always ends up being me with Dean.\""
        
        show C SAwkward_Sad with slowd
        
        cc"\"And everytime I think we're getting somewhere, I have to watch his eyes light up when he sees her again...\""
        
        "The wry smile twisting her lips twists my heart." #feels the same watching Jennifer with Dean.
        
        cc"\"So I'd appreciate it if you told Jennifer to stop setting up time for us to be alone.\""
        
        p"\"Why haven't you told her?\""
        
        cc"\"Because... if {b}{i}I{/i}{/b} told her my feelings, she'd only persist more.\""
        
        p"\"She does know...\""
        
        cc"\"I know...\""
        
        cc"\"I just question whether she knows Dean likes her.\""
        
        show C YGentle_Sad with fastd
        
        show J 2YHappy_Smile at PCR2 with moveinright
        
        show De 2YRelax_Smirk at PCL2  with moveinleft
        
        "Her smile returns as they do."
        
        "Jennifer places a small glass in each of our places."
        
        j"\"Shots!\""
        
        "I sip back my beer."
        
        p"\"I've still got this beer.\""
        
        "Dean places down another drink in each place and takes his seat."
        
        #mention he measures Peter's reaction when he buys him one at the bar.
        
        show De 2YRelax_OpenSmile at PCL2  with slowd
        
        D"\"Drink much, Peter?\""
        
        #"I stare into the golden, bubbling liquid before me."
        
        "My first pint is barely halfway and they've finished their drinks."
        
        p"\"Can't say I do...\""
        
        #Just a beer before with Jennifer? 
        
        show De 2YRelax_Smirk at PCL2  with slowd
        
        "Jennifer lifts her shot glass."
        
        j"\"Casey's eighteenth!\""
        
        "We all gives cheers tilt our shots back. The taste of chemicals fills my mouth as the liquid burns down my throat."
        
        "They share a laugh as my face contorts and I fail to contain a cough."
        
        
        #don't you know the team evaluation is soon? 
        
        
        #Jennifer will bring up that Dean should swim with Casey at the bar.
        
        j"\"So, Dean, aren't you going to swim with Casey?\""
        
        #In other routes you'll find Dean has joined Jennifer as a partner (and they pass). She's still miserable though (Sarah Scenes).
        
        "Dean takes a glace at Casey and sighs."
        
        #show d cnorm at Position (xpos = 0.5, xanchor=0.9, ypos=1.0, yanchor=1.0) with slowd
        
        show De 1YRelax_Frown with slowd
        
        D"\"I've got a lot on my plate right now.\""
        
        j"\"But the team evaluation is soon!\""
        
        "Casey stares into her empty shot glass."
        
        show C SAwkward_Sad with slowd
        
        cc"\"He has a lot on his plate.\""
        
        "She reiterates his words in a flat tone."
        
        "I take a sip of my beer just to feel like I belong here." #of my drink, in this scene." 
        
        #Casey downs her own drink and leaves? 
        
        j"\"We should do more shots!\""
        
        cc"\"No, thank you.\""
        
        show C SAwkward_Sad at PM1 with slowd
        
        "Casey rises."
        
        cc"\"We've got a table booked at Isabella's.\"" 
        
        "She casts her gaze on Dean who looks perplexed."
        
        cc"\"It's packed tonight.\"" 
        
        show De 2YRelax_Bemused at PML1 with slowd
        
        D"\"Oh, yeah.\""
        
        "Casey necks back her cocktail."
        
        cc"\"We should go, it's almost half-seven.\""
        
        "Dean downs his own drink and follows."
        
        D"\"Later.\""
        
        hide C cnorm 
        
        hide De cnorm
        
        with moveoutleft
        
        show J 2YSad_Flat at PC1
        
        with move
        
        "As they exit, Jennifer sighs and rests her face in her palms."
        
        p"\"Should we see if there are any free tables?\""
        
        j"\"They're not going to Isabella's...\""
        
        p"\"They know?\""
        
        j"\"Yeah.\""
        
        "..."
        
        p"\"Do you know Dean doesn't like her?\""
        
        j"\"He hasn't given her a chance...\""
        
        "I don't have it in me to bring up that he likes her..."
        
        "It's something I rather wouldn't accept."
        
        p"\"So why are you pushing it?\""
        
        j"\"I thought we could be teams together; I thought we'd be a group of friends.\""
        
        j"\"But I keep... fucking that up.\""
        
        show J 2YSad_Sad with slowd
        
        #"She rises to her feet."
        
        j"\"I'm getting a drink.\""
        
        p"\"I'll get one, too. As long as it's not another shot.\""
        
        show J 2YHappy_Grin with slowd
        
        "Her solemnity gone as quickly as it appeared."
        
        j"\"You're a wuss. What'dya want, a cocktail?\""
        
        "Her tone filled with sarcasm but I'm curious."
        
        p"\"Sure, they look pretty good.\""
        
        hide J 2YHappy_Grin with slowd
        
        "She wriggles into the crowd by the bar and manages to get served before most."
        
        "Soon appearing with two cocktails."
        
        show J 2YHappy_Smile at PC1 with slowd
        
        j"\"You'll like this one!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She passes me the cocktail as we make our way back, and we take our seats."
        
        p"\"What is it?\""
        
        j"\"Sex on the Beach!\""
        
        p"\"I think we're living in the wrong country for that.\""
        
        show J 2YHappy_Grin at PCM1 with slowd
        
        j"\"We? I didn't say it'd be with you.\""
        
        
        "She winks and slaps my arm."
        
        p"\"Uh...\""
        
        "Heat rises into my cheeks."
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"It's too easy! Had to get you back for pushing me in the pool.\""
        
        p"\"You pushed me in first!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She laughs and waves it away."
        
        j"\"Thanks for joining me. I do appreciate it y'know.\""
        
        "I shrug and release a bashful smile."
        
        p"\"What did you mean before, about the team evaluation?\""
        
        j"\"Five teams are chosen but only one couple will be picked to compete against other schools.\""
        
        j"\"Then the winners then get a chance to complete at a semi-professional level...\""
        
        #p"\"I promise I'll try my best. We'll train every morning.\""
        
        p"\"I'll train with you in the mornings.\""
        
        "My tongue loose from the alcohol. To see her smile now is worth my future effort." 
        
        j"\"Make it official.\""
        
        #"She holds up her glass and I meet it."
        
        "We clink glasses and latch our pinkies."
        
        p"\"To the Olympics.\""
        
        #p"\"I'll see you in the Olympics.\"" #p"\"I'll see you swimming in the Olympics.\""
        
        "We neck back our drinks."
        
        show J 2YSad_Flat at PCM1 with slowd
        
        j"\"Is that what you want?\""
        
        p"\"Me? I'm not sure what I want—\""
        
        "I carry on as her brow tilts."
        
        p"\"—Eating would be nice, though.\""
        
        "She snatches her phone from her bag."
        
        show J 2YHappy_OpenSmile at PCM1 with slowd
        
        j"\"Pepper's is still open, hurry!\""
        
        "She finishes her drink and I follow suit."
        
        stop music fadeout 2.2
        
        stop environment fadeout 3.0
        
        scene restaurant05_day 
        
        show J 2YHappy_Smile at PCM1 
        
        with slowf
        
        "Jennifer brings our orders back to the table."
        
        #bensound sexy XD
        stop music
        play music "audio/music/bensound-sexy.mp3" fadein 2.0
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        "She holds out a fast food container, flourishing her free hand above it as though casting a spell."
        
        j"\"Jennifer! She's brought to you by...\""
        
        "Her high-pitched commentary is synchronised with the revelation of its contents."
        
        j"\"Pepper's Mediterranean Grill.\""
        
        "She disects the burger with great care, noting each ingredient with her pinky."
        
        #j"\"A freshly cooked chicken fillet, coated in a home-made Mediterranean marinade.\""
        
        #j"\"Accompanied by fresh red onion, lettuce, tomato, and mayonnaise, on a perfectly grilled bun.\""
        
        j"\"A freshly cooked chicken fillet, coated in a home-made Mediterranean marinade—accompanied by fresh red onion, lettuce, tomato, and mayonnaise, on a perfectly grilled bun.\""
        
        
        "She points to the bag she placed on the table."
        
        j"\"Along with a side of fries and a drink. All for just four ninety-five!\""
        
        "She tilts back her head, bringing the burger to her lips."
        
        stop music fadeout 0.8
        play sound "audio/sfx/Record Scratch.mp3"
        
        "I can't contain my laughter as mayonnaise rolls down her chin."
        
        #scratch sound? XD
        
        #p"\"Talk about food porn.\""
        
        #"She laughs and wipes her chin."
        
        #j"\"Try it, it's really good!\""
        
        #future Peter. It was much easier to say this at the time with some acohol in my system. xd
        
        #hug?
        
        show J 3YAnnoyed_Pout with slowd
        
        j"\"What're you laughin' at?\""
        
        p"\"At least you could apply for a role in an advert if you don't make it in the Olympics.\""
        
        "{i}Or a porno.{/i}"
        
        "She wipes her chin and glares!"
        
        j"\"Arsehole! Now you have to make sure we make it!\""
        
        p"\"I'll do my best.\""
        
        show J 2YHappy_Smile with slowd
        
        "She smiles and nods."
        
        j"\"Now eat up! It's really good.\""
        
        #time skip
        #long st
        
        play environment "audio/background/city2.mp3" fadein 2.0
        
        scene street001_night_light with slowf
        
        p"\"I won't lie, they were almost as good as your wraps.\""
        
        j"\"Almost?\""
        
        p"\"Y'know, I might just have to try them again to clarify.\""
        
        "She smirks and winks."
        
        j"\"You just might.\""
        
        
        
        #near school
        #does Jen live here or what?? Yes.
        
        stop environment fadeout 2.0
        
        scene school_out003_night_light 
        
        show J 2YHappy_Smile at PC1
        
        with slowf
        
        j"\"My dorms are on the other side from yours.\""
        
        #p"\"I'll see you tomorrow.\""
        
        show J 2CHappy_Smile at PCC1 with slowd
        
        "She wraps me in a hug."
        
        #Vamoose, cretin xd
        

        
        j"\"Thanks, Peter. I needed this tonight.\""
        
        "{i}Me too.{/i}"
        
        "I allow myself to wrap my arms around her and feel solace for a brief moment before she lets go."
        
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        
        p"\"What about Dean and Casey?\""
        
        j"\"I'll leave it to them.\""
        
        "Casey's words echo through my mind."
        
        p"\"I think that's probably best.\""
        
        j"\"Goodnight, Peter.\""
        
        p"\"'Night.\""
        
        #room
        
        scene room_boy16_night_light with slowf
        
        #"I can still feel the warmth of her hug."
        
        "Why did she hug me? I can almost feel her warmth as it flashes back through my mind."
        
        "Can we really make it?"
        
        "{i}No.{/i}"
        
        "{i}At least not me.{/I} I flop back onto my bed."
        
        t"If she makes it without me, would she leave me behind?" with slowd
        
        t"Even if she didn't, {i}I'd only hold her back.{/i}"
        
        #t"Would she forget me as gleefully as she met me?"
        
        #t"{i}I'd only hold her back, anyway.{/i}"
        
        t"She should have someone like Dean... atheletic, smart, motivated..."
        
        "{i}Are we just holding Jennifer and Dean back...?{/i}" with slowd
        
        nvl clear
        window hide
        
        t"All those nights I've spent alone, wondering what it was to have a friend." with slowd
        
        t"And now here I am, being selfish, wondering if I'll lose her because of what she wants."
        
        #t"I'm still... paralysed by my own venom."
        
        nvl clear
        window hide
        
        "I sit up and rest my head in my palms." with slowd
        
        "{i}I'm still... paralysed by my own venom.{/i}"
        
        "I will make sure she makes these trials."
        
        "...Maybe I'll make it too."
        
        
        #I'd never make it. But with Jennifer? I think we can.
        
        #Erm... I don't think I'd explained it that well earlier; I forgot to mention that individuals are picked to make teams, rather than teams being picked.
        
        
        #t"Would I hold her back?"
        
        #wouldn't I just hold her back?
        
        #She should have someone like Dean... atheletic, smart, motivated...
        
        #All those nights I've spent alone, wondering what it was to have a friend. 
        
        #And now here I am, being selfish, wondering if I'll lose her because of what she wants. 
        
        #I'm still... paralysed by my own venom.
        
        #I can help. I will help her train. I... might even get through too.
        
        play sound "audio/sfx/Mp3-alarm-clock.mp3"
        scene room_boy16_evening with longf
        
        stop sound fadeout 0.7
        
        "My early alarm stirs regret in my stomach."
        
        #stop sound fadeout 0.7
        
        scene black with slowd
        
        "Today's the day where the teams are picked."
        
        #"An angry Jennifer is enough to make me snooze my alarm for five minutes."
        
        #"I smash the snoozebutton."
        
        #My body aching
        
        #play sound "audio/sfx/Mp3-alarm-clock.mp3"
        
        scene room_boy16_evening with slowd
        
        "Nervousness is wedged in my stomach."
        
        "We've trained every day for two weeks, but it just doesn't feel enough."
        
        #stop sound fadeout 0.7
        
        #"The fact I don't want to let her down makes me rise..."
        
        #have a scene here of them being more serious about it
        
        
        scene school12_evening with longf
        
        #"We've been training every day for the past two weeks." #Today is the day we're picked for teams."
        
        p"\"Hey.\""
        
        show J 1CHappy_OpenSmile at PC1 with slowd
        
        "I greet her nonchalantly, but a smile conquers my lips just at the sight of her."
        
        j"\"Peter!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "Jennifer wraps me in her arms; I stiffen before reciprocating."
        
        p"\"Err?\""
        
        "Is the only response my brain can muster."
        
        j"\"Am I not allowed to hug my friend?\""
        
        p"\"Of course.\""
        
        j"\"I haven't even been able to sleep...\""
        
        p"\"You've got to be ready for everyday!\""
        
        "I imitate her hyperbole, grateful to hear a chuckle from her."
        
        show J 3YUpturned_Grin with slowd
        
        j"\"Arsehole!\""
        
        p"\"We've done everything we can do now. I know you'll make it.\""
        
        scene school15_day with slowd
        
        "We huddle around the instructor, who begins naming the candidates; Jennifer's fingers dig into my forearm."
        
        #
        q"\"Casey, Claire, Matthew, Marcus, Jennifer...\""
        
        show J snormals with slowd
        
        "She wraps me in a hug."
        
        j"\"We did it!\""
        
        "As he finishes with names, my heart drops at the lack of my own."
        
        p"\"You did it...\""
        
        j"\"Thank you so much...\"" 
        
        "It's not something I wanted to do, but I wanted to go with her."
        
        "But as long as she's happy..."
        
        p"\"Good luck this weekend.\""
        
        j"\"I won't let you down, I promise!\""
        
        #room 
        
        #Dream prelude:
        
        scene black with longf
        
        centered "Jennifer Act 2"
        
        
        
        scene room_boy16_night_dark with longf
        
        "I feel deflated after failing to make it. It was naive to think I could..."
        
        "Sleep doesnt come easy..."
        
        #Dream:
        
        #Music?

        play music "audio/music/Drone in D.mp3" fadein 3.0
        
        scene black with longf
        
        #centered "I'm back in this shack. This time, I'm lay on the floor." with slowd
        centered "The darkness shifts into a wooden ceiling. {i}This shack...{/i}" with slowd
        
        #centered "The ceiling shifts into wood and hay. {i}This shack.{/i}." with slowd
        
        show ghost angel scream with slowd 
        
        t"I crawl towards her and she looks toward the pans on the stove." with slowd
        t"{i}Dinner will be ready soon.{/i}"
        #t"She lifts me up and holds me in her arms, rattling a toy."
        
        t"She calls me toward her, rattling a toy."
        
        hide ghost angel scream with slowd
        
        #t"She lays it down and exits, door slamming behind her."
        
        t"As I near her, she lays it down and exits."
        
        t"{i}Don't leave me alone.{/i}"
        
        window hide
        nvl clear
        
        "The doors and windows merge into wooden panels." with slowd
        
        centered "{i}I'm trapped.{/i}" with slowd
        
        #"The pans overflow and flames spill down to the floor."
        
        play environment "audio/sfx/Flames.ogg" fadein 5.0
        
        show text "Flames overflow from the pans and spill to the floor." at truecenter with dissolve
        pause 0.5
        #hide text with dissolve
        
        #flame sound
        
        #"Flames overflow from the pans and spill to the floor." with slowd
        
        scene white with longd
        
        #Fade into white screen like him losing his memories to begin with. Symboling his fear of losing her like in the dream. 
        
        stop environment fadeout 2.5
        stop music fadeout 2.5
        
        scene room_boy16_evening with longf
        
        play music "audio/music/myuu - Nebula.mp3" fadein 3.0
        
        "I wake up in a cold sweat." #{i}That dream...{/i}"
        
        "{i}What have I lost...?{/i}"
        
        "What was my life like... {i}before?{/i}"
        
        "What was it like to feel... {i}loved...{/i}"
        
        #"I wipe my dried tears, wondering what I've really lost."
        
        #"Wondering what I will lose..." matter
        
        #"The life I had {i}before{/i} feels like nothing. The time at the hospital and my uncle's feels like a distant memory."
        
        #"Will I lose Jennifer too? Will I... forget her...?"
        
        #time skip.
        
        scene room_boy16_day with slowf
        
        "My anxiety peaks again but for different reasons." 
        
        "The thoughts of Jennifer slipping from my grasp..."
        
        "The thoughts that I'm only holding her back..."
        
        "Will I lose Jennifer too?" #Will I... forget her...?"
        
        "The trials are today. And all I can do is contemplate my selfishness." 
        
        "She told me to meet her at that bar at 6pm." 
        
        stop music fadeout 2.0
        
        "Whether win or lose, she would need a drink. {i}I think I do, too.{/i}"
        
        
        
        
        #"I head out to greet them."
        
        #p"\"Where's Jennifer?\""
        
        #cc"\"She's at that bar.\""
        
        #p"\"Who with?\""
        
        #cc"\"Herself.\""
        
        #p"\"She didn't...?\""
        
        #"Casey shakes her head. She gives a grim smile."
        
        
        #Why didn't you tell me sooner?
        
        #Because you were trying so hard to help me, I didn't want to put pressure on you so soon.
        
        
        
        
        #p"\"Do you know that Dean likes you?\""
        
        #"She pulls off from me, a wry smile seizing her lips."
        
        #"A wry smile seizes her lips."
        
        #"{i}Idiot. Why did I ask that...?{/i}"
        
        #have some time skips and then 
        
        #Peter doesn't make the team and anxiously awaits Jennifer.
        
        
        #She finds out on a Sunday that she hasn't made it, you meet her in that bar
        
        #
        
        #
        
        play music "audio/music/Lounge Bar - Background Instrumental Music - Royalty Free.mp3" fadein 3.0
        
        #play environment "audio/background/bar.ogg" fadein 2.0
        
        scene Bar with slowf
        
        "I arrive and smile when I see her."
        
        p"\"Celebrating?\""
        
        "She necks back her cocktail and orders another."
        
        p"\"Jennifer?\""
        
        "She pours another down her throat."
        
        show J 2YHappy_OpenSmile at PC1 with slowd
        
        j"\"Woooo!\""
        
        #p"\"Are you—\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Let us eat and drink, for tomorrow we die!\""
        
        p"\"That's...\""
        
        j"\"—From the Bible!\""
        
        p"\"Just because it's...\""
        
        #"After that dream, I'm ready for a drink right now."
        
        
        p"\"—ah, fuck it. Get me a drink.\""
        
        "She hands me a drink and is about to neck back another. I block her with my hand."
        
        p"\"Calm down, we've got class tomorrow.\""
        
        show J 2YSad_Sad at PCM1 with slowd
        
        j"\"I didn't make it...\""
        
        "Her confession comes with a sigh."
        
        "I could already tell from the scene." 
        
        #"But to hear her say it stabs me with a pang of relief, and then guilt for feeling relieved."
        
        #"But to hear her say it stabs me with a pang guilt for my thoughts earlier." #earlier thoughts
        
        "As low as I feel seeing her like this, there's a part of me that's glad she didn't make it without me." #glad she didn't* #Incase she moved out of reach.  
        
        #"I can't stand to see her like this; a pang of guilt stings the part of me that's glad she didn't make it."
        
        p"\"What about the other competitions?\""
        
        j"\"What's the point?\""
        
        "..."
        
        #scene black with slowd
        
        #cut here?
        
        #centered "Might cut it here, let me know if you think I should." with slowd
        
        #scene Bar with slowd
        
        #show J cflat
        
        p"\"How many have you had?\""
        
        j"\"Just two.\""
        
        "She finishes her drink and I follow suit."
        
        j"\"Another for both of us.\""
        
        "The barman prepares our drinks and slides them over."
        
        p"\"Are you OK?\""
        
        j"\"Do I look like I'm OK?!\""
        
        p"\"Sorry...\""
        
        "She take a deep breath and sighs."
        
        j"\"No, {i}I'm{/i} sorry. I don't mean to take it out on you.\""
        
        show J 2YHappy_Smile with slowd
        
        j"\"Wanna finish our drinks and go somewhere?\""
        
        p"\"Like where?\""
        
        j"\"There's a park nearby!\""
        
        p"\"If you want.\""
        
        j"\"We can get some Alisay on the way.\""
        
        p"\"I'm down.\""
        
        "{i}As long as it's with you.{/i}"
        
        stop music fadeout 1.5
        
        stop environment fadeout 3.0
        
        scene black with slowd
        
        # park scene
        
        #play music "audio/music/Windy Forest.mp3" fadein 2.0
        play music "audio/music/Fruhlingsblute.mp3" fadein 2.0
        
        
        
        scene park008_night_light with slowf
        
        "We park ourselves on a bench and open our bottles; Jennifer got cherry and I got blueberry."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Cheers.\""
        
        "She holds her bottle up and I meet it with mine."
        
        p"\"Cheers.\""
        
        "We both guzzle from our bottles."
        
        p"\"Oh, that's pretty good.\""
        
        "She ignores me."
        
        j"\"May your glass be ever full. May the roof over your head be always strong.~\""
        
        j"\"And may you be in heaven half an hour before the devil knows you're dead.~\""
        
        "She delivers it with a sense of longing."
        
        p"\"What's that?\""
        
        j"\"It's an Irish blessing! Now drink.\""
        
        "I abide and drink with her."
        
        p"\"Are you Irish?\""
        
        j"\"My father's Irish, my mother was Indian.\""
        
        p"\"...Was?\""
        
        j"\"Oh, she's not dead. I just never see her.\""
        
        show J 2YSad_Sad at PCM1 with slowd
        
        "She pulls her phone from her bag and stares into it."
        
        j"\"She was supposed to be there...\""
        
        j"\"But I don't care anymore, she might as well be dead.\""
        
        "It irks me that she'd discard her mother like that..."
        
        p"\"Y'know... there'd never be a chance to see her again if she was dead.\""
        
        j"\"I don't know her. My dad's ex has been more of a mother than she ever has.\""
        
        p"\"...\""
        
        #p"\"I see...\""
        
        #"With no words I take a drink."
        
        "She takes a deep drink fom her bottle.\""
        
        j"\"It's just something else I fucked up.\""
        
        "It's unnerving to hear her say something like that."
        
        p"\"What do you mean?\""
        
        j"\"My relationships never seem to last, friends or family.\""
        
        p"\"Your friends?\""
        
        j"\"Dean and Casey must hate me for my antics—Danielle already does.\""
        
        p"\"Danielle?\""
        
        show J 2YSad_Grin at PCM1 with slowd
        
        j"\"When I found out she was making a fantasy game, I made fun of her.\"" 
        
        "She chuckles to herself."
        
        j"\"She hated it in public, so it just made me do it more...\""
        
        show JX Tears at PCM1 with slowd
        
        "A tear meets her wry smile." 
        
        "They seemed so close in class, but that tear a symbol of how far they've drifted."
        
        j"\"I miss her... I miss the times we shared growing up.\"" #best friends become strangers
        
        #"Her wistful words stab my heart for my own reasons."
        
        "Her wistful words stab my heart. I don't want to be lonely, either."
        
        show J 2YSad_Sad at PCC1 
        show JX Tears at PCC1 
        with slowd
        
        "I place my arm around her shoulder. She leans into my side; her warmth flowing into my chest."
        
        show J 2YSad_Smile at PCC1  with slowd
        
        j"\"What about you, Peter? You never mention your past.\""
        
        #"It's scary how fast her mood can change..."
        
        "My past? I struggle to define what that is. I take a swig from my bottle."
        
        p"\"...I never had one.\""
        
        "I blurt out my usual self-hatred."
        
        #"I take a sip from my bottle after blurting out my usual self-hatred."
        
        
        j"\"You never had one?!\""
        
        p"\"It's... complicated...\""
        
        hide JX Tears at PCC1 with slowd
        
        "She wipes her eyes and sniffles."
        
        #j"\"Why are we talking about this stuff? We should be enjoying ourselves!\""
        
        j"\"Like, you never grew up playing with friends?\""
        
        p"\"Not... really.\""
        
        "{i}I never grew up.{/i}"
        
        show J 2YHappy_Smile at PC1 with slowd
        
        j"\"We're gonna play a game!\""
        
        p"\"What...?\""
        
        j"\"Hide-and-seek!\""
        
        #p"\"I don't think here is the best place to play.\""
        #p"\"I don't think now's the best time to play.\""
        
        p"\"I don't think now's the best time to play. It's dark, we don't know who's about.\""
        
        #p"\"But anyone could—\""
        
        j"\"Close your eyes!\""
        
        scene black with slowd
        
        "She strokes my eye-lids shut with her fingers, whispering in my ear."
        
        j"\"If you find me, you'll get a surprise.\""
        
        "Her breathe raises the hairs on my neck."
        
        p"\"Fine.\""
        
        j"\"Count to twenty. Don't peek!\""
        
        p"\"One...\""
        
        "Her soft steps leave me alone..."
        
        "..."
        
        scene park008_night_light with slowd
        
        p"\"...Twenty.\""
        
        "I rise and scan the area. {w}{i}Empty.{/i}" 
        
        #p"\"Jennifer?\""
        
        #"I call her. No answer."
        
        #"A breeze rustles the leaves on a nearby bush." 
        
        #"I peer in but it's too dark to see."
        
        "I follow the sound of her footsteps." #and peer into the surrounding foliage but it's too dark." 
        
        "Shadows dance in the bushes; I move the leaves aside to reveal darkness."
        
        #"The leaves rustle in the wind, so I can't hear her."
        
        "The leaves rustling in the wind kill the little chance I had of hearing her."
        
        p"\"Jennifer?\""
        
        "No answer..."
        
        #"Shadows dance in the bushes; I move the leaves to the side to reveal nothing."
        
        "How far could she have gone in twenty seconds?"
        
        #"..."
        
        scene fantasy07_night_dark with slowf
        
        "It's been ten minutes and I still can't find her."
        
        #stop music
        stop music fadeout 3.0
        
        centered "{i}Something's happened.{/i}" with slowd
        
        "The thought extracts a pang of anxiety in my chest." with slowd
        
        "{i}I knew this was a bad idea.{/i}"
        
        "I pull out my phone and ring her..." 
        
        #play music "<from 65.7>audio/music/Fruhlingsblute.mp3" fadein 4.0
        
        play sound "audio/sfx/short vibrate.mp3" fadein 1.0
        #stop environment fadeout 4.0
        
        "Her ring tone calls out behind me as the call ends."
        
        
        #play music from
        #play music "<from 50.0>audio/music/Windy Forest.mp3" fadein 4.0
        
        play music "<from 65.7>audio/music/Fruhlingsblute.mp3" fadein 4.0
        
        show J 2YHappy_Grin at PC1 with slowd
        
        j"\"Did you think you'd lost me?\""
        
        "Her grin annoys me."
        
        p"\"No!\""
        
        "But relief extinguishes it."
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Would you miss me if you couldn't find me?\""
        
        "She presses herself against me, meeting my eyes with a grin."
        
        #the scent of cherry
        
        p"\"I... I'd never forget you.\""
        
        show J 2YUpturned_Grin at PCC1 with slowd
        
        j"\"Close your eyes.\""
        
        "The breath from her whisper tickles my nose."
        
        scene black with slowd
        
        "Her fingers brush over my eyelids."
        
        
        p"\"Jenni—\""
        
        #"Her lips press against mine."
        "Her lips cut me off."
        
        #"The taste of cherry invades my mouth from her tongue."
        
        "Her tongue bursts through my lips with the taste of cherry."
        
        "Our lips part, leaving me breathless."
        
        
        #show J cupturnedc #with slowd
        scene fantasy07_night_dark
        show J 2YUpturned_Grin at PCM1 
        with slowd
        
        
        "My eyes open to her grin."
        
        #You need to edit previous scenes and give signs of alcohol useage. 
        
        # act 2 #probably a continuation of act 1 XD 
        
        
        "My chest feels light, like a burden was lifted from my shoulders."
        
        "Jennifer closes my open jaw."
        
        j"\"Let's go back to the bar.\""
        
        p"\"Don't you think we've drank enough?\""
        
        #show J cupturnedc #with slowd
        
        j"\"Stop being boring, c'mon!\""
        
        
        #sprite
        #"She presses herself against me."
        
        p"\"I don't think it's a—\""
        
        scene black with slowd
        
        "Her lips cut me off again."
        
        scene fantasy07_night_dark with slowd
                
        "And just like that, I'm grounded by her hand tugging my sleeve."
        
        j"\"Let's go!\""
        
        "And my resistence is left a token."
        
        #scene change
        
        scene park002_night_light with slowf
        
        "We neck back the remainder of our bottles and put them in a bin on the way out."
        
        #scene change
        
        scene street001_night_light with slowf
        
        "A wave of euphoria washes over me. I feel on top of the world."
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        "I look to Jennifer, who returns a grin."
        
        j"\"Drunk, Peter?\""
        
        p"\"I think so... Aren't you?\""
        
        j"\"A little.\""
        
        p"\"Is that why you just...?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Don't think about it so much. Just have a good time!\""
        
        
        "If feel more at ease this time around. It's OK to let loose sometimes, right?"
        
        stop music fadeout 2.0
        
        "My thoughts are stopped by the bouncer asking to check our IDs."
        
        #cold funk
        
        play music "audio/music/Cold Funk.mp3"
        
        scene Bar with slowf
        
        "I notice the change in atmosphere as we enter; the music has changed in both genre and volume, the tables are filled with bubbling patrons, and there's a space cleared  for a small dance floor, which nobody is using."
        
        "We manage to find a table of two with seats in the crowded atmosphere."
        
        #p"\" \""
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        j"\"You ever had a tequila slammer?\""
        
        p"\"Can't say I have...\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Save my seat.\""
        
        hide J 2YHappy_Smile with slowd
        
        "She strides for the bar, my eyes and thoughts in tow."
        
        #nvl window
        
        t"{i}She kissed me...{/i}" with slowd
        
        t"Just the thought makes my heart leap again."
        
        t"There's just something so adventurous about her. I can't help but be attracted to it."
        
        t"It's like I've just recognised how much I appreciate her storming into my life with hindsight. I'd just be alone, rotting in my thoughts without her..."
        
        t"And just the thought of something more between us..."
        
        nvl clear
        window hide
        
        "A group of men laughing on the table beside breaks me from my reverie." with slowd
        
        #"Laughter from a group of men adjacent breaks me from my reverie."
        
        "The anxiety being alone in a crowded bar with nothing to keep me occupied reminds me this probably wasn't a good idea."
        
        show J 2YHappy_Smile at PC1 with slowd
        
        "But to see Jennifer shimmying through the crowd with an assortment of salt, shots, and sliced lime is a relief."
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Ready?\""
        
        "She places the tray on the table and the relief is short lived."
        
        p"\"What's this?\""
        
        "She places salt on her hand, and grabs the shot with the other."
        
        j"\"Salt, shot, then you suck the lime.\""
        
        j"\"Ready?\""
        
        "{i}Not really...{/i} I ready some salt on my hand and nod."
        
        "We give cheers and perform our ritual."
        
        "The salt and lime actually manage to make it bearable. "
        
        show J 2YHappy_Smile with slowd
        
        "Jennifer pulls the neck of my top and peers inside."
        
        j"\"Finally grown a few chest hairs?\""
        
        "I shake off the alcohol burning down my throat and release my pride."
        
        p"\"Let's get another.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"It's already on its way.\""
        
        show J 2YHappy_Smile with slowd
        
        "Her eyes rest on the approaching waiter, who places down another round of slammers and cocktails."
        
        "{i}Fuck.{/i} I'm not ready for another so soon."
        
        p"\"I can't afford to pay for so many drinks.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Don't worry! It's on me.\""
        
        "{i}It's alright to let loose sometimes, right?{/i} I mock myself."
        
        #"As alchol rushes over my senses, I'm beginning to think it might just be OK."
        
        scene Bar with slowf
        
        "As alchol rushes over my senses, I lose the constant feeling of anxiety I'd gotten used to."
        
        "{i}Everything will be OK.{/i} Somehow, I believe it."
        
        #"I sway forward and catch my temple in my palm."
        
        "I sprawl over the table and catch my temple in my palm."
        
        #"I lean my head in my hand and stare at Jennifer with a stupid smile on my face."
        
        #"I lean my head in my hand and stare at Jennifer, a stupid smile seizing my lips."
        
        #"An urge rises in me to kiss her again."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "As I look at Jennifer, an urge rises in me to kiss her again."
        
        j"\"You OK, Peter? Had too much?\""
        
        p"\"I'm fine.\""
        
        p"\"I just don't know what I'd be doing without you.\""
        
        show J 2YSad_Flat at PCM1 with slowd
        
        "She shoves me and I sway back."
        
        j"\"You'd probably do better without me.\""
        
        "Jennifer's  answer rolls off like water from a duck's back."
        
        p"\"If I hadn't met you, I—\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"Let's do another slammer!\""
        
        #timeskip
        
        scene white with slowd
        scene Bar with longd
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"Put your hands on my hips.\""
        
        j"\"Don't act so awkward, you've lifted me by my butt before.\""
        
        "She delivers it with a wink."
        
        "I loosen up and she wraps her arms over my shoulders."
        
        j"\"We'll make a dancer of you yet.\""
        
        p"\"I might just enjoy it, yet.\""
        
        "I flow with Jennifer's movements, each movement stimulating. I want to put my hands on her rear but I fear a reaction, either from her, or myself."
        
        "My hands move towards her rear naturally as her hips sway."
        
        stop music fadeout 3.0
        
        scene white with slowd
        scene school_out003_night_dark with longd
        
        "She peeks around the corner to see if a guard is stationed at the front gate."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "She stumbles back and slants her finger across her lips."
        
        j"\"Shh!\""
        
        p"\"I wasn't... speaking.\""
        
        j"\"We're gonna have to climb over the wall.\""
        
        #timeskip
        
        scene school15_night_dark with slowf
        
        "She pushes my butt up as I pull myself up."
        
        p"\"Shouldn't you go first?\""
        
        j"\"But you have t' catch me on the other side.\""
        
        #timeskip
        
        scene white with slowd
        scene black with longf
        
        #blackscreen
        
        "My brain thumping against my skull stirs me into consciousness."
        
        "I beg for sleep to return but my bladder protests."
        
        "My arm is numb; I try to lift it and it slumps over the side of my bed."
        
        "Realising I'm so close to the edge I roll back onto something warm and soft..."
        
        #open eyes
        
        scene room_boy16_day with slowd
        
        "{i}Jennifer!{/i}"
        
        "I lift her arm off of me and slide out of bed, catching myself on my desk."
        
        "{i}What the hell happened last night?{/i}"
        
        p"\"Jennifer?\""
        
        "..."
        
        p"\"Jennifer?\""
        
        "I poke her arm and she stirs."
        
        j"\"Mmmmm.\""
        
        p"\"Jennifer?\""
        
        "I shake her arm and she snatches it away."
        
        j"\"Mmmmmmmmmm!\""
        
        p"\"Jennifer?\""
        
        j"\"Fuck off.\""
        
        p"\"You're in my room... \""
        
        "She snuggles into the quilts and ignores me."
        
        #"She snuggles into the quilts and ignores me."
        
        "I can't help but take note of her bare leg poking from from under the sheets, and her stockings, skirt, and shirt scattered across the floor..."
        
        "I put my shorts and a T-shirt on and head to the bathroom."
        
        #bathroom
        
        scene room_bath01_day with slowf
        
        "After appeasing nature, I measure myself in the mirror."
        
        "{i}Did we do it?{/i}"
        
        "What if she's... {w}{i}pregnant?{/i}"
        
        "{i}I forgot everything...{/i}"
        
        "I watch the colour drain from my cheeks."
        
        "My stomach churns, and salivia fills my mouth."
        
        "{i}I'm gonna throw up.{/i}"
        
        "I hug the toilet and hurl into the bowl."
        
        #"I hug the toilet and exhale the contents of my stomach into the bowl."
        
        #kitchen
        
        scene room_kitchen06_day with slowf
        
        #"I'm just glad I emptied my top end before my bottom."
        
        "My head is in pieces."
        
        "I need to get it together."
        
        "I down a glass of water, but it glides over my cotton mouth."
        
        "I pour another for myself and one for Jennifer."
        
        
        #bedroom
        scene room_boy16_day with slowf
        
        "She's sprawled across the bed with her eyes closed. Her chest riding on her breath is the only sign of life."
        
        "It's pleasant to see Jennifer so peaceful."
        
        "It gives me a moment of calm to approach her."
        
        p"\"Jennifer?\""
        
        "..."
        
        "I shake her shoulder."
        
        p"\"I got you a glass of water.\""
        
        "She stretches and rubs her eyes."
        
        j"\"I feel fragile.\""
        
        p"\"Me too, I'm never drinking again.\""
        
        "She bursts into a fit of laughter."
        
        j"\"That's what they all say.\""
        
        "She sits up and snatches the glass from my hand, downing the water in continuous gulps." 
        #She sits up and snatches it from my hand, before downing it in continuous gulps."
        
        p"\"...You're welcome.\""
        
        j"\"Thanks, I needed that.\""
        
        p"\"You told me to fuck off.\""
        
        "She giggles."
        
        j"\"Sorry, I'm tired!\""
        
        p"\"Morning's nothing. It resides under my boot.\""
        
        "I imitate her hyperbole in a high-pitched voice."
        
        j"\"I'm not wearing my boots.\""
        
        p"\"That not...\""
        
        "I can only laugh after being defeated by such logic."
        
        "She begins fumbling under the quilts and looking around the room."
        
        j"\"Where are my clothes?\""
        
        p"\"Along the side of the bed, here.\""
        
        "She looks at me expectantly."
        
        p"\"I'll give you some space.\""
        
        #hallway
        scene hospital03_day with slowf
        
        "I stop playing a game on my phone and check the time again. It's been ten minutes."
        
        "I tap on my door."
        
        p"\"Hey, are you decent?\""
        
        "Her voice muffled through the door."
        
        j"\"Yeah, come in.\""
        
        #room
        scene room_boy16_day with slowd
        
        show J 2YHappy_Smile at PC1 with slowd
        
        "She's stretching as I enter; although she claims to feel rough, she certainly doesn't look it. She's even managed to sort her hair out in that small amount of time."
        
        #show J cnormal with slowd
        
        j"\"Damn, can't believe I lost my key again. They're gonna kick up a fuss…\""
        
        p"\"Regular occurrence?\""
        
        "A wry chuckle is her response."
        
        j"\"Well, kinda...\""
        
        j"\"They're gonna know I've been drinking.\""
        
        p"\"You're old enough, right?\""
        
        j"\"Yeah, it's just frowned upon.\""
        
        "She looks guilty for a brief moment before regaining her energy."
        
        j"\"I know the perfect remedy for a hangover, if you wanna join me after?\""
        
        p"\"Yeah, sure. Anything to get rid of this.\""
        
        "Her tongue brushes over her teeth."
        
        j"\"And I need to go and brush my teeth and get a shower.\""
        
        p"\"Yeah, same.\""
        
        j"\"I'll see you later!\""
        
        p"\"Later.\""
        
        hide J 2YHappy_Smile with slowd
        
        "..."
        
        
        #"I fall in to thought as she leaves. My bed calls me like a gravitational force."
        
        "My bed calls me like a gravitational force."
        
        "I wrap myself in my sheets."
        
        "Her scent makes my heart leap. I can almost feel her warmth against me."
        
        t"Fuzzy memories of last night resurface. {i}She kissed me.{/i}" with slowd
        
        #flashback in gray
        
        t"What does that mean? When I'm to meet her later, how am I supposed to regard her?"
        
        t"As my friend? A lover? {w}{i}A plaything?{/i}"
        
        
        t"The feelings of her lips against mine makes me wish for a happy ending." 
        
        window hide
        nvl clear
        
        #flashback
        
        scene white with slowd
        
        scene flashback 
        show J 2YHappy_Smile at PCC1
        with slowd
        
        "I try to plant a kiss on her lips."
        
        scene flashback2 
        show J 2YSad_Sad at PCC1
        with slowd
        
        j"\"I told you not to?\""
        
        "I manage to kiss her cheek and loll my heavy head."
        
        scene white with slowd
        
        scene room_boy16_day with slowd
        
        #custardian
        
        #flashback
        
        "{i}I tried to kiss her... {w}she rejected me...{/i}" #with slowd
        
        t"Then why'd she kiss me to begin with?" with slowd
        
        #"Does she not see me that way? What did that kiss mean?"
        
        t"Does she not see me that way?"
        
        t"{i}Who would?{//i}"
        
        t"I wring my bed sheets up by my chin."
        
        window hide
        nvl clear
        
        p"\"I'm so fucking cringe.\"" with slowd
        
        "{i}What even possessed me to do that?{/i}"
        
        "I'm not sure I'm even ready to face her after that."
        
        "It feels worse than this hangover."
        
        "I should really go and get that shower..."
        
        scene room_boy16_day with slowf
        
        # time skip
        
        "I throw my towel in the washing pile; I'm surprised Jennifer didn't mention how large it's getting."
        
        "I wouldn't have left my room this way if I knew she was staying over."
        
        "{i}20 20 hindsight.{/i}"
        
        #"And in the same thought, I didn't expect to wake up next to her with a hangover and... no memory... of falling asleep with her."
        
        "I don't know if I can face her... I just hope that she doesn't remember."
        
        "I keep thinking to text her and call it off. I don't even know where she wants to go. I don't want people to see me with how bad I feel right now."
        
        "My phone's screen lights up suggesting I've missed a call and I take it from my bedside table."
        
        "Three missed calls and a message, \"Im on me way!\""
        
        "That was five minutes ago—"
        
        #knock
        play sound "audio/sfx/soft knock.mp3"
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "Jennifer barges into my room before my response."
        
        p"\"Hey! I could've been naked.\""
        
        
        j"\"You're not, you're ready. Let's go!\""
        
        #"I get the feeling the only thing that'd matter to her if she walked in on me naked, is the fact I wasn't ready when she arrived."
        
        "If I had been naked, I get the feeling the only thing that would matter is I wasn't ready in time."
        
        #restaraunt.
        
        play music "audio/music/bensound-tenderness.mp3"
        
        scene restaurant03_day with slowf
        
        "We sit ourselves down at a table."
        
        j"\"What you gonna get?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\"Dunno.\""
        
        j"\"Don't you know the cure to a hangover?\""
        
        p"\"No...\""
        
        show J 2CHappy_OpenSmile at PCM1 with slowd
        
        j"\"An English breakfast!\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "I nod in satisfaction."
        
        p"\"Now that does sound good.\""
        
        j"\"The coffee here is like oil, too.\""
        
        p"\"That... not so much.\""
        
        j"\"In a good way; it's probably too strong, but it will keep you fueled on a hangover.\""
        
        #time skip
        scene restaurant03_day with slowf
        
        "I fill my toast with bacon, sausage, and egg, and enjoy as much as my mouth can bite."
        
        "I finish my mouthful with satisfaction, and notice Jennifer is shovelling mushrooms on her toast with a fork."
        
        p"\"Really? You use your toast to eat mushrooms?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"I love mushrooms on toast! And bacon and sausages are so tasty on their own.\""
        
        p"\"It looks how I feel, like death on toast.\""
        
        j"\"You don't like mushrooms?!\""
        
        p"\"Not really. \""
        
        "Her fork sweeps up a portion of my mushrooms before I can respond."
        
        p"\"That will cost you a sausage!\""
        
        "I try to reach in but she's on guard."
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        j"\"Arsehole! You don't even like 'em.\""
        
        p"\"You could put them back.\""
        
        j"\"No.\""
        
        "She eats them on her next slice of toast."
        
        "It doesn't feel in character to play with her, but I can't  help return her playful nature."
        
        p"\"Look how much you already have! What don't you like?\""
        
        j"\"I like everything.\""
        
        p"\"Fine.\""
        
        hide J 2YUpturned_Smile with slowd
        
        "I tend to my plate until hear the crunch of toast."
        
        "At this point, I'm too committed to the role."
        
        show J 2YHappy_Flat at PCM1 with slowd
        
        j"\"Hey!\""
        
        "Crumbs explode from her lips as I swipe a sausage from her plate and bite into it."
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        j"\"This is war!\""
        
        "She forks a piece of bacon before I can block her with mine."
        
        p"\"Not the bacon!\""
        
        "I swipe back a piece of hers but the waiter approaches."
        
        
        
        w"\"Can you please calm down. You're disturbing our other patrons.\""
        
        show J 2DMellow_Smile at PCM1 with slowd
        
        "People glare from nearby tables."
        
        "I share a glance with Jennifer."
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"I want a sausage back. You don't even like mushrooms!\""
        
        "They both glare towards me."
        
        p"\"Fine.\""
        
        show J 2YUpturned_Smile at PCM1 with slowd
        
        "I pull my face as she takes a sausage from my plate."
        
        j"\"Sorry, sir. We won't cause any more disturbance.\""
        
        p"\"Sorry.\""
        
        "He accepts our apology and resumes a neutral countenance."
        
        w"\"No problem. Can I get you anything else?\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        "Her grin lets me know I'm in trouble."
        
        j"\"We'll take two Sicilian lemon ciders.\""
        
        w"\"Certainly.\""
        
        "The waiter writers it down and strides to the bar."
        
        p"\"Sicilian lemon cider? What could go wrong?\""
        
        j"\"What couldn't go right? Haven't you heard of hair of the dog?\""
        
        p"\"No.\""
        
        j"\"The cure is from the hair of the dog that bit you.\""
        
        "I shoot a confused brow at her."
        
        p"\"And?\""
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        j"\"If you've got a hangover, another drink is the cure.\""
        
        p"\"I thought an English breakfast was the cure, and oil coffee?\""
        
        j"\"This is step three!\""
        
        "I had always noticed my uncle would return smelling of alcohol and women's purfume. I'd begun to despise it."
        
        "Yet here I am, already about to drink again after telling myself I wouldn't drink again, for a girl."
        
        show J 2DMellow_Flat at PCM1 with slowd
        
        j"\"Peter?\""
        
        p"\"Hm?\""
        
        j"\"You don't need to drink again if you don't want, y'know?\""
        
        "I shrug."
        
        p"\"It's fine.\""
        
        "And my reflexive answer seals my fate."
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        "The waiter reappears right on cue and places down the cloudy yellow liquid."
        
        #j"\"Cheers.\""
        
        #p"\"Cheers.\""
        
        #"This time I have nothing."
        
        "We follow our ritual of giving cheers and each have a deep drink."
        
        p"\"Wow. That's actually really good.\""
        
        show J 2YUpturned_Grin at PCM1 with slowd
        
        j"\"What could go wrong?\""
        
        
        
        #Need to fill here
        
        scene restaurant03_day with slowf
        
        
        "This goes down way too easy."
        
        "Despite how ill I felt this morning. I'm climbing back on top of the world."
        
        #
        
        show J 2YHappy_Smile at PCM1 with slowd
        
        p"\"Jennifer... what happened last night?\""
        
        j"\"What do you mean?\""
        
        p"\"I mean... we slept together...\""
        
        j"\"Don't make it sound like that! I couldn't let you sleep on the floor in your own room...\""
        
        "Before my frozen mind can answer, she delivers."
        
        j"\"You're truthful. Whether you know it or not, it's written on your face.\""
        
        "Her assessment leaves me reeling for a retort."
        
        j"\"I trust you.\""
        
        p"\"Thanks...\""
        
        "How much it means to hear that after last night... and all I can think about is why didn't she kiss me back?"
        
        "I just don't understand. Could I trust myself enough to make her happy?"
        
        "I just pray she doesn't remember that part of last night herself. "
        
        "She measures me and speaks."
        
        j"\"I had fun last night. I have fun when I'm with you. So don't worry yourself so much.\""
        
        "I couldn't defeat this smile if I tried."
        
        
        
        #p"\"stop\""
        
        #j"\" \""
        
        #p"\" \""
        

        
        
        
        #They seemed so close in class, but that tear a symbol of how far apart they've drifted.
        
        #Can we go get food now? I'm starving.
        
        #"Pepper's is still open if we hurry!"
        
        #bensound sexy scene XD
        
        
        #Damn, I didn't even drink much and I made that commitment.
        #
        
        
        #do you mention that here or for another scene?
        #you could even have, "even though she says that, I can't help wonder whether they'd be good together."
        
        scene black with slowd
        
        centered "Thanks for reading! Be sure to check out the other route segments and bad ending."
        
        #centered "Feel free to leave feedback at Facebook.com/NamelessNoun"
        
        centered "Please be patient for the credits, there's also a .txt file."
        
        call credits from _call_credits
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    label Jen2n:
        
        p"\"I never wanted to...\""
        
        #j"\"...\""
        
        show J mflatc with slowd
        
        #Her bottom lip pulls up into a smile that wavers on her lips."
        
        "Her lips waver and fall flat."
        
        #p"\"...\""
        
        j"\"I can't force you...\""
        
        j"\"Thanks for at least trying it out.\""
        
        "She twines her hair around her finger."
        
        j"\"I'll see you around.\""
        
        hide J mflatc with slowd
        
        p"\"Bye...\""
        
        "I'm left feeling guilty. I shake what could've been from my head and saunter back to my room."
        
        
        jump Jen1n2
        
        #scene black with slowd
        #centered "Scroll back and click yes! <3"
        #centered "The next click will take you back to the menu... >.>"
        #return
        
        #Everyone heads in to get changed and I'm left to wait for Jennifer. 
        
        #The scent of coconut fragrance lingers in my nostrils. I get a last whiff as I hand her towel back.
        #Thanks. 
        #So, Peter, you should come out with us! 
        #She shakes my shoulders.
        #C'mon! You always look so down.
        #(yes/no)
        
        #next day in class she'll add you on FaceAP. 
        
        #they say the way to a man's heart is through his stomach.
        
        #Then I'm yours. 
        
        #I devour the wrap and realise my Freudian-slip.
        #I take a bite and realise my Freudian-slip.
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        #Sarahr Danieller
    label Jen1n:
        
        stop music fadeout 5.0
        
        #"I find myself rubbing the back of my neck."
        "My hand glides to the nape of my neck."
        
        p"\"I... er... I'll pass.\""
        
        show J 2YSad_Sad at PC1 with slowd
        
        #"Her lips fall flat for a moment and perk back up."
        "Her lips fall flat and waver in the corners."
        
        j"\"Hey, that's OK. If it's not your thing then...\""
        
        #"Awkward silence ensues."
        "Her sentence wanes into silence."
        
        "She searches through her lush hair and curls it around her fingers."
        
        j"\"I'll see you around, Peter.\""
        
        show J 2YSad_Smile at PC1 with slowd
        hide J 2YSad_Smile at PC1 with slowd
        
        "She flashes a smile and turns back to her chair."
        
        #hide J cflat with slowd
        
        p"\"Bye...\""
        
        #"I can't help feel bad. She looked dejected."
        "I'm struck by a pang of guilt."
        
        "She looked dejected. I didn't think she'd place so much weight on me coming."
        
        #bedroom scene
        #scene 
        
        jump Jen1n2
        
    label Jen1n2:
        
        scene school02_day with longf
        
        "Another day in school, no attention paid. I'm beginning to wonder why I attend."
        
        
        
        #"Jennifer didn't speak to me today." 
        
        "Jennifer greeted me from afar this morning. It seemed a little strange."
        
        "At least she isn't pestering me to swim, it saves me the guilt of saying no again."
        
        "But my stomach slumps with the passing thought. I hope I didn't upset her." #Her greetiings helped me early class."
        
        scene room_boy16_day with longf
        
        "But what do I do now? Having too much free time isn't good." 
        
        "Nothing to distract me..."
        
        "The mind is the worst enemy when left alone with it for too long. {w}Something I know all too well."
        #speaking from experience. 
        #something I know all too well.
        
        "I scan over my room, knowing I won't get shit done." #But it buys me a little time from my wondering mind"
        
        "Inevitably, my mind wanders to my parents... {w}Sarah's picture."
        
        "I wonder what Sarah's doing."
        
        "She knocked on off her own back to show me that picture. I didn't think she'd acknowledged my question." #I didn't think she had taken me seriously."
        
        "I have an urge to knock on her room."
        
    menu: 
        
        "Knock on":
            jump Sar1y
            
        "Don't knock":
            jump Sar1n
        
        #(yes/no)
        
    label Sar1y:
        
        "I could knock on her room; she did knock on mine."
        
        #corridor
        scene hospital03_day with slowd
        
        #bang sfx
        
        "I find myself on the corridor, rapping my fist on her door."
        
        #"As the footsteps approach I freeze, what do I have to say?"
        "The shuffle of footsteps makes me freeze. What do I say?" 
        #my heart freeze
        
        "She had a reason to knock on…"
        
        #msuic
        play music "audio/music/bensound-enigmatic.mp3"
        
        "The door creeks open and she peers through the opening. Her eyes widen." #stands in
        #"The door creeks open and she peeps through the opening with widening eyes." #Her eyes widen."
        
        s"\"Hey.\""
        
        p"\"Hey… Sarah. What are you doing?\""
        
        s"\"N-nothing...\""
        
        "My brain spins its wheels for something to say."
        
        p"\"Er… I was wondering… if you wanted to do something?\""
        
        s"\"Like what?\""
               
        p"\"I don't know...\""
        
        "Blood rushes to my cheeks."
        
        s"\"…\""
        
        #hide sprite
        
        stop music fadeout 2.0
        
        "She shimmies back into her room and closes the door."
        
        "{i}Did she just reject me?{/i}"
        
        "..."
        
        #"Should I just go back to my room?"
        
        
        show S 2DSad_Flat at PC1 with slowd
        
        "I'm about to turn when her door creeks open again. She emerges with her pad and a set of pencils."
        
        show S 2YCalm_Flat with slowd
                                        
        
        
        "There's an awkward moment of silence as our eyes meet."
        
        p"\"Er… where are we going?\""
        
        #Do you want to join me? 
        
        play music "audio/music/Kevin_MacLeod_-_Dream_Culture.mp3" fadein 5.0
        
        s"\"The... field? It’s nice today.\""
        
        
        "I crack a smile."
        
        p"\"Sounds good.\""
        
        show S 2AAnxious_Smile with slowd
        
        "Her eyes drop and a smile tugs on her lips. I follow her lead."
        
        
        #scene outside
        scene school16_day with slowd
        
        #What about Peter's anxiety to make convo? The art covers for this? 
        
        #"Sunlight rests on my skin like a warm blanket."
        
        "The field is empty, we walk into it with no aim so I sit down."
        
        #"She takes her shoes and socks off and plants herself across from me."
        
        show S 2YSad_Smile at PCC1 with slowd
        
        "She takes her trainers and socks off and plants herself across from me."
        
        "A cool breeze brushes through the grass and meets us. It extracts a satisfying shiver from me."
        #the scent of fresh cut grass. 
        p"\"Do you come out here often?\""
        
        show S 2YAnxious_Smile at PCC1 with slowd
        
        s"\"Sometimes...\""
        
        "I can see why, it's secluded from the main grounds."
        
        s"\"Would you like...?\""
        
        #"She hands me her spare pad and a piece of paper to rest on it."
        "She holds out her spare pad and a piece of paper to rest on it."
        
        
        p"\"Thanks.\""
        
        s"\"What do you want to draw?\""
        
        p"\"I'll just try to draw the buildings and trees in the background.\"" #field and trees
        
        s"\"Start with basic outlines. Then…\""
        
        p"\"Then?\""
        
        s"\"Well... you should find what works for you. That's just how I'd do it.\""
        
        p"\"Thanks. I'll give it a try.\""
        
        scene school16_day with slowf
        
        "I spend half an hour rubbing out and redrawing the outline." #It's frustrating, but it feels good now I'm happy with the outcome."
        
        "And still my trees look like deformed clouds, my buildings look like squares and spikes, and the dirt patch looks like a pond."
        
        #"It's frustrating."
        "I sigh and lie it in front of me."
        
        show S 2YCalm_Smile at PCC1 with slowd
        
        s"\"That's not bad. You should start working on the details now.\""
        
        "Not bad? It's terrible."
        
        p"\"...I don't know where to start.\""
        
        show S 2YSad_Smile with slowd
        
        #"She flips to a blank page in her pad. I watch in anguish as sketches an outline better than mine in no time." #even adding detail."
        
        "She flips to a blank page; I watch in anguish as she sketches an outline better than mine in half the time."
        
        #with ease 
        
        
        s"\"Like this...\""
        
        "She adds lines and dots that accentuaute each area, windows on buildings, grains of dirt on the patch and branches and foliage on trees."
        
        show S 2YCalm_Smile at PCC1 with slowd
        
        p"\"Thanks. I'll give it a try.\""
        
        #hide S 2YCalm_Smile with slowd
        
        scene school16_day with slowf
        
        "It looked so easy. I can't get anything right."
        
        #"She adds braches and foliage to the trees and windows
        
        #have peter rubbing it out and redoing it? 
        
        #"I look back into my piece with a 
        
        #rip up that scene where she draws it better than you in no time. XD
        
        #"I keep trying to detail the trees, but even with full concentration I can't compare to Sarah's rapid detail."
        
        "I give up on my drawing."
        
        #sky
        scene sky003_day with slowd
        #nvl
        
        #t"I lie back and clasp blades of grass between my fingers." with longd
        t"I lie back and sieve blades of grass through my fingers." with longd
        
        #t"Sunlight bathes my skin, but a wave of grey clouds approach in my peripheral." #I bathe in the sunlight
        
        t"Sunlight rests on my skin like a warm blanket, but a wave of grey clouds approach in my peripheral."
        
        #I lie back and gaze into the sky
        
        t"It hasn't rained in a while—not since I arrived."
        
        t"Sarah's scratching and trees sighing leave me lost in thought."
        
        t"I can feel her presence. My usual thought patterns falter with Sarah here beside me." 
        
        #I can't deny I enjoy her placid company."
        
        t"{i}I want to know more.{/i}"
        
        window hide 
        nvl clear 
        
        #"I can feel her presence. It's the first time she's seemed relaxed."
        
        #"My usual thought patterns falter with Sarah here beside me." 
        
        
        
        #"I peek over."
        #back to normal view
        
        scene school16_day 
        show S 2DSad_Smile at PCC1
        with slowd
        
        
        #"From my sideline view I find myself comparing her to a surgeon making an incision, every stroke performed with immense concentration and precision."
        
        "From my sideline view she's like a surgeon making an incision, every stroke performed with immense concentration and precision."
        
        #"She's glued to that sketchbook. It piques my curiosity why she's not in the art club." 
        
        "I've seen her once without that sketchbook." # It piques my curiosity to why she's not in the art club."
        
        "Does she have any friends? I've not seen her with anybody."
        
        #I've seen her more with her sketchbook than 
        #It's like her only friend is that sketchpad. 
        "It piques my curiosity to why she's not in the art club."
        
        "Wouldn't that be a good place to draw and make friends?"
        
        "Is she too shy to join?"
        
        stop music fadeout 3.0
        show S 2YCalm_Smile at PCC1
        with slowd
        
        "She peeks up from her pad and catches me staring."
        
        #s"\"Aren't you...?\""
        
        s"\"Are you... OK?\""
        
        p"\"Oh, er... yeah.\""
        
        s"\"Finished?\""
        
        p"\"N-no, I was just observing...\""
        
        p"\"...The landscape, I mean.\""
        #I feel the need to add. 
        show S 2DSad_Smile at PCC1 
        show SX Blush
        with slowd
        "I feel the need to add. She flusters and delves back into her drawing."
        
        "I shut my mouth and do the same."
        
        #"Why do I feel obliged to carry on?"
        
        
        #Maybe merge her helping you into this and then skip to the clouds. 
        
        
        
        #And she's glued to her sketch pad
        #"She stirs as the sky turns orange."
        
        
        #"Instead of the sun setting, the clouds roll in."
        
        #clouds have rolled in
        
        
        
        
        
        #"just as I'd gotten into it..."
        
        
        #forshadowing what's about to come. 
        
        play music "audio/music/Kevin_MacLeod_-_Clean_Soul.mp3" fadein 3.0
        scene school16_cloud with slowf
        #scene sky002_cloud with slowf
        
        #"The clouds roll in." 
        
        "I improve it by merging the buildings and trees into darkness. Who needs detail when the weather is on your side?"
        
        #"Rain droplets hit my arms and face, pulling me from the picture."
        "Rain droplets leave dark spots on the paper, pulling me from the picture."
        #"Rain droplets hit my arms and leave darkened spots on my paper."
        
        #The trees and buildings merge into darkness. 
        
        #scene school16_cloud with slowd
        
        p"\"It's spitting.\""
        
        #show S slook with slowd
        show S 2DSad_Flat at PCC1 with slowd
        
        "She lifts her attention from her sketch for a moment."
        
        s"\"...A little longer.\""
        
        "She shivers and goosebumps ascend the back her neck."
        
        #I can see goosebumps trailing up beneith her sleeves. (arms)
        
        
        play environment "audio/background/Rain.ogg" fadein 5.0
        scene sky002_rain with slowd
        #hide Sarah     
        "I look to the ominous sky and rain starts pelting my face."
        
        "As if my very gaze conjured its wrath."
        #aggravated
        scene school16_rain with slowd
        
        "I hoist myself up with a grunt—didn't realise how relaxed I was."
        
        #"Sarah shuts her pad."
        
        "A curious smell emanates from the patch of ground."
        
        p"\"What's that smell?\""
        
        show S 2DSad_Flat at PCC1 with slowd
        
        s"\"Petrichor.\""
        
        #"It's like the word was pulled from her throat."
        "It's like the word was plucked from her lips."
        
        p"\"Hm? What's that?\""
        
        show S 2YAnxious_Flat at PCC1 with slowd
        
        "She looks up with widening eyes, as if she's made a faux pas."
        
        s"\"The smell of rain on soil after a dry period. I... like it.\""
        
        p"\"Me too. And I like that you know that.\""
        
        show S 2YCalm_Smile with fastd
        hide S 2YCalm_Smile with slowd
        
        "A chuckle escapes her lips and she opts to get ready."
        
        #"A chuckle escapes her lips and she turns away."
        #"Her lips twist into a smile and scrunch flat."
        
        #p"\"Anyway, aren't your feet getting wet?\""
        
        #s"\"Yeah...\""
        
        #"She gets herself ready and we rise."
        
        show S 2YCalm_Smile at PM1 with slowd
        
        s"\"...We should head in.\""
        
        #"She's already off and I'm left to catch up."
        
        "A fleeting thought strikes me: I ask Sarah about the art club?"
        
        #"A strange pang strikes me: an urgency to ask Sarah about the art club."
        
        #"It feels like a fleeting chance to do so."
        
        #choice 2 
        
        #her fingers search her fringe, as if contained answers. 
        #Searching her fringe for an illusive answer. 
        
    menu: 
        
        "Ask":
            jump Sar2y
            
        "Don't ask":
            jump Sar2n
        
        # stop music after each option
        
    label Sar2y:
        
        p"\"Hey... Sarah?\""
        
        show S 2YAnxious_Open at PM1 with slowd
        
        s"\"Hm?\""
        
        p"\"How come you're not in the club?\""
        
        stop music fadeout 3.0
        show S 2AAnxious_Flat with slowd
        
        s"\"I... I'm just not.\""
        
        "Her pace picks up."
        
        #"I convince myself it's the rain rather than my question."
        
        p"\"Is it because people will see your art?\""
        
        s"\"It's not that...\""
        
        "She stops and musters a breath." #rain trickling from her hair."
        
        show S 1AAnxious_Flat with slowd
        
        s"\"I had joined before, but...\""
        
        "Her sentence wanes into silence." 
        
        "Was she alone? {w}{i}She's alone now...{/i}"
        
        #"The sad glint in here eyes and the rain trickling from her hair compel me."
        
        "Rain trickles from her hair."
        
        #Because I'm scared of being alone too.
        p"\"What if I joined? Would you join with me?\""
        
        ##The sad glint in here eyes and the rain trickling from her hair compel me."
        
        
        #"It just seems like the only way I can spend time with her."
        #"It just seemed like the only way I can spend time with her."
        
        #It reminds me of Jennifer's attempts to recruit me."
        
        show S 1YAnxious_Open with slowd
        
        "She reels back, as suprised as I am."
        
        "{i}What am I saying?{/i} I don't think I've ever taken an interest by the quality of my picture."
        
        #"It reminds me of Jennifer's attempts to recruit me."
        
        s"\"You... want to draw?\""
        
        #Her stern tone makes the question twice as heavy. < Save for later? Would me and Sarah fall apart without the rivet of art? 
        
        "I muster a breath and voice my decision."
        
        p"\"Yeah...\""
        
        show S 1YAnxious_Flat with slowd
        
        "Her tone falls flat."
        
        s"\"Meet me outside the dorms. Tomorrow, after school.\""
        
        show S 1AAnxious_Flat with slowd
        
        "She lowers her head and steps back."
        
        s"\"I... I need to go.\""
        
        hide S 1YSad_Flat with slowd
        
        #"She shoots off, following the wall of the building."
        "She shoots off, following the perimeter of the school buildings."
        
        p"\"Wait, Sarah.\""
        
        "She doesn't turn to look."
        
        s"\"I'll see you tomorrow.\""
        #Go the way we came, I have to go. I'll see you tomorrow.
        
        #
        #"I want to follow her, but she seems like she wants to be alone."
        
        
        #when she showed me where the shop is."
        
        
        #"It'd explain our walk to the shops."
        
        #"Why is the art club a touchy subject?"
        
        "Was that a yes?" 
        
        "Only tomorrow will tell."
        
        #another thing she's done when I asked. I think she really is afraid to say no.
        #fade into another scene? :p
        
        scene black with longf
        centered "Sarah Act 1"
        
        stop environment fadeout 2.5
        scene school_out002_day with longf
        
        "After a day in class to think about it, I'm nervous. I have no stake in art."
        #put the art in fart. 
        "I'm envious of Sarah's sense of purpose when she's drawing, and yet, she doesn't seem to want to join herself."
        
        show S 2DSad_Flat at PC1 with slowd
        
        "The door creeks open behind me to reveal Sarah."
        
        #"She seems evasive when I mention the art club. She did the same on our walk to the shop now that I think about it. " 
        
        #"I can't tell. She seems evasive anyway."
        
        
        p"\"Hey.\""
        
        s"\"Hey. Let's go...\""
        
        "Her eyes don't meet mine."
        
        scene school_in004_day 
        
        show S 2DSad_Flat at PC1
        
        with slowf
        
        #p"\"Sarah, we don't have to join, y'know?\""
        
        "She remains silent, head still bowed." #It's like a final walk on death row."
        
        "There's a sense of determination about her strides, but the worried look on her face makes me uneasy."
        
        #"Sarah stops outside the room and my momentum pushes her inside."
        "Sarah stops outside the room and my momentum sends us tumbling inside."
        
        scene school08_day 
        
        show S 2YAnxious_Open at PC1
        
        with slowf
        
        #Maybe Sarah will run off here? 
        
        p"\"Sorry!\""
        
        show S 2AAnxious_Flat with slowd
        
        s"\"It's...\""
        
        
        #"Her voice tremulous, giving way on her mid-sentence. It's not hard to see why when all eyes are on us."
        
        "Her voice stolen by a sharp breath. It's not hard to see why when all eyes are on us." #taken inhale
        
        #"The classroom erupts into a din of whispers. The air is palpable and the glances pierce." #it's disquieting."
        
        "The classroom erupts into whispers. The air is palpable and the glances pierce." #it's disquieting."
        
        hide S 2AAnxious_Flat with slowd
        
        "Sarah lowers her head and strides for a seat at the front." #I follow with cautious steps."
        
        #"As I follow, I catch a few coherent sentences from the whispers."
        
        "As I follow, I catch a few coherent sentences from the din."
        
        pp"\"Is that...?\""
        
        pp"\"It can't be.\""
        
        po "\"Sarah?\""
        
        pp"\"Yeah, the girl from last year.\"" 
        
        "I miss the rest as we make it out of ear shot."
        
        pl"\"Did you hear what happened?\""
        
        "The girl leans over and whispers in her friend's ear."
        
        "Is this why she was evasive at the mention?"
        
        "Come to think of it, she shut off when I mentioned it on our walk to the shops too."
        
        "I had mistaken it as shyness."
        
        "She slumps over the desk and buries her face in her arms. I trudge through knee deep guilt and sit beside her. "
        
        "The people sat across from us keep shooting glances, as do the rest of the class."
        
        "But the din falls into silence."
        
        "My question's answered when I turn to the doorway, where a lanky, ageing man with dark, shaggy hair observes the room." 
        
        "His gaze comes to a stop on me and Sarah." #before pin pointing on us."
        
        q "\"I see we have new faces in the class. Are you here to join up, or are you here for a taster?\""

        #"I catch Sarah startle at his voice and speak up."
        
        "Sarah startles at his voice so I speak up."
        
        p"\"Y-yes, Sir. We're here to join.\""
        
        mrt "\"Good, I'm Mr Thatcher. Can I get your names.\""
        
        "His words questioning, but his voice demanding."
        
        p"\"I'm Peter, this is—\""
        
        mrt"\"Let her speak for herself, you have already answered once for her.\""
        
        "His gaze shifts to Sarah."
        
        mrt"\"Can you address me properly, please.\""
        
        #"As I look around the classroom, I feel the mounting pressure on Sarah. All eyes are on her."
        
        "I glimpse around the room, feeling the mounting pressure on Sarah."
        
        #"My introduction was nerve-racking; I can't imagine how somebody as shy as Sarah must be feeling under more strain."
        
        "Shock sweeps across his face as Sarah lifts her head. A smile lightens his stern features."
        
        #"Shock sweeps across his face before a smile lightens his stern features."
        
        "He strides to his desk without a word, and jots what I assume are our names down on the clipboard."
        
        "He then waltzes to the front of his desk and claps his hands together."
        
        mrt "\"Right then, class. Today we are going to be doing an imaginative exercise.\""
        
        
        mrt "\"I want you to all draw something that you think represents yourself.\""
        
        mrt "\"This can be something you like, or something that is important to you. Abstract or concrete.\""
        
        mrt "\"You can use any equipment and style that you like, as this adds to the representation of yourself.\""
        
        mrt "\"We'll be starting our projects soon. So take the opportunity to practice now and in the coming weeks.\""
        
        "With that said, he sits down and picks out a large stack of paper from his drawer, holding them at different angles and distances as he examines each one."
        
        "We wait for the class to get up and take their desired equipment, before picking out a few pencils."
        
        "I'm not sure why we have more than one; I just copy Sarah and follow her back to our seats."
        
        "I glance around, everybody looks either deep in thought or they're setting to work on the outlines of their representation."
        
        #"I think Sarah's started, but I can't quite tell as she's huddled over her work, examining it closely." 
        "Sarah's huddled over her paper."
        
        "A tactical manoeuvre I imagine, to hide her work from prying eyes such as mine."
        
        "I notice that every now and then she glances over to the door, it gives me the impression that she wants to escape." 
        
        "I feel lost as I stare down at the piece of paper, it already represents me as it is." 
        
        "Blank."
        
        "I almost consider handing it in, but I don't fancy two trips to Mr Adams' office in a week."
        
        "I place a curved line on the page. {w}Then another." 
        
        "Before I know it, a face is forming."
        
        "The resemblance is uncanny, even through my inept execution." #as I draw the curly hair. Even if it is badly drawn."
        
        #"My mother."
        
        "With the picture of my mother coming into fruition, I huddle over my work like Sarah." 
        
        "This is a part of myself I'd rather others wouldn't see, with the possibility of them asking questions."
        
        scene school08_evening with slowd
        
        "I'm enjoying this more than I thought I would. It's therapeutic."
        
        "I carry on trying to refine it, but it never seems to turn out right. Most of the time it turns out worse than before, which is frustrating."
        
        "Mr Thatcher stands in front of his desk and clears his throat."
        
        mrt "\"Ahem, if I can get your attention.\"" 
        
        "The whole class sit up at attention."
        
        mrt "\"The class has finished for today, do what you like with your pictures.\""
        
        mrt "\"As I said earlier, your projects will start soon, so get in as much practice as you can in the meantime.\""
        
        "I take one last look at my picture before folding it into a square and pocketing it." 
        
        "I can't say that I'm happy with it, but I'm glad that I did it."
        
        scene school_in004_evening with slowf
        
        "I can't help but question to myself about the whispers and Mr Thatcher's reaction."
        
        p"\"So... how come you left the art club?\""
        
        "Nor can I stop myself from asking, it seems."
        
        #show S mnormal2 with slowd
        show S 2DSad_Flat at PC1 with slowd
        
        s"\"I... I was busy.\""
        
        "It's obviously a lie. I'm not about to pick her up on it, though."
        
        scene hospital03_day
        
        show S 2AAnxious_Flat at PC1
        
        with slowf
        
        s  "\"How was... your first lesson?\""
        
        
        
        "I jolt in surprise as she breaks the silence."
        
        p "\"It was good. I enjoyed it, even if I'm bad at it.\""
        
        #s "\"You're not that bad.\""
        
        show S 2YAnxious_Flat with slowd
        
        s "\"Can I... take a look?\""
        
        "I find myself hesitant with the roles reversed. I now see how hard it can be to just reveal a part of yourself like that."
        
        p "\"Only if... I can see yours too.\""
        
        #"She debates it internally for a few moments."
        
        "Her features debate my proposal." #it internally for a few moments."
        
        show S 2AAnxious_Smile with slowd
        
        s"\"O...K.\""
        
        show S 2YAnxious_Smile with slowd
        
        s"\"But... I want you to wait in the corridor when we view them.\""
        
        p"\"Why's that?\""
        
        show S 2AAnxious_Flat with slowd
        
        s"\"...\""
        
        "It's clear that she isn't going to make her reason apparent, so I accept her terms. It's better for me too." 
        
        "There's a final urge to decline, and not risk her asking questions... but I will have to reciprocate if I expect her to open up."
        
        hide S 2AAnxious_Flat with slowd
        
        "I wait until she's in her room and unfold her drawing."
        
        window hide
        nvl clear
        
        t"The shading is impeccable, contrasting with the thick lines that shape the layers of gloomy clouds across the top, and the deciduous trees that roam along the edges." with slowd
        
        t"A desolate path forms through the middle. The only bit left untouched, is a lonesome unshaded silhouette." 
        
        t"Standing alone amidst the storm and yet, not actually there."
        
        t"A poignant reminder that we're both loners." #Not by choice either, at least in my case. I wonder about Sarah."
        
        t"I can see why art appeals to somebody like Sarah. She can express herself to people without being in their presence."
        
        window hide
        nvl clear
        
        "Her door creeps open behind me." with slowd
        
        show S 2AAnxious_Smile at PC1 with slowd
        
        s"\"She's... beautiful.\""
        
        "She whispers wistfully."
        
        p "\"How could you even see that through my awful drawing?\""
        
        show S 2YSad_Flat with slowd
        
        s "\"It's really... not that bad.\""
        
        p"\"Yours puts mine to shame.\""
        
        "She takes one last look and then we exchange back our pieces."
        
        show S 2YAnxious_Flat with slowd
        
        s "\"Can I... ask who she is?\""
        
        p"\"It's my mother, I...\""
        
        "Stop myself from going too far."
        
        show S 2YSad_Flat with slowd
        
        s "\"I see...\""
        
        "I knew I wasn't ready, yet I still showed it to her." 
        
        p"\"I'll see you around, Sarah.\""
        
        show S 1YSad_Flat with slowd
        
        s"\"B-bye.\""
        
        "Her lips part again, but words fail to form."
        
        
        scene room_boy16_evening with slowf
        
        "I hide behind my door incase they do."
        
        "{i}Why did I show her?{/i}"
        
        "I made it so much more obvious with my hesitance. Now she knows something's wrong. Now she's going to want to pry."
        
        "I muster a deep breath and relax with my exhale."
        
        "The woman in the picture captures my eye."
        
        "This woman is an angel in my dreams. Maybe she was once an angel in my life. But now all I can hear is her ear-piercing scream."
        
        
        #"I tear it to shreds and slump onto my bed."
        
        
        #Look at yourself like a canvas, you get to create who you want to become. 
        
        #My apology draws the glances of everyone in the room. 
        
        #Sarah's face
        
        #FACKDASFSDGNBFDXGJKD 
        
        play music "audio/music/bensound-straight.mp3" fadein 3.0
        
        scene office10_day with longf
        
        a"\"Peter! Good to see you again.\""
        
        "His flourish becoming an annoyance; I force a smile as I take the seat."
        
        a"\"How are things?\""
        
        p"\"Good.\""
        
        a"\"I'm glad to hear.\""
        
        "He clasps his hands and rests his elbows on his desk."
        
        a"\"My sources tell me you've joined the art club, convincing Sarah no less.\""
        
        p"\"I did...\""
        
        a"\"I'm impressed. I've been asking her for some time.\""
        
        "This draws a real smile from me."
        
        p"\"Yeah, but I'm not sure how well I fare with art.\""
        
        a"\"Do you enjoy it?\""
        
        p"\"I can't say I don't.\""
        
        a"\"Then isn't that what matters?\""
        
        "I shrug." 
        
        "His brow furrows as he assesses me."
        
        a"\"I'll tell you what I can about Sarah, if you listen to my advice.\""
        
        "He assesses me too well. I accept his terms with a nod."
        
        a"\"Sarah is avoidant. She's had more than a few problems because of this in her life, and here is no different.\""
        
        "How can I be so self obsessed? Of course she has problems. I'm not the only one with a cross to bear."
        
        "I've been ready to drop this whole art club thing."
        
        p"\"Can I ask what problems?\""
        
        a"\"I must clarify that I can't speak much about Sarah, confidentiality, but I'll tell you what I can.\""
        
        a"\"But I want you to promise me something.\""
        
        p"\"What?\""
        
        a"\"That you will speak with me, honestly.\""
        
        
        "I inhale and nod once again."
        
        "I've already said too much to Sarah. As far as I know, she may tell him about my reaction to the picture."
        
        a"\"Sarah had a friend. A friend that moved away close to the time she stopped attending the art club.\""
        
        a"\"I also know art is her passion. If you're able to help her stick it out, I'd be grateful.\""
        
        p"\"Thank you.\""
        
        "He looks to me expectantly. Awkward silence lingers..."
        
        "Damn, I expected more."
        
        p"\"I... I've been having dreams.\""
        
        "His brow tilts."
        
        #Obviously he's intrigued from the earlier scene
        
        a"\"What about?\""
        
        p"\"My...\""
        
        "The word sticks in my throat."
        
        p"\"...Parents.\""
        
        a"\"Do you miss them?\""
        
        "This question brings my own brow to tilt."
        
        "I can't tell whether he knows they're dead..."
        
        "Does he know I can't remember...?"
        
        p"\"That's the thing... I can't remember them.\""
        
        "His eyes squint in confusion."
        
        "Apparently not..."
        
        #a"\"Were you seperated from them when you were young?\""
        
        #p"\"No...\""
        
        p"\"...I can't remember anything past about a year ago.\"" #replace this with a date?
        
        "I kick myself for dropping my guard, but I can't rationalise why I'm so guarded."
        
        #a"\"I see...\""
        
        "He acknowledges me with a, \"hm,\" and scribbles down his thoughts as expected."
        
        #a"\"So you don't remember anything of your parents?\""
        
        #"His eyes search mine."
        
        #a"\"What happened?\""
        
        
        
        a"\"And you don't remember anything of your parents?\""
        
        p"\"No, nothing.\""
        
        "His scribbling stops as his eyes search mine."
        
        a"\"What are your dreams about?\""
        
        "{i}I've already passed the event horizon.{/i}"
        
        "I run through the details of my dreams and give some context..."
        
        stop music fadeout 3.0
        
        scene office10_day with slowf
        
        a"\"So it was only recent that your dreams took a dark turn?\""
        
        p"\"Yeah.\""
        
        a"\"Do you remember anything from before the accident?\""
        
        p"\"I can't remember anything since I woke up in that hospital bed.\""
        
        "His scribbling comes to an end."
        
        a"\"I originally instructed this for the betterment of Sarah, but I believe she will more than better you, too.\""
        
        a"\"As for you, I think you may be suffering from anxiety. Your dreams strangely signify PTSD.\""
        
        a"\"I can offer antidepressants.\""
        
        "My face contorts at his offer."
        
        #a"\"Don't get me wrong, I'm not trying to say you're depressed. Or that you're crazy, or whatever people say.\"" 
        a"\"Don't get me wrong, I'm not trying to say you're crazy. Or anything else you've heard.\"" 
        
        a"\"Antidepressants are a viable solution to anxiety.\""
        
        a"\"I can manage a prescription, but only if you agree.\""
        
        "I wave his offer away and head for the door."
        
        p"\"I'll think about it. Thanks.\""
        
        a"\"Wait, I also want to speak to you about--\""
        
        stop music fadeout 3.0
        
        #scene school4_evening with slowf
        scene school4_day with slowf
        #change this ffs
        
        #"How come I have never told anyone until now? Why'd I give it up so easy to Mr Adams?"
        
        #"I can hear him calling out about further information about
        
        "I've had as much as I can take for one day."
        
        "The curdling in my stomach makes me feel like I've just made the biggest mistake of my {i}new life.{/i}"
        
        "I think back to all those times I'd asked about my parents. My uncle would shut off every time, revealing so little."
        
        "I stopped enquiring before long. It was easier to leave that life buried."
        
        
        "Either way, my lungs are lighter having spilled my dreams." #My breath at ease in the first time in memory."
        
        "I take what solace I can from his confidentiality."
        
        #"Why did I tell him?"
        
        #"I can only take solace in confidentiality."
        
        
        scene school08_day with longf
        
        "I arrive and sit myself in the same seat as last time."
        
        show S 1AAnxious_Smile at PM1 with slowd
        
        "As the class enter, Sarah sits down beside me again."
        
        show S 1AAnxious_Smile at PC1 with slowd
        
        "We match an awkward nod and smile."
        
        hide S 1AAnxious_Smile with slowd
        
        "Beneath the table, her fingers clasp into her thighs."
        
        "It looks painful." 
        
        "As painful as thinking of our last encounter. It feels so awkward now."
        
        "Mr Thatcher clears his throat and relays instructions."
        
        #Her hand submerges beneath the desk and clenches her thigh. The tension present from our last talk.
        
        scene school08_evening with slowf
        
        "The lesson ends. We haven't spoken a word."
        
        "The class leave; I remain in hesitation."
        
        "It'd be too awkward to walk back together."
        
        
        scene school_in004_evening with slowf
        
        "As I leave, Sarah is talking to some girls from the club. Our gazes catch and I turn away."
        
        #"After telling Mr Adams everything, I've squandered every opportunity to speak to her..."
        
        #"Since my last interactions with her and Mr Adams, I've distanced myself." 
        
        "Since my last interactions with her and Mr Adams, I've distanced myself from everyone." 
        
        scene room_boy16_evening with slowf
        
        #"Night beckons the sun." 
        #Is this that night? ;s Even I don't know XD 
        "Having spent the week practising, the novelty of art has quickly faded."
        
        t"I stare out the window to the waning sun." with slowd
        #"I'm not as good as I thought I was. Sarah's encourgement only went so far, and I seem to be getting worse."
        t"I'm not as good as I thought I was. Sarah's encourgement feels a mile away now."
        
        t"I've been trying to improve my technique, looking up guides and watching videos on the internet."
        
        t"Watching people create art I'd be proud of—and to them, this is just a tutorial..."
        
        t"I clench my fist; the pencil's nib tears into the paper and snaps."
        
        t"Is this really for me? Why did I sign myself up for this…?"
        
        window hide 
        nvl clear 
        
        "{i}Sarah.{/i}" with slowd
        
        "If I hadn't asked her to join, we'd have no reason to speak." 
        
        "{i}Not like we speak anyway.{/i}"
        
        "I keep kicking myself for not speaking to her in the lesson."
        
        "I've asked her to join and have been distant because of my own problems."
        
        #"This rivet of art is holding us together. But… {w}I want more. I want to know her..."
        
        scene hospital03_day with slowd
        
        "I find myself outside my door, trying to build the courage to knock on her room again."
        
        "I don't know what to say. Maybe I could ask her to come out again."
        
        "She always seems to say {i}yes{/i}."
        
        "Is she really afraid of saying no? I chuckle to myself at how cute that is."
        
        #"But my amusement ends with a twinge at the whole mystery surrounding the art club."
        
        "But my amusement ends with a twinge at the whole art club situation."
        
        "Between the lessons and what Mr Adams said, something is clearly off."
        
        play sound "audio/sfx/soft knock.mp3"
        
        "Here goes..."
        
        #knock sound
        
        "My knocks leave me frozen to the spot, again."
        
        #"Her head pops out from the opening."
        "Her eyes peek from the opening."
        
        #sprite
        
        p"\"Hey... I'm sorry to disturb you. I was just wondering if you wanted to do something?\""
        
        "My wordy greeting is met with a smile."
        
        s"\"...Like what?\""
        
        "I manage a queasy smile and a shrug."
        
        s"\"I... sometimes go to the forest...\""
        
        p"\"Won't it be too dark soon?\""
        
        s"\"We... could go to the park.\""
        
        p"\"Sounds like a plan.\""
        
        "We share an awkward chuckle. But I couldn't be happier that she's accepted."
        
        scene school_out003_night_light with slowf
        
        "The stars protrude from the sky, signifying the clearest night since I've been here."
        
        "The cold air stings my nostrils, giving me an idea."
        
        p"\"Hey, we should get a coffee. Pick a place and I'll pay. Sound good?\""
        
        show S 2AAnxious_Smile at PM1 with slowd
        
        "She nods and leads."
        
        scene park002_night_dark with slowf
        
        "We saunter into the park in silence, it's not awkward though."
        
        scene park008_night_dark 
        
        show S 2AAnxious_Smile at PM1 
        
        with slowf
        
        #"When it comes down to it, the only subject we've had is art."
        
        "I carry our drinks on a cardboard drink holder."
        
        p"\"Wanna sit down somewhere and drink these?\""
        
        p"\"It would kinda defeat the purpose if they cooled down.\""
        
        "She chuckles and nods."
        
        "A smile rests on her lips as we park ourselves on a nearby bench." 
        
        #show S 2AAnxious_Smile at PC1 with move
        hide S 2AAnxious_Smile with slowd
        
        t"With our small amount of force-talk, I'm no longer optimistic about our outing." with slowd
        
        t"Sarah's more guarded even than me. I don't know how to approach her."
        
        t"When it comes down to it, the only subject we've had is art. And I know nothing."
        
        t"But I can't say that I dislike her placid company."                 
        
        #"I wonder what Sarah thinks about me...?" with slowd
        
        "{i}What does Sarah think about me...?{/i}" with slowd
        
        nvl clear 
        window hide
        
        #"I wonder what Sarah thinks about me." with slowd
        
        play music "audio/music/Fruhlingsblute.mp3" fadein 3.0
        
        window hide 
        nvl clear 
        
        scene Sarah CG eyes open down with longd
        
        "But when I look at her, she's lost in her own world."
        
        "Her lips flicker as her gaze sweeps across the night sky. It's like a ritual, as if she's counting or naming the stars."
        
        p"\"I... take it you like the stars?\""
        
        #show S mFsmile with slowd
        
        scene Sarah CG eyes open smile with slowd
        
        "She breaks from her reverie with a smile."
        
        s"\"Yeah, I... like nights like this.\""
        
        
        #show S cSsmile with slowd
        
        
        t"Though her smile is sweet, her eyes glint with melancholy." with slowd
        
        t"It was what I had come to expect from her. I had gotten used it to the point that it took a smile to make me realise."
        
        t"She takes her beverage from the holder and gives thanks, cupping it in her hands and taking a sip." #with slowd
        
        t"I follow suit, the warmth sends goosebumps up my arms. The joint steam of our drinks and breaths dissipate into the night."
        
        window hide
        nvl clear
        
        p"\"I'd sometimes to go down to a park near my uncle's house; the stars were prevalent in the countryside.\"" with slowd
        
        "My words dissipate in the air, as if the breeze blew them away."
        
        s"\"What...\""
        
        "She whispers, trailing off as quickly as she began."
        
        p"\"Hm?\""
        
        #show S cFsmileHBH with slowd
        
        "She takes a deep breath, as if it was the courage to breathe the words."
        
        s"\"What do you... think about when you look at the stars?\""
        
        "The question stumps me. I feel like I've been put on the spot, as though it could decide my grade for a test."
        
        scene sky006_night_light with slowd
        
        "I realise the truth will suffice."
        
        p"\"Back then? It was a beautiful night. I stared for hours, reflecting on my life, wondering what my place is in all this...\""
        
        "Or at least partial truth, I'd also asked myself {i}why didn't I die in that crash?{/i}" 
        
        "That night... {i}I wished I had.{/i}"
        
        #"That night... I'd wished I did."
        
        #That night, I'd wished I had # I wish I did.
        
        
        #"Or at least partial truth, I also wondered whether or not I should've died in that crash." 
        
        #"Or at least partial truth, that night I'd wishd I died in that crash..." 
        
        #"That night, I... wished I had."
        #"Or at least partial truth. I also wondered why I survived, and whether or not I should've died."
        #"Or at least partial truth. I also wondered why I survived, and grieved for nothing in particular."
        
        #"Now, I'm smiling to be sat next to someone."
        
        #"My reality crashed into my consciousness—an empty loss of people I no longer knew, a happiness I'd forgotten and the loneliness that consumed me."
        
        #s"\"I... used to view them from my auntie's back garden. It was one of the places I could be alone.\"" 
        
        
        scene Sarah CG eyes open down with longd
        
        s"\"I... used to view them from my auntie's back garden. It was one of the places I could be alone.\"" 
        
        s"\"I could lose myself, knowing there was so much more out there...\""
        
        
        #s"\"It makes your problems feel so insignificant.\""
        
        "Her fingers wind around the bench as she gazes into the stars."
        
        s"\"I would... wonder if there was other life out there. There could be something looking into its own night sky, wondering the same thing as me...?\""
        
        #"I chuckle at her nebulous thoughts. My laughter evokes a blush."
        "I chuckle at her far out nebulous thoughts, evoking a blush."
        
        p"\"I wouldn't argue against it—it could be possible.\""
        
        #show S cFsmile with slowd
        
        scene Sarah CG eyes towards down with slowd
        
        "I'm met by an intrigued gaze that wills me to continue. My mind runs dry."
        
        #show S cFsmileHBH with slowd
        
        scene Sarah CG eyes open down with slowd
        
        s"\"Do you think... there's other life out there?\""
        
        "But it seems she can’t contain her inquisitive nature or I my chuckle."
        
        p"\"There's an estimated two-hundred-billion galaxies in the observable universe, each containing a billion or so stars.\"" 
        #p"\"There's an estimated two trillion galaxies in the observable universe, each containing a billion or so stars.\"" 
        
        #p"\"Then consider each star can harbour a multitude of planets...\""
        
        p"\"Then consider each star can harbour multiple planets...\""
        
        #show S cshock with slowd
        
        #hide S cshock with slowd
        
        scene Sarah CG eyes open smile with slowd
        
        #"Her jaw drops a measure. She takes in the night sky, awe renewed." 
        
        "A smile perches on her lips. She takes in the night sky, awe renewed." 
        
        "I imagine the sky as a canvas in her mind."
        
        #We couldn't even communicate with them in our lifetime with the limitations of light. 
        
        s"\"Observable universe?\""
        
        p"\"Think of it like the horizon, but it's at the point where space is expanding away from us faster than light can reach us.\"" 
        
        s"\"How do you know?\""
        
        p"\"Heh. Let's just say I had the time on my hands to watch more than a few space documentaries.\""
        
        #p"\"But yeah, it's probable.\""
        
        scene sky006_night_light with slowd
        
        t"Our conversation dries up. I follow her gaze into the sky, a lazy smile resting on my lips." with slowd
        
        t"It's funny, this is the last conversation I thought I'd have here. Hell, I had doubts that I would make a friend at all."
        
        t"The few annoying drama shows I watched were all I had to go off. They didn't prepare me for school, never mind this."
        
        t"Then again, Sarah seems different anyway. I can't place my finger on her."
        
        scene Sarah CG eyes towards smile with slowd
        
        window hide
        nvl clear
        
        #show S cnormal with slowd
        
        "I'm drawn to her movements in my peripheral. She lowers her cup and catches my gaze." 
        
        s"\"Where do you think everything came from?\""
        
        "I contain my snort and brandish a smile."
        
        p"\"Nobody knows. The big bang is the theory accepted by the majority in the scientific community.\""
        
        #"She gives it some thought."
        
        scene Sarah CG eyes open down with slowd
        
        "Her head tilts and her lips scrunch up."
        
        #" and her gaze is sharp enough to pierce physical reality"
        
        #s"\"So if it's true, everything we see was once the same point as you and me?\""
        #s"\"So if it's true, we were all once the same point in space?\""
        s"\"So if it's true, we were all once the same point?\""
        
        p"\"Yeah, I guess so...\""
        
        p"\"Never thought of it like that before.\""
        
        #show S cHBBS with slowd
        
        "She responds with a smile. It's not forced either, nor was this topic."
        
        t"Which strikes me as strange in itself; just asking for her name caused her discomfort and she's comfortable talking about this?" with slowd
        
        t"Her strange musings perpetuate my own. My impressions of her have been shattered."
        
        t"And I was confused enough to begin with."
        
        #t"My coffee finishes with a final swill."
        
        t"I finish my coffee with a final swill."
        
        window hide
        nvl clear
        
        p"\"Finished?\"" with slowd
        
        s"\"Yeah.\""
        
        p"\"Wanna go for a walk?\""
        #p"\"Fancy a stroll?\""
        
        #show S mFsmile with slowd
        
        "She smiles and rises."
        
        scene Sarah CG eyes towards smile with slowd
        
        scene park004_night_dark with slowf
        
        "The wind whispers through the tops of the trees."
        
        "She's still pensive, gazing into the sky—I can't help smile at how relaxed she is."
        
        s"\"Wouldn't it have been easier for there to have been nothing?\""
        
        p"\"I guess not... We're here, aren't we?\""
        
        s"\"True...\""
        
        #custard - nothingness or meaninglessness. 
        
        p"\"Why, does the thought of nothing scare you?\""
        
        s"\"Sometimes... {w}Sometimes it comforts me.\""
        
        p"\"I... think I can agree there.\""
        
        "It's satisfying to see her smile, even at relating to a depressing revelation."
        
        "I check my phone, 10pm."
        
        p"\"Should we head back? It's getting late.\""
        
        #s"\"Sure.\""
        
        "She answers with a nod."
        
        scene street001_night_dark with slowf
        
        t"She remains pensive as we make our way back—as am I." with slowd
        
        t"As far as my goals go, this was a success, but nothing like I'd imagined it."
        
        window hide
        nvl clear
        
        show S 2ACalm_Flat at PC1 
        show SX Blush at PC1 
        with longd
        
        
        s"\"Peter?\"" #with slowd
        
        "Her whisper breaks me from my thoughts."
        
        p"\"Hm?\""
        
        show S 1AAnxious_Flat with slowd
        
        s"\"Do you think... I'm weird?\""
        
        "I can't help chuckle. I would consider her out of the ordinary, to say the least."
        
        p"\"Yeah, a little.\""
        
        "Realising she could take my answer and laughter the wrong way, I’m quick to amend myself."
        
        p"\"But not in a bad way, it's refreshing.\""
        
        show S 1ACalm_Smile with slowd
        
        "She blushes and lowers her head, but I can see the smile tugging on her lips. It's contagious."
        
        show S 2DSad_Smile with slowd
        
        "She composes herself with a new air of confidence."
        
        s"\"Would you like... to come for a walk in the forest sometime?\""
        
        show S 2YCalm_Smile with slowd
        
        "She shoots an anxious glance from behind her fringe."
        
        "Does she think I'd say no?"
        
        p"\"Sure, sounds good.\""
        
        show S 1ACalm_Smile with slowd
        
        "She releases a sigh, smile beaming on her lips."
        
        "This is the first time Sarah has offered to do something with me, off of her own volition."
        
        "The thought leaves a smile on my lips for the journey home."
        
        
        
        #(Make a segue into forest)
        
        
        
        #Sarah knocks on your room
        
        stop music fadeout 3.0
        
        scene room_boy16_day  with longf
        
        "Dammit—even after copying tutorials—I still can't get her eyes right."
        
        "I have to keep trying..." #I sigh and rub it out. 
        
        play sound "audio/sfx/soft knock.mp3"
        
        "A knock disturbs me. I sigh and drop the pencil."
        #knock sfx
        
        
        
        scene hospital03_day 
        
        show S 2DSad_Flat at PC1
        
        with slowd
        
        "I open the door and a smile seizes my lips."
        
        p"\"Hey, Sarah.\""
        
        show S 1AAnxious_Smile with slowd
        
        "Sarah perks up and greets me with a nod."
        
        s"\"...Would you like to come to the forest?\""
        
        p"\"Sure!\""
        
        "The fact she's followed through with this..."
        
        p"\"Give me a moment to get ready.\""
        
        scene hospital03_day with slowf
        
        "When she turns to lead the way, a worn looking satchel hangs from her back."
        
        play music "audio/music/A Wish to the Sky.mp3"
        
        #play music "audio/music/Fr/xfchlingsbl\xfcte ?????-  Sad & Beautiful Piano.mp3"
        
        
        scene forest008_day with longf
        
        "As we reach the steps, she relaxes with a deep breath."
        
        #"It all feels surreal; the air is fresh, the subtle melodies of the birds, the trees swaying in the pleasant afternoon breeze." #, and the girl next to me to keep me company
        
        "It all feels a little surreal. The air is fresh; the birds sing subtle melodies; the trees sway in the afternoon breeze." #, and the girl next to me to keep me company
        
        "It all brings with it a carefree smile to my face."
        
        scene forest002_day with slowf
        
        "The sun creeps through openings in the canopy. Specs of dust dance in the rays of light."
        
        #"Sarah watches a pair butterflies revolve around each other up into the canopy."
        
        "She slows, a gentle smile resting on her lips. I follow her gaze to see two butterflies flying in circles together."
        
        "She imbues the simple things with a sense of wonder."
        
        #"Her shoulders loosen as we walk the trail, and her hands relax by her sides. The carefree smile still rests on her lips." 
        
        #"I find myself smiling at the sight."
        
        #thoughts here?
        
        #"As we're getting further into our trek, I notice her looking at the floor more than usual, which is strange due to the fact that she doesn't seem to be anxious."
        
        "All of a sudden she stops and brushes away some leaves. She picks up a stone and inspects it before slipping it into her satchel."
        
        p"\"What are you doing?\""
        
        show S 2AAnxious_Smile at PC1 with slowd
        
        s"\"Collecting pebbles.\""
        
        "I'm not exactly sure what to say to that—it's a stone—but I feel a need to keep the conversation going."
        
        p"\"Is it a hobby of yours?\""
        
        show S 1AAnxious_Smile with slowd
        
        s"\"Well... kinda.\""
        
        p"\"Ah... cool.\""
        
        "But quickly run out of things to say."
        
        t"Although I do enjoy her placid company, it's hard to appease my curiosity of her." with slowd
        
        t"It's like there's a wall around her, and every time I seem to remove a brick, she replaces it with another."
        
        t"It only adds to her mysterious nature. I'm fascinated to learn more about her, her past, and her… {w}memories."
        
        t"Yet, I'm too scared to ask as she will most likely expect me to reciprocate."
        
        t"Contrition settles in my stomach when I realise I'm hiding behind my own wall."
        
        t"It makes me question {i}my{/i} part in this—how can I expect her to open up if I'm holding out myself...?"
        
        "My thoughts put a downer on my good mood; one thing I could say that I'm consistently good at." with slowd
        
        #"It puts a bit of a downer on my good mood; one thing I could say I'm consistently good at." with slowd
        
        nvl clear
        hide window
        
        scene fantasy01_day with slowf
        
        t"As we reach the reservoir, she stops and takes in the view; I follow suit." with fastd
        
        t"The placid water is like a symbol of the atmosphere, in scenery and company."
        
        nvl clear
        hide window
        
        "But it breaks as I see a movement in my peripheral, and a stone skimming across the water… four, five, six-seven-eight-nine."with slowd
        
        p"\"Woah.\""
        
        show S 2YAnxious_Smile at PC1 with slowd
        
        "I turn to her; she flashes a bashful smile and shrugs."
        
        s"\"This is why… it was kinda my hobby.\""
        
        hide S 2YAnxious_Smile with slowd
        
        "She proceeds to take out another stone and lines herself up, leaning her left leg forward and following through with a twist in her abdomen."
        
        "I hear it skim eight times, but can't take my eyes from Sarah."
        
        show S 2YAnxious_Smile at PC1 with slowd
        
        s"\"Want one?\""
        
        "I inspect the rock, noticing it's smooth, flat, and rounded."
        
        hide S 2YAnxious_Smile with slowd
        
        "I set myself up, trying to imitate her throwing posture, but I only get an initial bounce."
        
        "She hands me another."
        
        s"\"You've got the stance down, but allow it to spin off of your finger.\""
        
        s"\"Like this.\""
        
        "She demonstrate how to hold the stone, and motions how it should flick from the tip of the index finger."
        
        s"\"The spin will keep it steady when it deflects off of the water's surface.\""
        
        "I follow her advice the best I can... {w}one, two, three-four-five."
        
        p"\"Hey, did you see that?\""
        
        show S 2YCalm_Smile at PC1 with slowd
        
        "She nods and giggles sweetly, lining herself up for another throw."
        
        hide S 2YAnxious_Smile with slowd
        
        #Really old script? I can't remember the convo
        
        
        p"\"Do you do this often?\""
        
        s"\"Sometimes...\""
        
        p"\"Alone?\""
        
        s"\"The past few times...\""
        
        #p"\"And before that?\""
        
        #s"\"I used to come with my friend, but she left...\""
        
        p"\"What about those girls from the art club?\""
        
        s"\"They're... not my friends...\""
        
        "Her pebble sinks without a single skim."
        #"Her pebble submerges without a single bounce."
        
        show S 1DSad_Flat at PC1 with slowd
        
        p"\"I see...\"" 
        
        p"\"Well, thanks for bringing me.\""
        
        show S 2YSad_Smile with slowd
        
        "She matches my smile."
        
        s"\"It's nice to have company...\""
        
        "{i}I can't agree more...{/i}"
        
        hide S 2YSad_Smile with slowd
        
        "I take another stone and manage a decent throw."
        
        
        p"\"Sarah?\""
        
        s"\"Yeah?\""
        
        "I fight with ways to phrase my circumstances."
        
        p"\"What... do you think's left of a person who's lost their memories?\""
        
        #"Even as we carry on skimming stones, I notice her head tilt with the thought."
        #"As we continue to skim stones, I notice her head tilt with the thought."
        "She skims a stone and tilts her head in thought."
        
        #s"\"That's hard... I'm not sure.\""
        s"\"That's hard... I think deep down they'd still be similar, but your experiences shape you.\""
        
        s"\"It reminds me of an old Russian proverb: dwell on the past and you'll lose an eye; forget the past and you'll lose both eyes.\""
        
        #nvl here?
        
        s"\"What makes you ask?\""
        
        p"\"I've just been wondering what makes people who they are...\""
        
        s"\"I'm interested in psychology, but I'm probably not the best person to ask.\""
        
        p"\"No, it's a good answer. Thank you.\""
        
        "She nods and holsters her stone."
        
        show S 1YCalm_Flat at PC1 with slowd
        
        s"\"What's your passion, Peter?\""
        
        #"My mouth opens but my brain is running circles."
        
        "Her sudden question leaves my mouth open and brain frozen."
        
        p"\"I... I don't know.\""
        
        show S 1ACalm_Smile with slowd
        
        "Her brow furrows. Her lips twist and her smile returns."
        
        s"\"Not many people do...\""
        
        t"It only makes me question myself more. {i}Is art really for me?{/i}" with slowd
        
        t"There's one thing I do know, I don't regret my decision to join."
        
        #t"I wouldn't have joined the art club under any other circumstance. I was desperate to make a friend in Sarah."
        
        #t"I wouldn't have joined the art club under any other circumstance. I was desperate to make a friend; I want to get to know Sarah."
        
        
        hide window
        nvl clear
        
        "Sarah throws another and scores eleven." with slowd
        
        s"\"That was the last one...\""
        
        "She zips up her satchel and motions to leave."
        
        #p"\"We should get going?\""
        
        stop music fadeout 3.0
        
        scene forest002_day with slowf
        
        #"I now realise how hard it is to make conversation after our correlative quietude. I find myself trying to think of something, anything to break the silence."
        
        t"I'm still pensive about her response." with fastd
        
        t"It's always been clear that I've been blind to the past, but that makes me blind to the future too?"
        
        #t"One thing does remain clear, I want to keep spending time with Sarah in the future."
        #t"One thing does remain clear, I want Sarah in my future."
        
        t"But for the first time, I'm beginning to look forward to the future."
        
        window hide
        nvl clear                               
        
        play environment "audio/sfx/Bee.mp3" fadein 3.0
        
        p "\"It's been—\"" with slowd
        
        "I'm put off by a giant bee in my peripheral, buzzing loudly by my ear." 


        "It anticipates my every move as I dodge left and right."
        
        
        p "\"Argh!\""
        
        s "\"S-stop, moving around so much!\""
        
        hide sarahsurp with slowd
        
        stop environment fadeout 3.0
        
        #"I end up running away and manage to evade the bee before making my way back to Sarah, who is… laughing?"
        
        #show sarahds at Position (xpos = 0.5, xanchor=0.5, ypos=1.3, yanchor=1.3) with slowd
        
        "I run away and manage to evade the the bee."
        
        "As I return, she covers her mouth with the back of her hand, giggling sweetly." 
        
        show S 2DSad_Smile at PC1 with slowd
        
        "In these first few weeks together, I realise that this is the first time I've seen her genuinely laugh."
        #Unable to contain her sweet giggle with the back of her hand
        "I chuckle and rub the nape of my neck."
        
        p "\"Well, I'm glad to be of some entertainment.\""
        
        p"\"But... it's been nice. Thanks for bringing me.\""
        
        show S 2YCalm_Smile with slowd
        
        "Her lowering hand reveals her smile."
        
        
        s"\"It has... Thanks for coming...\""
        
        
        #Where is she?  
        
        #I bump into Sarah and she stumbles into the room.
        #Everyone stares for a moment and the classroom erupts into a din of whispers.
        #She turns back to face me with a look of panic. 
        
        
        #She buries her face in her arms.
        
        
        
        #I feel like Jennifer here, pestering Sarah to join the art club. XD 
        
        #mention that she looks down after the mention of the art club. 
        
        #I doubt I'd find her here in the rain. (but you will XD) 
        
        
        #Mr Adams scene here or wait for the one after?
        
        
        
        #fight
        
        scene school08_day with longf
        
        #"I'm excited for this lesson. I'm excited to see Sarah again."
        
        "We've both decided to head straight to the art room; I sit myself down and wait for Sarah."
        
        #"We haven't spoken since the forest, but I feel like we've made some good ground."
        
        #show S cHBB with slowd
        
        show S 2AAnxious_Smile at PC1 with slowd
        
        "Our gazes catch and a smile seizes her lips as she turns away."
        
        #show S cHBBS with slowd
        
        #"She avoids my gaze and takes the seat beside me."
        
        p"\"Hey.\""
        
        #show S cHBBS with slowd
        
        #"A smile seizes her lips."
        
        s"\"Hey.\""
        
        "Just a small greeting is nice after our silence last lesson."
        
        #"She's a brick wall in here."
        
        #end lesson
        scene school08_evening with slowf
        
        #"The lesson is uneventful, Sarah lingers behind and I wait."
        
        "The lesson is uneventful." 
        
        "Sarah seems busy by the back, but when I make my way over she's staring into the equipment."
        
        show S 1DSad_Flat at PC1 with slowd
        
        p"\"Got any plans for your project?\""
        
        s"\"Not really...\""
        
        show S 1ACalm_Flat at PC1 with slowd
        
        "Laughter echoes in from the hallway. She stiffens and gazes toward the window."
        
        p"\"Should we go?\""
        
        "She nods."
        
        hide S 1DSad_Flat with slowd
        
        #"She turns with a nod and heads for the door."
        
        "As I make my way out, I can feel her presence dragging in tow."
        
        #She seems tense again.
        
        #projects aren't graded ffs XD 
        
        
        #corridor
        
        scene school_in004_evening with slowf
        
        
        "The laughter continues; it's the same girls I saw her speaking to after last lesson. Sarah shrinks as they approach."
        
        "The smallest girl meets us. She's blonde with a small frame and a confident strut." # sprite here
        
        q"\"Hey, Sarah.\""
        
        "There's a moment of silence as Mr Thatcher passes through."
        
        #"Her lips twist into a grin."
        
        #trouble maker?
        
        play music "audio/music/myuu - Troublemaker Theme.mp3" fadein 2.0
        
        "Her eyes narrow."
        
        q"\"Do you think coming back with a guy is going to change things?\""
        
        s"\"No... It's not—\""
        
        "Sarah's wavering voice sinks my stomach into the pit of realisation."
        
        p"\"What's going on here?\""
        
        "The girl's lips squeeze into a smirk."
        
        q"\"Sarah's not as {i}straight{/i} as she seems.\""
        
        "A red flush paints Sarah's cheeks."
        
        s"\"It's not that—\""
        
        q"\"Don't lie!\""
        
        "Sarah startles. Her outburst even catches me off guard."
        
        p"\"What business is that of yours?\""
        
        q"\"She made it my business when she kissed her in front of me.\"" # and drew those... pictures
        
        q"\"Tongues and everything.\""
        
        "Her eyes narrow at Sarah."
        
        q"\"You're a freak.\""
        
        #step in front of her? 
        
        "The scorn in her voice matched by sniggers from her friends."
        
        "Rage wells up my throat." #I'm unable able to tame my tone."
        
        p"\"You need to shut your mouth.\""
        
        "I position myself between her and Sarah, thrusting my finger in her face."
        
        q"\"Are you threatening me?\""
        
        "Sarah tugs my sleeve but I'm not about to back down."
        
        p"\"I'm warning you.\""
        
        q"\"Do you even know who I am?\""
        
        p"\"Some bitch.\""
        
        q"\"This bitch's brother will shut {i}{b}your{/i}{/b} mouth.\"" #Have "your" in italics? How?
        
        p"\"Is that why you’re a bitch? Because you can hide behind others?\""
        
        #"Her friends grab her by the shoulders."
        
        "Her friends grab onto her shoulders."
        
        q"\"C'mon, we need to go.\""
        
        #q"\"Let me go! I’m not finished here!\""
        
        #"I match her scowl."
        
        #p"\"The weakest dogs bark loudest. Because they're always calling for help.\""
        
        #"She turns for the doors with her friends in tow."
        
        q"\"Fine.\""
        
        
        
        "She looks over me with a scoff and addresses Sarah." #directs her anger towards Sarah."
        
        q"\"Go and slit your wrists. I'm sure your boyfriend will help.\""
        
        "She shoots a grin as they walk through the doors."
        
        #p"\"What a fucking bitch...\""
        
        #Rachel and Ryan. 
        
        #Sarah's reaction
        
        stop music fadeout 3.0
        
        
        "I turn to Sarah who’s burying her gaze into the ground."
        
        show S 1DSad_Sad at PC1 
        show SX Shadow at PC1
        with slowd
        
        #show S cnormal2 with slowd
        
        p"\"Are you OK?\""
        
        "She grasps her thigh and exhales."
        
        s"\"I'm sorry...\""
        
        p"\"Why are you sorry?\""
        
        s"\"...I knew I shouldn’t have come back here.\""
        
        p"\"This isn't your fault. They shouldn't treat you like that.\""
        
        #p"\"You can’t let them treat you like that. It’s not right.\""
        
        #"She doesn’t even move, so I feel a need to reassure her."
        
        show S 1AAnxious_Sad with slowd
        
        "She stiffens up, her arms tremble by her sides."
        
        p"\"Look, it'll be OK.\""
        
        "I place my hand on her shoulder, but she flinches to my touch."
        
        s"\"You… you don’t know her brother.\""
        
        #"Her queasy smile sinks my stomach into doubt. But I cast a stern tone."
        "Her quivering voice leaves me in a moment of doubt. But I cast a stern tone."
        
        p"\"Have you told Mr Thatcher about this?\""
        
        "She shifts her head to the side."
        #"She shrugs and rests her gaze to the side."
        
        p"\"What about Mr Adams?\""
        
        #"She shakes her head meekly."
        "Then the other side."
        
        p"\"You need to tell them.\""
        
        #"She unwinds and snaps toward the exit."
        
        hide S 1AAnxious_Sad with fastd
        
        "She snatches a breath and snaps towards the exit."
        
        #You can't just leave it like that? Surely.
        
        
        #corridor
        
        scene hospital03_day with slowf
        
        "I barely keep up; I'm left to watch on as she shuts her door."
        
        #knock sound
        
        play sound "audio/sfx/soft knock.mp3"
        
        p"\"Sarah?\""
        
        "..."
        
        play sound "audio/sfx/hard knock BA.mp3"
        
        p"\"Sarah?!\""
        
        "......"
        
        #"I knock again and press my ear to her door. Not a sound."
        
        #"I can't even hear a movement."
        
        "It's clear she wants to be alone."
        
        #back in your room. 
        
                                            
        scene room_boy16_evening with slowf
        
        #Should I knock on her room? He knocks on and doesn't get an answer.
        
        #"She clearly wants to be alone."
        
        "I slam my fist on the desk."
        
        t"What had they said to her after the last lesson?" with slowd
        
        t"...I just walked on by, lost in my own worries. {w}{i}Useless.{/i}" #{w}{i}Am I that blind?{/i}"
        
        t"{i}Go and slit your wrists.{/i}" 
        
        #t"{i}Go and cut yourself.{/i}" 
        
        #t"{b}{i}Go and cut yourself.{/i}{/b}" 
        
        t"It shocked me to hear her say it."
        
        t"{i}How could a human being say that to another?{/i}"
        
        t"I shudder at my naive question."
        
        nvl clear 
        window hide 
        
        scene room_boy16_night_dark with slowf
        
        t"I can't settle my mind or the anger in my stomach. I can't believe how horrible that bitch would treat Sarah." with slowd
        
        t"My palm keeps connecting with her cheek in my mind's eye, knowing I couldn't do it..."
        
        #t"What am I going to do? {w}I'll talk with Mr Adams. Surely he can help."
        
        window hide
        nvl clear
        
        #"What am I going to do?{w} I'll talk with Mr Adams. Surely he can help." #option? 
        
        #play music "audio/music/Shunt.ogg" fadein 3.0
        
        scene room_boy16_day with longf
        
        t"With  a clearer head, I brood over yesterday's events."
        
        #t"I didn't know I had it in me to defend her like that. I'm not sure I'd have defended myself like that, even."
        t"I didn't know I had it in me to defend her like that. I don't think I'd have defended myself like that."
        
        t"But the scorn she treated Sarah with... just for being... {i}different.{/i}"
        
        t"The thought resparks a pang of anger."
        
        t"Why would Sarah have joined the club again? Because of my whim?"
        
        window hide
        nvl clear
        
        "I need to talk to Mr Adams. He wouldn't have urged her to rejoin if he'd known." with slowd
        
        "But my stomach falls empty; I don't think we'd have spoken much without my whimsical choice."
        
        #"{i}Would we drift apart without this rivet of art?{/i} {w}It's a thought I've put more weight on than I realised..."
        
        "{i}Would we drift apart without this rivet of art?{/i} {w}It's a question I've put more weight on than I realised..."
        
        #corridor
        scene hospital03_day with slowf
        
        "As I leave for class, I'm caught up with an urge to knock on Sarah's door."
        
        "But what would I say? She's probably left for class anyway."
        
        
        #classroom
        scene school02_day with slowf
        
        "Just as I'm getting into the swing of schoolwork, my concentration is knocked."
        
        "Jennifer waves and glances over a few times, but she doesn't speak."
        
        #"I could've used a distraction. But I can't deny that I've pushed her away."
        
        "I could've used a distraction. But I can't deny that I've pushed her away."
        
        "{i}I push everyone away.{/i}"
        
        
        #Mr Adams room
        
        #play music "audio/music/bensound-funkyelement.mp3" fadein 3.0
        
        play music "audio/music/bensound-straight.mp3" fadein 6.0
        
        
        scene office10_day with longf
        
        "His annoying flourish a familar comfort at this moment."
        
        a"\"How can I help you?\""
        
        
        "I explain through the details to Mr Adams."
        
        scene office10_day with slowf
        
        a"\"It sounds like Rachel. She's a troublesome one...\""
        
        a"\"As for Sarah, I had expected something beyond what she had told me. I wasn't aware of the exact reason why she'd stopped attending.\"" 
        
        "He pauses in thought and releases a sigh."
        
        a"\"I had presumed it was due to Emma leaving...\""
        
        "His pensive expression insinuates he's thinking aloud as much as tellign me."
        
        #"His professional countenance slips with a pensive frown."
        
        p"\"Why did Emma leave?\""
        
        #a"\"She had to move away due to family reasons. She was very close with Sarah.\""
        a"\"Confidentiality.\""
        
        "It's not the answer I want to hear, but Sarah is the focus here."
        
        "He breaks from the screen. "
        
        a"\"The registers indicate that Sarah hasn't been in class today.\""
        
        p"\"What should I do?\""
        
        a"\"I recommend that you don't return to the art club for the time being. I will inform Mr Thatcher.\""
        
        p"\"So we're the ones being punished for it?\"" #That's bullshit.
        
        "His face stiffens, but eases as he catches my eyes."
        
        a"\"I know you're upset, but procedures must be followed. I think the best thing you can do right now is to make sure Sarah's OK.\""
        
        #p"\"But...\""
        
        p"\"But I've tried... I knocked on her room afterwards and she didn't answer.\""
        
        a"\"She would've wanted some space, I'm sure. She'll let you in when she's ready.\""
        
        "An easy smile rests on his lips."
        
        a"\"besides, I've heard you've both spent some time together outside of school.\""
        
        p"\"We have...\""
        
        a"\"I think it might be a good idea for you to go and see her.\""
        
        "{i}He's right.{/i}"
        
        p"\"But, what should I say to her?\""
        
        a"\"What have you spoken about so far?\""
        
        "A smile seizes my lips from our conversation at the park."
        
        "I don't think now's the right time to talk to her about the orgin of the universe."
        
        a"\"Your smirk assures me you'll be fine.\""
        
        a"\"Sarah's stronger than she appears. But I'm sure she'd appreciate a friend right now.\""
        
        p"\"Thank you.\""
        
        "This time, I offer him a handshake and he claps down with both hands."
        
        a"\"Believe me, I'm worried about Sarah, too. I'm glad she's found a new friend in you.\""
        
        "As I turn to leave, he calls out."
        
        a"\"Take some time with this, but please come back and talk to me about yourself when you're ready.\""
        
        stop music fadeout 3.0
        
        #office corridor
        
        #el custard
        
        
        #scene school04_day with slowf
        scene school4_day with slowf
        
        "I have a friend, Sarah." 

        "I almost smile, but I know she needs someone right now." #It's a fact best left for later consideration."
        
        #Dorm corridor
        
        #stop music fadeout 3.0
        
        scene hospital03_day with slowf
        
        play sound "audio/sfx/soft knock.mp3"
        
        "The sound of footsteps fill me with hope and apprehension." #I knock and press my ear to her door. 
        
        "I knock; the lock clicks and the door creeps ajar. She pokes her eye in the frame."
        
        s"\"H-hey...\""
        
        "She measures me, waiting for me to begin."
        
        p"\"Hey.\""
        
        "Silence constricts my lungs. She's right here, and it's like I can't reach her."
        
        p"\"Have you been to class?\""
        
        "I know the answer, but it's the only question I have."
        
        "She sinks into herself, gaze fixed on my shoes."
        
        "What confidence I had slumps into a stupor. My mouth opens, but my words are lost."
        
        "After a few tense moments, she steps from behind the door; it creeks open."
        
        "She's let me in..."
        
        #forest tune here too?
        
        #Sarah's room
        
        play music "audio/music/HeartBreaking.mp3" fadein 1.0
        
        scene european_in04_day with slowf
        
        "Her room strikes me as archaic compared to my own. But her room looks neglected; a few used plates, crisp packets, cans, and numerous paper balls are scattered across her room."
        
        "She navigates her way through the mess and sits on her bed. Her head craned towards the back wall."
        
        p"\"...Are you… OK?\""
        
        "It's painful to ask such a stupid question given the sight. I feel stranded and ashamed as I stare at her from across the room."
        
        "It takes her a few seconds for her response: a nod, and a strained smile that twists my heart."
        
        "I force myself to take the difficult first step, and make my way over to the bed. I sit down gingerly beside her."
        
        p"\"Do you want to talk—\""
        
        "My words are stolen by a shake of her head."
        
        t"Time seems to stand still in the room; I'm not sure whether I'm the cause, or if she's secluded herself in here like this since yesterday." with slowd
        
        t"There's this distinct feeling that I shouldn't be here gnawing at me..." 
        
        t"But the significance that she's let me in isn't lost on me, I'm just not sure what to do if she won't talk."
        
        #t"The significance that she's let me in isn't lost on me, but I'm not sure what to do if she won't talk."
        
        window hide
        nvl clear
        
        "The feeling that she'd be better off alone wins. I rise, frozen by a tug on my sleeve." with slowd
        
        #"The feeling that she wants to be alone wins. I rise, frozen by a tug on my sleeve." with slowd
        
        s"\"D-don't...\"" 
        
        #"Unsure of how I should react, I sit back on the bed beside her. To my surprise, she leans her head against my shoulder."
        
        "Unsure of how I should react, I sit back on the bed beside her."
        
        #t"To my surprise, she leans her head against my shoulder." with slowd
        
        t"To my surprise, she leans against my shoulder." with slowd
        
        t"Her room has clearly been neglected before this happened, none of the plates look fresh."
        
        t"I can't help think about the apathetic state I was in at my uncles." 
        
        t"I didn't care about my surroundings; I would do anything to distract myself."
        
        t"I finally form something to say, but bask in our mutual silence and relish her warmth against me."
        
        
        #t"The feeling of being needed, that I matter, is enough to make me pause and appreciate another person's touch." #with slowd
        
        #t"And as I look to her, I can't rationalise why I care about this girl beside me so much." 
        
        window hide
        nvl clear
        
        "The feeling of being needed, that I matter, is enough to make me pause and appreciate another person's touch." with slowd
        
        show S 1AAnxious_Sad at PCC1 with slowd
        
        
        "As I look to her, I can't rationalise why I care about this girl beside me so much." 
        
        "But if she doesn't want to talk, I can at least help with her surroundings." #with slowd
        
        "{i}My surroundings have often been as scatterbrained as my mind.{/i}"
        
        p"\"Hey, we should clean up.\""
        
        s"\"...\""
        
        show S 1ACalm_Sad at PCM1 
        show SX Blush at PCM1 
        
        with slowd
        
        "She blushes, levering herself from my shoulder and taking in the room."
        
        "Knowing how hard it is to get out of a rut, I'm ready to push it."
        
        p"\"Believe me, I've created worse.\""
        
        show S 1AAnxious_Smile at PCM1 with slowd
        
        "Although she chuckles, she still looks unsure."
        
        p"\"Hey, come on. It'll be a lot faster with the two of us.\""
        
        hide S cNsmile with slowd
        
        "I take the initiative and begin throwing wrappers in the bin, but it's already full."
        
        p"\"Are there any more bags?\""
        
        s"\"I think I know where some are...\""
        
        "Once she leaves, my curiosity takes over; I unravel a paper ball."
        
        t"The image within is a shaded silhouette, with a finger gun pressed to its head." with slowd
        
        t"There's one colour, the blood spurting from the exit wound."
        
        t"The paint is fresh... {w}smudged."
        
        t"Uncharacteristic from what I've seen of her work."
        
        window hide
        nvl clear
        
        "Her footsteps draw near, so I scrunch it up and throw it towards the bin." with slowd
        
        "She arrives with the bags and we tackle the room in silence." #mention about her guarding me from a particular spot
        
        #time skip
        
        stop music fadeout 3.0
        
        scene european_in04_evening with slowf
        
        "Her shoulders ease as she takes in the room."
        
        p"\"Much better, I need to do the same in my room now.\""
        
        show S 2AAnxious_Smile at PCM1 with slowd
        
        "She smirks and stares back to the floor."
        
        "But I know I can't let our mutual relaxation get in the way of the situation."
        
        p"\"Sarah?\""
        
        show S 2YSad_Open at PCM1 with slowd
        
        s"\"Hm?\""
        
        p"\"Do you want to go back to the art club?\""
        
        show S 2AAnxious_Sad at PCM1 with slowd
        
        "She shrugs and turns her head away."
        
        #s"\"\""
        
        p"\"Think about it. Will you at least go to class tomorrow?" #Mr Adams is worried about you, too.\""
        
        show S 2YSad_Flat with slowd
        
        "Her lips purse."
        
        s"\"I will...\""
        
        "She seems unsure, but there's a certain resolve in her voice."
        
        #"I'm not sure if she's agreeing to both, but there's a certain resolve in her voice."
        
        p"\"I'll see you around, then.\""
        
        hide S 2YSad_Flat with slowd 
        
        "I turn for the door."
        
        s"\"Bye, Peter.\""
        
        "As I reach the door, I turn on the ball of my foot."
        
        p"\"I'm across the way if you ever need someone to talk to. Even if you just wanna hang out.\""
        
        show S 2YSad_Smile at PC1 with slowd
        
        "The smile breaking out on her lips is more than a reward."
        
        #"The smile breaking out on her lips leaves a flutter in my stomach."
        
        s"\"Thank you.\""
        
        #hide S 2YSad_Smile with slowd
        
        scene hospital03_day with slowd
        
        "I leave her to her thoughts. I know I've got plenty more to think about myself."
        
        
        
        
        
        #incident
        
        #class corridor
        
        scene school05_day with longf
        
        #"I never did tell Sarah not to return to the art club today."
        "Despite Mr Adams' warning, I never did tell Sarah not to return to the art club today."
        
        "I was so focused on her in the moment that I completely forgot..."
        
        "She did seem doubtful, but there’s no way I can chance leaving her in the lesson by herself after what's happened."
        
        #art room
        
        scene school08_day with slowf
        
        #"I’m a little early, finding Sarah in her usual space beside mine. Mr Thatcher breaks away from a conversation with her."
        
        
        "I’m a little early; Sarah is in her space beside mine, in a conversation with Mr Thatcher."
        
        "{i}I was ready to leave if she didn't show.{/i}"
        
        "I approach as Mr Thatcher breaks away from a conversation with her."
        
        
        
        
        p"\"Hey.\""
        
        play music "audio/music/Kevin_MacLeod_-_Dream_Culture.mp3" fadein 3.0
        
        show S 2YCalm_Smile at PCM1 with slowd
        
        "Her body relaxes with a sigh. A smile breaks out on the corner of her lips."
        
        #"To see her smile after seeing her so down in her room leaves a flutter in my stomach."
        
        
        #"To see her smile again evokes a flutter in my stomach."
        
        
        "After seeing her so down in her room, her smile leaves a flutter in my stomach."
        
        s"\"Hey.\""
        
        "Her head rests a notch higher with the absence of Rachel."
        
        p"\"Got any ideas for your project?\""
        
        show S 2DSad_Smile at PCM1 with slowd
        
        "She nods as she flicks her pad open. At ease when it comes to art." 
        
        "It's a familiar view, school buildings and dorms in front of the forest."
        
        p"\"You've been on the roof?\""
        
        show S 2YCalm_Smile at PCM1 with slowd
        
        "She responds with a nod."
        
        s"\"I want to make a collage of landscapes.\""
        
        p"\"Good idea.\""
        
        show S 1AAnxious_Smile at PCM1 with slowd
        
        s"\"What are you going to do?\""
        
        "My smile yields as I scrunch my lips in thought."
        
        p"\"I… don’t know. Haven’t really thought about it.\""
        
        "All I’ve been able to think about is how Rachel treated her."
        
        "About her locking herself in her room."
        
        "About her resting against my shoulder…"
        
        #"My smile returns at the latter."
        
        show S 1YAnxious_Smile at PCM1 with slowd
        
        s"\"You could do some landscapes with me... {w}That's... if you want?\""
        
        p"\"Yeah, sure!\""
        
        p"\"I found it easier to do landscapes than... people.\""
        
        hide S cSsmile with slowd
        
        "She gives a satisfied nod as Mr Thatcher Grabs the class's attention."
        
        #{i}And I can't miss the chance to spend more time with you.{/i}"
        
        stop music fadeout 3.0
        
        
        #"Mr Thatcher Grabs the class's attention and begins the exercise."
        
        #time skip 
        
        #stop music fadeout 3.0
        
        scene school08_evening with slowf
        
        "The session wraps up, I don’t think it could’ve gone better."
        
        t"Mr Thatcher has surely intervened with Rachel, even her friends have been absent." with slowd
        
        t"I've managed to learn a better shading technique with the help of Sarah."
        
        t"And the fact Sarah's been so responsive in a lesson is a blessing in itself."
        
        window hide
        nvl clear
        
        #walking back to the rooms
        
        scene school_in004_evening with slowf
        
        p"\"Are you going to work on something later?\""
        
        show S 1AAnxious_Smile at PC1 with slowd
        
        s"\"I had just planned to go back to my room.\""
        
        p"\"When are you going to start working on another piece?\""
        
        show S 2YAnxious_Smile at PC1 with slowd
        
        s"\"I might do later.\""
        
        scene school_out009_evening with slowf
        
        p"\"Can I come if you do?\""
        
        show S 2DSad_Smile at PC1 with slowd
        
        s"\"Sure.\""
        
        p"\"Just knock on if you feel up to it.\""
        
        show S 2YSad_Smile at PC1 with slowd
        
        s"\"I will.\""
        
        #dorms
        
        scene school_out002_evening 
        
        show S 2ACalm_Open at PC1 
        
        show SX Shadow at PC1
        
        with longd
        
        "Sarah's features tighten as we reach the dorms."
        
        hide S 2ACalm_Open at PC1 
        
        hide SX Shadow at PC1
        
        with slowd
        
        #what music?
        
        play music "audio/music/myuu - Troublemaker Theme.mp3" fadein 3.0
        
        "I realise why as I follow her gaze. It's Rachel, and what I assume is her older brother."
        
        rr"\"Ryan, meet Peter.\""
        
        "Her voice loaded with malice."
        
        "A pang of fear freezes over my spine when his eyes lock on mine." 
        
        "This guy is massive; his short hair descends to his beard that adorns his gritted teeth."
        
        ry"\"What the fuck did you say to my little sister?\""
        
        "He slams his chest into mine, nostrils flaring; his ragged breath assaults my own."  
        
        p"\"L-look, we don't want any trouble.\""
        
        "Despite my wavering voice, I puff out my chest."
        
        p"\"Do you even know why I defended Sarah?\""
        
        "His fingers flex into a fist."
        
        #jolt screen and blur
        #r"\"\""
        #le custard
        scene school_out002_evening tilt with fastd
        
        "Before I can react I'm flailing back, jaw smarting from impact."
        
        scene school_out002_evening Blur 1 with slowd
        
        "My heart pounds to the beat of adrenaline. I hoist myself up, wary of another blow."
        
        p"\"S-stop, listen!\""
        
        "He's not listening. I step back and avoid his next swing"
        
        rr"\"Get off me, bitch!\""
        
        "We turn to find Sarah's pinned down Rachel. Ryan turns his sights."
        
        ry"\"Get off'o her!\""
        
        "{i}You're not touching Sarah.{/i}"
        
        "I catch his jaw with a right hook that shocks even myself. Words bubble from my lips." with vpunch
        
        #p"\"Listen, you fucking idiot! Your bitch of a sister told Sarah to cut herself.\""
        
        p"\"Listen, you fucking idiot! Your bitch of a sister told Sarah to slit her wrists.\""
        
        "Despite the anger burning down my throat, the words are cast cold."
        
        scene school_out002_evening Blur 1 with vpunch
        
        "Adrenaline floods to the tips of my fingers; I assault his shield of arms."
        
        #sky picture
        
        "He lunges forward; his tackle taking me off guard." 
        
        scene sky003_evening Blur 1 with vpunch
        
        "We crash to the ground, his weight crushes the air from my lungs."
        
        #flash white screen
        
        scene white 
        scene sky003_evening Blur 1 with slowd
        
        #"My vision flashes as his fist connects with my eye."
        "His fist connects with my eye."
        scene sky003_evening Blur 2 with vpunch
        
        "Then my nose; my eyes well up and the taste of blood rises from the back of my throat."
        
        D"\"Ryan! Get off him!\""
        
        "Dean drags him back with the help of a familiar member of staff."
        
        ry"\"Get off! I'll kill him.\""
        
        "I pick myself up but my legs give way; I stumble forward and catch myself on hands and knees."
        
        stop music fadeout 3.0
        
        scene school_out002_evening Blur 2 with longd
        
        "Sarah rushes over, lifting me from under my arms."
        
        #close sprite with blurred background
        
        show S 2DSad_Sad at PCC1 
        show SX Shadow at PCC1
        with slowd
        
        s"\"Oh my God! Are you OK?\""
        
        "I nod in response, residual adrenaline coursing through my veins." 
        
        "My ears ring and my head lolls. Blood drips down my chin onto her sleeve."
        
        p"\"Sorry 'bout that.\""
        
        show S 2YSad_Sad at PCC1 with slowd
        
        "She brings her face level and looks into my eyes."
        
        p"\"I'm fine.\""
        
        "A hand print reddens her cheek."
        
        #"I reassure her with a palm on the shoulder."
        
        p"\"Are you OK?\""
        
        show S 2YSad_Flat at PCC1 with slowd
        
        s"\"Yeah, I'm OK.\""
        
        q"\"Peter! Come with me.\""
        
        "Another teacher collects Sarah as I follow."
        
        
        
        #bedroom the next day?
        
        play music "audio/music/Shunt.ogg"
        
        scene room_boy16_day with longf
        
        t"{i}I don't want to face the world today.{/i}" with slowd
        
        t"The thoughts of how I hadn't warned Sarah not to attend keep playing on my mind." 
        
        t"And my ego is an open wound."
        
        t"For a moment, I had thought everything was OK." 
        
        t"Sarah had actually begun to open up since the first time, and it happens again."
        
        window hide
        nvl clear
        
        "Mr Brent instructed me to go to the staffroom this morning. At least I get to skip some of first period." with slowd
        
        #staffroom
        
        scene office09_day with slowf
        
        
        #"With the majority of teachers in class, there are only a few other members of staff besides Mr Brent."
        
        mb"\"Peter! Take a seat.\""
        
        "I pull up the chair."
        
        mb"\"Your story checks out from what footage I can find on camera.\""
        
        #"Relief gives me a little solace."
        
        p"\"Thanks for checking through it so soon.\""
        
        mb"\"I've been looking through their records and they seem to have been invloved in numerous instances.\""
        
        #mb"\"There's been a formal appeal submitted to have them both expelled. Ryan was on the brink as it was.\""
        
        mb"\"I can assure you that the necessary actions will be taken.\""
        
        #"{i}Good riddance.{/i}"
        
        #p"\"Maybe they should've gone sooner.\""
        
        #mb"\"Maybe so, but rules must be followed.\""
        
        "I take what solace I can, hoping they'll never return."
        
        p"\"Have you spoken to Sarah?\""
        
        mb"\"No, I'm not certain who she spoke to.\""
        
        p"\"So, is that everything cleared up, can I go?\""
        
        mb "\"Certainly. Don't hesistate to find me if you have any more problems.\""
        
        "He flashes a wink. It feels out of place."
        
        p"\"Thanks.\""
        
        "{i}I'm not ready for class today...{/i}"
        
        #skip Jennifer's section for now?
        
        
        #corridor.
        stop music fadeout 3.0
        
        scene school02_day with longf
        
        #knock noises
        
        "I'm anxious to see Sarah. Things had seemed bad enough after the first time."
        
        scene hospital03_day with longf
        
        play sound "audio/sfx/soft knock.mp3"
        
        p"\"Sarah?\""
        
        "I press my ear to the door. Nothing."
        
        "I follow an inkling..."
        
        #windy forest
        #forest
        
        play music "audio/music/Windy Forest.mp3"
        
        scene fantasy01_day with longf
        
        p"\"Thought I'd find you here.\""
        
        show S 2YCalm_Sad at PM1 with slowd
        
        "She stiffens and the pebble slips from her fingers."
        
        hide S 2YCalm_Sad with slowd
        
        "I take it from the ground and manage six skims."
        
        p"\"Got any more?\""
        
        "She lays her satchel between us, taking another and lining herself up."
        
        s"\"I'm sorry.\""
        
        "We keep our gazes fixed out on the reservoir."
        
        p"\"Don't be.\""
        
        s"\"I knew she was still there... I thought I could've avoided something like that.\""
        
        "I shrug, taking another stone."
        
        p"\"Shit happens.\""
        
        "I manage a calm tone, but just thinking about it ignites anger in my stomach."
        
        s"\"Thank you.\""
        
        "I ease up, lifting my brow."
        
        p"\"What for? Getting my arse kicked?\""
        
        "Venom leaks from my wounded ego."
        
        s"\"For sticking up for me. {w}For... being here for me...\""
        
        p"\"If I hadn't asked you... \""
        
        s"\"You didn't know. And you could've dropped it when you did... \""
        
        p"\"I wouldn't have...\""
        
        "Whether I stayed because I felt it was my fault or for the fact I'm able to spend time with Sarah conflict."
        
        p"\"What made you go back?\""
        
        "She tilts her head. Such nuances about her seem amplified."
        
        s"\"It was a promise I'd made...\""
        
        p"\"To who?\""
        
        s"\"Emma...\""
        
        s"\"When Rachel... saw... she started calling me out.\""
        
        "She stumbles and tries to push more words out. I skim another stone in silence."
        
        s"\"Before Emma left, I drew a picture for her and shared it with the class...\""
        
        #s"\"Rachel waited for me after class and pulled my hair in front of her friends...\""
        
        s"\"Rachel spread rumours... and pulled my hair in front of her friends...\""
        
        p"\"How come... you didn't hit her when you had the chance?\""
        
        #s"\"I... didn't want to hurt her. I don't like hurting anything...\""
        
        #"No matter how naive it seems, all I can think is {i}you're an angel.{/i}"
        
        #s"\"If she thinks she'll be happy by hurting other people, then she's more lost than I am.\""
        
        #"{i}Then how lost am I?{/i}"
        
        #p"\"But... that doesn't mean she should hurt you...\""
        
        s"\"I... didn't want to hurt her. I don't like hurting anything...\""
        
        "No matter how naive it seems, all I can think is {i}you're an angel.{/i}"
        
        
        
        s"\"...Emma had me promise her that I'd keep art up and not let people like her stop me from the club...\""
        
        p"\"Sounds like you were close.\""
        
        "A wry smile twists her lips."
        
        s"\"Yeah...\""
        
        #p"\"It sounds like you were good friends.\""
        
        #s"\"Yeah... friends...\"" 
        
        #"I wasnt sure what else to day."
        
        p"\"Since Emma left, haven't you made any friends?\""
        
        s"\"No.\""
        
        "Her candid answer leaves us in silence. I fight with curiosity."
        
        p"\"Why not?\""
        
        s"\"I... I don't really like people.\""                                                             
        
        "Sometimes I question whether or not I should be here."
        
        p"\"What about me?\""
        
        #show S cnormal 
        #hide S cnormal with slowd
        
        #show S 2YCalm_Flat at PC1 with slowd
        
        "She glances into my eyes. It takes her a moment to pierce my soul."
        
        #hide S 2YCalm_Flat at PC1 with slowd
        
        s"\"You're... different.\""
        
        "For the first time... I'm happy to be... {i}different.{/i}"
        
        "We finish off the stones in mutual silence."
        
        #sun setting
        
        scene fantasy01_evening with slowd
        
        "Somehow, I feel closer to her than ever." 
        
        "We sit on the bank, watching the sun's reflection dance on the water."
        
        "My smile weighs on my aching jaw. But with this girl beside me, I can't help it."
        
        p"\"I have to say, the melodies of the birds are so relaxing.\""
        
        "I attempt to retain the lightened mood."
        
        s"\"Not if you're a worm.\""
        
        "I follow her gaze to a worm on the bank and chuckle."
        
        #"I chuckle, following her gaze to a worm on the bank." 
        
        "{i}Just what goes through that head of hers?{/i}"
        
        p"\"Can worms even hear?\""
        
        "She shrugs, smile pulling on the corners of her lips."
        
        s"\"Iunno.\""
        
        stop music fadeout 3.0
        
        #Act 2/1 -  graveyard - existential drawing 
        
        #black screen
        
        scene black with longf
        centered "Sarah Act 2"
        
        ############################
        
        #make an act 2 here
        
        scene street001_cloud with longf
        
        "I've never gone this far up Long Rd, but Sarah seems determined."
        
        "She's anxious to get there. But she never told me where we were going."
        
        
        play music "audio/music/Kevin_MacLeod_-_Clean_Soul.mp3" fadein 4.0
        
        scene church13_cloud with slowf
        
        "She turns off into a graveyard."
        
        #graveyard
        
        "I wasn't expecting this."
        
        #"She said about doing a collage, but I don't really see how this fits with the school roof."
        
        "She's quiet, following a predetermined path."
        
        show S 2DSad_Flat at PCM1 with slowd
        
        "She slows and homes in on a gravestone. A lump wedges itself in my throat."
        
        p"\"Who...\""
        
        s"\"A gentleman, once named Sam Davidson.\""
        
        p"\"Did you know him?\""
        
        show S 2YSad_Flat at PCM1 with slowd
        
        s"\"No. It's just... the message on his gravestone.\""
        
        #"I swallow the lump in my throat."
        
        hide S 2DSad_Flat at PCM1 with slowd
        
        "The sharp lump in my throat softens and I swallow it."#{i} I wasn't ready for it to be a dead relative.{/i}"
        
        t"The gravestone reads, \"I used to be like you; you'll one day be like me...\"" with slowd
        
        t"A serpent curls into a circle below, tail devoured by its own jaws."
        
        window hide
        nvl clear
        
        p"\"We'll also be dead soon?\"" with slowd
        
        p"\"That's... depressing.\""
        
        show S 2YSad_Smile at PCM1 with slowd
        
        "I'm surprised to see her lips edge into a smile."
        
        s"\"It's a reminder to follow your passions in life.\""
        
        show S 1AAnxious_Smile at PCM1 with slowd
        
        s"\"This...\""
        
        "She points to her skull hair piece."
        
        s"\"...Is a memento mori.\""
        
        p"\"What's that?\""
        
        show S 2YCalm_Smile at PCM1 with slowd
        
        s"\"It's something to remind you that you have to die.\""
        
        p"\"Again, depressing...\""
        
        p"\"Wouldn't it make more sense to live now?\""
        
        show S 1YAnxious_Smile at PCM1 with slowd
        
        s"\"That'd be Carpe Diem. I think memento mori is a roundabout way of saying to live now.\""        
        
        s"\"But how can you really appreciate everything now unless you know it's limited? {w}Precious...\""
        
        "Her last word delivered in a whisper."
        
        p"\"People do it everyday.\""
        
        show S 1AAnxious_Flat at PCM1 with slowd
        
        s"\"They really seem to... But I can't.\""        
        
        "I release a wry snort."
        
        p"\"Yeah, me either.\""
        
        "The only time I've really thought of death, was wishing I had in that crash. But if I had, I wouldn't be here now..."
        
        p"\"What about the snake?\""
        
        s"\"Ouroboros.\""
        
        p"\"What's that?\""
        
        s"\"A snake eating its own tail.\""
        
        p"\"Well, I can see that much.\""
        
        show S 1YAnxious_Smile at PCM1 with slowd
        
        "She chuckles."
        
        s"\"It's symbolic; it's a cycle, like life. \""
        
        p"\"So like the saying; we'll one day be dead and someone else will be like us now.\""
        
        s"\"Pretty much.\""
        
        p"\"So why should you remember you're going to die?\""
        
        "I point to her hair piece."
        
        s"\"Because how can you live now if you don't regard death?\""
        
        
        p"\"School, work, retirement.\""
        
        s"\"But how will you stop planning for the future when you don't see the end in sight?\""
        
        p"\"Then what does it all even matter when we'll die and be replaced?\""
        
        s"\"What other meaning is there?\""
        
        hide S 1YAnxious_Smile with slowd
        
        "I shrug and she begins to unpack her equipment."
        
        "As if on cue, rain leaves a few droplets on her pad."
        
        
        #"My sombre thought evokes some droplets of rain."
        
        #"Sarah retrieves her art equipment nonetheless."
        
        
        p"\"Will it be OK to draw? It's spitting.\""
        
        s"\"It'll be fine.\""
        
        play environment "audio/background/Rain2.ogg" fadein 3.0
        
        scene church13_rain with slowd
        
        "The rain picks up."
        
        
        
        p"\"Should we find shelter?\""
        
        s"\"I... don't mind the rain.\""
        
        p"\"It's getting heavy though, is it locked?\""
        
        "I point towards the nearby church and she shrugs."
        
        p"\"One way to find out.\""
        
        scene church01_rain with slowf
        
        #church bg
        
        s"\"The groundskeeper lives in the house back there. He might be inside.\""
        
        "I rap the iron knocker and seconds of silence respond."
        
        p"\"Hello?\""
        
        "The door yields to a shove."
        
        #inside church bg
        
        stop environment fadeout 4.0
        
        scene church11_night_dark with slowf
        
        "The creak echoes around the empty building."
        
        "We take a seat on a pew and unpack our equipment."
        
        show S 1AAnxious_Flat at PCM1 with slowd
        
        s"\"Do you believe in God?\""
        
        p"\"Can't say I do, haven't put much thought into religion. What about you?\""
        
        s"\"I used to...\""
        
        "We're left in silence, save for the rain pattering on the windows."
        
        s"\"People have told me I'm... unnatural.\""
        
        p"\"Becuase of Emma?\""
        
        show S 1AAnxious_Smile at PCM1 with slowd
        
        s"\"Yeah.\""
        
        p"\"I don't see how, it's found throughout the animal kingdom.\""
        
        #show S 1AAnxious_Flat at PCM1 with slowd
        
        s"\"Mhm.\""
        
        hide S 1AAnxious_Smile at PCM1 with slowd
        
        "She takes out her pad and begins a sketch. I follow suit."
        
        "But I can't keep the questions from circling in my mind."
        
        show S 1AAnxious_Flat at PCM1 with slowd
        
        s"\"Does that mean there's no meaning?\""
        
        "But she's first to break the silence with her own question."
        
        p"\"If there's no God?\""
        
        s"\"Yeah.\""
        
        "I find myself playing Devil's advocate, despite struggling to find meaning myself."
        
        p"\"Didn’t you say your skull was to remind you to follow your passion? Isn’t that meaning?\""
        
        s"\"But what’s left then when you’ve lost what’s meaningful?\""
        
        "{i}Did Emma mean that much to her?{/i}"
        
        p"\"Don't you have to find meaning?\""
        
        s"\"Is it that easy?\""
        
        #"I'm left wordless. The only meaning I've found is... {i}Sarah.{/i}"
        
        "{i}What meaning have I found...?{/i}"
        
        p"\"No, I guess not...\""
        
        show S 2YSad_Flat at PCM1 with slowd
        
        "She measures me and takes a breath."
        
        s"\"This is how I search. I want to capture the meaning of {i}now{/i} in a picture.\""
        
        s"\"I'm going to be dead much longer than I'm alive. Maybe I can make something that lives longer than me.\""
        
        hide S 2YSad_Flat with slowd
        
        "She retrieves her pad and pencils and sets off to work. My questions fade away as I watch her delve into her mode."
        
        "Her eyes pierce the windows and decor between flitting to her sketchpad." 
        
        "I set to work on my own piece..."
        
        scene church11_night_dark with slowf
        
        p"\"Have you thought about sharing your art?\""
        
        #"She continues as if I hadn't said a word."
        
        #show S cHBB with slowd
        
        s"\"Not really.\""
        
        "She continues in her work."
        
        p"\"There's competitions online and forums where you can post your art.\""
        
        "She stops for a moment."
        
        #s"\"Not really.\""
        
        s"\"It's scary... for people to judge what you've put your heart into.\""
        
        "After almost not showing her my picture after the first art lesson, it's hard to find a response."
        
        "I join her and begin on a painted glass window..."
        
        stop music fadeout 3.0
        
        #bedroom
        
        scene room_boy16_night_dark with slowf
        
        "Sarah wasn't very responsive as we made our way back. She looked exhausted"
        
        "She wakes up everyday with a reminder that she's going to die. That can't be good for the psyche."
        
        "The picture I found in her room flashes through my mind..."
        
        "Sleep doesn't come easy."
        
        play music "audio/music/Drone in D.mp3" fadein 3.0
        
        scene black with longd
        
        #dream
        
        #Tree branches twist against the grey sky. Gnarly.
        
        #A tree rests beside it, its branches twit and gnarl against the grey sky. 
        
        centered "As sleep claims my senses, an image surfaces in my mind—a gravestone."
        
        t"One of thousands scattered under a bleak sky. The clouds merge from grey to black above above one grave." with slowd
        
        t"The grave before me reads, \"Memory.\""
        
        t"A spade falls from the air and thumps into the dirt."
        
        t"I lever the handle, uprooting the earth. I shovel it aside and scoop again."
        
        t"Again and again. I dig until my chest contracts."
        
        t"{i}Can't. Breathe!{/i}"
        
        window hide
        nvl clear
        
        t"I have no control, it's like I'm possessed." with slowd
        
        t"As I'm about to suffocate, air fills my lungs. I've hit something solid."
        
        t"I fall back as the coffin rises to the surface, soil dancing on its surface."
        
        t"The door swings open, scattering dirt through the air."
        
        t"A corpse rises into the air enshrouded in a dark mist."
        
        t"I try to rise but my limbs sink into the mud. It floats forward and lifts its head."
        
        window hide
        nvl clear
        
        centered "I scream but no sound comes out. I can't turn away; its face meets mine." with slowd
        
        #wake up
        
        stop music fadeout 3.0
        
        scene white with slowd
        
        scene room_boy16_day with slowd
        
        "I jolt up and gasp for breath."
        
        "The image of the decaying face fresh in my mind's eye."
        
        "That face... {w}{i}that was me.{/i}" #mine
        
        #
        scene school02_day with slowf
        
        "I rest my forehead in my palm and stare into my desk."
        
        "I'm not ready for class today. {w}Not sure what day I am."
        
        play music "audio/music/bensound-enigmatic.mp3" fadein 4.0
        
        q"\"Peter.\""
        
        show D 2YGentle_Flat at PC1 with slowd
        
        "It's not the voice I was expecting."
        
        #show Danielle
        
        d"\"Not interested in Magnum Dilon?\""
        
        p"\"Sorry, not interested.\""
        
        "A pang of guilt stems from my blunt answer. Not like Danielle would spare me remorse."
        
        p"\"I've just got too much going on.\""
        
        show D 1YSerious_Smile with slowd
        
        d"\"I'm glad to see you're being productive then.\""
        
        "{i}Productive{/i} wouldn't be the right word."
        
        show D 1Closed_Flat with slowd
        
        j"\"Peter!\""
        
        "And the voice I first expected intervenes."
        
        hide D 1Closed_Flat with slowd
        
        d"\"Later.\""
        
        "Danielle's quick to leave the scene."
        
        show J 2YUpturned_Smile at PC1 with slowd
        
        j"\"What's up? You've got a face like a slapped arse.\""
        
        p"\"I'm OK. Just can't seem to get a good night's sleep here.\""
        
        show J 2YUpturned_Grin with slowd
        
        j"\"You should try some alcohol. Works a treat.\""
        
        p"\"To get you to sleep I bet, but you won't sleep properly.\""
        
        show J 2YUpturned_Smile with slowd
        
        j"\"So? Isn't the point of sleep to escape for a little while?\""
        
        "It strikes me as a bit too nihilistic for Jennifer.{w} Or what little I know of her."
        
        p"\"Not really.\"" #But alcohol isn't the best medicine for that ailment.\""
        
        "Mrs Brown enters."
        
        #show J cupturned with slowd
        
        j"\"Borin' arse.\""
        
        hide J 2YUpturned_Smile with slowd
        
        stop music fadeout 3.5
        
        "Their interactions leave me with a smile."
        
        #scene with slowf
        #
        
        scene school02_day with slowf
        
        t"My face from the grave..."
        
        t"Was that me?"
        
        t"...Was it a reminder of who I was before?"
        
        t"Is the person who I was before dead now?"
        
        t"Maybe still alive? Buried inside?"
        
        window hide
        nvl clear
        
        m"\"Peter!\"" with slowd
        
        p"\"Hm?\""
        
        m"\"What do you think the answer is?\""
        
        "She points to the board where numerous questions are laid out."
        
        #"The bottom question being, \"what was the most prevalent form of reproduction for dinosaurs in the Mesozoic Era?\""
        
        "The bottom question being, \"In the Mesozoic Era, how did dinosaurs reproduce?\"" 
        
        p"\"Egg?\""
        
        "She glares at me."
        
        m"\"I'll let you off.\""
        
        "Thankfully, I've watched too many random documentaries."
        
        #bedroom
        
        scene room_boy16_evening with slowf
        
        "Class today dragged. I'm thankful to undress and get into bed."
        
        t"The decaying image of my face isn't as fresh as it was this morning, but I can't stop thinking about it." with slowd
        
        t"What did that dream mean?"
        
        t"Do dreams really reveal a layer of our subconscious mind as the psychologists say?"
        
        window hide
        nvl clear
        
        "Knocks on my door break me from my thoughts." with slowd
        
        "I can only smile."
        
        "{i}Sarah.{/i}"
        
        "I almost answer the door but realise I'm in my boxers."
        
        p"\"Give me a minute!\""
        
        "I put a T-shirt on and fall against my desk as I pull my trousers up."
        
        
        s"\"Are you OK?\""
        
        "Her voice muffled through the door but I open it."
        
        scene hospital03_day 
        
        show S 2YCalm_Smile at PC1

        with slowf
        
        p"\"I'm OK. What's up?\""
        
        "Sarah greets me with a smile."
        
        s"\"Wanna work on the collage at the park?\""
        
        
        p"\"Sounds good! Give me a minute to get ready.\""
        
        #park 
        
        play music "audio/music/lifeis.ogg"
        
        scene park008_night_light with longf
        
        "Night falls as we make it to the familiar bench."
        
        "I almost wonder why I try as I mess up my picture multiple times."
        
        #CG!!!!!!!
        
        scene Sarah CG eyes open down with slowd
        
        "But when I look at Sarah, I don't care if art isn't for me."
        
        "Watching her awe of our surroundings makes my heart melt for reasons I can't articulate."  #makes me feel a child-like joy."
        
        "But I feel a twist as I notice her eyes are brimming with tears."
        
        p"\"Sarah? Are you OK?\""
        
        scene Sarah CG eyes closed down with slowd
        
        "Her eyes flicker open and shut but fail to contain a tear."
        
        scene Sarah CG eyes towards down with slowd
        
        s"\"It's just...\""
        
        p"\"Hm?\""
        
        scene Sarah CG eyes open down with slowd
        
        "Her eyes shimmer as she takes in our surroundings."
        
        s"\"One day everything's going to die. All of this will be dead.\""
        
        s"\"Me and you... will be dead.\""
        
        p"\"That's... depressing.\""
        
        scene Sarah CG eyes open smile with slowd
        
        s"\"Is it?\""
        
        "A smile breaks her lips."
        
        s"\"The fact that everything's here; that we're here right now... it blows my mind.\""
        
        s"\"I want to capture this beauty every time I can see it.\""
        
        s"\"Life only makes sense in these moments.\""
        
        scene park008_night_light with slowd
        
        "She delves into her art once more."
        
        "I remain stumped at her shifting thought patterns around the ideas."
        
        p"\"What do you mean by every time you can see it?\""
        
        scene Sarah CG eyes closed down with slowd
        
        s"\"It's rare that we ever realise how beautiful life truly is.\""
        
        scene Sarah CG eyes open down with slowd
        
        s"\"In a thousand years all of this will be gone. Who knows where nature and humanity will be then.\""
        
        #I want to hug her, and let her know it will be OK. Even if I know it won't always be."
        
        "As her words evaporate on the breeze, an urge rises to hug her."
        
        #Something about her worldview makes me want to hug her.
        
        #"As her words evaporate on the breeze, an urge rises to kiss her on her cheek."
        
        #"The butterflies in my stomach well up my throat."
        
        p"\"Isn't that why right now is so beautiful?\""
        
        #I want to hug her, and let her know it will be OK. Even if I know it won't always be." #no matter what happens.
        
        s"\"It is... a beautiful tragedy.\""
        
        "I nod in agreement."
        
        scene park008_night_light with slowd
        
        "Sarah continues her work and I follow suit."
        
        "I just can't focus, I want to talk to Sarah."
        
        "The small talk rattling around my mind just doesn't seem worthy of distracting her in this mood."
        
        "I'm more interested in Sarah than the scenery. I decide to add her into it."
        
        "We work in silence..."
        
        #timeskip
        
        scene Sarah CG eyes towards down with slowf
        
        s"\"Sorry...\""
        
        p"\"What for?\""
        
        scene Sarah CG eyes open down with slowd
        
        s"\"For always bringing up these kinda things.\""
        
        "I release a snort and a smile."
        
        p"\"Y'know, when I met you, I didn't really expect to have conversations like this. I didn't know what to expect moving here.\""
        
        p"\"Honestly, I was just nervous about the whole situation...\""
        
        scene Sarah CG eyes open smile with slowd
        
        "She giggles."
        
        s"\"What did you expect?\""
        
        p"\"I'm not sure really. I didn't really expect to make friends. I just expected small talk that I wouldn't be able to keep up.\""
        
        "The smile remains on her lips."
        
        s"\"I hate small talk, too. Why did you think you wouldn't make friends?\""
        
        p"\"I... don't know.\""
        
        scene Sarah CG eyes towards smile with slowd
        
        s"\"You're a good person. Anybody would be lucky to have you as a friend.\""
        
        scene Sarah CG eyes open smile with slowd
        
        "It hits a sentimental spot. Nobody's said something like that to me before."
        
        p"\"Thanks... I want you to know you're  a good person, too.\""
        
        scene Sarah CG eyes closed smile with slowd
        
        "It comes out so awkward, but her smile widens."
        
        s"\"I'm glad you convinced me to join the club again.\"" 
        
        scene Sarah CG eyes closed down with slowd
        
        s"\"I've been in such a block since...\""
        
        scene Sarah CG eyes towards smile with slowd
        
        s"\"Would you wanna join me at the forest again tomorrow? And I have another spot in mind for later...\""
        
        scene Sarah CG eyes open smile with slowd
        
        p"\"Definitely. I'm looking forward to it.\""
        
        s"\"I'll meet you at the forest steps after school?\""
        
        p"\"Sounds good.\""
        
        stop music fadeout 5.0
        
        scene park008_night_light with slowd
        
        "Sarah rises."
        
        s"\"We should head back.\""
        
        p"\"Yeah, it's getting late.\""
        
        #maybe on the road
        
        scene street001_night_light with slowf
        
        p"\"Thanks, Sarah. I'm enjoying this.\""
        
        "Her smile makes my heart melt."
        
        s"\"Me too.\""
        
        #Forest steps 
        
        play music "audio/music/A Wish to the Sky.mp3" fadein 4.0
        
        scene forest008_day with longf
        
        "I've been waiting all day for this."
        
        "Sarah's already waiting for me by the steps."
        
        show S 2YCalm_Smile at PC1 with slowd
        
        "She greets me with a smile and I can't contain my own."
        
        p"\"Hey Sarah, have a good day?\""
        
        "She shrugs."
        
        s"\"I suppose. But I'm looking forward to this.\""
        
        p"\"Me too.\""
        
        #forest
        
        scene forest002_day with slowd
        
        "Her gaze curious, but stops in the distance to a felled tree."
        
        s"\"If a tree falls in the forest and nobody's there to hear it, does it make a sound?\""
        
        "{i}Her questions have started already.{/i} I can only smile."
        
        p"\"No, it'd only be vibrations until it hits an ear drum.\""
        
        "I can see the gears turning in her head as she contemplates my answer."
        
        s"\"Would the universe exist if there was no life to experience it?\""
        
        #"Her question  leaves me in a moment of thought."
        
        p"\"Yeah, why wouldn't it?\""
        
        "She retreats into thought for a while. And I'm just stumped at her question, it seems obvious."
        
        s"\"So what about the Shrodinger's cat thing? Where it's a wave or a particle whether or not we obseve it?\""
        
        "It takes me a moment to see where she's going."
        
        p"\"So the universe is just potential until life observes it?\""
        
        "She shrugs."
        
        s"\"Maybe... I know it sounds stupid...\""
        
        p"\"Even Einstein contested it. A reponse of his to quantum physics, 'is the moon really there when nobody looks?'\""
        
        s"\"I just don't see what it is without life to observe it. It might as well be nothing.\""
        
        p"\"I... think I can agree there.\""
        
        p"\"But why would you want to believe the universe is only potential without us?\""
        
        s"\"Because what other meaning does life have?\""
        
        p"\"Doesn't this mean something? That we're here now? Memento mori?\""
        
        "Angst wells up in me. {w}{i}Could I give meaning to her?{/i}"
        
        s"\"But then what's the point?\""
        
        p"\"Of us being here now?\""
        
        s"\"No. What's the point of life?\""
        
        p"\"I don't know...\""
        
        #p"\"Who knows...?\""
        
        #"I want to tell her that she means enough for me. But all I can muster is something generic."
        
        "All I can muster is something generic..."
        
        p"\"Well, isn't the point now? Isn't that what memento mori means? That we're now friends and we're here together?\""
        
        s"\"We need to take a left here.\""
        
        "She brushes off my answer and we take the turn."
        
        #scene change
        
        scene forest003_day with slowf
        
        "It feels like rejection."
        
        "{i}Emma...{/i} I'm just a friend and she was a lover. {i}Could I ever mean as much?{/i}"
        
        "We remain in silence..."
        
        s"\"It means a lot that you're doing this with me.\""
        
        "And my feelings turn in an instant."
        
        p"\"I'm glad you wanted to do it with me.\""
        
        "With nothing else left to say, silence ensues."
        
        
        #Finish scene
        
        scene fantasy26_day with slowf
        
        "We arrive at an opening with a bench and an expansive view."
        
        p"\"Wow.\""
        
        "My smile matches hers."
        
        s"\"It's beautiful, isn't it.\""
        
        p"\"It is...\""
        
        s"\"I last came with Emma.\""
        
        p"\"Don't other people come here?\""
        
        s"\"No.\""
        
        p"\"Then why's there a bench?\""
        
        s"\"It's a memorial, for a Mrs Eames. I've never seen her family here... or anyone else.\""
        
        p"\"It's a beautiful spot, even better without other people.\""
        
        "She smiles and nods at my answer, taking a seat on the bench. I join."
        
        s"\"I'm sorry, but I really want to focus on my work here.\""
        
        stop music fadeout 3.0
        
        p"\"No problem, I'll focus on my own work.\""
        
        "..."
        
        scene fantasy26_evening with slowf
        
        "..."
        
        "Sarah really has been quiet, deep in her work."
        
        "I nudge her."
        
        show S 2YAnxious_Open at PCM1 with slowd
        
        p"\"Should we go soon? It's starting to get late.\""
        
        show S 2DSad_Smile at PCM1 with slowd
        
        s"\"This is the best time...\""
        
        "It's certainly beautiful, but I rather wouldn't go back through the forest in the dark."
        
        q"\"Ahem.\""
        
        show S 1ACalm_Open at PCM1 
        show SX Shadow at PCM1 
        with slowd
        
        "A voice startles us from behind."
        
        hide S 1Calm_Open at PCM1 
        hide SX Shadow at PCM1 
        with slowd
        
        "It's Mr Brent."
        
        mb"\"You guys should head back,  it'll be dark soon.\""
        
        "We start packing our equipment. Even after realising there's no threat, Sarah's still anxious."
        
        scene school_out002_evening with slowf
        
        "Mr Brent parted with us at the school gates."
        
        show S 1AAnxious_Flat at PC1 with slowd
        
        s"\"Something about him just gives me a bad feeling.\""
        
        p"\"He helped us when it happened here...\""
        
        p"\"I'm just grateful it wasn't Ryan who found us there.\""
        
        "Sarah agrees with a nod, but still seems unsure."
        
        hide S 1AAnxious_Flat at PC1 with slowd
        
        "We resume in silence."
        
        scene hospital03_day with slowf
        
        "Sarah breaks the silence when we reach our doors."
        
        show S 1AAnxious_Flat at PC1 with slowd
        
        s"\"I said I had another place in mind...\""
        
        show S 1YAnxious_Flat at PC1 with slowd
        
        s"\"Do you want to come with me next weekend?\""
        
        p"\"Sure, sounds good.\""
        
        s"\"I'll see you Friday.\""
        
        #"She's inside her room in sync
        
        
        #Savfk - the meaning of words
        
        #
        
        #Bridge
        
        play music "audio/music/The Meaning of Words.ogg"
        
        scene road003_night_dark with longf
        
        "True to her word, I haven't seen her until today."
        
        "A few cars pass, but it's almost dead." #I didn't expect her to be hesitent to come here."
        
        "Despite that, I can still feel the gravitas of the outing. Sarah's tense."
        
        s"\"I wasn't sure whether to come here... but I think it's right.\""
        
        "She leans her elbows against the rails and sways back and forth."
        
        #"I rest on the barrier beside her. I lean back due to feeling unease."
        
        "I follow suit beside her, but lean back due to feeling uneasy."
        
        "A motorway runs below. Moonlight glimmers on the distant lake."
        
        s"\"Do you trust yourself?\""
        
        p"\"What do you mean?\""
        
        s"\"Do you ever get an urge to jump? Like something's pulling you towards the edge?\""
        
        p"\"Yeah, a little.\""
        
        s"\"It's the call of the void.\""
        
        s"\"That's what I feel when I create art. I'm scared, but it pulls me to the edge.\"" #it wants to pull me over the edge
        
        #Sarah Custard
        
        #I don't understand how people can just accept it. Why they don't question how amazing and fragile abd tragic it all is. 
        
        p"\"Why do you think about all of this stuff so much?\""
        
        s"\"I can't help it... I just can't understand...\""
        
        p"\"Understand what?\""
        
        s"\"What's the meaning of anything? I don't understand how people can live their lives without questioning...\""
        
        p"\"Questioning what?\""
        
        s"\"Everything...\""
        
        s"\"Why does anything exist at all? Why is life here? Why has life found the ability to question itself? Why then does it often choose not to?\""
        
        p"\"But isn't that what religion is? Isn't that what science is?\""
        
        s"\"But how do they not question it? Why do they accept so easy?\""
        
        p"\"Life is hard... when you're trying to survive day by day, it's easier to accept a paradigm.\""
        
        s"\"But then why live at all?\""
        
        
        p"\"Instincts? Family? Love? Wealth? Pleasure?\""
        
        s"\"Is that really all there is?\""
        
        #p"\"I think so.\""
        
        "I can only shrug."
        
        s"\"I mean why then did we create religions? Why would we create the scientific method? There has to be something we're looking for.\""
        
        p"\"It seems so. Maybe we'll never find it.\""
        
        s"\"That's... depressing.\""
        
        #"Sarah retrieves her equipment. I gather my own."
        
        
        
        
        
        
        
        
        
        
        
        #Sarah will shut herself off and create a lot of art? Those scenes of you knocking? Where you sit down and be with her in silence. 
        
        #He'll then attend incase she does. Which she will? Or she won't and the fight will happen?...
        
        
        #Sarah custard
        
        
        #After class the next day
        
        #"I've been itching for the lesson to end. I avoid Jennifer and dart for the hall.."
        
        #"I need to tell Mr Adams. I have to do something."
        
        #Mr Adams office       
        
        
        #"Rachel keeps staring at her, I return a few grimaces and she only grins."
        
        
        
        
        
        #grave scene 
        
        #scene church13_cloud with longf
        
        #"She turns off into a graveyard. I wasn't expecting this."
        
        #"She's quiet, following a predetermined path."
        
        #"A lump wedges itself in my throat as she stops before a grave."
        
        
        
        #p"\"Who...?\""
        
        #s"\"A gentleman once named Sam Davies.\""
        
        #p"\"Did you know him?\""
        
        #s"\"No. It's just... his message.\""                                                                  
        
        #"I swallow the lump."
        
        #"The headstone reads, \"I used to be like you; you'll one day be like me...\""
        
        
        
        #p"\"...We'll also be dead soon?\""
        
        #p"\"That's... depressing.\""
        
        #"I'm surprised to see her lips edge into a smile."
        
        #s"\"This...\""
        
        #"She points to her skull hair clip."
        
        #s"\"...Is a memento mori.\""
        
        #p"\"What's that?\""
        
        #s"\"It's something to remind you that you will die.\""
        
        #s"\"So... follow your passions now.\""
        
        #"{i}What passions do I have?{/i}"
        
        #"I retreive my pad from my bag. I kinda enjoy art, but I couldn't claim it as a passion."
        
        
        
        #p"\"Who...\""
        
        #s"\"Who...\""
        
        #p"\"Who...\""
        
        #s"\"Who...\""
        
        #p"\"Who...\""
        
        #s"\"Who...\""
        
        #p"\"Who...\""
        
        #s"\"Who...\""
        
        
        
        #You tell Sarah to inform Mr Thatchar but she doesn't. 
        
        scene black with slowd
        
        centered "Thanks for reading! Be sure to check out the other route segments and ending."
        
        #centered "Feel free to leave feedback at Facebook.com/NamelessNoun"
        
        centered "Please be patient for the credits, there's also a .txt file."
        
        call credits from _call_credits_1
        return
        
        
        
        
        
        
        
        
        #to Danielle arc
        
    label Sar2n:
        
        stop music fadeout 2.5
        
        "..." 
        
        "We walk back in silence."
        
        stop environment fadeout 2.5
        
        scene room_boy16_cloud with slowf
        
        #"I feel like I missed the opportunity to ask her."
        
        "I feel like an opportunity just slipped through my fingers."
        
        "..."
        
        
        jump Sar1n2
        
        #scene black with slowd
        #centered "Scroll back and click Ask! <3"
        #centered "The next click will take you back to the menu... >.>"
        #return
        
        
        #Now's my chance to ask her. 
        
        #When asking her to join the art club
        #She searches her fringe as if contained answers.    ??? But this will probably be better to use at another point         
        
        
        #Art club scene from last VN and the showing of pictures. 
        
        
        #A touch that says more than words ever could. 
        
        
        #With Danielle the choice is to message her? Then when you meet up she'll ask you about getting an account. 
        #If you do you start the new game and get killed by rats. 
        #If not you have a few more fights and decide to never play her again. :p 
        
        
        #Scroll back and press yes! XD
        
        #Second chance. It finishes after this.
        
    #I want to drink myself into oblivion. It's easier to forget. I wouldn't have this amnesia, otherwise. 
    
    #"I wonder if it would've only been seen by herself otherwise."
    #"I wonder if she would've kept it to herself otherwise."
    
    
    #"I wonder how many people she's shown her art to. 
    
    #room 
    
    
    #An option could be to tell him, which leads down Sarah's arc? The damage has already been done. 
    
    
    #p"\"\""
    
    #a"\"\""
    
    #p"\"\""
    
    #He trusts in Mr Adams and tells him about the dream? Maybe this is only in Sarah's route as he stops attending in the others?
    
    #label Sar2n:
        
        #..."
        
        #"Have him message Danielle instead later on at night?"
        
        #"The rain sings on the window. It's the first time it's rained since my arrival."
        
        #"Rain pelts the window. It's the first time it's rained since my arrival."
        
        
        return
    
    label Sar1n:
        
        "..."
        
        scene room_boy16_cloud with slowf
        
        
        #"Have him message Danielle instead later on at night?"
        
        #"The rain sings on the window. It's the first time it's rained since my arrival."
        
        "Rain pelts the window. It's the first time it's rained since my arrival."
        
        jump Sar1n2
        
    label Sar1n2:
        
        "I draw out my phone and send a message to Dest—Danielle."
        
        t"L0stc4us3: Long time no speak."
        
        "It's a strange coincidence. Though, I've never been sure what she thinks of me."
        
        #vibrate
        
        #use wuu2 for Jennifer 
        
        t"x-Destiny-x: Hello."
        
        "She never makes it easy."
        
        t"L0stc4us3: Wuu2?"
        
        t"x-Destiny-x: Working on my project."
        
        t"L0stc4us3: Your game?"
        
        t"x-Destiny-x: Yes. What else would it be?"
        
        window hide 
        nvl clear 
        
        "Damn. Touchy."
        
        #t"L0stc4us3: Not sure..."
        
        #"I leave it at that, not sure she wants to speak to me."
        
        #vibrate
        
        "I'm not sure what to say, so I'm glad for another message."
        
        
        
        t"x-Destiny-x: Did you like Magnum Dilon?"
        
        t"L0stc4us3: Can't say, I was too busy dying."
        
        t"x-Destiny-x: That's because you're a noob." 
        
        #t"\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ ..." 
        
        #centered "..." with slowd
        
        "\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \ \ \ \ \ \ ..." with slowd
        
        t"x-Destiny-x: Do you want to join me again on Saturday? Though, there's a catch."
        
        #t"x-Destiny-x: I was wondering if you wanted to join me again on Saturday? Though, there's a catch."
        
        t"L0stc4us3: What's the catch?"
        
        t"x-Destiny-x: My friend will be online, so you'll have to buy an account."
        
        
        
        
        
        window hide 
        nvl clear 
        
        #if it was perfect, then you wouldn't need to release it, right?
        
        #"I drift off to the sound of the rain."
        
        #The rain helps me drift off to sleep.
        
        #I'd like to say I feel lost. But I've never felt found. 
        
        #My friend's online, though. You'll have to buy an account.
        
        
        #first choice to message her then second to buy an account on the day? 
    menu: 
        
        "Buy an account":
            jump Dan1y
            
        "Save the cash":
            jump Dan1n
        
        #(yes/no)
        
    label Dan1y:
        
        t"L0stc4us3: Sure. I'd rather play the game than fight you."
        
        t"x-Destiny-x: See you around, noob."
        
        
        window hide 
        nvl clear 
        
        scene room_boy16_day with longf
        
        #"Well, I'm going to buy the account anyway. I might as well head down early."
        
        "I might as well head down early. I'm going to buy an account anyway."
        
        scene school_in004_day with slowf
        
        "It's not open yet. I knock and get no response."
        
        "I spot that strange teacher dawdling down the corridor."
        #He wears a furrowed brow as he approaches;
        "His pensive expression accentuates his slim jawline and the lines of age in his cheeks."
        
        "What was his name again...?"
        
    menu: 
        
        "Mr Adams":
            jump MrAdams
            
        "Mr Brent":
            jump MrBrent
        
        "I've forgotten":
            jump forgotten 
            
            
    label MrAdams:
        
        p"\"Hey, Mr Adams.\""
            
        "He looks up and raises his brow."
         
        mb"\"No, wrong person; I'm Mr Brent.\""
            
        p"\"Ah, sorry.\""
        
        jump Dan1yy
        
    label MrBrent:
        
        p"\"Hey, Mr Brent.\""
            
        "His face melts into a smile as he looks up."
         
        mb"\"I'm surprised you remembered.\""
        
        p"\"Yeah. We're the new guys.\""
        
        "I fail to mention that he's eccentric or the fact there's a lot of new students even when you disregard the first years."
        
        jump Dan1yy
        
    label forgotten:
        
        "I wait until he's close."
        
        p"\"Hey, Mr...\""
        
        mb"\"Mr Brent.\"" #even if it is Saturday. You may aso refer to me as sir.\""
        
        "I offer an awkward smile."
        
        p"\"Sorry, sir.\""
        
        jump Dan1yy
        
    label Dan1yy:
        
        p"\"Can I access the computers?\""
        
        "He unlocks the door."
        
        mb"\"Certainly.\"" #Just make sure to use the computer you were on last time.\""
        
        #"He unlocks the door and 
        
        #p"\"Will do, thank you.\""
        
        scene Computer_Room with slowf
        
        mb"\"I'll log you in.\""
        
        
        "He takes me to the far computer and logs it in."
        
        mb"\"I'm busy, so I must be right back.\""
        
        "He measures me for a moment."
        
        mb "\"Don't let the other teachers know I left you alone in here.\""
        
        p "\"I'll keep it under wraps. Thank you, sir.\""
        
        "Maybe he's not so weird, after all."
        
        "He leaves and I begin creating and purchasing an account."
        
        #play music "audio/music/bensound-thejazzpiano.mp3" fadein 6.0
        scene Computer_Room with slowf
        
        d"\"You're early.\""
        
        "I jump to her voice." 
        
        show D 1YSerious_Flat at PC1 with slowd
        
        #"I was getting into it; I didn't notice Mr Brent and the other teachers enter either."
        "I was caught up in creating my account; I didn't notice Mr Brent and the other teachers enter either."
        
        p"\"I thought I may as well buy an account and get started.\""
        
        d"\"Good. You're going to need to put some time in if you ever want to surpass noobhood.\""
        
        p"\"Don't worry, I'm going to beat you one day.\""
        
        #p"\"Don't worry, I'm going to beat you.\""
        
        
        
        #"Her lips curve into a smirk."
        
        show D 1YSerious_Smirk at PC1 with slowd
        
        d"\"I'm waiting.\""
        
        hide D 1YSerious_Smirk  with slowd
        
        "She sits down on the other computer and logs into the game."
        
        d"\"I have a low level Viktese Warrior. I could help you through some low level content if you like.\""
        
        p"\"Sounds good.\""
        
        d"\"Join my friends talk.\""
        
        p"\"Why? We can speak.\""
        
        d"\"Because then you can see the markers I place.\""
        
        p"\"Oh, I see.\""
        
        stop music fadeout 3.0
        
        #d"\"Because the game displays messages about the people you're with.\""
        
        t"I follow the marker she sets and it leads me to a cave." with slowd
        
        play music "audio/music/myuu - It_s Not Over Yet.mp3" fadein 5.0
        
        t"I enter on my guard..."
        
        t"It's a small opening with numerous passageways leading off into darkness."
        
        #"I follow a tunnel and end up back where I started," I won't be long.
                                    
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Wait up. I'm just messaging my friend.\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"I'm already inside.\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"I know. Don't die.\""
        
        #tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"I'll be fine.\""
        
        #FFS!
        
        window hide 
        nvl clear 
        
        t"I refresh my memory of the controls—my sword strikes the wall and draws the attention of nearby rats."
        #I trigger a trap and rats flood out of the tunnels to attack. 
        t"More scurry from the depths of the tunnels."
        
        t"I hack and slash them but they're tough. I find myself pressed up against the wall."
        
        t"That's when I notice... {w}my health is low!"
        
        t"I watch my character twist and drop to the ground in dramatic fashion."     
        
        #get trapped on a wall and die to a mob of rats. XD 
        
        #window hide 
        #nvl clear 
        
        stop music fadeout 3.0
        
        #"My death leaves a message in the clan talk, \"L0stc4us3 died to: rat.\"" with slowd
        "A message appears in the clan talk, \"L0stc4us3 died to: rat.\"" with slowd
        
        window hide 
        nvl clear 
        
        "Danielle slaps her palm against her forehead, releasing a sigh."
        
        show D 1Closed_Flat at PCM1 with slowd
        
        d"\"You really are a noob.\"" 
        
        #d"\"Did you just die to a rat?\"" 
        
        #d"\"Did you just die to a rat?\"" 
        
        p"\"There were seven of them…\""
        
        show D 1YSerious_Flat at PCM1 with slowd
        
        d"\"You died to a rat...\""
        
        #show D cnormal with slowd
        
        #"I have no comeback so I hang my head in shame."
        
        d"\"Hurry. I'll wait outside.\""
        
        "Having no comeback, I do as she says."
        
        hide D 1YSerious_Flat with slowd
        
        window hide 
        nvl clear 
        
        t"I make it back and follow Danielle's lead; she assures to not get cornered by enemies." with slowd
        
        #"We defeat the rats with e\ase and move on."
        
        t"We explore the labrinth, sharing the loot we obtain, before coming to a halt at a force field."
        #acquiring loot
        #d"\"Ready?\""
        
        #p"\"What for?\""
        
        #d"\"There's a boss in the next room.\""
        
        #p"\"Let's do it.\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Ready?\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"What for?\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"There's a boss in the next room.\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"We got this.\""
        
        window hide 
        nvl clear 
        
        
        #"I say that but there's a fear of dying niggling me." #I don't want to let her down, and I don't want to be called noob again."
        
        t"I say that, but the thought of dying again is niggling me."
        
        t"She jams a gem into the terminal and the force field dissipates." #ceases #evaporate
        
        t"I steel myself and follow with caution..."
        
        t"...An empty cavern."
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Keep your health high.\""
        
        
        #myuu - it's not over yet


        #play music "audio/music/myuu - It_s Not Over Yet.mp3"
        
        play music "<from 68>audio/music/myuu - It_s Not Over Yet.mp3" fadein 4.0


        #wall crashing sound effect?
        
        window hide 
        nvl clear 
        
        #"A cutscene plays of a giant rat crashing through the wall."
        
        t"A giant rat crashes through the wall." with slowd
        
        t"The cutscene flings us into action and I dodge debris falling from the ceiling."
        
        #d"\"You take the left; I'll go right.\""
        
        #nvl names
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Take the left, I'll go right.\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"On it.\""
        
        
        t"It lunges at Danielle so I take the opportunity to strike its rear."
        
        #d"\"Good job.\"" #<—?
        
        t"It sweeps around and I avoid its claw. I run around the edge of the room and Danielle strikes it."
        
        #swimgs around
        
        window hide 
        nvl clear 
        
        t"A few more strikes and its health nears half of its bar."
        
        #p"\"This isn't too bad.\"" # or "This is easy."
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"This isn't too bad.\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Don't die.\""
        
        t"My blow lowers it below half health." 
        
        #d"\"Don't die.\""
        
        
        
        #"She snickers."
        
        t"It screeches in rage and slams the ground; I'm caught in the shockwave."
        
        t"Damn, it nearly killed me."
        
        window hide 
        nvl clear 
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"But seriously, don't.\""
        
        
        t"I flee, spamming apples." #health potions." # in panic
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"No pressure.\""
        
        #"I can't heal fast enough."
        #t"I can't eat them fast enough."
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Attack it!\"" 
        
        t"Danielle's cornered. I strike it in the nick of time."
        #at the critical moment
        
        
        #"I gather my bearings and notice it's coming for me."
        #You could have it where he buys some shit food coz it's cheap and he's spamming apples XD
        
        window hide 
        nvl clear 
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Run! The agro's switched.\""
        
        
        t"I sprint, again spamclicking my apples. I can't eat them fast enough" #spamming health potions."
        
        
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"What food are you using?\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Apples.\""
        
        #"I hear her release a sigh."
        
        t"I hear a sigh behind me."
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Keep it busy until I'm charged and run past me.\""
        
        window hide 
        nvl clear 
        
        t"I trail it along the walls."
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Now!\""
        
        t"I lure it past Danielle and she unleashes a barrage of blows into its side."
        
        t"It shrieks and rolls onto its back."
        
        
        stop music fadeout 3.0
        
        window hide 
        nvl clear 
        
        show D 1YSerious_Flat at PCM1 with slowd
        
        d"\"Good job, noob.\"" #with slowd
        
        "Dammit."
        
        p"\"Thanks, not bad yourself.\""
        
        #show D cSER with fastd
        show D 1YSerious_Smirk at PCM1 with slowd
        
        "She rolls her eyes and cracks a smile."
        
        d"\"That's where I expected you to die, not entering the cave.\""
        
        p"\"Alright, you don't have to rub it in.\""
        
        d"\"Oh, but I do.\""
        
        p"\"How are you even supposed to kill that thing alone, anyway?\""
        
        show D 1YSerious_Flat at PCM1 with slowd
        
        d"\"Boosters help.\"" #, it's easy to solo.\""
        
        p"\"Ah, yeah. I forgot about them.\""
        
        d"\"Anyway, come on. There's loot through the wall it broke through.\""
        
        hide D 1YSerious_Flat with fastd
        
        t"There's two chests waiting for us, so we loot one each." with slowd
        
        #td"\"Oh wow, I got a rare sword.\""
        
        #tp"\"Is it good?\""
        
        #td"\"No. Well yes, at this level.\""
        
        #td"\"Here.\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Oh wow, I got a rare sword.\""
        
        tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Is it good?\""
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"No. Well yes, at this level.\""
        
        t"She sends a trade request."
        
        td" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Here.\""
        
        #tp" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"We've got this.\""
        
        
        
        
        window hide
        nvl clear
        
        p"\"Thanks. Why'd you give it me?\"" with slowd
        
        d"\"You need it more than I do.\""
        
        #"..."
        "I don't know whether to take it as a present or an insult..." # 
        
        p"\"Thanks.\""
        
        #d"\"Up for another?\""
        
        #p"\"Sure.\""
        
        "We make our way back into town."
        
        d"\"What posessed you to only bring apples?\""
        
        p"\"They're five gold each and heal twenty HP; the cheapest potions were fifty gold and only healed one-hundred and twenty.\""
        
        d"\"Because potions can save your life in certain situations.\""
        
        #"Her brow lifts."
        
        "I match her lifted brow."
        
        p"\"Hey, I didn't die.{w} At the boss...\""
        
        "I'm quick to add."# my insurance." #I need to protect myself
        
        #d"\"No, you died to a rat...\""
        
        "She shakes her head in dissaproval."
        
        d"\"Cheap ass. You're buying potions now.\""
        
        #d"\"I'll give you that, but you're buying potions now.\""
        
        p"\"I will, but you didn't tell me how to gear. How do you expect me to know?\""
        
        d"\"Apples could've saved you from a rat.\""
        
        #p"\"I will yo, but you didn't tell me how tha fuck ta gear yo. How tha fuck do you expect me ta know?\""
        
        #d"\"Applez coulda saved yo biiiatch ass from a rat.\""
        
        "I concede to my stupid death."
        
        d"\"I'll take you through town before the next.\""
        
        #fade in/out
        scene Computer_Room with slowf
        
        
        "We complete another. This time, I didn't die."
        
        show D 1YSerious_Flat at PCM1 with slowd
        
        d"\"Good job, noob. You're improving.\""
        
        p"\"Thanks...\""
        
        "Something just irritates me when she calls me noob."
        
        "But it's nice to actually recieve some praise from her."
        
        d"\"I can't deny it was fun, either.\""
        
        d"\"I need to go to a clan event, though.\""
        
        p"\"Oh, OK. Thanks, it was fun.\""
        
        hide D 1YSerious_Flat with slowd #save test
        
        "We stay in the staffroom until the teachers are ready to leave." #level up as much as I can."
        
        #show SA1 YouSad_Smile: 
        #zoom 5.0
        
        #show SA1 YouSad_Smile:
        #zoom 0.5 xalign 0.5 yalign 0.5
        #linear 5 zoom 5.0
        
        
        "I've gained quite a few levels, but I felt left out being too low to join her clan..."
        
        
        
        
        
        
        
        
        
        #Danielle Act One Custard
        
        scene Internet_Cafe with longf 
        
        t"Everyday after class I've been heading down to this Internet_Cafe I found to train my account." with slowd
        
        t"I've found that 4-5pm of Danielle's afterschool schedule consists of raiding with her clanmates."
        
        t"With my account coming into mid-level, our compatible content has decreased to nothing."
        
        t"I thought I'd get closer by sticking at it, but now it feels so far before I can play with her again."
        
        "x-Destiny-x: Bye." with slowd
        
        "I notice her message in the chat. It's 4:29pm." #16:29
        
        window hide
        nvl clear
        
        t"L0stc4us3: Where are you going?" with slowd
        
        t"x-Destiny-x: I'm heading into town."
        
        t"L0stc4us3: Just so happens I'm in the Internet_Cafe on Long Rd."
        
        t"x-Destiny-x: I'm going to Pot Kettle Black."
        
        t"x-Destiny-x logged out."
        
        window hide 
        nvl clear
        
        "..." with slowd
        
        #"She's logged out..." with slowd
        
        
        play music "audio/music/bensound-tenderness.mp3" fadein 4.0
        
        scene restaurant03_day with longf
        
        "After some trouble finding the place, I find her at the back alcove with a strawberry and chocolate icecream in a parfait glass."
        
        scene DCG 1Gentle_Flat with slowd
        
        p"\"Y'know, I didn't exactly expect you to go for an icecream.\""
        
        #show D cnarrow with slowd
        
        d"\"If I was alone, then I could eat icecream without being questioned for it.\""
        
        p"\"Should I go?\""
        
        scene DCG 1Gentle_Grin with slowd
        
        "{i}That{/i} smirk."
        
        d"\"Yeah, go order something.\""
        
        scene restaurant03_day with slowf
        
        "I order a ham and cheese toastie, caught up in a thought as I make my way back."
        
        scene DCG 1Gentle_Flat with slowd
        
        p"\"You barely had time to meet me on the roof but you're here ordering ice cream?\""
        
        #show D cAC with slowd
        
        d"\"A schedule isn't all work. You need breaks, and you need to reward yourself, too.\""
        
        p"\"And all it takes is some gaming and a little ice cream?\""
        
        d"\"If you can't enjoy the simple things, then you'll be waiting a long time.\""
        
        #show D cnormal with slowd
        
        d"\"What do you enjoy?\"" 
        
        "She asks as the waiter places down my meal."
        
        p"\"Magnum Dilon and ham and cheese toasties, I guess.\""
        
        scene DCG 1Gentle_Grin with slowd
        
        "She offers a smirk that says {i}point proven{/i} and eats a scoop of ice cream."
        
        d"\"I see you've been levelling up pretty quickly.\""
        
        d"\"You might even be ready to face me soon, noob.\""
        
        p"\"Gonna stop calling me noob when I beat you?\""
        
        "I’m beginning to enjoy her smirk."
        
        d"\"I might if you hurry, noob.\""
        
        p"\"Well, after all, beating you is something I'd enjoy.\""
        
        d"\"I'd enjoy—\""
        
        scene restaurant03_day 
        
        show J 2YHappy_Grin at PCR1
        
        show D 1YGentle_Flat at PCL1
        
        with slowd
        
        j"\"What are you guys doing here together?!\""
        
        "{i}Just as we're finally spending time together...{/i}"
        
        d"\"He happened to be town and I was coming here.\""
        
        j"\"Shouldn't you be on an epic quest?\""
        
        show D 1YSerious_Flat with slowd
        
        "Jennifer's wink raises a scowl from Danielle." #evokes #raises a brow
        
        d"\"Shouldn't you be playing Cupid?\""
        
        #I am!
        
        #You should take this more seriously.
        
        #I've left them to it. And I'll leave you both to it. #What about knight etc?
        
        show J 2YHappy_Smile with slowd
        
        j"\"I've left them alone together.\""
        
        d"\"Again?\""
        
        j"\"Yeah, I'm only getting in the way.\""
        
        d"\"You do know he likes you, right?\""
        
        j"\"I...\""
        
        show J 2YHappy_Grin with slowd
        
        "Jennifer gives her statement some consideration before her grin resumes."
        
        j"\"He's not my knight.\""
        
        "She delivers it with a wink and Danielle rolls her eyes."
        
        d"\"You should take this more seriously.\""
        
        "Jennifer shrugs."
        
        j"\"I'll leave it to them. And I'll leave it to you.\""
        
        hide J 2YHappy_Grin with moveoutright
        show D 1YSerious_Flat at PC1 with move
        
        p"\"Later.\""
        
        "She's gone as fast as she appeared."
        
        p"\"Are you sure she doesn't know you play it?\""
        
        d"\"I'm confident.\""
        
        p"\"Why?\""
        
        show D 1Closed_Flat with slowd
        
        d"\"Believe me, you'd know.\""
        
        show D 1YSerious_Flat with slowd
        
        "She inspects her phone."
        
        d"\"Eat up, I'm heading back soon.\""
        
        #p"\"I'll come with.\""
        
        scene street001_day with slowf
        
        "Knowing she's not about to make conversation, I release a question on my mind."
        
        p"\"What are the fastest ways to train at level 15?\""
        
        d"\"You can kill Breals at the bottom of Julagga Mountains which is chill. But if you want the fastest XP, you'll need to focus on Bragens at the top.\"" 
        
        d"\"You should go kill Gloastrians at level 23; you'll find them nearby the Salt Sea.\""
        
        #"I have a vision of Jennifer hearing that, and I have to check aroud to make sure she's gone."
        
        p"\"Thanks.\""
        
        "I have a vision of Jennifer hearing that and look around. Danielle follows in my caution."
        
        
        p"\"Bet you're glad Jennifer wasn't here to hear that.\""
        
        "She shakes her head."
        
        d"\"You should be glad, too.\""
        
        "..."
        
        p"\"I'll see you tomorrow. I'm gonna train for a few hours.\""
        
        d"\"Bye.\""
        
        ### Unready Raid
        
        stop music fadeout 3.0
        
        scene Internet_Cafe with longf
        
        "I take Danielle's advice and find the expierence rates much faster."
        
        "And I'm only doing the \"chill\" method."
        
        "x-Destiny-x: Noob, where are you?"
        
        "L0stc4us3: I’m training in the Julagga mountains."
        
        "x-Destiny-x: Come join our raid."
        
        "{i}She must be a player short or something...{/i}"
        
        "L0stc4us3:The monsters are way too high for me."
        
        "FauxCuss: Not sure if you’re smoking the same shit as them; all you have to do is lure and dodge."
        
        "x-Destiny-x: Shut up, Luke. You’ll be fine, come on."
        
        "I take the comment on the chin with Danielle’s reassurance." #Both messages arrive at the same time. 
        
        "L0stc4us3: Fine."
        
        scene Internet_Cafe with longf
        
        #Danielle won't tell them bout Peter being being in the same school yet. (until he gets a VPN XD)
        
        "{i}One thing I've learnt....{/i}"
        
        "L0stc4us3: I really need to level up."
        
        "x-Destiny-x: Yeah, noob."
        
        "L0stc4us3: I swear I'm going to beat you..."
        
        "x-Destiny-x: Noob, hurry up. ;)"
        
        
        scene street001_night_light with slowf
        
        "I've stayed up way too late. I can't believe that place stays open until 11pm."
        
        "But I've made some good progress."
        
        
        #Have a scene in class with Danielle? 
        
        
        ### Peter wagging it 
        
        play music "audio/music/sumumfachunk uninspired.ogg" fadein 4.0
        
        scene room_boy16_evening with longf
        
        ##I got back late, the Internet_Cafe doesn't shut until 11pm. And they're half price after 8pm." (20% discount being a student? Xd)
        
        "I haven't slept well. I've been up most of the night coughing. All I want to do is sleep."
        
        scene black with slowd
        
        "The decision reels through my mind."
        
        scene room_boy16_evening with slowd
        
        "I force myself up, locating the attendance number and adding it into my contacts."
        
        "I stare at the number, my fingers flex and it's dialling..."
        
        "I fake a few coughs as a woman's voice breaks the ringing tone."
        
        q"\"Good morning, you're through to Janette on the Sunnyvale attendance line. How can I help you today?\""
        
        p"\"Good morning, I'm Peter. I'm feeling a little under the weather today.\"" 
        
        q"\"Can I take your student number?\""
        
        p"\"I'm in Mrs Brown's class.\""
        
        q"\"Sorry, but I would need to take your number.\""
        
        "I fake some coughs as I rummage through my paperwork."
        
        p"\"...It's 123117.\""
        
        scene room_boy16_evening with slowf
        
        "{i}It's done.{/i}"
        
        scene black with slowd
        
        "I snuggle in my sheets."
        
        "But lack of sleep gives my brain time to rearrange priorites."
        
        "..."
        #sneaking out here
        
        scene school_out003_day with slowf
        
        "I keep my hood up and my head down." 
        
        "I make sure to keep my ID on show; I imagine they're told to question anybody without one."
        
        scene Internet_Cafe with slowf
        
        #"I'm too tired to focus today, but Danielle's AFKable suggestion is noticeably faster..."
        
        "After an energy drink, Danielle's focus suggestion is noticeably faster."
        
        scene room_boy16_evening with longf
        
        "I open my eyes and hover my finger over the call button."
        
        "{i}No.{/i}"
        
        "I’ve already called in sick..." 
        
        "{i}But...{/i} {w}it {i}would{/i} be more believable if I take another day off." #But another day won’t hurt. 
        
        "It'd also give me time to get {i}\"better\"{/i} over the weekend."
        
        "And {i}I’ll{/i} actually be useful if I’m able to equip boosters and the steam hammer..." 
        
        #Still convincing himself at the Internet_Cafe? XD
        
        "...And I can also get it done by tonight if I focus grind all day..."
        
        stop music fadeout 3.0
        
        scene room_boy16_day with longf
        
        "Saturday's arrived. I haven't spoken to Danielle since Wednesday."
        
        "I've had my private chat off..."
        
        "She doesn't really talk to me in class or when raiding, anyway."
        
        "But still, I'm a little worried about how she'll take my absense..."
        
        
        scene Computer_Room with slowf
        
        "I arrive at the computer room, expecting to see Danielle at a computer by the back but she's not there."
        
        "But I notice a familiar grey coat."
        
        p"\"Hey, Mr Brent. Where's Danielle today?\""
        
        "He spins in his chair and shrugs."
        
        mb"\"She hasn't been by today. But you're welcome to use the computers.\""
        
        "Danielle's not here? {i}Where could she be?{/i}"
        
        p"\"Thanks, I'll come back later.\""
        
        mb"\"Off to find Danielle?\""
        
        "His smile makes me want to deny I'm curious..." 
        
        "...but I haven't received a reply from her since this morning."
        
        #"I can't deny that I'm curious but I don't even know where her dorm is..."
        
        p"\"Not sure if I can.\""
        
        mb"\"I'll give you a hint: Danielle might be more creative than you think.\""
        
        scene school_in004_day with slowf 
        
        "{i}More creative than I think...?{/i} I don't even know where to begin."
        
        #Maybe have some eqed piano here that stop when he opens the door.
        
        #"A piano melody bleeds through the music room's door."
        
        #"...A piano melody echoes from the music room."
        
        "...A piano melody echoes down the corridor."
        
        #show scene black with slowd
        
        "{i}The music room.{/i}"
        
        "The door yields with a creak."
        
        scene school11_day with slowf
        
        "Danielle turns to me, lifting her fingers from the keys."
        
        show D 1YSerious_Flat at PC1 with slowd
        
        d"\"What are you doing here?\""
        
        p"\"I heard music... I thought you'd be at the staffroom.\""
        
        d"\"I was going to go soon. I've just... fallen behind.\""
        
        "Her tone leaks with guilt." 
        
        p"\"I just didn't expect you to play.\""
        
        "{i}Or fall behind...{/i}"
        
        d"\"Not many do.\""
        
        p"\"Would you play that piece for me?\""
        
        "Her eyes flicker in consideration."
        
        #show D cnormal with slowd
        
        d"\"You'd better not laugh.\""
        
        "A smile slithers onto my lips."
        
        p"\"Now I already want to.\""
        
        show D 1YAngry_Flat with slowd
        
        "If looks could kill..."
        
        p"\"OK, I promise.\""
        
        "I hold my hands up and surrender my smile." #up in surrender 
        
        play music "audio/music/Mixed5 (1).ogg" fadein 3.0
        
        hide D 1YAngry_Flat with slowd
        
        #what song?
        
        #piano snip kevin macleod? 
        
        #"She nods and readies her fingers on the keys." 
        
        t"She takes a deep breath and meets the keys with her fingers." with slowd
        
        t"Her lips ease as the melody begins, her foot tapping the tempo."
        
        t"I'm not sure what I thought her secret was to begin with, but it wasn't {i}this.{/i}" # don't know what
        
        t"She rocks back and forth, captured by her music."
        
        t"I'm captivated by {i}her{/i}..."
        
        window hide 
        nvl clear 
        
        #fade out both music and scene
        
        stop music fadeout 3.0
        
        #scene school11_day with longf
        
        p"\"...Wow.\"" with slowd
        
        show D 1YSerious_Flat at PC1 with slowd
        
        d"\"It's nothing.\""
        
        "Her face betrays her with a notch of red. I'm wary of the smile threatening to creep on my lips."
        
        p"\"You wrote that?\""
        
        d"\"Yeah. But it's not finished.\""
        
        p"\"I {i}really{/i} do like it.\""
        
        show D 2YGentle_Flat with slowd
        
        "She calms; her shoulders fall slack."
        
        d"\"Thanks.\""
        
        p"\"Wait, if Jennifer didn't know you still game, was she was going to suggest that I could play music with you on my first day?\""
        
        "Her eyes drop for a moment."
        
        d"\"Yep. This was it. At least she doesn't try to tease me in public for this.\""
        
        p"\"It's not something to be embarrassed about.\""
        
        d"\"I was just never good enough.\""
        
        "She states it as a trivial fact."
        
        p"\"You're very good. Haven't you thought about making music for your game?\"" #You could even create music for your game.\""
        
        d"\"Maybe, one day.\""
        
        #she questions him now?
        
        show D 1YSerious_Flat at PC1 with slowd
        
        d"\"Why weren't you in class?\""
        
        "She turns the topic on its head with a narrowed brow. {w}I'd almost forgotten..."
        
        p"\"I was ill.\""
        
        d"\"You don't look ill now.\""
        
        #"{i}I wasn't...{/i}"
        "Her probing questions evoke a pang of guilt."
        
        p"\"I'm feeling quite a lot better today after some sleep.\""
        
        d"\"Oh, really. Did you get to level twenty-four in your sleep?\""
        
        #"Her probing questions evoke a pang of guilt."
        "{i}Red-handed.{/i}" #"I feel like I've been caught red-handed."
        
        p"\"I thought I might as well train with the time off.\"" 
        
        show D 1Closed_Flat with slowd
        
        "She sighs and shakes her head."
        
        #"She ponders for a moment and sighs, shaking her head."
        
        d"\"I'd tell Mrs Brown that you're going to make up for it, if you know what's good for you.\""
        
        p"\"I will. I'll dedicate Monday and Tuesday night to make up for it.\""
        
        show D 1YSerious_Flat at PC1 with slowd
        
        d"\"Good.\""
        
        p"\"But c'mon, we might aswell do some raids now that I can be useful.\""
        
        #"A smile breaks her lips."
        
        #d"\"Wanna do a raid, noob?\""
        
        #p"\"Sure. I've got boosters and I can use the Steam Hammer now.\""
        
        show D 1YSerious_Smirk at PC1 with slowd
        
        "She smirks and shakes her head."
        
        d"\"If you use any more school time to train, then I'ma call you noob forever.\""
        
        p"\"Deal.\""
        
        d"\"C'mon, noob.\""
        
        #Danielle Raids Scene Custards
        
        scene Computer_Room with slowf
        
        d"\"Meet at Horthorpe Tavern.\""
        
        p"\"That's miles away, I've left myself by the dungeons.\""
        
        d"\"We always meet here, sharing drinks at the tavern fortifies health by ten percent for an hour after you leave.\""
        
        p"\"Oh...\""
        
        window hide
        nvl clear
        
        scene Computer_Room with slowf
        
        t"The pressure builds as I continue to miss chances to take out the Rillifers."
        
        t"FauxCuss: Fuck, who invited this noob?" #FauxCuss #Adam
        
        t"x-Destiny-x: Give him a chance, it's his first time as an attacker."
        
        t"I message her in private, it'd feel weird to say it aloud."
        
        window hide
        nvl clear
        
        "L0stC4us3: Doesn't he remember me?" with slowd
        
        "x-Destiny-x: Apparently not."
        
        "L0stC4us3: Doesn't your clan know I'm your friend IRL?"
        
        "I take a glance. But she continues in text."
        
        "x-Destiny-x: I'll speak to you later."
        
        "..."
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        
        
        scene room_boy16_night_light with longf
        
        "I just {i}can't{/i} focus on my school work."
        
        "There's extra homework this week, too..."
        
        "{i}No rest for the wicked.{/i}"
        
        play sound "audio/sfx/short vibrate.mp3"
        
        #I try to focus but my mind is everywhere else. 
        
        #I want to play Magnum Dilon. I want to... see Danielle.
        
        t"x-Destiny-x: You'd better not be slacking, noob." with slowd
        
        "I'm pleasantly surprised she'd check on me." with slowd
        
        t"L0stC4us3: Don't underestimate the noobking. I'm coming for you soon."
        
        t"x-Destiny-x: lol noob." 
        
        window hide
        nvl clear
        
        #You'd better not laugh.
        
        #"I didn't really think she'd hold me to this." 
        
        "I don't want to let her down." with slowd
        
        "And I'm not sure I'd surive the wrath of both Mrs Brown and Danielle..." #I don't think
        
        "Homework looks a little more appealing all of a sudden."
        
        "..."
        
        #Part one of Danielle's arc 
        
        #time skip
        
        scene room_boy16_night_light with slowf
        
        "Ugh, I'm not accustomed to this. I've at least hit the criteria for each question."
        
        "It's 22:34. I wonder if she's still awake."
        
        t"L0stC4us3: Done."
        
        t"x-Destiny-x: Good."                    
        
        "A few minutes pass and I'm certain that's all she's going to say."
        
        "I just can't leave it at that."
        
        t"L0stC4us3: Be ready, noob."
        
        t"x-Destiny-x: Pfft. You better be ready to fight me with talk like that." 
        
        "We both know I'm not ready."
        
        t"L0stC4us3: Give me a week..."
        
        t"x-Destiny-x: Hurry up!"
        
        window hide
        nvl clear
        
        t"x-Destiny-x: Good night." 
        
        t"L0stC4us3: 'Night."
        
        window hide 
        nvl clear
        
        "I wasn't expecting her to say goodnight. Maybe in some roundabout way, we're becoming friends." with slowd
        
        window hide
        nvl clear
        
        "Well, I'd better get an early night, rested for a grind after school tomorrow..."
        
        scene black with longf
        
        
        #Missing Pieces https://www.youtube.com/watch?v=z7GH8ikf2ps
        
        #sepia beach? - Sand castle image with black lines?
        
        play music "audio/music/Missing_Pieces.mp3" fadein 4.0
        
        scene beach02_day_sepia with slowd
        
        "Warm rays lay on my skin, a cool breeze meets my nose with a salty fragrance."
        
        scene beach02_day with slowd
        
        #"Warm rays lay on my skin, a cool breeze meets me with a salty fragrance."
        
        #The scent of the beach
        
        "I place down the last castle and revel in our creation."
        
        pd"\"Good job, high five!\""
        
        
        
        "I make two legged finger men and duel on the battlements."
        
        pm"\"Peter! Here’s your ice cream.\""
        
        "{i}Ice cream!{/i}"
        
        pm"\"This one's for my little architect.\""
        
        p"\"Thank you, mummy!\""
        
        pm"\"This one's for me.\""
        
        pm"\"None for daddy!\""
        
        pd"\"I helped, too!\""
        
        #pm"\"This one's for daddy.\""
        
        #"Mummy licks his ice cream."
        
        #fade back in
        
        scene beach02_day with slowf
        
        "{i}Delicious.{/i}"
        
        "With my ice cream finished, I'm ready to play."
        
        p"\"Where's daddy?\""
        
        "Water sprays up my back and the question is answered."
        
        pm"\"Run!\""
        
        "We take cover behind the sand castle."
        
        #pm"\"His weak spot is his back. I’ll distract him and you get him!\""
        
        "Mummy pulls out some water bombs and water pistols."
        
        pm"\"I’ll distract him and you get him!\""
        
        "A sand tower crumbles from water gun fire."
        
        pm"\"Go go go!\""
        
        "She lobs a water bomb over the battlements and runs in."
        
        #(noises here?)
        
        "I take the opportunity to flank him and throw my water bomb."
        
        pd"\"Hey!\""
        
        "{i}Missed!{/i} He turns his sights on me."
        
        "I flee and fire my water gun aimlessly behind me."
        
        pd "\"You're not getting away that easily!\""
        
        "He catches me in his arms and we tumble to the ground."
        
        stop music fadeout 2.0
        
        scene beach02_day_sepia with fastd
        
        scene black with slowd
        
        scene room_boy16_evening with slowd
        
        "My body jolts me into consciousness."
        
        "I tame my breathing and calm myself."
        
        "That... {i}felt so real.{/i}"
        
        #He'll have some ice cream next time he's out. 
        
        #scene change - Internet_Cafe or class?
        
        play music "audio/music/sumumfachunk uninspired.ogg" fadein 3.0
        
        scene Internet_Cafe with longf
        
        t"I can't stop thinking about that dream. I've had so many vague nightmares..." with slowd
        
        t"{i}But was that really my past?{i}"
        
        t"{i}A memory...?{/i}"
        
        nvl clear
        window hide
        
        "x-Destiny-x: Noob, how did you even die there?" with slowd
        
        "L0stC4us3: Sorry, zoned out."
        
        "x-Destiny-x: You're lucky we'd already taken out the boss."
        
        "FauxCuss: Focus, man!"
        
        "L0stC4us3: I'ma call it for today."
        
        "x-Destiny-x: Too much of a noob?" 
        
        "L0stC4us3: I was training to beat you, you're distracting me."
        
        "FauxCuss: Ha! I'd pay to see that."
        
        "x-Destiny-x: You didn't have to come." 
        
        "L0stC4us3: Later."
        
        "I leave her friends chat to train alone with my thoughts."
        
        #scene skip to dark outside
        
        scene street001_night_light with slowf
        
        "{i}I thought it'd distract me from my thoughts.{/i}"
        
        "My mind's scrambled."
        
        "Maybe it's because of this gaming with her that I even had that dream?" 
        
        "I'm determined to beat her. I could get the levels I need in a few days."
        
        "This noob thing can work to my advantage; if she doesn't know what I'm capable of, I might bypass her defence."
        
        "I'll only get one shot... I'll need to practice once I'm ready."
        
        stop music fadeout 3.0
        
        "But... {i}who with?{/i}"
        
        #timeskip Xd
        
        scene Internet_Cafe with longf
        
        "FauxCuss: Sure."
        
        "L0stC4us3: Really?"
        
        "I was expecting an insult."
        
        "FauxCuss: If Danielle insists on raiding with you, then you need to carry your own weight."
        
        "..."
        
        play music "audio/music/bensound-extremeaction.mp3" fadein 2.0
        
        scene Internet_Cafe with slowf
        
        #"FauxCuss: How long do you think we have?"
        
        #"L0stC4us3: That bad?"
        
        "I try to dodge his swing and he catches my side."
        
        "FauxCuss: Block!"
        
        "His attitude is grinding my gears."
        
        "L0stC4us3: Right."
        
        "I block his blow and dodge his swipe."
        
        "FauxCuss: Now, Danielle likes to..."
        
        "He boosts to my side and delivers a long slash."
        
        "FauxCuss: Cleave her enemies. "
        
        "L0stC4us3: How can I counter it?"
        
        "FauxCuss: How long do you think we have?"
        
        "L0stC4us3: Two days."
        
        #"L0stC4us3: "
        
        "FauxCuss: I'm not that committed. Couple hours tonight and tomorrow night."
        
        "But I can't deny his help right now. And Danielle will be offline in that time."
        
        "L0stC4us3: Alright. Thanks."
        
        "He boosts and I boost backwards as he slashes."          
        
        "FauxCuss: Your reactions could be workable at least."
        
        "I boost in and slash, catching a critical on his leg."
        
        "L0stc4us3: Let's do it."
        
        "He avoids my next swing and thrusts his sword through my back."
        
        stop music fadeout 3.0
        
        "{i}...{/i}"
        
        "FauxCuss: Don't get cocky. C'mon, there's a few strategies for each map."
        
        #stop music fadeout 3.0
        
        scene Computer_Room with longf
        
        #Corridor scene first? 
        
        show D 1YSerious_Smirk at PCM1 with slowd
        
        d"\"So, today's the day?\""
        
        p"\"Today's the day you stop calling me noob.\""
        
        d"\"We'll see.\""
        
        hide D 1YSerious_Smirk at PCM1 with slowd
        
        "I shake the nervousness off and set myself up; but I can't budge the unease in my stomach."
        
        "{i}Why am I so nervous?{/i}"
        
        centered "3... 2... 1... Fight!"
        
        #play music "audio/music/"   
        
        #play music "audio/music/bensound-epic.mp3" 
        
        play music "<from 55.75>audio/music/Malicious.mp3" #fadein 2.0
        
        #play music "<from 54.7>audio/music/Malicious.mp3" fadein 2.0
        
        #play music "<from 65.7>audio/music/Fruhlingsblute.mp3" fadein 4.0
        
        t"We're summoned to the cityscape." with slowd
        
        t"We're both cautious in the approach, gliding past the edge of corporate buildings until we meet on the main street. "
        
        t"She taunts, her character brandishing her bastard blade. I rush in, attempting to catch her off guard during the animation."
        
        t"She anticipates and counters with a Vicious Cleave. The blow pierces my armour, dealing additional damage."
        
        t"I don't falter, engaging her and landing a few blows in her stomach chinks."
        
        t"She retreats; I charge at the scent of blood."
        
        window hide
        nvl clear
        
        t"She evades my attacks, darting around the building on her boosters. I dash the first corner, but run the next to reserve fuel."
        
        t"She shoots ahead of me, anticipating a dash on boosters."
        
        t"So that's her game? She wants me to rush in. With pleasure."
        
        t"I'm quick to react, boosting around her and landing an Incense Strike."
        
        t"She rolls away from my next strike and extinguishes the fire damage."
                                                                    
        t"I swipe in but she blocks and we exchange blows."
        
        window hide 
        nvl clear
        
        t"Lag freezes time for a moment; my blow slips through her defence and strikes a critical."
        
        td " \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ : \"Mother...\""
        
        t"Her health bar goes red. I lunge in and she parrys my strike and I stumble."
        
        t"Her sword protrudes through my chest and I'm slammed into the ground." 
        
        stop music fadeout 3.0
        
        window hide
        nvl clear
        
        "Her name slams the screen and I restrain myself from slamming the desk." with slowd
        
        show D 1YSerious_Frown at PCM1 with slowd
        
        d"\"These lag spikes have only started since you've moved here...\"" 
        
        p"\"All a part of my master plan.\""
        
        "She rolls her eyes at my joke."
        
        d"\"God forbid you actually beat me because of lag.\""
        
        d"\"And I can't have you complaining you would've beat me if there wasn't lag.\""
        
        "She delves into her screen"
        
        d"\"Ugh, they've added new software.\""
        
        "She lowers her voice; eyes still locked on the screen."
        
        d"\"I've been told not to tinker, but turning a few programs off should be fine.\""
        
        #"She turns with a concerned expression."
        
        show D 1DManic_Flat at PCM1 with slowd
        
        "Her eyes widen a notch; her lips tighten flat."
        
        d"\"There's something tracking these computers...\""
        
        "I barely catch the words under her breath."
        
        p"\"Wha—\""
        
        "She places her finger on her lips."
        
        "I write out a question as she delves back into the screen."
        
        "{i}Why would anybody track these computers?{/i}"
        
        "She glances and resumes."
        
        "I didn't think Danielle would be so paranoid."
        
        "I remain quiet as she she browses her computer. It's awkward."
        
        "She motions to leave; her computer screen fades to black."
        
        hide D 1DManic_Flat with slowd
        
        "I'm baffled."
        
        #play music "audio/music/bensound-scifi.mp3" fadein 3.0
        
        scene school_in004_day with slowf
        
        #"I try to form a question but there's too much to ask."
        
        "I try to form a question, but I'm overwhelmed with how much I want to ask."
        
        p"\"Why would anybody track them? And why would that effect us?\""
        
        show D 1YManic_Grit at PCM1 with slowd
        
        "She bares her teeth and contains herself."
        
        show D 1YManic_Flat with slowd
        
        d"\"They can track everything we do; where we are. Who we are...\""
        
        "Maybe they can help me find who {i}I{/i} am."
        
        p"\"You think someone's trying to track you?\""
        
        show D 1YSerious_Flat with slowd
        
        "Her eyes flick to me and over my shoulder."
        
        mb "\"Peter. Danielle.\""
        
        "He greets us each with a nod and furrows his brow."
        
        mb"\"It's Saturday. Shouldn't you guys be gaming?\""
        
        p"\"We believe there may be someone tracking the computers.\""
        
        "His brow remains furrowed but his lips harden."
        
        mb"\"Tracking the computers, huh?\""
        
        mb"\"That could be a serious offense if someone unauthorised can access the network.\""
        
        "His voice calm and monotone. {i}Why is everyone acting so weird?{/i}" # {i}Why is everyone acting so weird?{/i}" 
        
        mb"\"Please, show me what you've found.\""
        
        #stop music fadeout 3.0
        
        scene Computer_Room with slowf
        
        "Danielle proceeds to show him her findings. Mr Brent waves them away."
        
        "I'm left non the wiser."
        
        #timeskip
        
        play music "audio/music/myuu - Nebula.mp3"  fadein 4.0
                                           
        scene school_out004_day with slowf
        
        "I follow her out into the carpark. There's a few cars in the lot, but nobody's around."
        
        p"\"Danielle?\""
        
        #p"\"What's going on?\""
        
        show D 1Closed_Flat at PCM1 with slowd
        
        "Her stoic expression is betrayed by her features flickering in thought."
        
        #d"\"The school network is encrypted; my VPN has kept my laptop encrypted.\""
        
        show D 1YSerious_Flat with slowd
        
        d"\"The VPN on my laptop means nothing if he's able to access the school's network.\""
        
        p"\"Who?\""
        
        #show D 1YSerious_Flat with slowd
        
        "She sighs."
        
        d"\"I'm not sure. It could be Luke.\""
        
        #d"\"If he's able to track everything on these computers, then not only am I at risk, but everyone else.\""
        
        p"\"What do you mean? He's your friend.\""
        
        show D 1Closed_Flat at PCM1 with slowd
        
        d"\"You can't trust anyone.\""
        
        p"\"He helped me train for this fight, because he knew you wanted to bring me along in game.\""
        
        show D 1YSerious_Flat with slowd
        
        d"\"It's not likely. But it's possible.\""
        
        p"\"Why would anybody be tracking you?\""
        
        show D 1YManic_Flat with slowd
        
        "Her breath catches in her throat and she relaxes with a sign."
        
        show D 1DManic_Flat with slowd
        
        d"\"I've been stalked before.\""
        
        #show D cnormal with slowd
        
        d"\"I played with him online a few years back and we got close.\"" 
        
        d"\"But when we started drifting apart, he got controlling; so I said goodbye.\""
        
        "There's a chink in her voice."
        
        d"\"But he found my adress through my IP and began stalking me.\""
        
        d"\"He had spoken to me in the street a few times and he was strange. I didn't know what he looked like then.\""
        
        show D 1YManic_Flat with slowd
        
        d"\"I didn't realise it was him until I woke up at two am with him at the end of my bed.\""
        
        show D 1Closed_Flat with slowd
        
        #rape?
        
        "She looks ashamed in herself for it."
        
        p"\"You couldn't have known. But that doesn't mean that you have to suspect luke.\""
        
        "My mind shoots to her threatening to ring the police when I told her I was here."
        
        p"\"Did you suspect me, too?\""
        
        "Her nostrils flare." 
        
        d"\"It's not a bad thing to suspect you.\""
        
        "I assure to keep a calm tone."
        
        p"\"Definitely not. But do you trust me?\""
        
        show D 2YGentle_Frown with slowd
        
        #"Her features soften."
        
        
        d"\"I do.\""
        
        "It's a relief to hear."
        
        p"\"Then you have to let me know if you find out anything else.\""
        
        #p"\"What will you do?\""
        
        
        #d"\"Why did you tell him?\""
        
        show D 1YSerious_Frown with slowd
        
        d"\"You shouldn't have told him.\""
        
        p"\"Told who?\""
        
        d"\"That new teacher. He's right; it's likely nothing. I feel stupid for it.\""
        
        d"\"But something just doesn't feel right.\""
        
        p"\"It'll be fine. C'mon, want to go to Pot Kettle Black while we're out?\""
        
        stop music fadeout 4.0
        
        show D 1YSerious_Frown at PC1 with slowd
        
        d"\"No, thanks. I'll see you Monday.\""
        
        hide D 1YSerious_Frown with slowd
        
        "She marches inside."
        
        p"\"B-bye...\""
        
        "Her body language makes me not want to follow."
        #room
        
        play music "audio/music/myuu - Prey -Reprise-.mp3" fadein 3.0
        
        scene room_boy16_day with slowf
        
        "I thought she might want to spend some time together, take her mind off things."
        
        t"But what if she's seriously being stalked?" with slowd
        
        #"Would she actually trust me enough to tell me?"
        
        t"Her paranoia makes me uneasy, but I just can't help feel that it's not the case."
        
        t"I just wanted to be there for her. To make her feel comfortable."
        
        t"Her confirming words play in my head."
        
        t"{i}I do.{/i}"
        
        window hide
        nvl clear
        
        t"{i}Do you trust me, though?{/i}"
        
        t"Does she have a reason to? We've played Club Seal and Magnum Dilon together."
        
        t"I get the feeling she wouldn't have told me about her music if I hadn't found her."
        
        t"She doesn't even trust Jennifer enough to tell her about her gaming."
        
        t"Maybe I'm just looking too much into everything."
        
        window hide
        nvl clear
        
        "But maybe she's right." with slowd
        
        "Someone's actually trying to track her. And I'm here doubting her."
        
        "I talk about friendship and trust, yet I don't trust her with this."
        
        "And even with how calculated she is, she's seriously concerned."
        
        
        
        
        #"When I look at the situation logically, 
        
        #Mr brent can come along during this and Danielle will downplay it, Peter will say, though.
        
        #I'm not sure I trust him. 
        
        #Well, if you think there's something tracking the computers then someone should know.
        
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        #p"\"\""
        
        #d"\"\""
        
        
        #t"L0stC4us3: "
        
        #t"x-Destiny-x: " 
        
        #t"L0stC4us3: "
        
        #t"x-Destiny-x: " 
        
        #t"L0stC4us3: "
        
        #t"x-Destiny-x: " 
        
        #t"L0stC4us3: "
        
        #t"x-Destiny-x: " 
        
        
        
        
        
        
        
        
        #Build up to their fight on Magnum Dilon 
        
        
        
        #d"\"Because I could list off everything and you'd forget most of it, but you'll remember if you learn from a mistake. You'll understand why you need it.\""
        
        
        
        
        #have him die? XD 
        
        
        
        
        #"I'm poor, OK?"
        
        #You noob, you should buy a few potiuons too. #save "nice save" for now?
        
        #You didn't tell me how to gear. How do you expect me to know?
        
        #OK, I'll take you through town now and we'll gear for another?
        
        #p"\"Sure, sounds good.\""
        
        #Go and buy potions. 
        
        #Quick, I'm trapped. Kill it! 
        
        #after the second trip?
        #d"\"Good job, noob. You're improving.\""
        
        #What kind of noob brings apples?
        
        #They were cheap. I'm poor. 
        
        #The four races of Kilashnov
        
        #Yeah? Well a noob just got more kills than you. 
        
        #Oh, are you ready to fight me now? 
        
        #Let's do it!
        
        #
        
        window hide 
        nvl clear 
        
        
        
        #Or at the end of it she'll say "Good job, noob." Just to piss on Peter's chips. 
        
        
        
        scene black with slowd
        
        centered "Thanks for reading! Be sure to check out the other route segments and ending."
        
        #centered "Feel free to leave feedback at Facebook.com/NamelessNoun"
        
        #centered "Please be patient for the credits (because I'm a noob), there's also a .txt file."
        
        centered "The credits are slow because I'm a noob. Might be better to check the .txt file, links included!"
        
        call credits from _call_credits_2
        return
        
        
    label Dan1n:
        
        #Death scene. 
        
        t"L0stc4us3: I'll pass, thanks."
        
        "She doesn't respond." with slowd
        
        window hide 
        nvl clear 
        "..." 
        
        scene black with longd
        
        #"What to do with it..."
        
        
        centered "Three months later." with slowd
        
        #scene black with slowd
        
        #the grave of memories scene. 
        
        
        
        play music "audio/music/myuu - Prey -Reprise-.mp3" fadein 3.0
        
        scene shop01_day with slowd
        
        "So much for this \"new life.\""
        
        t"I thought there would be more to it than this. But all I do is seclude myself and stew in my room." with slowd
        
        t"Solitude is a hard won ally—an ally I've never made."
        
        t"I trudge along with school work but I'm apathetic to it. I still don't know who I am or what I want, so how can I care?"
        
        t"My semblance of happiness has been enough for me to slip in and out of class and councelling unnoticed."
        
        t"Everyday it became harder to make connections, so I stopped trying."
        
        #t"As days went by, it became harder to make connections." 
        
        #t"So I stopped trying."
        
        window hide 
        nvl clear 
        
        "I make it to the checkout, offering the chashier a smile. Faux smiles come easy now." with slowd
        
        "He returns it and scans through my microwave meals, pots of noodles, cans of cola and bottles of water."
        
        "I bought appliances for my room so the only reasons I have to leave is for the toilet or class."
        
        C"\"That's nine ninety-five, please.\"" 
        
        "I hand him a ten and leave with my bags."
        
        play environment "audio/background/city2.mp3" fadein 4.0
        scene shop006_night_light with slowd
        
        "The evening's cold air embraces me. {i}The only thing that will{/i}."
        #stop music fadeout 3.0
        scene street001_night_dark with slowd
        
        "I spot a familiar grey coat approaching in the crowd. The man's jawline is slim and his cheeks are etched with lines of age. "
        
        "I catch his gaze as he walks by; his eyes narrowed, emanating malice."
        
        "Icy fingers grasp my heart."
        
        "Is he... following me?"
        
        "No, he can't be. I'm just being paranoid."
        
        "I scan through the crowd again but he's nowhere to be seen."
        
        "I cut down a side street." 
        
        stop environment fadeout 3.0
        scene street004_night_light with slowd
        
        "It's quiet down here, at least."
        
        #"That man, where have I seen him before?"
        
        "I rack my brain but I can't remember where I've seen that man before."
        
        stop music fadeout 5.0
        "Not that I care if anything—"
        
        #gunshots
        #silence music
        #stop music fadeout 5.0
        play sound "audio/sfx/gunshots.mp3"
        #ears ringing/heartbeat
        #scene street004_night_light_Version2 with vpunch
        #Have the tilted screen and add the white trim with his last breath
        
        play environment2 "audio/sfx/heartbeat.mp3" fadein 5.0
        scene street004_night_light leanblur with vpunch
        #scene street004_night_light with vpunch
        
        #show blood spray with slowd
        #show smudge with slowd
        #show bloodmbm with slowd #rip, make png 
        
        "My body jolts to every gunshot."
        
        #heartbeat _Version2
        
        "I drop to my knees wide-eyed; bags spilling from my fingers."
        
        #"Was I hit?"
        #scene street004_night_light_Version2 with slowd
        
        "My fingers follow the warm, sticky liquid up to my chest. The pain of touching it steals the last breath from my lungs."
        
        #slump with effect
        #"I slump face-first onto the pavement, wondering if I'd ever lived."  #I wonder if I've ever lived..." #My last thought wondering if I'd ever lived."
        #"I slump face-first onto the pavement. My last thought wondering if I'd ever lived..."
        
        "The ground rushes up to meet me. My last thought wondering if I'd ever lived..."
        
        
        #stop music fadeout 3.0
        stop environment2 fadeout 3.0
        play environment "audio/sfx/Ear Ringing Sound Effect.mp3" fadein 4.1
        #scene bloodmbm with wd
        #scene blood spray white with longd
        
        scene white with wd
        
        stop environment fadeout 2.0
        #play music "audio/music/Level_Plane.mp3" fadein 6.0
        #play music "audio/music/Level_Plane 110.5 mul.mp3" fadein 6.0
        play music "audio/music/Passed.mp3" fadein 6.0
        
        
        scene black with longd
        
        
        centered "Thanks for reading! Be sure to check out the route segments."
        
        #centered "Feel free to leave feedback at Facebook.com/NamelessNoun"
        
        #centered "Please be patient for the credits, there's also a .txt file."
        
        centered "The credits are slow because I'm awful. Might be better to check the .txt file, links included!"
        
        call credits from _call_credits_3
        return
        
        
        
        
        
        
        
        
    call credits from _call_credits_4
    return

label credits:
    $ credits_speed = 50 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(0.7)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide thanks
    return

init python:
    credits = ('Backgrounds', 'ayaemo'), ('Sprites', 'K_Kisekae2 (18+)'), ('GUI', 'Ren\'Py'), ('Writing', 'NamelessNoun'), ('Programming', 'NamelessNoun'), ('Music', 'Bensound'), ('Music', 'Kevin Macleod'), ('Music', 'Myuuji'), ('Music', 'Riot'), ('Special thanks', 'Joe De Sousa'), ('Special thanks', 'Kiri Reeve'), ('Special thanks', 'Carlos Filgueiras'), ('Special thanks', 'Kofi Bradshaw'), ('Special thanks', 'Louis Albert Saleone'), ('Special thanks', 'Marco Aurello'), ('Special thanks', 'Luigi Ye')                                 
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.14.1" #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Euronoob.", text_align=0.5)
    
    
    
    #myuu - Collapse
    
    #I've been stewing all day. 
    
    
    

    
    
    
    
    #jump behind the wall: You bastard! - that scene XD < Wait, what? XD 
    
    
    #"Not only do I feel comfortable in my new room. I'm beginning to feel excited about my new environment, my new... Life."
    
    
    
    
    
    
    
    #She tickles my back, goosebumps descend from my neck to my wrists. 
    
    #She tickles my back and I shiver, evoking goosebumps. 
    
    #She strokes the hairs on my back. Goosebumps descend down my arms. 
    #A shiver sends goosebumps down my arms. 
    
    
    #Danielle has tried to talk with me a few times, I feel I should return the favour. 
    #I can't lie, I'm interested in her project. 
    
    #She will mention the bank robberies, and implementing it into her game? :p
    #I recall the broadcast, but I didn't pay much attention. 
    
    #Dean could be good at sports and science? I feel outmatched because he likes Jennifer too
    
    #Jennifer knows about Danielle's gaming but won't say anything? In Danielle's route she's reluctant to tell her. 
    
    #seasons change, but everything remains the same. 
    
    # Shopping scene now? Then with Danielle, you could go to the computer room? 
    
    #the town has recently been through a lot of renovation, this could lead to the bank robbery opportunity? 
    
    #"..."
    
    #"I move from the doorway, but she remains still."
    
    
    
    #fall asleep and wake up at like midnight? Re-meet Sarah in the kitchen? 
    
    
    #scene: Meet Daneille outside class by chance. Dig up some old script? 
    
    #When you've been left with your thoughts as long as I have, you think too deep into things.
    
    
    #She carries an invisible buden. 
    
    
    #He told me I was suffering from amnesia. But really, my amnesia is a defence mechanism for my suffering.
    #It's easier to forget. Easier to push it away. 
    #(I reach for the remote)
    
    #You always told me I should live in the moment. I never realised what you meant... until now.
    #I realise I want to be in this moment. With you.
    
    #I... I was never able to live in the current moment. 
    
    #Do a lunch scene where Jennifer leaves you alone with Danielle and you try to break the ice? <- gg idea
    
    
    #I'm sorry. You... scared me."
    #Wait, did she think I was—no, surely not.
    
    #Godspeed, good knight. May your journey be free of peril.
    
    #leave something behind dialogue?l
    #also speak 
    
    #mention wi-fi and maybe she gives you her number? This will be at dinner?
    #I've... got a girls number. On my first day in class. She's cute, too. 
    #judging from my knowledge of film, doesn't that mean... 
    #Did I just make... a friend?
    
    #A smile tugs on my lips, (after her greeting.)
    
    
    #Your uncle could have the worker looking after you for him. He reports to him with information?
    #Well, he'll be like the school psychiatrist? Not to that extent, but he helps the kids. 
    #So he will relay information when Peter begins recovering his memories? 
    #This could be a teacher sprite? But you have poo sprites lol. 
    
    #
    
    #Didn't realise how tired I was until I slump onto my bed.
    
    #She demonstrates how she allows the stone to roll off her index finger #philosopher's stone
    
    #https://www.reddit.com/r/vndevs/
    
    #Technically I could've started school again. But I seem to have nuggets of knowledge stored away. 
    
    # em dash — 
    #I think the world might implode if you don't speak soon.
