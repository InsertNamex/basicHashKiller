# basicHashKiller
This is a super basic hash killer that I made for the purpose of teaching in a discord community I'm apart of. It's probably super easy to break.

DISCLAIMER:
  This repository is to be used for educational purposes only. "Cracking" hashes can be fun and but I really do not recommend trying to use the program for illicit means. I made it in a few short hours theres way better programs for it so it doesn't even make sense to actually use it outside the scope of learning how hashes work and their flaws and benefits. Also this program is super easy to break. What I mean by that is if you're using this to learn and you do not follow the directions thoroughly you will run into errors.
  
Anyways with the slighlty legal bs out the way lets start learning d:

What is a hash and what are hashes and hashing algorithms?
  
    If you know how cryptography works then hashes will be super simple to pick up. To put it at a super basic and very misleading way, hashing algorithms take a string value and transform it into another value, I got that definition from a google search and it doesn't really tell you much. Hashing algorithms are simply algorithms that take data and change the the data to a form that cannot be reversed through the algorithm. 

For Example:

    Dog gets turned into "06d80eb0c50b49a509b49f2424e8c805" when using the md5 hashing algorithm.
    What's this long string of characters called? The hash!
    There is no way of taking the hash and using the algorithm to get the plain text input of dog. This is important and wise to take note of.

Okay. Why is this important to me?

    Website's used to store password in their databases in plain text. Until hackers came around and leaked these databases to the internet. This was in the early days of the internet and cybersecurity so you cannot really blame these companies for not really knowing better. What they did to combat this is they started hashing their users passwords and storing the hashes into the database. So if it was compromised, they hacker would just have files upon files of stored hashes.
    
But people know a-days still have their password leaked sometimes and theirs still so many databases being leaked, What's going on?!?!

    Well lets say I have this list of hashes that a website uses. (I do not, Federal Prison doesn't sound like a good time.) What can I do to find the plain text equivalent to these hashes? This question has multiple different answers. One of the most common, and easier methods is through the use of a wordlist that we can utilize to compare hashes using a script. What's a wordlist? It's just a text file with normally an extreme amount of common passwords or words that we can use to compare hashes.
    We can make a program that hashes every word in the wordlist and check to see if it matches the hash we already have! If it does, then we can print out the word with the match and theres our plain text match!

Steps:
    1. Copy one of the passwords in the fake passwords list. Run the createhash.py program and paste the fake password when prompted.
    2. This will spit out the md5 hash that we will be using the hashkill.py, run the hashkill.py program and input the hash.
    3. Wait for the program to find a match! It will print out the the match once it finishes.

Addition Info & conclusion

    Please view the program and read the comments. I'm going to add more information there explaining why certain lines are there and how they work.
    There are a lot of hashing algorithms. They all have different reasons for using them. Some are better than others. I encourage you to learn about these algorithms and why they're used or not used. Also theres something I didn't mention at all and that is salting. This repository teaches you about hashes and how they work as well as how to do a dictionary attack. The word list is considered a dictionary and salting a hash is how you deter and prevent dictionary attacks from happening. Salting is adding additional input to change the hash. So back to our dog example earlier. Once dog is inputted it would get changed to something like "dog0a12m" and then get hashed which would make our dictionary attack useless d: If this repository gains some traction i'll probably put more effort into making the program and the explanation better. Maybe even a youtube video, I really just did this because I had some spare time I enjoy teaching a lot.

