"""
This is the NormalGPRDataBuilder class.

"""
# import gprMax.GPRModule.gprMax.model_build_run
import argparse
import datetime
import os
import platform
import sys

from enum import Enum
from io import StringIO

from GPRDataBuilder import GPRDataBuilder
from gprMaxLocal.model_build_run import run_model

from gprMax.utilities import get_terminal_width
from gprMax.utilities import timer

from gprMax.constants import c
from gprMax.constants import e0
from gprMax.constants import m0
from gprMax.constants import z0

from gprMaxLocal.utilities import open_path_file
class NormalGPRDataBuilder(GPRDataBuilder):
    def __init__(self):
        self.inputfile = open_path_file('input.in')

        # TODO: 问题出在这里

        # inputlines = [line.rstrip() for line in self.inputfile if (not line.startswith('##') and line.rstrip('\n'))]
        # print(inputlines)
        # Create a separate namespace that users can access in any Python code blocks in the input file
        self.usernamespace = {'c': c, 'e0': e0, 'm0': m0, 'z0': z0, 'number_model_runs': 1, 'inputfile': os.path.abspath('input.in')}

    # From gprMax Project
    def run_std_sim(self, optparams=None):
        """
        Run standard simulation - models are run one after another and each model
        is parallelised using either OpenMP (CPU) or CUDA (GPU)

        Args:
            args (dict): Namespace with command line arguments
            inputfile (object): File object for the input file.
            usernamespace (dict): Namespace that can be accessed by user in any
                    Python code blocks in input file.
            optparams (dict): Optional argument. For Taguchi optimisation it
                    provides the parameters to optimise and their values.
        """

        # Set range for number of models to run
        # if args.task:
        #     # Job array feeds args.n number of single tasks
        #     modelstart = args.task
        #     modelend = args.task + 1
        # elif args.restart:
        #     modelstart = args.restart
        #     modelend = modelstart + args.n
        # else:
        modelstart = 1
        modelend = modelstart + 1
        numbermodelruns = 1

        tsimstart = timer()
        for currentmodelrun in range(modelstart, modelend):
            # If Taguchi optimistaion, add specific value for each parameter to
            # optimise for each experiment to user accessible namespace
            if optparams:
                tmp = {}
                tmp.update((key, value[currentmodelrun - 1]) for key, value in optparams.items())
                modelusernamespace = self.usernamespace.copy()
                modelusernamespace.update({'optparams': tmp})
            else:
                modelusernamespace = self.usernamespace
            run_model(currentmodelrun, modelend - 1, self.inputfile, modelusernamespace)
        tsimend = timer()
        simcompletestr = '\n=== Simulation completed in [HH:MM:SS]: {}'.format(
            datetime.timedelta(seconds=tsimend - tsimstart))
        print('{} {}\n'.format(simcompletestr, '=' * (get_terminal_width() - 1 - len(simcompletestr))))

    def AScan(self):
        self.run_std_sim()

