# python-citations-helper
Helps put in text citations into web versions of scientific reports. Uses WET-BOEW GoC.

## Usage
Run `citations.py` and input the in-text citation (ie, `(Claus, 2019)`). Then input the long citation. The in-text citation acts as a key, so the next time this citation comes up, it'll 
know it's already been created. Then the program automatically adds the long final citation to a separate file and copies the in-text html citation to your clipboard that you
can just paste in.

## Backstory

Way back in 2020, I was working for Environment and Climate Change Canada (ECCC). They wanted me to transcribe a huge research report into a webpage, and add these little
citations everywhere. It was very cumbersome and annoying, so of course as any CS student would do, this was my attempt at trying to automate it.
