Labs for EDAN55
===============

A set of exploratory assignments designed for the course EDAN55
“Advanced Algorithms” at Lund University.

Each lab has its own directory and contains one or two subdirectories:

    <labname>/data     -- data files
    <labname>/docs     -- lab documentation (LaTeX), including a
                          report skeleton

Installation
------------

To make the documentation, you need an up-to-date (2012) version of
LaTeX. To make an individual lab, run

    cd <labname>/docs
    make

To make all labs, just

    make

in the root, which will put all PDFs into the root level directory
`docs`.
