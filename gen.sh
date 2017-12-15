#!/bin/bash

echo "generating profile pic..."
python crop.py -r 0.4 shraman.jpg

echo "generating all other pics..."
python crop.py -s 0.15 -nc ICML17.png
python crop.py -s 0.6 -nc 6s191.png
