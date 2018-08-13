import sys
case = "/home/weibin/test"

from PyFoam . Applications . Decomposer import Decomposer
from PyFoam . Applications . Runner import Runner
from PyFoam . Applications . PlotRunner import PlotRunner
PlotRunner (args=["--progress","Decomposer","proc",2,"-case",case])
PlotRunner ( args =["--clear","blockMesh","-case", case ])
PlotRunner (args=["--progress","icoFoam","-case",case])  
