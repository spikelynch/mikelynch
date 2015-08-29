---
Title: Lucid dreaming with neural nets
Tags: deepdreams, graphics, ai, code
---
The [Deepdreams algorithm](http://googleresearch.blogspot.com.au/2015/06/inceptionism-going-deeper-into-neural.html) takes a deep neural net trained for
image-recognition and uses a forced-feedback loop to induce a kind
of machine-pareidolia or hallucination, with beautiful and often
nightmarish results:

![Cassowary](/images/cassowary.jpg)

The original algorithm picks details from all of the neural net's
training data, based on resemblances to the original image: the
default neural net was trained on a database with more than ten
percent dog breeds, which is why they have the nickname
'puppyslugs'.

![Puppyslugs](/images/puppyslugs.jpg)

About a month ago, [Audun Øygard posted some code](http://auduno.com/post/125362849838/visualizing-googlenet-classes) which produces visualisation of a single class
from the neural net's training data, starting out from random noise.
The results are not as weird, but they have a kind of dreamlike beauty,
and reveal fascinating details about which features of particular
classes are salient.

![Goldfish, shark, stingray](/images/deepdraw_original.png)


I started tinkering with Audun's code a couple of weeks ago to see
if it was possible to get a hybrid of the deepdreams and deepdraw
approaches: to generate controlled hallucinations from a base image.
Lucid deepdreams.

The original deepdreams code can be used to target one of many layers
in the neural net: a sample of these can be found in [my blog post](https://nannygoathill.wordpress.com/2015/07/12/all-nine-layers-of-the-deepdream-algorithm-ranked-in-order-of-eldritch-abominationhood/).
To focus on a specific image, Audun's code targets the neural net's
'loss layers': these compute the results of the image classification,
so they can be used to define a target image class.  While the rest
of the layers can take input images of different sizes, it seems that
the loss layers' image size is constrained to the size of the original
training data, which was 224x224.  Even at that low level, applying
the deepdraw algorithm to base images provides some really nice effects.

![Shark, peacock, frog](images/deepdraw_gap.jpg)

It's also possible to target more than one class at a time.  Sometimes
this doesn't work, but it can generate lovely mutants, like this
ostrich/nudibranch hybrid:

![Mutants](images/deepdraw_mutants.jpg)

Audun's original code worked on larger images by applying the technique
to randomly-selected 224x224 tiles, which can produce some nice
effects.

![Girl with traffic light earrings](images/girl_with_traffic_light.jpg)

When I modifed the code to apply the loss layer to different image
sizes without cropping, it crashed.  My knowledge of how neural nets
work is fairly sketchy, and tinkering with the pycaffe libraries just
made it crash in different ways.  So I resorted to a brute-force
approach: if I couldn't change the deepdraw input size, I could
apply it to all of the input image in 224x224 chunks. To try and
stop the grid producing artefacts at the edges, I wrote some code
which would pick out tiles in an overlapping spiral starting from
the centre of the image.  This is still producing some artefacts
around the edges, but is otherwise quite effective:

![Fort Denison with goldfish](/images/Denison_goldfish.jpg)

![Batemans Bay and stingrays](/images/Batemans.jpg)

![Nebula traffic lights](/images/nebula.jpg)

I've rolled this technique into my dream.py script, which is available
[on GitHub](https://github.com/spikelynch/deepdream).  I've also added a more detailed [usage guide](https://github.com/spikelynch/deepdream/blob/master/dream.md).

This is rough-and-ready: the original deepdream code,
and Audun's deepdraw, do passes at different scales ("octaves") to
pull out details at different levels, and I'd like to apply that
to the lucid dreams.  I also need to fix the edge artefacts.  This
version handles tiles which go outside the original image by padding
the missing content with the average colour of the rest of the tile,
but that's not working as well as expected.

The technique is a lot slower than ordinary deepdreams: each
iteration of a 224x224 tile takes about as long as a 1024x768
deepdream, and I don't have a GPU, so I won't be generating any
videos based on this very soon.

I need to learn how to do iPython for work, so I'll be releasing
the next cut of this code as an interactive notebook.  This whole
exercise has been more useful to eResearch work than I expected:
it's given me a lot of exposure to Caffe (the machine-learning
platform) and NumPy.

Also, if you like the images here, I'm posting lots more on [last-visible-dog.tumblr.com](http://last-visible-dog.tumblr.com).
