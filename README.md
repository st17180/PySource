# PySource
A system independent resource monitor written in python with psutil.

## The Idea
A program to view system information like cpu/memory/disk usage. the user will be able to save a copy of the currently displayed info, adjust how the info is shown etc. through a CLI for users, or to use the main as they want in their own code

## Rescrictions
depend on as few external librarys as resonable, (just psutil now)

## milestones 
- [X] the base functions on which the following milestones will be built to use ( unchecked as disk function only works on UNIX systems for now )
- [X] a CLI tester for the functions
- [X] a CLI for people to use  ( this and the tester are now one in the same, replacing the "read" flag to false will turn the CLI into the tester )
- [ ] saving output to a file.

## current plan 
- [X] create functions to update and format results into a format to be used by later sections like the GUI or CLI
  - [X] cpu usage as list of values related to the cpu core number if above 1 to list of all available cores
    - [X] add switch to change results from per core usage to total cpu usage
  - [X] mem usage as usage of total available in GB
    - [X] add switch to change results from GB to MB or TB etc
  - [X] disk usage as useage of total available in GB
    - [X] add switch to change results from GB to MB or TB etc
- [X] create CLI to interact with the base functions directly
  - [X] a human readable mode
    - [X] small menu to call each function with help option
  - [X] a system useable mode
    - [X] documented expected formatting for each function
  - [ ] add ability to save out to a file.

## testing
- [ ] base functions
  - [ ] cpu
    - [ ] per_cpu/total toggle
  - [ ] memory
    - [ ] mb/gb toggle
  - [ ] disk
    - [ ] mb/gb toggle
- [ ] CLI
  - [ ] flag to change between human readable, and system useable
  - [ ] huamn readable menu to call each function
  - [ ] system useable formatting for each function
  - [ ] output save option

## relavent implications

#### some relavent implications for this program are 
sustainability and future proofing, useability, functionality, legal

