#/usr/bin/python3

""" Given a number N, reads parteN-sol.ipynb and generates parteN.slides.html  (without the -sol!)

DIRTY script! 

TO CHECK:  
    - commands like 
      jupyter nbconvert --to slides parte2-sol.ipynb --SlidesExporter.reveal_theme=sky --SlidesExporter.reveal_transition=fade     
      Current supported options are here:
      https://github.com/jupyter/nbconvert/blob/68b496b7fcf4cfbffe9e1656ac52400a24cacc45/nbconvert/exporters/slides.py
    - currently (oct 2022) this option is NOT supported: --SlidesExporter.reveal_navigationMode=linear
    - how to specify a custom made theme from command line   
    - offline browsing

"""


custom_css = "_static/css/softpython-slides.css"


from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('slide', metavar='N', type=int, nargs='?', default=-1,
                    help='an integer for the slide number')
args = parser.parse_args()
print(args.slide)
sn = args.slide

if sn == -1:
    print("Please specify a slide number. Aborting.")
    exit(1)

prefix = f'parte{sn}'

import subprocess


import tempfile
import os

tempdir = tempfile.gettempdir() 

raw_slides_html = os.path.join(tempdir, f'{prefix}-sol')

cmd = ['jupyter', 'nbconvert', '--to', 'slides', f'{prefix}-sol.ipynb', '--output', raw_slides_html]
print(' '.join(cmd))
res = subprocess.check_output(cmd)

print(res)


dest = f'{prefix}.slides.html'

print("Reading", raw_slides_html)
with open(f'{raw_slides_html}.slides.html', encoding='utf8') as fr:
    s = fr.read()
    
    ps = s
    rev = '<div class="reveal">'    
    ps = ps.replace(rev, rev + f'\n <link rel="stylesheet" href="{custom_css}" id="theme">')
                    
    
    ps = ps.replace('transition: "slide",',
    """
            transition: "fade",
            navigationMode: "linear",                
    """)
    
    ps = ps.replace('slideNumber: "",', 
                    'slideNumber: true,')
    
    with open(dest, 'w', encoding='utf8') as fw:
        fw.write(ps)
        print("Done writing", dest)
        

