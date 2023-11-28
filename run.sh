#!/bin/bash
sudo snap install voxcraft-viz
python3 firstSimulation.py
./voxcraft-sim -i data/ -o results.xml -f > robot1.history
voxcraft-viz robot1.history