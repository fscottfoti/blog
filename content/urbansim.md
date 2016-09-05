Title: UrbanSim, etc
Category: urbansim
Date: 2016-09-02
Thumbnail: images/urbansim.jpg
SubTitle: A brief history of UrbanSim, Synthicity, and our Autodesk adventure

The next few blog posts are going to be about projects from the past couple of years.  Yes, I'm way behind in documenting a few very important projects, but better late than never.

## UrbanSim the Repo

For starters, let's discuss the new version of [UrbanSim](http://github.com/udst/urbansim).  The first commit was made by me in August of 2013, and was part of some consulting work being done through the firm Synthicity.  At the time it seemed like the circa 2003 version of UrbanSim (called OPUS) was overkill for a more simple analysis, and the nascent Pandas library was perhaps replacing a big part of the original infrastructure.  

This turned out to be a good call as Pandas exploded on to the scene over the next couple of years after that, and hooking the project to Pandas seems obvious in retrospect.

The bulk of the code in the repo at this time was written by Matt Davis (@jiffyclub on GitHub) who currently works at Clover Health.  The UrbanSim repo contains modules that still almost perfectly follow the methodology written by Paul Waddell (my PhD advisor at Berkeley) in the excellent [2002 paper](http://astro.temple.edu/~jmennis/Courses/GUS_0150/readings/Waddell02.pdf).  Matt put together modules for hedonics, location choice models (which required an MNL module), and transition models.  UrbanSim also has a few modules written by me: mainly Pandana, the DataFrame Explorer and the ProForma and Developer modules, and I will cover these in other blog posts.

## Synthicity the Startup

This post is intended to be a personal history as much as a technical one, and I think fondly of the long days coding on the 3rd floor above Telegraph Ave in Berkeley.  With street people near Amoeba music keeping us almost constantly distracted, and the outdoor deck of Cafe Durant serving for many a "pivot," the office was as much a lab as a startup.  I made some great friends in those days and I wish them all well in their future endeavors.  More than a few are still related to this project in some fashion.

We started to get more serious in 2014, if I have my dates correct, as we took a class with Steve Blank in the business school at Berkeley (the Lean Launchpad) and became Entrepreneurs in Residence in the San Francisco Planning Department.  Carlos, Fede, and Jason worked diligently on the UrbanCanvas city-scale planning support tool (for lack of a better term), and sometime around May, Justin Lokitz from Autodesk came to get a demo.

Take this as an opinion of just one person, but my read is that Autodesk was completely comfordable with the combination of simulation on the cloud with a 3D desktop GUI for designing cities.  More than a few of their products followed this model, and certainly Infraworks was headed in this direction, although Infraworks was more of an engineer's tool than a planner's.  They liked the synergy with InfraWorks, and liked that we were a hop, skip, and a jump from their headquarters now located in Downtown SF.  By Jan of 2016, we had been acquired and were working in their office.

## The Autodesk Experiment

I stayed on for only the first 6 months of working at Autodesk, as for me I prefer the lab or startup feel of an organization to protecting the value of the shares of a publicly traded company.  Autodesk seemed about as non-evil a large corportation as can exist on Wall Street, I just can't go to work on the dark side of a skyscraper and discuss sales all the time.  I went to work for MTC in July, essentially to continue my UrbanSim work and get them through the next Plan.

I wasn't privy to what happened next, but suffice it to say that Synthicity was spun back out of Autodesk in the spring of 2016 into UrbanSim Inc, with a renewed focus on regional modeling. Hopefully they make some good progress over the next couple of years and I wish all the luck to the folks at UrbanSim Inc.

*To learn more about the Pandas-based UrbanSim implementation see this [paper](https://journal2.osgeo.org/index.php/journal/article/download/223/189).*
