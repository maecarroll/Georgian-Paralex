
from paralex import paralex_factory

package = paralex_factory("Georgian Paralex Unimorph Data",
    {
     "paradigms": {"path": "Georgian_v_paradigms.csv"},
     "cells": {"path": "Georgian_v_cells.csv"},
     "paradigms": {"path": "Georgian_v_paradigms.csv"},
     "features-values": {"path": "Georgian_v_features.csv"},
     "sounds": {"path": "Georgian_v_sounds.csv"}
     },
     citation="Carroll, MJ (2022). Georgian Verbal Paradigms Paralex dataset. Online.",
     version="1.0.0",
     keywords=["Georgian", "paradigms"],
     id="",
     contributors=[{'title': 'MJ Carroll', 'role': 'author'}],
     licenses=[{'name': 'GPL-3.0',
               'title': 'GNU General Public License 3.0',
               'path': 'https://opensource.org/licenses/GPL-3.0'}],
               )
package.to_json("Georgian.package.json")
