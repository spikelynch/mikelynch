
## Immutable and pure

Functional programming is one of the oldest paradigms - Lisp, the first functional language, is the second-oldest in wide use - and the current functional programming renaissance (check this) is based on restrictions which are radical compared to these: immutablility and removal of side-effects.

In terms of our imaginary workshop, immutability is the principle that an object can be placed in a box once, and once only.  If box "A" contains that blue thing, it will contain the blue thing for all time ("all time" in this context does not necessarily mean "forever" - we'll get to that.)

The boxes in our workshop are variables, and immutability is a hard concept for a lot of coders to get their head around: an immutable variable seems like a contradiction in terms, and if you've come from the imperative paradigm much of what your program (thinking in terms of the little homunculus) actually *does* is change variables: take some input, do some calculations, and then set the relevant variables to the correct value.

Immutability doesn't mean that the program can't perform calculations: just that the results of these calculations must be stored in a different variable, not used to overwrite the old one. It's hard to overstate the scope of the potential for subtle bugs which this simple rule removes. In a program with mutable variables, at any point in its execution, the value in a variable X is (in a mathematical sense) a function of the inputs to the program and every single decision made in the program's execution up till that point. With immutable variables, the value of X is a function of its definition, and any input values which are implicated in that.

We've effectively removed the homunculus' ability to shuffle objects between boxes: instead of a workshop with an infinite array of shelves, immutable variables might better be though of as dials or sockets carrying signals.

## Purity

The second restriction, which is only imposed on a small number of functional programming languages, is easy to state in terms of our workshop, but may be more difficult for non-programmers to understand. It's really two restrictions placed on the tools in the workshop, which are:

* a tool should always produce the same output objects if it's used on the same inputs, and
* a tool's only effects can be the value of its outputs.

The problem with our analogy is that actual physical tools pretty much obey these rules anyway. If you drill a hole in a blue block of wood with a drill, and then take a second blue block of wood and drill a hole in the same place, you'll get two identical blue blocks of wood with holes in them. In our analogy, tools represent functions, and, unfortunately, in software, functions can very often break both of these rules:

* functions can refer to variables other than their inputs (but which are still within scope), so their behaviour is not solely determined by those inputs;
* functions can have side-effects: they can modify variables other than their outputs, or maintain internal state variables which will affect the results of later usage on the same inputs

(Immutable variables generally take care of the second of these restrictions, but it's worth stating it anyway.)

Side-effects are a ripe source of bugs, as they are a way in which the overall state of an application can be changed in ways which are not particularly obvious to the coder.  The conceptual problem with removing side-effects is that in one sense, especially if you've learned to program in the imperative paradigm, side-effects are how programs *work*. Your code accepts some inputs, performs calculations and shuffles data, and then *does something* (sets a variable, writes text to the command-line, makes a picture appear on the monitor); in other words, it has a side-effect.  Understanding how programs can even make sense without side-effects is a big hurdle to using pure functional languages, and one of the reasons I'm writing this is an attempt to communicate what a radical idea it is, without having to go into too much technical detail (although I'm aware I might have gotten well past that point about a thousand words ago).

As we've placed more and more restrictions upon the actions which the poor homunculus can perform in the workshop, something interesting has happened, which should remind us that the homunculus itself has always been a bad analogy. Implicit in the metaphor is the idea of a decision-point, however fictional: picture the homunculus looking at the next line in its recipe book, reading it, and thinking: what comes next? Do I need to look up one of the countless boxes containing an object of type "wooden"? Which tool should I use? When I use it, what boxes should I change as it operates? And where should I put the results?

The effect of the restrictions has been to reduce the scope of the imaginary decisions which the homunculus has to make.  It can't put objects back in boxes, because variables are immutable. It can't interrupt the operation of a tool to change anything, and it can't do anything with the output other than put them in new boxes.  Steadily, what started out as feeling like a kind of puppet show or drama has become more like fitting together components or wiring up a machine.

# Welcome to the machine

I can distinctly remember the first time I had this feeling, which was when I'd developed an intuition for the particular mathematical formalism which Haskell uses to represent operations with side-effects while remaining formally pure.  (They're called monads, and are sufficiently hard to grasp that monad tutorials are their own mini-genre: I won't go into more details, lest I add to it.)

The feeling was that in coding, I was no longer writing instructions, but describing the components of a machine: these components were well-defined, connected together properly, and, as a whole, were a sort of pipeline which accepted requests in at one end (the piece of software was a web server) and would provide the correct answers at the other.

The reason that this feeling is extremely good is so simple and straightfoward that it sounds kind of dumb to express it: when you write a computer program, you are configuring a machine.  You're not writing a script for an imaginary puppet. 
--
This gets to a paradox which I am starting to feel is at the heart of coding, and what it is we are actually doing when we sit in front of a glowing rectangle for hours, swearing under our breath. The idea of a programming language which excludes state changes seems completely counter-intuitive to someone who's learned to program in the older paradings of imperative or object-oriented programming. The mathematical formalisms which languages like Haskell use in order to do stateful computation - random numbers, input from the external world, interaction with a human user, output to external data stores or equipment - are borrowed from some of the more abstract and recent fields in pure mathematics like category theory, and are extremely non-trivial to understand, to the extent that one can do a lot of very productive programming in Haskell without being able to give a rigorous explanation of what a monad is, or even why it's necessary.

But, once you've reached the point I described at the start of this post, coding in a pure functional language starts to feel more intuitive and solid than any other form of coding, and when you then return to an imperative language, it feels incredibly wobbly and loose by comparison.

(If you're uninterested in technical details, you can skip the next few paragraphs)

To take a very simple example: the most basic form of syntax in imperative programming is the idea that one statement is executed after another, like so:

do_first_thing();
do_second_thing();
do_third_thing();

Haskell's equivalent to this style of programming - which is obviously necessary in many contexts, especially when the application has to take something from a source, perform a computation on it, and then return it - is, in effect, to wrap the sequence of computations in a formalism which maps order-of-execution onto order-of-evaluation, like so:

result = do_first_thing >>= do_second_thing >>= do_third thing

The key to understanding this is that instead of having a large, hard-to-visualise state which surrounds the sequence of statements, there's an actual value (in this case, a monadic wrapper around something) which gets passed from one statement to the next until the end result comes out.

Once you are used to a programming language in which a sequence of computations have to "plug into" one another (ie they have to pass a "state" token between them of the correct type), a language in which you can just say one thing after another and see what happens feels like driving with your seatbelt off.

One of the better analogies for monads is that they are "programmable semicolons": when I switched back into Perl after finishing a Haskell project, semicolons felt like brain-damaged monads.

(Ok, non-technical readers can stop skipping stuff now)

The paradox I'm talking my way around here is this:

Pretending that there's a little guy in the computer who does stuff for you, based on a set of instructions which you have written for him, is a natural way to try to understand what coding is about. But computers are formidably intricate machines, and the metaphor of the homunculus is not only an imperfect fit for them, but can actively get in the way of configuring them to do things.

The homunculus seems like a slave, but I think my second reading of the metaphor is more truthful: the homunculus is a metaphor for the coder, lost in a maze of implicit state, having to decide (from all the possibilities, with whatever restrictions that make this set of possibilities more tractable) what the hell is going on here. It's better if we abandon it altogether, drop the pretense that we are writing a script for a puppet, and learn better ways to make our machines work.

