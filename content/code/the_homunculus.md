--
Title: The Homunculus
Tags: ai, code, language, functional
Slug: homunculus

* In all humility: I used to be like this
* the nerd mistake: computers are idiots
* (digression about law)
* digression about bitcoin mashing together several different and
  distinct things
* creating an image of themselves which they project onto others
* (digression on interdisciplinary mischief)
* relevance to Haskell: true functions, immutability
* side-effects are not side-effects: they are the essence of
imperative code

_The first in a series of posts about the philosophy of programming_

This is the first in a series of posts about the way we think about
programming, the influence these ideas have on how we write code
and what languages we choose, and why I like the functional
programming paradigm in general and Haskell in particular.

Consumer notification: I've worked as a programmer for decades, but
for many of those years I wrote bad code in Perl, and I've had no
formal training in software design or computer science. These posts
should be taken as part sketchy meditation on the philosophy of
programming, part mea culpa.  I don't want to add another "burn
down software and start again" rant to the literature.

This first post is a digression into an unfairly extreme case of how
IT people misunderstand law, and a confession.  Here is the the
extreme case, taken from the manifesto of Ethereum, a project which is
planned as a replacement for both Bitcoin, and, speaking of burning
things down and starting again, the civil law:

http://etherscripter.com/what_is_ethereum.html

> The authors of laws and the writers of contracts face a special kind
> of challenge. Ideally, there should never be any confusion about the
> meaning of the agreement. But laws are written with words, and words
> are famously imprecise.
>
> So these are big problems with traditional law. Agreements are
> ambiguous. And enforcement is hard.
> 
> Ethereum solves both these problems. It does this with the marriage
> of two special ingredients: a digital currency, and a complete
> programming language. Let’s look at both.

This is an extreme example of what Evgeny Morozov calls "solutionism":
the belief that apparently intractable problems will melt away given a
correct technological framework. That's not why I'm quoting it here,
though, and this is where the confession comes in. I studied law for
my undergraduate degree. I never qualified as a solicitor, and only
spent a little over a year in a legal workplace before I realised that
the profession didn't suit my temperament. So I'm not equipped
to give any kind of advice.  However, as someone who studied law
after they had already learned the elements of programming, I can
recognise the way IT geeks misunderstand the law from a mile away. I
know this misunderstanding intimately, having suffered from it. It
can be summed up in a sentence:

> Legal rules are sufficiently like a computer progam that the one can
> be analysed and reformed using techniques from the other.

This is one of those seductive ideas that's superficially plausible
but wrong. It's wrong in a way which makes it very bad for analysing
law or politics, and in one way or another, most of the attempts by IT
people to grapple with these fields, whether these are scornful
dismissals or quixotic pledges of reform, can be reduced to it.

The Ethereum blogger thinks that they've found the worst problem with
law: that it's written in what IT people refer to as "natural
language" (ie, language), and "words are famously imprecise". The
solution to this problem is a legal system in which laws are
expressed not in ambiguous, clumsy language, but in the clean
precision of code.

It's my contention that this is not only a bad way to think about both
language the law, but is also a bad way to think about computers and
software.

# Commands

There's a metaphor which is used to introduce kids to computers: I
can't remember where I first encountered it, possibly in one of the
many books I bought from Dick Smith which were full of printouts of
BASIC programs to be typed into a TRS-80 (if you didn't understand the
last clause of that sentence it roughly translates to "I am old as
balls"). The metaphor is that the computer is a willing but idiotic
servant: it will do everything you tell it to, but only exactly what
you tell it to, even if your instructions are wrong. This is not a
bad way to introduce a ten-year-old to programming, particularly if
they've got the impression from pop culture that computers are smarter
than people.

The metaphor is baked into much of the terminology of the trade:

* command
* instruction
* program
* programming language
* imperative programming
* execution

I'm not saying that developers genuinely believe that they're telling
a little homunculus inside the computer what to do: I'm saying that
the way they explain and write and think about their code is
unconsciously built around the metaphor of telling a little homunculus
what to do.

It's this metaphor which the IT style of reasoning about law is
appealing to: programs are sets of precise, unambiguous instructions,
so if we can somehow embody laws in code, we can build a legal system
which is free from ambiguous language (and, perhaps, lawyers).

# No-one home

The metaphor hides a crucial aspect of human language: it is always
addressed to a person. By this I don't just mean that human listeners
bring to bear a huge, submerged mass of assumptions and tacit
knowledge which allow them to comprehend language. I mean that all
human language is part of a dialogue between persons who are capable
of action and who are members of a community. The imaginary homunculus
to whom a program is addressed is something like an ideal slave: the
programmer (the master) provides a set of instructions to cover every
eventuality, and the computer will follow them like an ideal slave.

Contracts, and laws in general, like all examples of human language,
are not like this. The essence of a contract is that of mutual
promise, usually a promise to pay in consideration of a promise to
provide either goods, services or labour: the contract per se is a
formal recognition of an agreement between persons, and it would make
no difference if the contract were expressed as a computer programme,
rather than a template filled out by a bored junior solicitor, in a
case where the parties unintentionally misunderstood one another, or
where one was seeking to actively deceive the other. It's important to
be diligent in checking a contract for errors, omissions or
ambiguities, but removing these alone wouldn't obviate the need for a
law of contract.

# Hard cases and corner cases

Another way of looking at the quality which social and legal systems
possess, and their radical difference from the systems governed by
programming languages, is expressed in the maxim "hard cases make bad
law".  (The existence and importance of maxims in law, of precepts
which cannot be reduced to simple rules, but instead embody a kind of
general principle, also proves my point.) "Hard cases make bad law" is
a sort of counterargument to the idea that the the exception proves
the rule: it expresses the idea that the vast majority of cases are
unexceptional, and that the particular circumstances of a celebrated
or notorious case are not necessarily the best way to understand the
principles behind a law.

One of the distinctive ways in which IT people go wrong when they try
to understand legal ideas is to immediately go for hard cases: anyone
who has spent ten minutes talking about intellectual property law with
a nerd should recognise our tendency to immediately identify and
exaggerate the most absurd consequences of copyright that we can think
of. This is a misapplication of an honourable and useful trait: the
ability to identify "corner cases" - situations, or inputs, which will
tend to produce bugs, either because the programmer hasn't anticipated
them, or through pure cussedness, admirable summed up in this tweet:

<blockquote class="twitter-tweet" lang="en"><p lang="nl" dir="ltr">QA Engineer walks into a bar. Orders a beer. Orders 0 beers. Orders 999999999 beers. Orders a lizard. Orders -1 beers. Orders a sfdeljknesv.</p>&mdash; Bill Sempf (@sempf) <a href="https://twitter.com/sempf/status/514473420277694465">September 23, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>

Hard cases may make bad law, but corner cases make good software.
