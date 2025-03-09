import random
import json

def generateCase(case_number):
    # Hardcoded case details with victims, crime details, killer etc.
    if case_number == 1:
        case_data = {
    "case_number": 1,
    "case_details": "James 'The Quiet' Moretti used a variety of weapons to murder four victims in personal spaces, each murder carried out with methodical precision.",
    "killer": "James 'The Quiet' Moretti",
    "weapon": "silk scarf, knife, injection",
    "location": "personal spaces (apartments, offices, clinics, restaurants)",
    "motive": "Obsessed with control and power, using his knowledge of his victims' lives to strike when they were most vulnerable.",
    "victims": [
        {
        "victim_name": "Emily Clark",
        "victim_age": 32,
        "victim_height": "5'6\"",
        "victim_weight": "125 lbs",
        "victim_eye": "blue",
        "victim_hair": "blonde",
        "victim_identification": "strangled with a silk scarf",
        "victim_related1": "Tommy, her ex-husband",
        "victim_related2": "Lily, her best friend",
        "victim_related3": "Detective Ryan, a long-time admirer",
        "victim_desc": "Emily Clark, age 32, with blue eyes and blonde hair, was found lying on the floor of her apartment, strangled with a silk scarf.",
        "victim_relation_desc1": "Tommy, her ex-husband, had a volatile breakup with Emily. Their last conversation was filled with unresolved anger.",
        "victim_relation_desc2": "Lily, her best friend, had grown distant after an argument about an art exhibit, but they recently reconciled.",
        "victim_relation_desc3": "Detective Ryan, a long-time admirer, often tried to protect Emily, but she always rejected his advances."
        },
        {
        "victim_name": "Mark Evans",
        "victim_age": 45,
        "victim_height": "6'0\"",
        "victim_weight": "180 lbs",
        "victim_eye": "brown",
        "victim_hair": "black",
        "victim_identification": "stabbed multiple times in the chest",
        "victim_related1": "Katherine, his assistant",
        "victim_related2": "John, his estranged brother",
        "victim_related3": "Rachel, his client",
        "victim_desc": "Mark Evans, age 45, with brown eyes and black hair, was found lying in his office, stabbed multiple times in the chest.",
        "victim_relation_desc1": "Katherine, his assistant, was often seen around Mark’s office late at night. Rumors say they shared more than a professional relationship.",
        "victim_relation_desc2": "John, his estranged brother, had a bitter family dispute regarding inheritance and recently threatened Mark during a meeting.",
        "victim_relation_desc3": "Rachel, his client, had become increasingly obsessed with Mark. She was once caught lurking around his office after hours."
        },
        {
        "victim_name": "Samira Patel",
        "victim_age": 38,
        "victim_height": "5'4\"",
        "victim_weight": "140 lbs",
        "victim_eye": "green",
        "victim_hair": "brown",
        "victim_identification": "injected with an unknown substance",
        "victim_related1": "Dr. Thompson, her colleague",
        "victim_related2": "Nina, her former best friend",
        "victim_related3": "Officer Harper, a regular at her clinic",
        "victim_desc": "Samira Patel, age 38, with green eyes and brown hair, was found lying on the floor of her clinic, injected with an unknown substance.",
        "victim_relation_desc1": "Dr. Thompson, her colleague, was rumored to have a secret rivalry with Samira over a prestigious position at the hospital.",
        "victim_relation_desc2": "Nina, her former best friend, had recently confronted Samira over a betrayal. They hadn't spoken in months, but rumors suggested Samira had replaced her in a professional capacity.",
        "victim_relation_desc3": "Officer Harper, a regular at the clinic, was rumored to have harbored romantic feelings for Samira. She often rejected his advances."
        },
        {
        "victim_name": "Joseph Turner",
        "victim_age": 50,
        "victim_height": "5'10\"",
        "victim_weight": "200 lbs",
        "victim_eye": "hazel",
        "victim_hair": "gray",
        "victim_identification": "neck snapped violently",
        "victim_related1": "Rebecca, his wife",
        "victim_related2": "Carlos, his business partner",
        "victim_related3": "Olivia, a waitress",
        "victim_desc": "Joseph Turner, age 50, with hazel eyes and gray hair, was found in his restaurant, his neck snapped violently, and his body was left in the freezer.",
        "victim_relation_desc1": "Rebecca, his wife, had been seen arguing with Joseph over his long hours at work. She had also been suspicious of his loyalty.",
        "victim_relation_desc2": "Carlos, his business partner, was seen leaving the restaurant the night of the murder. The two had disagreements over the management of the business.",
        "victim_relation_desc3": "Olivia, a waitress, had a secret affair with Joseph. She was devastated when she discovered Joseph was planning to end it."
        }
  ]
}
    elif case_number == 2:
        case_data = {
        "case_number": 2,
        "case_details": "Victor 'The Phantom' Frost systematically murdered four victims, each in a way that deeply affected their personal lives and passions, using intimate spaces as crime scenes and exploiting their most cherished possessions.",
        "killer": "Victor 'The Phantom' Frost",
        "weapon": "Poison, fire, suffocation with fabric (pillows), and strangulation with objects from the victims' personal lives (e.g., guitar strings, scarves)",
        "location": "Intimate spaces (private homes, fire station, school, music studio)",
        "motive": "Victor’s motive stems from a twisted need to destroy the very things his victims held dear, exploiting their professions and passions before ending their lives.",
        "victims": [
            {
            "victim_name": "Olivia Brooks",
            "victim_age": 29,
            "victim_height": "5'7\"",
            "victim_weight": "135 lbs",
            "victim_eye": "brown",
            "victim_hair": "black",
            "victim_identification": "suffocated with a silk pillowcase",
            "victim_related1": "Jake, her ex-boyfriend",
            "victim_related2": "Mason, her assistant",
            "victim_related3": "Vera, her mentor",
            "victim_desc": "Olivia Brooks, age 29, with brown eyes and black hair, was found in her boutique, suffocated with a silk pillowcase. Her body was arranged carefully, her hands folded as if she were just resting.",
            "victim_relation_desc1": "Jake, her ex-boyfriend, was still angry about their breakup and had threatened Olivia several times. He was deeply possessive and often expressed his frustration over their separation.",
            "victim_relation_desc2": "Mason, her assistant, had a hidden crush on Olivia, which he never confessed. He was seen arguing with her just a day before her death about her choice of a new design direction.",
            "victim_relation_desc3": "Vera, her mentor, had been critical of Olivia’s designs in the past. They had a complicated professional relationship filled with jealousy and admiration, with Vera often undermining Olivia's successes."
            },
            {
            "victim_name": "Derek Fisher",
            "victim_age": 34,
            "victim_height": "6'1\"",
            "victim_weight": "190 lbs",
            "victim_eye": "blue",
            "victim_hair": "brown",
            "victim_identification": "burned alive in a fire",
            "victim_related1": "Jason, a fellow firefighter",
            "victim_related2": "Lara, his wife",
            "victim_related3": "Tom, a rookie firefighter",
            "victim_desc": "Derek Fisher, age 34, with blue eyes and brown hair, was found in his fire station, burned alive. His body was discovered in the basement, his clothing charred beyond recognition.",
            "victim_relation_desc1": "Jason, a fellow firefighter, was seen arguing with Derek about a leadership position. Their rivalry had been escalating for weeks, with Jason feeling overlooked for promotions.",
            "victim_relation_desc2": "Lara, Derek’s wife, had an affair with a colleague of Derek’s, which Derek recently found out about. This revelation caused a strain in their marriage, leading to heated arguments.",
            "victim_relation_desc3": "Tom, a rookie firefighter, had a complicated relationship with Derek. Often feeling overshadowed by Derek's experience, Tom resented him for constantly being in the spotlight."
            },
            {
            "victim_name": "Lily Grant",
            "victim_age": 41,
            "victim_height": "5'5\"",
            "victim_weight": "140 lbs",
            "victim_eye": "green",
            "victim_hair": "red",
            "victim_identification": "poisoned with an unknown substance",
            "victim_related1": "Henry, a student",
            "victim_related2": "Jennifer, her fellow teacher",
            "victim_related3": "Charlie, her ex-husband",
            "victim_desc": "Lily Grant, age 41, with green eyes and red hair, was found in her school’s library, poisoned. Her body was cold and lifeless, with a book on the floor next to her. A chilling note was left inside the book.",
            "victim_relation_desc1": "Henry, a student, had a fascination with Lily, often writing her strange letters and poems. His obsession grew over time, and many worried about his fixation on her.",
            "victim_relation_desc2": "Jennifer, her fellow teacher, was jealous of Lily’s popularity among students. They had a public confrontation in front of the faculty, with Jennifer accusing Lily of undermining her professional achievements.",
            "victim_relation_desc3": "Charlie, her ex-husband, had been trying to rekindle their relationship, but Lily had refused. He was seen outside her school just days before her death, expressing his frustration with her rejections."
            },
            {
            "victim_name": "Ethan Harper",
            "victim_age": 25,
            "victim_height": "5'9\"",
            "victim_weight": "160 lbs",
            "victim_eye": "hazel",
            "victim_hair": "blonde",
            "victim_identification": "strangled with his own guitar strings",
            "victim_related1": "Rachel, his bandmate",
            "victim_related2": "Aaron, his manager",
            "victim_related3": "Kara, his childhood friend",
            "victim_desc": "Ethan Harper, age 25, with hazel eyes and blonde hair, was found in his home, strangled with his own guitar strings. His guitar was left in a position as if it had been used to play one final song.",
            "victim_relation_desc1": "Rachel, his bandmate, was often in conflict with Ethan about their musical direction. She was also rumored to have had a romantic interest in him, which added tension to their relationship.",
            "victim_relation_desc2": "Aaron, his manager, was involved in financial disputes with Ethan regarding unpaid royalties. Ethan had refused to perform unless the contracts were renegotiated.",
            "victim_relation_desc3": "Kara, his childhood friend, had recently confronted Ethan about a betrayal. She felt he had forgotten their shared past, and their friendship had soured as a result."
            }
        ]
}
    elif case_number == 3:
        case_data = {
        "case_number": 3,
        "case_details": "Lucinda 'The Whisperer' Voss systematically targeted professionals whose workspaces were deeply intertwined with their identities. Each victim was murdered in a location that symbolized their passion, profession, and personal life. The brutality of the killings was designed to destroy not only the victims but also the very aspects of themselves they held dear.",
        "killer": "Lucinda 'The Whisperer' Voss",
        "weapon": "Knife (for slashing throats), gun (for execution-style shooting), and blunt force trauma",
        "location": "Therapist offices, architect offices, private study rooms, and police vehicles",
        "motive": "Lucinda’s killings were fueled by a deep obsession with destroying the professional sanctuaries of her victims. She attacked them where they felt most secure, leaving no space untouched by her rage.",
        "victims": [
            {
            "victim_name": "Sarah Green",
            "victim_age": 33,
            "victim_height": "5'7\"",
            "victim_weight": "130 lbs",
            "victim_eye": "brown",
            "victim_hair": "black",
            "victim_identification": "throat slashed in her office",
            "victim_related1": "Hannah, a former patient",
            "victim_related2": "Greg, her estranged husband",
            "victim_related3": "Jack, a fellow therapist",
            "victim_desc": "Sarah Green, age 33, with brown eyes and black hair, was found in her office, throat slashed. Patient files were scattered around the room, and the office was eerily arranged as if untouched.",
            "victim_relation_desc1": "Hannah, a former patient, had an unhealthy attachment to Sarah. Their sessions had become increasingly personal, and there were signs of obsession.",
            "victim_relation_desc2": "Greg, Sarah's estranged husband, had recently attempted to reconcile with her, but their relationship remained strained and filled with unresolved anger.",
            "victim_relation_desc3": "Jack, a fellow therapist, had been in a silent competition with Sarah for years. He resented her growing success and professional recognition."
            },
            {
            "victim_name": "Thomas Brown",
            "victim_age": 42,
            "victim_height": "6'0\"",
            "victim_weight": "175 lbs",
            "victim_eye": "blue",
            "victim_hair": "brown",
            "victim_identification": "stabbed repeatedly in his office",
            "victim_related1": "Mila, his assistant",
            "victim_related2": "David, a rival architect",
            "victim_related3": "Sophia, his wife",
            "victim_desc": "Thomas Brown, age 42, with blue eyes and brown hair, was found in his office, stabbed repeatedly. His blueprints were scattered around him, revealing the violent nature of the attack.",
            "victim_relation_desc1": "Mila, his assistant, had been seen arguing with Thomas over a project. Their professional relationship had deteriorated, and her hidden feelings of resentment grew.",
            "victim_relation_desc2": "David, a rival architect, had been in constant competition with Thomas for prestigious projects. Their rivalry had become increasingly bitter.",
            "victim_relation_desc3": "Sophia, Thomas’s wife, had been distant in recent months, and rumors of infidelity created a growing rift between them."
            },
            {
            "victim_name": "David Walker",
            "victim_age": 50,
            "victim_height": "5'11\"",
            "victim_weight": "180 lbs",
            "victim_eye": "hazel",
            "victim_hair": "gray",
            "victim_identification": "shot in the head in his study",
            "victim_related1": "Emma, a former student",
            "victim_related2": "Liam, a colleague",
            "victim_related3": "Rebecca, his wife",
            "victim_desc": "David Walker, age 50, with hazel eyes and gray hair, was found in his study, shot in the head. His academic papers were scattered around him, as if the killer was searching for something specific.",
            "victim_relation_desc1": "Emma, a former student, had been in a secret relationship with David. After he ended it abruptly, she became obsessed with him and felt betrayed.",
            "victim_relation_desc2": "Liam, David’s colleague, had long been jealous of David’s recognition in their shared academic work. Their rivalry had festered for years.",
            "victim_relation_desc3": "Rebecca, David's wife, had grown suspicious of his late-night work sessions with a student. They had fought over this issue just days before his death."
            },
            {
            "victim_name": "Patrick Reed",
            "victim_age": 36,
            "victim_height": "5'10\"",
            "victim_weight": "190 lbs",
            "victim_eye": "green",
            "victim_hair": "black",
            "victim_identification": "shot execution-style in his patrol car",
            "victim_related1": "Anna, his ex-partner",
            "victim_related2": "Leo, a criminal informant",
            "victim_related3": "Gary, his superior officer",
            "victim_desc": "Patrick Reed, age 36, with green eyes and black hair, was found dead in his patrol car, shot execution-style. The crime was clean and calculated, with no signs of struggle.",
            "victim_relation_desc1": "Anna, his ex-partner, had a long history of jealousy and resentment. Their breakup had been tumultuous, and she never fully let go of her anger.",
            "victim_relation_desc2": "Leo, a criminal informant, had warned Patrick of a potential threat, but then mysteriously disappeared shortly after giving the tip.",
            "victim_relation_desc3": "Gary, Patrick’s superior officer, had been involved in a dispute with Patrick over a recent investigation, and rumors swirled that Gary had something to hide."
            }
        ]
        }

    elif case_number == 4:
        case_data = {
        "case_number": 4,
        "case_details": "Daniel 'The Shadow' was a meticulous killer who targeted individuals in fields where image, control, and public personas were paramount. Each victim was murdered in a way that disrupted the essence of their professional identity, leaving a chilling imprint of control and finality. The killer's focus was on creating a symbolic death, taking away their victims' image and their ability to influence others.",
        "killer": "Daniel 'The Shadow'",
        "weapon": "Suffocation with fabric, electrocution via faulty wire, poisoning, and asphyxiation by rope",
        "location": "Rehearsal studios, tech offices, apartments, and gyms",
        "motive": "The killer's motive stemmed from a twisted desire to disrupt the lives of those in positions of influence, targeting individuals in fields where appearance and control were critical. The victims were chosen based on their vulnerabilities within their respective professional environments.",
        "victims": [
            {
            "victim_name": "Clara James",
            "victim_age": 29,
            "victim_height": "5'5\"",
            "victim_weight": "120 lbs",
            "victim_eye": "blue",
            "victim_hair": "blonde",
            "victim_identification": "suffocated by a velvet curtain in her rehearsal studio",
            "victim_related1": "Victor, her ex-boyfriend",
            "victim_related2": "Lana, her dance partner",
            "victim_related3": "Marco, the choreographer",
            "victim_desc": "Clara James, age 29, was found suffocated by a velvet curtain in her rehearsal studio. Her body was arranged in an elegant pose, frozen in time, reminiscent of a dance move she once performed.",
            "victim_relation_desc1": "Victor, Clara's ex-boyfriend, had been stalking her since their breakup. He had an obsessive, controlling nature, unable to accept the end of their relationship.",
            "victim_relation_desc2": "Lana, Clara's dance partner, had been envious of Clara's rising success in the dance world. The two had frequent arguments about their partnership and Clara’s growing fame.",
            "victim_relation_desc3": "Marco, the choreographer, had a secret obsession with Clara. His admiration for her had crossed boundaries, and he often acted possessive over her success."
            },
            {
            "victim_name": "Isaac Knight",
            "victim_age": 40,
            "victim_height": "6'2\"",
            "victim_weight": "190 lbs",
            "victim_eye": "green",
            "victim_hair": "brown",
            "victim_identification": "electrocuted with a faulty wire in his office",
            "victim_related1": "Eve, his assistant",
            "victim_related2": "Oliver, his business rival",
            "victim_related3": "Tessa, his wife",
            "victim_desc": "Isaac Knight, age 40, was found electrocuted in his office, the victim of a faulty wire. His cluttered desk suggested an abrupt and unexpected end to his work.",
            "victim_relation_desc1": "Eve, Isaac’s assistant, had a rumored secret relationship with him. Although they never admitted to it, their close working relationship made her an emotional and vulnerable target.",
            "victim_relation_desc2": "Oliver, Isaac’s business rival, had been trying to acquire Isaac's startup. Their professional rivalry had escalated, and Oliver had made several veiled threats.",
            "victim_relation_desc3": "Tessa, Isaac’s wife, had recently discovered that Isaac was hiding significant financial problems. This revelation caused a rift between them, leaving Tessa feeling betrayed and mistrustful."
            },
            {
            "victim_name": "Amanda Lee",
            "victim_age": 34,
            "victim_height": "5'6\"",
            "victim_weight": "140 lbs",
            "victim_eye": "brown",
            "victim_hair": "black",
            "victim_identification": "poisoned by a glass of wine in her apartment",
            "victim_related1": "Paul, her editor",
            "victim_related2": "Zoe, her roommate",
            "victim_related3": "James, a fellow journalist",
            "victim_desc": "Amanda Lee, age 34, was found in her apartment, poisoned. A half-full glass of wine was left on the coffee table beside her. The death was slow and deliberate.",
            "victim_relation_desc1": "Paul, Amanda's editor, had an unspoken rivalry with her. He often dismissed her ideas, and their professional relationship was strained by subtle conflicts.",
            "victim_relation_desc2": "Zoe, Amanda’s roommate, had been seen arguing with Amanda over personal issues. Their living arrangement had become tense in the weeks leading up to the death.",
            "victim_relation_desc3": "James, a fellow journalist, had a deep grudge with Amanda. She had exposed his corruption in an investigation, leading to a personal vendetta."
            },
            {
            "victim_name": "Rafael Ortiz",
            "victim_age": 29,
            "victim_height": "5'9\"",
            "victim_weight": "175 lbs",
            "victim_eye": "brown",
            "victim_hair": "dark brown",
            "victim_identification": "asphyxiated by a heavy rope in his gym",
            "victim_related1": "Carmen, his girlfriend",
            "victim_related2": "Elena, his business partner",
            "victim_related3": "Carlos, a regular client",
            "victim_desc": "Rafael Ortiz, age 29, was found asphyxiated by a heavy rope in his gym. His body was positioned next to a weight machine, an unsettling scene of physical control.",
            "victim_relation_desc1": "Carmen, Rafael’s girlfriend, had grown increasingly suspicious of his flirtations with other clients. Their relationship was strained by her jealousy and distrust.",
            "victim_relation_desc2": "Elena, Rafael’s business partner, had been in frequent financial disputes with him over the ownership and management of the gym.",
            "victim_relation_desc3": "Carlos, a regular client at Rafael's gym, had become overly attached to him. Rafael’s shifting attention to other clients had caused Carlos to feel rejected and betrayed."
            }
        ]
        }

    
    return case_data

def pickCase():
    case_number = random.randint(1, 5)
    case_data = generateCase(case_number)
    
    # Save the case data as JSON
    with open('case_data.json', 'w') as json_file:
        json.dump(case_data, json_file, indent=4)



pickCase()