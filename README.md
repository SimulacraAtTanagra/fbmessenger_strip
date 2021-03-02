## The purpose of this project is as follows:
This program takes facebook conversation history exports and turns them into excel files.
## Here's some back story on why I needed to build this:
I had a long conversation history with someone that, with mutual consent, I wanted to set about mining for ideas. Needing to sanitize and organize the data before feeding it to someone (or something) else to tag/ parse required it being in a format that was amenable to scaling and automation. 
This project leverages pandas, beautifulsoup4.
##In order to use this, you'll first need do the following:
If you choose to run this from the commandline, you have to define FILENAME and OUTFILE first. FILENAME is the full filepath of the document (HTML file as of this writing), and outfile is the full filepath of an excel file that will be created upon completion. 
The expected frequency for running this code is As Needed.