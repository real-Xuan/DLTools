"""
This is the NormalGPRDataBuilder class.

"""


from rich import print
from GPRDataBuilder import GPRDataBuilder
from GPRModule.gprMax.model_build_run import run_model


class NormalGPRDataBuilder(GPRDataBuilder):
    def __init__(self, model, frequency, amplitude, phase, x, y, z):
        self.model = model
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.x = x
        self.y = y
        self.z = z
        self.batchSize = 512

    # From gprMax Project
    def run_std_sim(args, inputfile, usernamespace, optparams=None):
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
        if args.task:
            # Job array feeds args.n number of single tasks
            modelstart = args.task
            modelend = args.task + 1
        elif args.restart:
            modelstart = args.restart
            modelend = modelstart + args.n
        else:
            modelstart = 1
            modelend = modelstart + args.n
        numbermodelruns = args.n

        tsimstart = timer()
        for currentmodelrun in range(modelstart, modelend):
            # If Taguchi optimistaion, add specific value for each parameter to
            # optimise for each experiment to user accessible namespace
            if optparams:
                tmp = {}
                tmp.update((key, value[currentmodelrun - 1]) for key, value in optparams.items())
                modelusernamespace = usernamespace.copy()
                modelusernamespace.update({'optparams': tmp})
            else:
                modelusernamespace = usernamespace
            run_model(args, currentmodelrun, modelend - 1, numbermodelruns, inputfile, modelusernamespace)
        tsimend = timer()
        simcompletestr = '\n=== Simulation completed in [HH:MM:SS]: {}'.format(
            datetime.timedelta(seconds=tsimend - tsimstart))
        print('{} {}\n'.format(simcompletestr, '=' * (get_terminal_width() - 1 - len(simcompletestr))))

    def AScan(self):
        return self.run_std_sim()
