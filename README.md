# PySource
A system independent resource monitor written in python with psutil, mathplotlib, and TKinter

## The Idea
A Simple GUI program to view system information like cpu/memory/disk usage. the user will be able to save a copy of the currently displayed info, adjust how the info is shown etc.

## Rescrictions
depend on as few external librarys as possible, PSUTIL, TKinter and matplotlib are expected
keep seperate layers functions organized using oop where apropreate.
different layers of the program
- [X] a CLI test monitor for testing the process
- [ ] base GUI ontop of the CLI tools
- [ ] useage graphs for GUI

## current plan 
- [X] create functions to update and format systhem information into a human readable format
  - [X] cpu usage as list of values related to the cpu core number if above 1 to list of all available cores
  - [X] mem usage as usage of total available in GB
    - [ ] add switch to change results from GB to MB or TB etc
  - [ ] disk usage as useage of total available in GB
    - [ ] add switch to change results from GB to MB or TB etc
- [ ] create GUI area and setup to pipe the functions written before to
  - [ ] area for basic text results, and any switchs for them ( change from GB to MB etc )
  - [ ] area for graphs from matplotlib
- [ ] create graphs of the results with mathplotlib to pipe to the above gui
  - [ ] add graph on call ( a button or something similar)
  - [ ] update graph automatically as results come in
