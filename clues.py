# -*- coding: utf-8 -*-
from __future__ import unicode_literals

CLUES = {
    "clue-1": {
        "question": ("text", "Let's start with a standard riddle: 'I have billions of eyes, yet I live in darkness. "
                             "I have millions of ears, yet only four lobes. I have no muscle, "
                             "yet I rule two hemispheres. What am I?'\nTry it without using Google ;)"),
        "solutions": ("a human brain", "brain", "human brain", "brains"),
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
        ]
    },
    "clue-4": {
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
        "question": ("photo", {"caption": "I can program this... thing! but, what is ti?", "file": "files/clue5.png"}),
        "solutions": ("lego", "lego mindstorms", "lego mindstorm", 'mindstorm', 'mindstorms'),
        "answers": {
            "correct": ("text", "Great! You have another one! We're almost done! :D "
                                "Remember, you can use /current to check the new clue ;)"),
            "wrong": "Ups, that's not the answer you're looking for",
        },
        "hints": [
            "This is not only a 'robotic' stuff, it's also a toy!",
        ]
    },
    "clue-6": {
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
        ]
    },
    "clue-7": {
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
