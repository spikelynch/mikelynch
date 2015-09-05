Killing the Homunculus
======================

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

_The first in a series of posts about Haskell and the philosophy of programming_

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

I am going to start this off with an unfairly extreme case, and a
confession.  Here is the the extreme case, taken from the manifesto of
Ethereum, a project which is planned as a replacement for both
Bitcoin, and the current system of law:

http://etherscripter.com/what_is_ethereum.html

> Hopefully you wrote down the terms of that loan as a
> contract. However, the authors of laws and the writers of contracts
> face a special kind of challenge. Ideally, there should never be any
> confusion about the meaning of the agreement. But laws are written
> with words, and words are famously imprecise.
>
> So these are big problems with traditional law. Agreements are
> ambiguous. And enforcement is hard.
> 
> Ethereum solves both these problems. It does this with the marriage of
> two special ingredients: a digital currency, and a complete
> programming language. Let’s look at both.

This is an extreme example of what Evgeny Morozov calls "solutionism":
the belief that seemingly hard problems will melt away given a correct
technological framework. That's not why I'm quoting it here, though,
and this is where the confession comes in. I studied law for my
undergraduate degree.  I never qualified as a solicitor, and only
spend a little over a year in a legal workplace, so I'm not equipped
to give any kind of advice.  However, as someone who studied law
having already learned (somewhat) how to program a computer, I can
recognise the way IT geeks misunderstand the law from a mile away.
I know this misunderstanding really well, having suffered from it. It
can be summed up in a sentence

    Legal rules are sufficiently like a computer progam that the one
    can be analysed and repaired using techniques from the other.

This is not only untrue, it's deeply misleading, and the assumptions
underlying it are not only very bad for analysing law: they are bad
for writing computer progams.
