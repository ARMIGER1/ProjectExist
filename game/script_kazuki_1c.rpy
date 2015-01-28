label Kazuki_1j_skip:#we skipped lunch
    $ sio_l("bg workshop")
    $ minutes = minutes + 5
    #1:55PM
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for as long as anyone can remember, which is of course, not very 
         long at all. This in itself is a bit awkward, since Robert lost custody of his son when he was divorced. But changing the name of his little 
         shop would be an expensive pain in the ass in terms of both paperwork and physically changing the sign, so the name stuck."
    extend "\nHis words, not mine. There have been a few awkward moments though, when I have been mistaken as his son..."
    nmc "In any case, I happen to work for him. Three hours a day, by the sweat and grime  my brow, wrench in hand... actually I just handle 
         the taxes, the telephone, and the computers."
    mc "Hello, Robert and Son's Machines. Yes, we can service your BMW. Yes, I can schedule you for Monday. Certainly. Good day to you too."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Yes, Robert and Son's. No, we don't take walk-ins. No, the manager is actually working on a car at the moment. '99 Ford Explorer 
        actually, but... No, we are completely booked for Friday... We don't actually work on Saturday. Next Tuesday will work. Of course. 
        Enjoy the rest of your afternoon."
    $ minutes = minutes + 15
    $ sio_l("bg workshop")
    mc "Hello, Robert and Son's Machines. Fuck you too."
    nmc "Now normally, that sort of language would get me fired and could get me sued. However..."
    ro "Kazuki, was that Rachel on the phone?"
    mc "Yes sir."
    ro "What a bitch. Carry on."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. Not that we couldn't have repaired it, but she insisted that we 
         repair the phone for free and deliver the repaired phone on the same day the phone was brought in."
    nmc "A ridiculous customer by all accounts. So basically, everyone in the office hates this customer more than any other."
    ro "Oh, how's tomorrow's schedule looking?"
    mc "Completely booked."
    ro "And Monday's schedule?"
    call sn_draw("sn siebener")
    mc "One car. A Siebener. Nothing else for Monday."
    ro "I hate working on beemers. Tuesday?"
    mc "No cars at all. The whole week is basically empty, actually. I might not be needed for most of the week. Although I could still come in if 
        you'd like. Here, look at the schedule."
    nmc "There are indeed schedules worse than an overbooked one. Because even if you are working overtime, you are still in fact working. 
         When we have an underbooked schedule, we spend a lot of time twiddling our thumbs and since our salaries are comission-based, we 
         also don't get paid as much."
    ro "I didn't think it would be possible to have less business this week than last week. I'll have someone else do the phones on Tuesday. 
       Take Tuesday off."
    mc "To be fair, I haven't scheduled any appointments yet."
    ro "True."
    mc "Also... You could show me how to repair something instead."
    ro "Nope. You aren't licensed for... anything. Even if I did show you the insides of an iPhone, it would be all kinds of illegal for 
       you to do paid work. Unless you want to fix another coffee maker."
    mc "... I suppose I learned my lesson with the coffee maker."
    nmc "Robert was of course, referring to \"The Ground Problem\", or at least, that's what he calls it when he retells the story to customers. 
         Ground floor, ground coffee, haha."
    nmc "Although Robert is technically a mechanic, a few customers began to bring their computers to us. Originally, we told them that we didn't 
         have any computer parts. One Tuesday however, I told Robert to let me take a look at it, and as it turned out, the problem was between 
         the desk and the chair."
    nmc "\"My computer won't connect to the Internet!\" The problem wasn't the network interface controller, which is, of course, the thing that 
         the silly-looking blue wire goes in. The problem was actually with the settings on the operating system. Somehow, the computer was 
         trying to use Google as a router."
    nmc "... That's kind of like trying to use beef to fertilize the grass that cows eat. Which only makes sense if you know nothing about 
         farming. Ignoring the fact that some farmers do directly feed their livestock animal by-products. Which is basically bad beef."
    nmc "Anyway, I fixed the computer. The next day, I was admittedly cocky and tried to fix a coffee machine without telling Robert."
    nmc "Long story short, the carpet has a very large coffee stain in it."
    ro "Well, there are no cars left to work on, so I'm taking a nap."
    mc "Understood."
    nmc "And so, I allow another monotonous day of appointment scheduling and paperwork to drag on."
    $ sio_l("bg blackdrop")
    $ triple_min(25)
    $ sio_l("bg workshop")
    #3:25PM
    nmc "I had run out of tasks for today, so I began to record data of the cars Robert had worked on over the past week."
    nmc "Specifically, the more useless data. Such as, that 60.3 percent of the cars that came through our shop were originally painted white."
    nmc "Or that 32.4 percent had failed their previous smog check."
    nmc "Considering that I'm really not in the mood to work on my essay, this seemed to be a reasonably good use of time."
    nmc "I lost myself in the spreadsheets in Robert's computer..."
    jump Kazuki_1l_work
    
label Kazuki_1j_lunch:#originally had a bus crash intended; bad idea
    # 1:50PM
    $ minutes = 830
    $ sio_l("bg bus1")
    nmc "As I confirmed this morning, it takes 5 minutes to get to school if I sprint, trespass, pick a few locks, jump dangerously, and so on."
    nmc "But honestly, I'm not up for repeating all of that nonsense. So, I'm taking the bus home."
    $ sio_l("bg blackdrop")
    call triple_min(2)
    nmc "The rest of the bus drive proceeded without incident."
    $ sio_l("bg kazuki kitchen")
    nmc "I let myself into the apartment and begin getting things out of the refrigerator."
    nmc "Father doesn't own a car. He had a Subaru, but then he sold it to pay off his tab. So I can't actually tell if he's home or not."
    nmc "Not that I care."
    mc "...Freaking why."
    nmc "While all of my smoked salmon was where I left it, someone had eaten the last bagel after I left for school."
    nmc "I suppose white bread will have to do."
    "{i}Clatter!{/i}"
    mc "Who's there?"
    nmc "Without double-checking whether or not someone has actually joined me in the room, I get ready for a skirmish."
    nmc "I snap my wrist and adjust my grip of the butter knife, holding it as I would a dagger. It may not be particularly sharp, but it is threatening
         enough."
    nmc "The sound had been loud and unexpected, but its source is..."
    d "Go back to school, you little faggot."
    nmc "Father either just got back from the bar, or has just woken up with a hangover. Either way, he is hostile."
    nmc "In his drunken swagger, Father had succeeded in knocking my plate to the floor. Although gaudy, these new plastic plates are proving 
         to be nigh-unbreakable, saving me several dollars a day on housekeeping."
    mc "Tsk..."
    nmc "... He swings at me with his left arm, but I drop to the ground. The fist connects with nothing but air. I have a free shot here.{w} I push hard with 
         my right elbow, crushing his diaphragm. He falls over, wheezing."
    nmc "It takes considerable self-control to not use the knife."
    mc "You'd be in jail and out of alcohol if I wasn't paying for this place, dumbfuck."
    nmc "I put down the knife, and twist a rubber band around a bundle of 5's from my wallet. Father's beer money for the week."
    $ main_char_cash -= 50
    mc "And I'm going to work, not school. Once I shove some bread and meat down my throat, anyway. Which reminds me. Stop eating my crap. I 
        need my bagels."
    nmc "In response, Father gets up and takes another swing at me. Persistent bastard."
    nmc "I crack a cutting board over his head, hopefully putting him down for a bit longer than a few seconds."
    d "Hnngggrr eaaaaah-"
    nmc "Father collapses to the floor as a heap of flesh, making a gargling sound all the while."
    mc "You haven't won a fight since I turned 14... I'm leaving now."
    nmc "Father, still on the floor, lifts his right hand and makes a \"blah blah\" motion with it. An unsuspecting target for a wad of cash. 
         The money drops to the floor with a light rustle. I can't resist a smirk as I lift the plastic plate off of the floor while he picks 
         himself up."
    d "I wasn't ready."
    mc "You were always shit at catch."
    nmc "He bends over to pick up the money, and his back makes a cracking sound. My \"bagel\" made, I make my way towards the door."
    d "Kill me, goddammit. Put me out of my misery. I know you want to."
    nmc "I stop walking, but I don't look back."
    mc "As much as it disgusts me, you were the last thing my mother ever touched. If it wasn't for that, you'd have three bullets through your skull."
    nmc "I open the door and head out for work, intentionally leaving it open."
    jump Kazuki_1k_work

label Kazuki_1j_essay:
    nmc "... A 10 page essay on why I wasn't paying attention in class."
    nmc "\"Well gee, Ms. Amnaki, it may or may not have to do with your inability to teach things that are new to me.\""
    nmc "Mmm, an excellent topic sentence."
    nmc "\"Additionally, due to the nature of your teaching style, all I need to do is briefly scan the 40' x 30' 
         whiteboard to gain a full understanding of the day's lesson. For instance, on the day that you gave me this assignment, you 
         were in the middle of a simple two-dimensional rotation problem...\""
    nmc "..."
    $ minutes = minutes + 2
    $ sio_l("bg library1")
    nmc "And you were showing us how to transform matrices in a manner that... oh."
    nmc "... I'm not actually getting anything done..."
    nmc "I'm saying and typing a lot, but none of it is truly essay material."
    $ triple_min(10)
    nmc "\"In short, because your online notes are far clearer than you are while lecturing, 
         there is no real reason to pay attention in class.\""
    mc "... That's no good either."
    li "And now you seem angry."
    nmc "An unexpected but famiiliar voice rings through my eardrums, kindly pointing out that I am visibly losing control of 
         my emotions."
    mc "... How long have you been standing there?"
    li "Mmm. I dunno."
    mc "Well, when did you get here?"
    li "Don't know that either!"
    mc "Insufferable little..."
    nmc "I mumble the rest of statement. Lilian sticks her tongue out, and folds her hands behind her back."
    li "I heard that!"
    $ minutes = minutes + 5#2:27
    mc "I don't believe you."
    nmc "Lilian puts her tongue back in her mouth and frowns."
    li "You called me a bitch."
    mc "Dammit."
    li "Really, though. What are you up to?"
    nmc "I told Lilian how I fell asleep in today's math class and as punishment, had to write a paper."
    li "Oh. On why you fell asleep?"
    mc "Yes, unfortunately. I don't know how anyone could write 10 pages on the subject."
    li "Hee! You could write \"I am a moron.\" over and over again!"
    mc "... Even if I was willing to deprecate myself in that way, I don't think Amnaki would accept that. "
    extend "Although, using the same sentence repeatedly... eh, that sounds like the amount of effort I'm willing to 
            put into this stupid assignment."
    li "I figured as such. Would you like some help?"
    mc "Err... why are you offering?"
    li "So I can remind you that joining LAST is a good idea!"
    mc "That figures."
    li "Wah! I'm not actually that self-centered. That was a joke."
    mc "Ugh. You aren't a funny person."
    li "Okay really, I just don't have anything better to do. Do you want help or not?"
    $ cd_set(15, 15, 'Kazuki_1j_essay_what')
    show screen countdown
    menu:
        extend ""
        "Yes":
            $ answer_add("lily_essay_1_yes")
            call Kazuki_1j_essay_yes#returns
            if("self_40" not in answers):
                jump Kazuki_1j_liwrapup
            # logic block, yes--> [more, stop, lazy]
            if("lily_essay_2_yes" in answers):
                jump Kazuki_1j_essay_more
            elif("lily_essay_2_no" in answers):
                jump Kazuki_1j_essay_stop
            else:
                jump Kazuki_1j_essay_lazy
        "No":
            $ answer_add("lily_essay_1_no")
            jump Kazuki_1j_essay_no
        "...":
            $ answer_add("lily_essay_1_no")
            jump Kazuki_1j_essay_what

label Kazuki_1j_essay_yes:
    mc "I suppose that I wouldn't mind the help."
    li "Are you sure your pride can take it?"
    mc "Hm? Take what?"
    li "Oh, just the fact that you're going to be getting English help from a little girl."
    mc "Tiny would be the better word, I would think."
    li "That's not very nice."
    mc "Had you been in grade school or something along those lines, then I'd be pissed."
    li "Um... in that case, I'm leaving."
    mc "Hey now, that was just payback for your earlier jab. Really, I'm grateful for the help."
    li "Sure, sure. Let's look at it, top-downwards..."
    nmc "Lilian quickly scanned through the first page of actual content."
    li "... Wow. \"In somewhat-general terms, your lectures are mostly composed of senile ramblings.\" Really?"
    mc "Well... I'm not wrong."
    $ minutes = minutes + 5
    li "You said this was for Amnaki?"
    mc "Yeah. That one."
    li "Okay. Fine. You're not wrong."
    mc "Have I ever been wrong?"
    li "Statistically speaking you probably were at one point, but even if you're right, that isn't something you 
        can write here."
    mc "So, what do I write?"
    doublespeak li mc "Complete and utter..." "Bullshit?"
    li "Well, I was going to say nonsense, but that works too!"
    mc "Okay, that isn't really my thing. Unless I'm pretending that I'm well-prepared for a presentation or something."
    li "Perhaps it would be better to look at what you wanted to say, and then reverse it. You know, something like 
        \"I'd like to explain why I managed to fall asleep during your extremely informative lecture\"."
    mc "... And the whole paper needs to sound like that?"
    li "Hey, you wanna make her happy, right?"
    mc "Actually, I would prefer it if she was preparing for suicide."
    li "All right then. You want to pass her class, right?"
    mc "Well, I suppose I really don't have much of a choice."
    li "Exactly. Now as for this next sentence..."
    $ triple_min(10)#3:02?
    nmc "30 minutes later, we had... something. It certainly was an improvement from what I had written by myself."
    nmc "But the sentences simply didn't flow. Near the end, we may as well have been writing something along the lines of 
         \"Amnaki, you are great. I should have paid attention. This class is useful.\" and so on."
    nmc "... In fact, that {i}is{/i} what we wrote for our concluding paragraph."
    li "We did it!"
    mc "Ehh... Not really. Sure, there are 10 full pages of writing here, but some of it is childish. I mean, 
        \"You'll be the center of my attention from now on\"... Come on."
    li "I didn't write that."
    mc "You did. I am not a creepy person."
    li "But you're scary!"
    nmc "Lilian is actually tearing up. Is my face that fearsome...?"
    li "Actually, you're kinda cute! Like a super thin teddy bear!"
    mc "..."
    li "Hee hee! Messing with you is fun."
    nmc "I honestly couldn't tell if she was messing around or not, but for the sake of my sanity, I decided to let the comment 
         slide."
    mc "Whatever... hang on. Don't you have to be somewhere? I imagine that you're quite busy..."
    $ minutes = minutes + 3#3:05
    $ domchange("FP", -2, 0)
    li "Me? No, not really. I mean, I've got time. Why? Do you want to work on this more, or would you rather call it quits?"
    # if mc indicated that he isn't interested in the 40 we're making him say no
    if("self_40" not in answers):
        return
    $ cd_set(15, 15, 'Kazuki_1j_handle1')
    show screen countdown
    menu:
        extend ""
        "Yes":
            $ answer_add("lily_essay_2_yes")#more
        "No":
            $ answer_add("lily_essay_2_no")#stop
        "...":
            pass
    return
    
label Kazuki_1j_essay_no:
    mc "No thank you. Honestly, I should probably get to work."
    nmc "I save the file and close the window."
    mc "I'm actually already running a little late."
    li "Oh. In that case, I might as well head home myself. Do you want a ride?"
    mc "Umm, I certainly wouldn't say no to a lift, but are you sure?"
    li "Actually, I insist."
    nmc "As she pulls me by the hand, it occurs to me that I've never actually seen Lilian drive."
    $ jump_break()
    jump Kazuki_1k_early_lily

label Kazuki_1j_essay_more:
    mc "Yes."
    li "Eh!?"
    mc "You heard me. \"Yes.\" "
    extend "As in, \"yes, I am desperate\"... "
    extend "or \"yes, you have been helpful, believe it or not\"... "
    extend "or even \"look, I really want to get this garbage assignment out of the way\"."
    li "I didn't hear a \"yes\" in that last one..."
    $ jump_break()
    return

label Kazuki_1j_essay_lazy:
    $ answer_add("lily_essay_2_what")
    nmc "... I stared blankly at the laptop screen."
    mc "Uhh..."
    $ jump_break()
    return
    
label Kazuki_1j_essay_stop:
    li "Ooh. Kazuki's a quitter! Kazuki's a quitter!"
    mc "Grr..."
    li "Actually, that works out well. I haven't had lunch yet."
    "{i}Grumble...{/i}"
    nmc "Now that my stomach reminds me, I haven't had anything to eat since this morning."
    li "..."
    nmc "By now, the school cafeteria has probably stopped serving lunch."
    li "..."
    nmc "I didn't pack a lunch today, either."
    li "...!"
    nmc "I wonder what I could do for a-"
    li "{size=40}Hey! I'm talking to you!{/size}"
    nmc "I'm already fairly late for work... missing a day of work would certainly be unusual for me, but it probably wouldn't hurt."
    mc "... Well, fuck me."
    li "Aha, I'd rather not. But what's up?"
    mc "I'm late for work!"
    li "E-Eh!? What do you mean?"
    mc "We got so carried away working on the essay, that I didn't realize how much time had passed!"
    li "What do you mean by \"we\"? Ooh, how could you be so careless?"
    mc ""
    $ jump_break()
    jump Kazuki_1k_late_lily#get lunch with her

label Kazuki_1j_essay_what:
    nmc "I lazily stare back at the small girl in front of me. There is really no need for me to answer."
    li "Ah, I suppose I'll take that as a \"no\" then."
    nmc "Turning my head towards the eggshell white ceiling, I slightly slump into my chair to show my lack of care."
    li "Alright! Well, best of luck!"
    nmc "Perfectly understanding my desires, Lilian happily skips away from my table."
    nmc "... I should probably head to work now..."
    $ jump_break()
    return

label Kazuki_1j_liwrapup:
    mc "No, that won't be necessary."
    nmc "I save the file and close the window."
    $ jump_break()
    return

label Kazuki_1k_early_lily:
    $ triple_min(5)
    li "All right, we're here!"
    mc "..."
    li "Wakey wakey, lemon cakey. You said Robert and Son's, yeah? This is the place..."
    mc "I was ready to die..."
    return
    
label Kazuki_1k_late_lily:
    return
    
label Kazuki_1k_work:
    # 2:00PM
    $ minutes = 840
    nmc "On the half-hour walk to Robert and Son's Machines, I realize that I have some time to think about problems. Specifically 
         variants of impossible problems."
    nmc "Consider for a moment, the Mutilated Chessboard Problem, as posed by Martin Gardner. Although I would have called it the 2-by-1 Corner Truncation Problem. 
         The premise of the problem is that an unmodified chessboard can clearly be completely covered by a number of standard dominoes."
    nmc "Of course, assuming that you place a domino over two adjacent squares and don't do anything silly, like placing a domino diagonally, using oversized dominoes, 
         breaking dominoes in half, dangling dominoes off of the board's edge, and so on. If you remove two white squares on the board however, can you still fill 
         the chessboard with dominoes?"
    nmc "The answer is, of course, no. While it's certainly true that removing these spaces still leaves the board with an even number of squares... well."
    nmc "A domino placed with these restrictions must cover both a black and a white square. If the ratio between the quantity of black squares to white squares 
         is anything but one-to-one, this is evidently impossible."
    nmc "But what happens if I remove a black tile and a white tile? Does it matter which tiles I remove? And can I then fill the board with dominoes?"
    nmc "The answer then is, that I will always be able to fill the board regardless of the two removed tiles. Additionally, the proof is still somewhat geometric. 
         Imagine how a rook would travel through board, and realize that its movement 
         pattern must alternate tiles: black, white, black, white, and so on. A single path is not necessarily possible if these two tiles are removed."
    nmc "So what? Picture the removal of a black square. A single rook may still traverse the entire board, but starts and ends on a white square."
    nmc "Then remove any white square. If remove one of the end squares, then we've presented the problem in an incredibly stupid manner, and have just asked \"well 
         what happens if we remove a domino's worth of squares\"."
    nmc "Remove a white square in the middle though, and we absolutely create two paths. Black at the start and white at the end. A traversable path with different 
         ends. Quod erat demonstrandum."
    nmc "But what if we tried to solve the problem in a non-geometric manner? Hmm..."
    # alternate intro to robert hale
    $ sio_l("bg workshop")
    $ minutes = 870#2:30
    ro "Blasted self-entitled good-for-nothing ignorant plebeian consumerist sheep people cunt dicks."
    mc "Mr. Hale?"
    nmc "Robert Hale has been the proud owner of Robert and Son's Machines for as long as anyone can remember, which is of course, not very 
         long at all. This in itself is a bit awkward, since Robert lost custody of his son when he was divorced. But changing the name of his little 
         shop would be an expensive pain in the ass in terms of both paperwork and physically changing the sign, so the name stuck."
    extend "\nHis words, not mine. There have been a few awkward moments though, when I have been mistaken as his son..."
    nmc "Moments like these remind me of Robert's Irish descent."
    mc "Excuse me, Mr. Hale?"
    ro "That bitch Rachel called again."
    nmc "Rachel made the mistake of trying to get her cell phone repaired here. Not that we couldn't have repaired it, but she insisted that we 
         repair the phone for free and deliver the repaired phone on the same day the phone was brought in."
    nmc "In any case, I happen to work for Mr. Hale. Three hours a day, by the sweat and grime of my brow, wrench in hand... actually I just handle 
         the taxes, the telephone, and the computers."
    mc "She's still alive?"
    ro "Well her driver's license says that she's 84."
    mc "Didn't you say she was your first customer?"
    $ minutes = minutes + 2
    ro "Yep. Good ol' days, eh?"
    mc "Umm. I find it unlikely that I was even alive back then."
    ro "I suppose that would be unlikely yes. How old are you again? Twelve?"
    mc "Robert..."
    nmc "Our senses of humor are not exactly compatible."
    ro "Heheh. Anyway, I've got work for you."
    nmc "He points at the workstation."
    mc "Oh! Is the computer broken?"
    ro "No. The assholes have started scheduling appointments through e-mail."
    mc "Ah. I see."
    ro "You know what to do. I need a nap."
    mc "Pardon?"
    ro "You heard me. G'night."
    $ sio_l("bg blackdrop")
    call triple_min(15)
    $ sio_l("bg workshop")
    nmc "... Okay, this is actually hard."
    nmc "The issue here is that I am looking at the appointments detailed in emails, and trying to put these into the calendar At the same time, I am taking 
         phone calls, and putting those vocalized appointments into the calendar."
    nmc "Multitasking is normally one of my stronger suits, but not when all of my work is being done on the same peripheral."
    nmc "... This would actually be much easier if I had two computers and a tablet."
    mc "Hello, Robert and Son's Machines. Yes, we can service your Hyundai. Certainly, I can schedule you for Monday. Give me a moment. Oh, you said an Audi for 
        Friday? My mistake. One moment. Okay, you are all set for Wednesday. Oh my God, I am so sorry. Audi. Friday. Got it. Thank you for your business."
    nmc "The rest of the calls went something along those lines."
    jump Kazuki_1l_work

label Kazuki_1l_work:
    call triple_min(15)
    $ sio_l("bg workshop")
    $ minutes = 1005
    #4:45PM
    nmc "Robert wobbles into the room, clearly drowsy. I am just now putting in the last of the appointments."
    mc "Were you actually able to get some sleep?"
    ro "Enough."
    nmc "He says as he trips over absolutely nothing."
    mc "... Are you sure?"
    nmc "Robert picks himself up off of the floor and shakes his head as he answers."
    ro "No, but I'll live. How's the work coming along?"
    mc "Nearly all of the appointments are in your system. Next Tuesday will be busy for you."
    ro "Hmm. You did that a lot faster than I thought you would."
    mc "Considering that your expectations are generally low..."
    ro "\"Blessed is the man who expects nothing, for he shall never be disappointed.\""#write
    $ cd_set(7, 7, 'Kazuki_1l_work_minus')
    show screen countdown
    menu:
        extend ""
        "Mark Twain?":
            mc "Was it Mark Twain that said that?"
            ro "No. It was actully Alexander Pope."
        "Alexander Pope?":
            mc "That sounds like an Alexander Pope quote." 
            ro "It was indeed him who said it."
        "Oscar Fingal O'Flahertie Wills Wilde?":
            mc "That sounds like Oscar Fingal O'Flahertie Wills Wilde."
            ro "Who?"
            mc "You know. Oscar Wilde?"
            ro "No... no I don't know."
            mc "Never mind. So it wasn't Oscar Wilde who said that?"
            ro "No, it was actually Alexander Pope."
        "...":
            jump Kazuki_1l_work_minus
    jump Kazuki_1l_work_extend

label Kazuki_1l_work_minus:
    ro "Alexander Pope said that. He was a good man."
    mc "It sounds like you knew him."
    ro "I'm not that old... He died in 1744."
    jump Kazuki_1l_work_extend

label Kazuki_1l_work_extend:
    mc "So you're telling me that you didn't expect me to get anything done?"
    ro "Correct. And I was, in turn, impressed."
    ro "Well in any case, here's your check for the day."
    $ main_char_cash = main_char_cash + 60
    if("lunch_work_1" in answers):
        $ main_char_cash += main_char_cash + 20
    mc "Sir? This is cash."
    ro "Check, cash, money order, gift card, same thing."
    mc "I really don't think that finances work that way."
    ro "Sure they do. Money is money."
    mc "If you say so. Thank you."
    ro "I'm closing up, now. Get out of here."
    jump Kazuki_1m_routing

label Kazuki_1m_routing:
    return