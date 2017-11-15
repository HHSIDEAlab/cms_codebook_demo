# Convert PDF CodeBooks to html

This is a hack that takes the CMS Fee For Service Code Book and converts
it from a PDF document to a series of html files.

The IDR JPDFHTML converter is used to convert the PDF file.
The resulting zip file should be downloaded and unzipped.

The converter is here:
https://www.idrsolutions.com/online-pdf-to-html5-converter/


Te output consists of a series of page files: 1.html to nnn.html
Each file has an accompanying folder: 1 to nnn that contains the graphics
for the relevant page.

This hack will load each file in turn and look for a line with the following 
content:

    LABEL:</div>
    
Get the previous line and extract the content of the DIV. This is the name 
of the CODE.

The hack should save the file with a new filename that is the CODE.

The hack should cycle through each page file and perform this process.
The resulting files should be uploaded to github to a codebook repository.

This should be available as browseable files via github pages.