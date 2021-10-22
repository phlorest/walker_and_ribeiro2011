import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "walker_and_ribeiro2011"

    def cmd_makecldf(self, args):
        """
summary.trees: original/aruakout
	nexus trees -t -c $< $@

posterior.trees: original/Aruakrrw.trees.txt.zip
	unzip -c $< > tmp
	nexus trees -n 1000 -c tmp -o $@
	rm tmp

data.nex:
	cp original/ArawakNexusFile.txt $@
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'aruakout',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.read_nexus(
                self.read_gzipped_text(self.raw_dir / 'Aruakrrw.trees.txt.zip'),
                remove_rate=True,
            ).write(),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'ArawakNexusFile.txt')
