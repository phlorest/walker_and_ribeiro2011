import pathlib

import phlorest

def fix_rate(x):
    return x.replace("[&rate=1.0]", "")



class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "walker_and_ribeiro2011"

    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
            self.raw_dir.read_tree(
                'aruakout', detranslate=True),
            self.metadata,
            args.log)

        # We ran Markov chains for 2 x 10^7 generations, sampling trees 
        # every 10^4 generations to remove autocorrelation and disregarding
        # the initial half to allow ample burn-in time
        posterior = self.raw_dir.read_trees(
            'Aruakrrw.trees.txt.zip',
            preprocessor=fix_rate,
            burnin=5000, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('ArawakNexusFile.txt'),
            self.characters,
            args.log)
