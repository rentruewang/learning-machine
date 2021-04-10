# Intro to machine learning

## What exactly is machine learning?

_"Machine learning (ML) is the study of computer algorithms that improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to do so."_ --- Widipedia

Woah, woah! That's a mouthful! What is it supposed to mean?

Machines do what programmers tell it to do. Exactly. Without exception. If the machine didn't do what you want it to do, then your are the one who made the mistake in writing a program. Normally we call this a **bug**.

But Wikipedia says _"make predictions or decisions without being explicitly programmed to do so."_ How can I write a program without telling it what to do? Does it automatically do what I want it to do?Well, sort of. Let me elaborate on that. 

## Why is machine learning helpful?

Usually when a program is created, the programmer writing it would design the program to do specific things. Your "Hello World" program is designed to log strings to the console. We all have the experience of finding a computer program, a website, or a mobile app, so dumb it's infuriating to use. It's likely because the designers of the program have failed to cover all the cases that a user might want to use it. **In other words, they haven't seen you use the app, so they didn't consider it used this way.** This is where machine learnings might come to the rescue!

Alternatively, you design a program that's extensible, it acts according to data it receives. It _learns_ what is given to it. Now your problem of programs not doing what the users want is no more! Your program now automatically adapts to your users. And you have eliminated a lot of edge cases you previously have to write.

An example of that would be the modern translation system. Sure, you know how 'hello' can be translated into 'bonjour', but there are just too many ways of how 'hello' can be integrated into a sentence. In other words, there are just too many possibilities to list all of them down. And there is just not a simply rule for it. **But the power of machine learning is to generalize on seen data, and to extend it beyond what is known.** With it, which we'll cover "how" down the book, you will see how this is done without explicitly programmed into the program.

But the benefits doesn't just stop here. The generalization of machine learning is so powerful it can aid in problems where programmers often don't even know where to start. Say, telling bananas from apples. It's a simple enough task but very difficult to be described in simple constructs (if, else, for...), so much that before machine learning this is nearly impossible to do. Again, you'll see how to solve this problem with machine learning in the book.


## Summary

If we only care about seen data, we could simply use a mapping and call it a day. **The reason machine learning is so powerful is because how well it can generalize on previously unseen data.**
