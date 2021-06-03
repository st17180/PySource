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
  - [X] add ability to save out to a file.

## testing see [Closed + Testing flags](https://github.com/st17180/PySource/issues?q=label%3ATesting+is%3Aclosed)
- [X] base functions
  - [X] cpu
    - [X] per_cpu/total toggle
  - [X] memory
    - [X] mb/gb toggle
  - [X] disk
    - [X] mb/gb toggle
- [X] CLI
  - [X] flag to change between human readable, and system useable
  - [X] huamn readable menu to call each function
  - [X] system useable formatting for each function
  - [X] output save option

## relavent implications
functionality Does the outcome work as intended and why it matters, useability does the outcome give the user freedom does it have error prevention and recoverey and is it consistent in this, NEED ONE MORE HERE, sustainability and future proofing will the outcome remain up to date and relevant.
#### how they'll be addressed in this program
for functionality each release of the program was tested to atleast have some level of the end goal in functionality, each commit pushing the program further in that direction, weather or not the program functions correctly matters because if a nonfunctional version was released and users update to it, it could break any of their projects that depend on it or their own personal use of the program may lead them to getting missinformation

for useability the program was broken up into multiple layers, firstly weather or not it was going to be used by a human or another program in the "readability" varaiable the "Monitor" class asks for, as well as the many different function specific flags such as mb or gb in disk and memory functions. the user has complete freedom over what results they get so even though the default is made for human readable formatting they could just as easily make it use the systems format, as well as error prevention and recovery, if a function is configured it will just return a string saying as such, if the CLI getts a innapropreate responce it will correct the user both error prevention, and error recovery

for NEED ONE MORE HERE

for sustainability and future proofing each outcome was planned out ( and later even rewriten) for readable code, code that depended on as little 3rd party librarys as possible ( this was taken down to just psutil ) as well as minimal lines of code and work arounds, the less the program depends on other programs the lower the chance it breaks because of them, the less moving parts in a program then lower the points of failure. and making sure this is all written in a reliably readable way ensures the program will continue to be easily adpated to any changes that might be needed in the future making it alot more sustainable

