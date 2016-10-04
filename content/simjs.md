Title: Taking a Crack at UrbanSim in Javascript
Category: urbansim
Date: 2016-9-30
Thumbnail: images/simjs.png
SubTitle:
Tags: urbansim

One of my biggest beefs about doing urban modeling in Python and Pandas is when the specific modeling task doesn't map well to a vectorized operation.  Since Python performance degrades significantly over simple for loops - see [this](http://stackoverflow.com/questions/8097408/why-python-is-so-slow-for-a-simple-for-loop) for more info - a simple code section inside of a loop that runs a million times can take an order of magnitude longer to run in Python than other languages.

Interestingly, JavaScript does not suffer from this problem, and since everyone has a JavaScript environment already installed - their web browser - there are disctinct advantages to coding in Javascript.  About a year ago I spent a few hours writing up a few simple UrbanSim models in Javascript to see what it might look like, and the results are available [here](https://github.com/oaklandanalytics/sim.js).

Javascript, combined with a simple utility library like Underscore or Lodash, begins to look more like Python.  For the actual data analysis I used the popular (for visualization mainly) d3 library.  Most variables were aggregations at the TAZ level which d3 does a little [awkwardly](https://github.com/oaklandanalytics/sim.js/blob/a0981d4d1a175785ed8e45fa98f56f92c58dda85/sim.js#L112) compared to Pandas.  There are a few Javascript libraries which attempt to mimic Pandas more [closely](https://github.com/data-forge/data-forge-js), but none of them seem to have the user base yet to use in big projects.

I then took the actual specification from the Bay Area UrbanSim and attempted to copy the residential hedonic, which can be seen [here](https://github.com/oaklandanalytics/sim.js/blob/a0981d4d1a175785ed8e45fa98f56f92c58dda85/sim.js#L193).  This does simulation but not estimation.  It seems to me that for a use case like this, you'd estimate in your preferred language, save the coefficients, and copy the model into Javascript.  There are also [libraries](https://github.com/simple-statistics/simple-statistics) which can do regression in Javascript, but I don't know of any libraries to do choice models in Javascript though it seems entirely plausible to write one.

The real win comes when you run the developer pro formas in a non-vectorized form (no [arg maxes](https://github.com/UDST/urbansim/blob/master/urbansim/developer/sqftproforma.py#L629!) which looks like [this](https://github.com/oaklandanalytics/sim.js/blob/a0981d4d1a175785ed8e45fa98f56f92c58dda85/sim.js#L319).  This to me is the natural way a pro forma should look for these kinds of models.

This was just a proof of concept which shows promise, but in the end the power and breadth of Python and Pandas still takes the day for me for most use cases.  Running simpler analysis in the browser seems utterly feasible (no pun intended) though, and future blog posts will continue exploring this topic.
