# PYTHON_READER_ASSISTANT

The objective is to provide for readers of science or philosophy articles, and books, a tool for identifying the "gist." 
The simplest function returns the list in decreasing order of frequency the main content key-words of the corpus.
This is easy to do - provided the corpus has been adequately pre-processed.
The pre-processing also converts a .DOCX (previously created, say, by Export of .PDF using Adobe Acrobat DC) into a list
of sentences as a list of strings.
Input of a .TXT file is also an option.
One function worth having is to return sentences with the highest number of most frequent key-words.
Sentences found should have the key-words converted to UPPER-CASE for ease of reading.
Ultimately, syntax analysis of sentences identified as above shoudl provide further "gist" information.
In particular, preposition analysis is a syntax analysis goal.
The PYTHON_READER_ASSISTANT should be to reading of technical articles and boosk as the Coq proof assistant is to mathematics.
