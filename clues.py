# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

import emoji

CLUES = {
    "clue-1": {
        "available": datetime.date(day=16, month=12, year=2015),
        "question": ("text", "Let's start with a standard riddle: 'I have billions of eyes, yet I live in darkness. "
                             "I have millions of ears, yet only four lobes. I have no muscle, "
                             "yet I rule two hemispheres. What am I?'\nTry it without using Google ;)"),
        "solutions": ("a human brain", "brain", "human brain", "brains", "human brains"),
        "answers": {
            "correct": ("text", "Great! You have the first one! :D. "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "I'm afraid it's quite easy if you use Google",
            "May be the riddle appears in some comic... may be...",
            "OK, you can use Google if you are desperate :P",
        ]
    },
    "clue-2": {
        "available": datetime.date(day=17, month=12, year=2015),
        "question": ("photo", {"caption": "Where was I in this picture?", "file": "files/clue2.png"}),
        "solutions": ("camino de santiago", "santiago", "cruz de ferro"),
        "answers": {
            "correct": ("text", "Great! You have another one! :D "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "The history of Spain almost start there",
            "It's like the most famous path!",
        ]
    },
    "clue-3": {
        "available": datetime.date(day=18, month=12, year=2015),
        "question": ("text", "Today (or at least the day this clue was released) is the premier of the "
                             "new movie of Star Wars, could you tell me the name of new bad guy?"),
        "solutions": ("kylo ren",),
        "answers": {
            "correct": ("text", "Great! You have one more! :D. "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "Naa, too easy for more clues",
        ]
    },
    "clue-4": {
        "available": datetime.date(day=19, month=12, year=2015),
        "question": ("audio", {"text": "What am I doing while this music sounds in my mind?", "file": "files/clue4.wav"}),
        "solutions": ("boxing", "rocky", "rocky balboa"),
        "answers": {
            "correct": ("text", "Great! You have it! "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "Never give up!",
            "I guess what I’m trying to say is, if I can change, and you can change, everybody can change.",
        ]
    },
    "clue-5": {
        "available": datetime.date(day=20, month=12, year=2015),
        "question": ("video", {"caption": "Who am I going to vote on the next spanish elections?",
                               "file": "files/clue6.mp4"}),
        "solutions": ("alberto", "alberto garzon", "alberto garzón", "garzon", "garzón"),
        "answers": {
            "correct": ("text", "Great! You have another one! You know a lot of things about me now!"
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "They are the cats of the candidate!",
            "He has my same age!",
        ]
    },
    "clue-6": {
        "available": datetime.date(day=21, month=12, year=2015),
        "question": ("photo", {"caption": "I can program this... thing! but, what is ti?", "file": "files/clue5.png"}),
        "solutions": ("lego", "lego mindstorms", "lego mindstorm", 'mindstorm', 'mindstorms'),
        "answers": {
            "correct": ("text", "Great! You have another one! We're almost done! :D "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "This is not only a 'robotic' stuff, it's also a toy!",
            "Blocks, blocks and more blocks!",
        ]
    },
    "clue-7": {
        "available": datetime.date(day=22, month=12, year=2015),
        "question": ("photo", {"caption": "This is where my favorite animated series takes place", "file": "files/clue7.png"}),
        "solutions": ("ooo", "land of ooo"),
        "answers": {
            "correct": ("text", "Great! You have another one! We're almost done! :D "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "What time is it?",
            "Yes, I like cartoons, but only the good ones!"
        ]
    },
    "clue-8": {
        "available": datetime.date(day=23, month=12, year=2015),
        "question": ("text", "How does a 'snake' says 'hello' to all the world?"),
        "solutions": ("print('hello world')", 'print("hello world")', 'print("hello world!")', "print('hello world!')",
                      'print("hi world")', "print('hi world')"),
        "answers": {
            "correct": ("text", "Great! You have one! :D. "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "Everything is about computers!",
            "Which is the first program you should learn to write?",
            "Which is the 'snake' programing language?",
            "It's a single and basic line in a programming language...",
        ]
    },
    "clue-9": {
        "available": datetime.date(day=24, month=12, year=2015),
        "question": ("text", emoji.emojize(":christmas_tree: Happy merry christmas! :christmas_tree:\n"
                                           "(Just answer 'merry christmas!' to continue the game)\n"
                                           "https://open.spotify.com/track/6MPpnJDLk37GEIM0iGGITd")),
        "solutions": ("happy merry christmas!", "merry christmas!"),
        "answers": {
            "correct": ("text", emoji.emojize(":santa: :gift: :gift: :gift: oh oh oh!", use_aliases=True)),
            "wrong": ("text", emoji.emojize(
                    ":christmas_tree: Just answer 'merry christmas!' to continue the game :christmas_tree:",
                    use_aliases=True
            )),
        },
        "hints": [
            emoji.emojize(
                    ":christmas_tree: Just answer 'merry christmas!' to continue the game :christmas_tree:",
                    use_aliases=True
            )
        ]
    },
    "clue-10": {
        "available": datetime.date(day=26, month=12, year=2015),
        "question": ("audio", {"text": "What specie is the animal who makes this sound?", "file": "files/clue10.mp3"}),
        "solutions": ("cat", "kitten", "pebe"),
        "answers": {
            "correct": ("text", "Great! You have another one! We're almost done! :D "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "Really? It's the only animal in Internet!",
        ]
    },
    "clue-11": {
        "available": datetime.date(day=27, month=12, year=2015),
        "question": ("text", "And the final question... who the hell am I? ;)"),
        "solutions": ("marcos", "markos", "marcos gabarda", "markos gabarda"),
        "answers": {
            "correct": ("sticker", "BQADBAADJgADGolEAAER8FNsi1NergI"),
            "wrong": "Nope, try again ;)",
        },
        "hints": [
            "No more clues this time :P",
        ],
        "solve": True
    }
}
