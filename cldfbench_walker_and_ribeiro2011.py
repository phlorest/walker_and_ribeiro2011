import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "walker_and_ribeiro2011"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree('aruakout', detranslate=True),
            self.metadata,
            args.log)

        posterior = self.sample(
            self.raw_dir.read_nexus(
                'Aruakrrw.trees.txt.zip',
                remove_rate=True,
            ).write(),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('ArawakNexusFile.txt'),
            self.characters,
            args.log)

