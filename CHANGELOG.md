# Changelog
All changes to this project will be documented in this file.
- Project Conception: 2019-05-09
- First Full Release: 2019-07-09  [Version 1.0.0]
- Second Full Release: 2019-04-07 [Version 2.0.1]
- Updates Since First Release: 4

## [2.0.0] - 2020-04-07 10:19:17 CST
### Comments
- Version 2 working edition of RFD
- Version 2 at this point has been tested slightly and bug squashing is in progress
### Added
- Interface implemented redesigned with PyQt5
- Source code with new and refactored code for more efficient and maintanable code

### Changed
- GUI is now implemented with PyQt5 to provide a more responsive and cleaner interface that is easier to maintain/update and compatible automatically adjusts to Windows 7 environments.
- Soure code has been broken up into seperate files each with a single use. Methods have been refactored or added to allow simpler and less code heavy methods.
- Source code has been refactored and further debugged and all known faults have been repaired

### Removed
- Interface inplemented in Tkinter
- Complicated and dense methods that were inefficient and not developer friendly

## [1.0.0] - 2019-08-23 12:37:00 CST
### Added
- Instruction Manual to accompany program.

### changed
- Modified function that writes to log file. Log file now contains alarm states
  for each parameter.
- Changed official release name of program to Raspet Flight Display.

### Removed
- cluttering code and non-functional lines previously used for test-cases and debugging purposes.
  
## [1.0.1] - 2019-07-17 12:37:00 CST
### Added
- Limits window now closes after a successful set button click.
- User can now choose to run with or without writing output to a log file.
- Status bar now shows the exact time user starts the program.
- Status bar now shows the total elapsed time of program.

### Changed
- Percentage between WARNING and ALERT have been tightened from 75% to 10%

## [1.0.1] - 2019-07-09 15:27:25 CST
### Added
- Changelog file to track changes throughout the lifespan of this project.
- Window title.

### Changed
- Build and repackage executable, updated to reflect changes made.

### Removed
- Un-used code implemented in early development for debugging or testing purposes.
- Unnecessary files.

## [1.0.0] - 2019-07-09 14:05:10 CST
### Added
- Project packaged into a single executable for the first time.