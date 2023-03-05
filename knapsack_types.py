from typing import Callable, List, NamedTuple, Tuple

# type declaration
Genome = List[int]
Population = List[Genome]
FitnessFunction = Callable[[Genome], int]
PopulateFunction = Callable[[], Population]
SelectionFunction = Callable[[Population,
                              FitnessFunction], Tuple[Genome, Genome]]
CrossoverFunction = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunction = Callable[[Genome], Genome]
Item = NamedTuple(
    'Item', [('name', str), ('value', float), ('weight', float)])
