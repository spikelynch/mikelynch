---
Title: State
---
Even though I've complained about the metaphor of the homunculus, it can be used as a useful device to explain the differences between programming paradigms to a non-technical audience. I'm optimistic about this: it's possible to understand the differences between musical or fictional genres without being a composer or a novelist, even though very little day-to-day programming is on that level. Most of it, to extend the analogies, maps onto ringtones or financial reports. You don't need to be able to program to have an appreciation of the problems and conflicts which different languages allow you to solve.

Let's return to the obedient slave at the heart of it all: the homunculus. At any point in time, it (the homunculus, like Ariel in The Tempest, is genderless) has three things at its disposal:

* the current state
* its instructions
* its actions

"State" is such a familiar term in the trade - and so often abused, in coinages like "stateful", which doesn't mean the same thing as "stately" at all - that it's worth a small digression to explain what I mean by it. In this context, "state" refers to the state of things both inside and outside the computer.  The contents of its memory, its permanent storage, and also - and this may seem a bit weird - the state of the 'external world'. For most computers, the "world" consists of whatever the user is doing to the keyboard, mouse or touch screen, the webcam, plus whatever other computers have been contacted via the internet. Computers in more specialised contexts, such as laboratories, have additional inputs from sensors and equipment.

A way to understand what state means to programming is to picture one of the most familiar scenarios in our working day: looking at part of the source code, a debugger backtrace or a log file, and muttering under our breath: "what's going on here?"  State is what's going on, and when a coder puts herself in this position, they are putting themselves in the homunculus' shoes: trying to figure out what has happened so far, what the loyal servant thinks is going on. The homunculus, seen in this light, is not so much an ideal slave as a metaphor for the coder.

So, when we stare at our image on the other side of the monitor and mutter "what's going on here", more than anything else out of the three aspects listed above, we is trying to understand the program's state. How we do this depends very much on the nature of the language she's working in, and the different ways in which programming languages manage state provide a useful way to examine the major programming paradigms.

Let's forget about computers for a moment and picture our servant in a workshop. The three things at the disposal of the servant can be understood metaphorically, as follows:

* a large storage rack containing boxes, each of which contains objects
* a book containing instructions
* a set of tools

The first of these represents the state, the second is the program, and the third are the actions available to to the servant. The differences in programming paradigms can be crudely explained by in terms of a series of restrictions on how these three aspects are allowed to work.

## Imperative

The imperative programming paradigm is the earliest, and, in an important sense, the most basic: all of the other paradigms build on it. When a program is actually executed, at the lowest level, it's imperative: all of the other paradigms are built on this one, in a similar sense to the way in which all everyday objects are made of molecules and atoms.

Working in the imperative paradigm, a typical command might be something like "get the objects found in the boxes labelled "A" and "B", operate on them with the tool called "DIVIDE", and put the result back in the box labelled "A". There are no real restrictions on what the book can tell the servant to do at a given point in time, so on the face of it, this seems to be very simple.

Things get complicated when we are attempting to get an intuition for "what's going on here" at some point in time: typically, when something's gone wrong. It could be that the contents of boxes "A" and "B", when worked on with the tool called "DIVIDE", cause the tool to malfunction (the technical term for this is "run-time exception"). The first question to ask is, how did it come to pass that boxes "A" and "B" had those values? And the reason for the complication is that the contents of "A" and "B" could have been modified by any previous stage of the instructions. Reconstructing the situation which led to the error will require (literally) tracing the instructions one step at a time from some point prior to the error in order to see what previous instruction put the forbidden object into "A" or "B".

## Scope

The potential number of previous tools, operations and values for even a simple set of instructions is dizzyingly large, so the most elementary restrictions on how this set-up works act to reduce the number of boxes and tools which can be used for a particular section of the instructions. At the top of each page in the instruction book, there is now a list of tools, and a list of boxes: if any of the instructions on that page refer to tools or boxes which aren't in the list at the top, the servant can report that something's wrong with the instructions and refuse to attempt to carry them out.

This refusal not only rules out a huge number of incoherent programs from the start, but the reduction in scope of what the instructions can refer to also makes it easier to grapple with the state of the program at any point: the potentially endless list of boxes or tools brought to bear is reduced to those which are explicitly referred to at the top of the page of instructions.

Scope can be used to narrow down the terms of reference even more.  The instructions can define temporary boxes which can only be used for a single page, or a shorter passage, of the instructions. We can think of this as a way for the instructions to define custom labels for the boxes: a subsection might start with "get two empty boxes and label them 'A' and 'B'". The servant, or the programmer, can now be confident that in that subsection, the contents of those two boxes depends completely on what has been placed in them within that subsection.  (What happens to the temporary boxes at the end of the subsection? We'll get to that soon.)

This restriction still allows us to refer to boxes which aren't "local" to a subsection, and those boxes could contain values from any other parts of this page, or other pages, so the possible sequences of events which led to a particular program state is still very large.

## Variables, objects and functions

We can place further restrictions on the homunculus' workshop to reduce the opportunities for things to go wrong when it applies the tools, by applying rules to the boxes in which the materials are stored and on the tools themselves.  Boxes can be given types, which dictate the sort of thing that can be put into them, and tools can be given instructions which specify what sorts of objects they can be applied to.  Again, this is basically giving the homunculus the ability to determine in advance whether our instructions are inconsistent, before carrying them out - for example, if we say that box "A" can contain only blue objects, and that the tool "X" can only work on red objects, and that the homunculus should take a the contents of box "A" and operate on it with tool "X". It would be possible and tiresome to develop this analogy to illustrate all of the different ways in which modern programming languages attempt to anticipate bugs, but in their different ways they all boil down to an attempt to reduce the "size" of the program's state at any point ("size" is in scare quotes because we're talking about a fairly abstract concept of "size" here which isn't directly related to the size of the source code or the computer or hard drive). For example:

* object-oriented languages use data encapsulation: an object is a structured data set which "walls off" its internal state and only interacts via a restricted set of operations ("methods")

* event-driven programming, in a sense, "encapsulate" time by breaking programming tasks down to very simple operations that react to a restricted subset of triggers

* unit testing is another form of fragmentation which breaks the criteria for the program's successful operation down into the simplest meaningful tests, allowing these to be verified in isolation from one another


