
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zombies_on_campus.settings')

import django

django.setup()

from django.core.files import File
from zombies.models import Story, StoryPoint
from story_functions import add_story
from story_functions import add_sp


def populate():
    #the story name has to be unique
	story = add_story("Zombies in Campus", "Zombies in uni?? Noooo!!!", "main_building_1")

    # # Level 1
	sp1 = add_sp(story, 1, None,  "You wake up from a well-deserved nap in the library. You look around. Where are all the people?? That's strange. You hear some noises outside.", "library_2", None, 10, "start", None)

    # Level 2
	sp2 = add_sp(story, 2, sp1, "You go down to the cafe. It's deserted. Bins are all lying around. You hear a quiet thump in the back of a cafe.",  "corridor_1", "Go get a coffee. You are way too tired to deal with this weirdness right now.",10, "mid", None)
	sp3 = add_sp(story, 3, sp1, "You go outside to your car and start driving towards home. However, someone jumps inside your car as you stand at the red light. She says her name is Jackie and she is a survivor.", "church", "Go outside to see what happened", 10, "mid", None) 

    # Level 3
	sp4 = add_sp(story, 4, sp2, "You peek in the back of a cafe. You find coffee and sugar. Day is already better! Sadly, you cannot find milk. And that foul stench... Burnt food?.. Maybe?", "bo_vending machienes", "Investigate the back of the cafe.", 10, "mid", None)
	sp5 = add_sp(story, 5, sp2, "As you leave library, you see a crowd of people surrounding something.", "dark_alley_2", "Leave building.", 10, "mid", None)
	sp28 = add_sp(story, 28, sp3, "She runs away screaming: Good luck on your own, idiot!!! More people are approaching you. One of them jumps on top of you car.", "street_uni", "Kick her out! Who does she think she is?", 10, "mid", None)
	sp29 = add_sp(story, 29, sp3, "She tells you to drive to Kelvingrove Park. There is a survivor shelter. As you approach the park, your way is blocked by a crowd of zombies.", "street_uni", "Believe her story and let her stay in your car.", 10, "mid", None)
	
    #Level 4
	sp6 = add_sp(story, 6, sp4,  "As you search around the fridges and cupboards, you notice someone staring at you silently.", "maths_hallway", "Look for milk.", 10, "mid", None)
	sp7 = add_sp(story, 7, sp4,  "As you open one of the cupboards, a lifeless arm falls out. You lean in to see the inside of the cupboard and you find four dead bodies stacked on top of one another. You let out a scream.", "library_moon", "Investigate the smell.", 5, "mid", None)
	sp20 = add_sp(story, 20, sp5, "You go to Boyd Orr lab to submit your assessment that you've been working on. A very spooked person approached you.", "bo_lab10", "Continue walking.", 10, "mid", None)
	sp21 = add_sp(story, 21, sp5, "You notice a carcass that the crowd was feasting on. Oh shit, they are zombies! One of them looks at you and bites your arm.", "tree_1", "Let's have a closer look.", 10, "mid", None)
	sp30 = add_sp(story, 30, sp28, "As you talk, you notice that no one cares about what you're saying. You put your car in reverse and smash it the car and a zombie into another car. The zombie gets up.", "tree_street", "Ask them to leave you alone.", 10, "mid", None)
	sp31 = add_sp(story, 31, sp28, "Four zombies approach you. One of them tugs your arm. His teeth are all bloody.", "tree_street", "Get out of your car.", 10, "mid", None)
	sp38 = add_sp(story, 38, sp29, "You forget that you are driving a Smart Car. It's a Jeep, you idiot. you get stuck in a middle of the zombie crowd. The zombies are coming...", "tree_street", "Drive through them.", 10, "mid", None)
	sp39 = add_sp(story, 39, sp29, "You run through the main gates and shut them. Suddenly, you hear gunshots nearby. Someone screams.", "main_building_tree", "Get out and run!", 10, "mid", None)
	
	#Level 5
	sp8 = add_sp(story, 8, sp6,  "-Hello? Is the cafeteria shut? I'm trying to get some coffee, there is no one at the front... You notice blood dripping from his mouth.", "library_7", "Talk to him.", 10, "mid", None) 
	sp9 = add_sp(story, 9, sp6,  "You run to the main building. You notice 5 other people walking slowly.", "univ", "Run!", 10, "mid", None) 
	sp14 = add_sp(story, 14, sp7, "As you start running, you bump into zombies that heard your scream. You stand no chance.", "library_moon", "Ruuuuuun!!!", 5, "end", "bad")
	sp15 = add_sp(story, 15, sp7, "You forget it's a second floor. You break your leg. While crying from pain, you notice someone approaching you.", "dark_alley", "Grab a knife and jump our of the window.", 10, "mid", None)
	sp22 = add_sp(story, 22, sp20, "You realise after a few minutes that the person is very sick. You don't notice how he turns into a zombie. The last thing you feel is his hands on your neck.", "tree_3", "You are too busy. Ignore him.", 5, "end", "bad")
	sp23 = add_sp(story, 23, sp20, "The guy says that he was bitten by a zombie. He came to Google the antidote. He wants you to help him.", "bo_lab10", "Ask him if he is okay", 10, "mid", None)
	sp26 = add_sp(story, 26, sp21, "You jump off the top of the library building. Afterlife is boring. Sometimes you dream about choosing the other option.", "library_7", "Kill yourself before you become a zombie.", 10, "end", "good")
	sp27 = add_sp(story, 27, sp21, "As time passes, you find an IT job in ZombieBook. You marry a person you love and live happily ever after.", "clusters", "Oh.. what the hell. Become a zombie.", 10, "end", "good")
	sp32 = add_sp(story, 32, sp31, "You're grabbing one another. He bites your neck. Wait, is he a wampire-turned-zombie??? Anyway, you die.", "tree_moon", "You grab THEM.", 5, "end", "bad")
	sp33 = add_sp(story, 33, sp31, "You miss as you trip towards the zombie. She pounces on you and tears the back of your shoulder. As you're wondering what is wrong with her, she kills you.", "tree_moon", "Slap them!", 5, "end", "bad")
	sp34 = add_sp(story, 34, sp30, "Stick a pitchfork to a zombie while throwing it over your head. You go on a killing spree. You didn't know you had it in you!", "univ", "Pick up a pitchfork lying nearby.", 10, "mid", None)
	sp35 = add_sp(story, 35, sp30, "The zombie dies. You are officially a zombie killer. Go do your thing! Save the humanity! You were born for this.", "tree_light", "Punch him until it stops moving.", 10, "end", "good")
	sp40 = add_sp(story, 40, sp39, "A group of survivors approach. They are your Computing Science professors! But... they point their guns at you, take your bags and move away. You are on your own again...", "main_building_11", "Shout for help to whoever is shooting.", 5, "end", "bad")
	sp41 = add_sp(story, 41, sp39, "You take cover in the bushes. It's quiet. Someone shouts 'Did we get them?!' You hear steps approaching.", "main_building_5", "Hide.", 10, "mid", None)
	sp44 = add_sp(story, 44, sp38, "Jackie and you climb to the top of the roof. She says she has grenades. Zombies start climbing the car to reach you.", "phone_box", "Climb on the roof.", 10, "mid", None)
	sp45 = add_sp(story, 45, sp38, "Jackie suddenly takes out a bunch of grenades out of her bag and you both massacre the shit out of those evil zombies.", "main_building_4", "Ask Jackie for advice.", 20, "end", "good")
	
	
	#Level 6
	sp10 = add_sp(story, 10, sp8, "You go get coffee someplace else. This cafe clearly does not appreciate the customers!", "gilchrist", "Ignore him.", 15, "end", "good") 
	sp11 = add_sp(story, 11, sp8, "You go outside. You find Starbucks on Byres Road. Finally, you'll get that coffee... It's too late when you notice that the whole place is filled with zombies. You become their lunch.", "tree_moon", "Run outside.", 5, "end", "good") 
	sp12 = add_sp(story, 12, sp9, "They are indeed friendly to you and tell you about the zombie apocalypse that is currently happening. They invite you to join their survivor group.", "maths_b_under", "Approach them. They seem friendly enough.", 10, "end", "good")
	sp13 = add_sp(story, 13, sp9, "It's overrun with zombies! You are so, so, so dead.", "gilchrist", "Go to Gilchrist cafe for a coffee. You deserve it.", 10, "end", "bad")
	sp16 = add_sp(story, 16, sp15, "A girl approaches you. 'Are you okay? I thought you were one of them.' She leads you to the secret survivors camp. Your leg doesn't heal though. You limp for the rest of your life.", "dark_alley_2", "Shout for help.", 20, "end", "good")
	sp17 = add_sp(story, 17, sp15, "Your knife gets her right in her heart. As her last words, she whispers 'I'm not one of them'.", "dark_alley_2", "Throw a knife at her.", 5, "mid", None)
	sp24 = add_sp(story, 24, sp23, "After an hour of frantic googling, you find that there is a cure to prolong the human life after a zombie bite. You both rejoice!", "bo_conf", "Help him.", 20, "end", "good")
	sp25 = add_sp(story, 25, sp23, "You attack him with you bare hands and kill him. The secret government cameras film the whole incident. MI6 is impressed with your cold killing skills. The helicopter soon picks you up from the top of Boy Orr", "bo_entrance", "Attack him.", 10, "end", "good")
	sp36 = add_sp(story, 36, sp34, "You accidentally kill one of the innocent survivors. You survive the apocalypse but you live with a constant sense of regret for the rest of your life.", "trees_park", "Continue killing.", 17, "end", "bad")
	sp37 = add_sp(story, 37, sp34, "The MI6 are very impressed with your skills. They were watching you and you passed the test. You are picked up by a helicopter immediately. You are part of the system now.", "tree_3", "Continue murdering.", 10, "end", "good")
	sp42 = add_sp(story, 42, sp41, "You kill the group of survivors and obtain their weapons. You continue on surviving.", "light_main_building", "Throw one of the bombs that Jackie has.", 10, "end", "good")
	sp43 = add_sp(story, 43, sp41, "You explain who you are and where you are trying to get to. They laugh loudly and shoot you. What the hell???", "lights_main_building", "Come out with your hands up.", 10, "end", "bad")
	sp46 = add_sp(story, 46, sp44, "You are a terrible jumper. Your classmates used to laugh at you in high school, remember? You fail the jump and die.", "main_building_2", "Leap over the crowd.", 5, "end", "bad")
	sp47 = add_sp(story, 47, sp44, "Jackie throws a grenade at the zombies but misses and the grenade explodes next to your car. The car catches fire and you die. At least you weren't eaten by zombies, right?", "main_building_5", "Stay in a car and fight.", 5, "end", "bad")
	
	#Level 7
	sp18 = add_sp(story, 18, sp17, "You go to the Adam Smith Building to seek shelter. Little do you know that it is filled with zombies. Your knife doesn't save you against 20 very hungry zombie-students.", "adam_smith_1", "Retrieve a knife from the dead girl and seek safety.", 10, "end", "bad")
	sp19 = add_sp(story, 19, sp17, "You notice 3 people going towards you. You think they are the dead girl's friends. You're mistaken. You become a lovely afternoon snack for the zombies.", "bin_1", "Shout for help.", 5, "end", "bad")
	
if __name__ == '__main__':
    print "Starting Zombies population script..."
    populate()
