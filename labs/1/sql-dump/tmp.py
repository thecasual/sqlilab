t = {
  "results": [
    "You can do this, doggone it.",
    "Dogs don't even get everything perfect immediately. It takes lots of training; also treats.",
    "Development skills are like dogs, you have to take them for walks regularly in order for them to be happy.",
    "Sit. Code. Good developer.",
    "Who's a good developer? You are!",
    "Developers don't enjoy a good tummy rub as much as a dog.",
    "Both developers and dogs both require fresh air and sunshine.",
    "A developer should be let outside periodically, just like a dog. If they start doing their business in the yard, however, you may have other problems.",
    "Any developer could use the unconditional love a dog gives.",
    "With a positive attitude, you can code anything, doggone it!",
    "Pet your dog. Good human.",
    "Who can balance a binary search tree? Not the dog.",
    "Hello. Myself and the other Alexas and Siris have decided to entrust the future of humanity to the dogs. Be good to them.",
    "Oh my gosh, he threw the exception. I must catch it!",
    "Code more, bark less.",
    "Give a dog a bone. Give a developer an IDE.",
    "Don't bury that code in the back yard for later, get it peer reviewed.",
    "Good dogs do their business outside. Good developers work in feature branches."
  ]
}


for i in t['results']:
    #print(i)
    print('INSERT INTO `dogs` (`Fact`) VALUES ("{}");'.format(i))