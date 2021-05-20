# PySource
A system independent resource monitor written in python with psutil, mathplotlib, and TKinter

## The Idea
A Simple GUI program to view system information like cpu/memory/disk usage. the user will be able to save a copy of the currently displayed info, adjust how the info is shown etc. through a GUI, or use a CLI to use the functions as they want.

## Rescrictions
depend on as few external librarys as possible, PSUTIL, TKinter and matplotlib are expected
keep seperate layers functions organized using oop where apropreate.

## milestones 
- [ ] the base functions on which the following milestones will be built to use ( unchecked as disk function only works on UNIX systems for now )
- [X] a CLI tester for the functions
- [ ] a CLI for people to use independly of the gui or in another program of their own
- [ ] GUI ontop of the base functions.
- [ ] useage graphs for the GUI

## current plan 
- [X] create functions to update and format results into a format to be used by later sections like the GUI or CLI
  - [X] cpu usage as list of values related to the cpu core number if above 1 to list of all available cores
    - [X] add switch to change results from per core usage to total cpu usage
  - [X] mem usage as usage of total available in GB
    - [X] add switch to change results from GB to MB or TB etc
  - [ ] disk usage as useage of total available in GB ( unchecked as it only currently works on UNIX systems with root '/' )
    - [X] add switch to change results from GB to MB or TB etc
- [ ] create CLI to interact with the base functions directly
  - [X] a human readable mode
    - [X] small menu to call each function with help option
  - [ ] a system useable mode
    - [ ] documented expected formatting for each function
- [ ] create GUI area and setup to pipe the functions written before to
  - [ ] area for basic text results, and any switchs for them ( change from GB to MB etc )
  - [ ] area for graphs from matplotlib
- [ ] create graphs of the results with mathplotlib to pipe to the above gui
  - [ ] add graph on call ( a button or something similar)
  - [ ] update graph automatically as results come in

## testing
- [ ] base functions
  - [ ] cpu
    - [ ] per_cpu/total toggle
  - [ ] memory
    - [ ] mb/gb toggle
  - [ ] disk
    - [ ] mb/gl toggle
- [ ] CLI
  - [ ] flag to change between human readable, and system useable
  - [ ] huamn readable menu to call each function (the tester for the base functions)
- [ ] GUI
  - [ ] basic text display from base functions
  - [ ] toggles for base functions to change the text display
  - [ ] program management buttons ( exit, save results)
  - [ ] graphing results in a chart


## relavent implications
#### some relavent implications for this program are 
sustainability and future proofing, useability, functionality, legal
#### why they are relavent to this program
sustainability and future proofing, the concept for this program is to be a platform agnostic way to view system resources and useages. for this to be a reasonable goal the program will need to be easily worked on and adapted so it can continue to work on more than one system. as well as to be able to adapt to changes in the different sections of the program like the backend functions to get system resources or the graphical user interface.

#### how they will be addressed when creating the program
sustainability and future proofing, to address the need to have the program be easily adaptable in the future, and easyily modified for those potentional future changes I will be using as little external librarys as I can within reason, stick to a standard programming style (PEP8) and keep the program sectioned in planning and in programming like so. (base functions, GUI, testing tools, CLI).
