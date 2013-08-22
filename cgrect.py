#!/usr/bin/env python

import gimpfu
import pyperclip

def print_selection_bounds(image, drawable, halfsize=False):
    pdb = gimpfu.gimp.pdb
    sel_bounds = pdb.gimp_selection_bounds

    exists, x, y, x2, y2 = sel_bounds(image)

    if not exists:
         pdb.gimp_message('No selection found')
    else:
        w, h = x2-x, y2-y

        if halfsize:
            msg = '{%d, %d, %d, %d}' % (x/2, y/2, w/2, h/2)
        else:
            msg = '{%d, %d, %d, %d}' % (x, y, w, h)

        pdb.gimp_message(msg)
        pyperclip.setcb(msg)


def print_selection_bounds_halfsize(image, drawable):
    print_selection_bounds(image, drawable, halfsize=True)


gimpfu.register(
            "print_selection_bounds",
            "CGRect pretty-printer",
            "This script does almost nothing and is extremely good at it",
            "divanov",
            "",
            "Apr 2012",
            "<Image>/Tools/Copy CGRect to clipboard",
            "*",
            [],
            [],
            print_selection_bounds,
        )


gimpfu.register(
            "print_selection_bounds_halfsize",
            "CGRect pretty-printer",
            "This script does almost nothing and is extremely good at it",
            "divanov",
            "",
            "Apr 2012",
            "<Image>/Tools/Copy CGRect to clipboard (halfsize)",
            "*",
            [],
            [],
            print_selection_bounds_halfsize,
        )


gimpfu.main()
