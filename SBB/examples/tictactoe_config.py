import copy

"""
##### Results using Mann-Whitney U-Test (http://www.socscistatistics.com/tests/mannwhitney/Default2.aspx):

balanced_opponent_populations True or False?
hall_of_fame True or False?
diversity?

TICTACTOE_DEFAULT x TICTACTOE_PROGRAM20
- cerca de 6500 secs per run x cerca de 9850 secs per run
- best team validation: The U-value is 331. The Z-Score is -0.119. The p-value is 0.90448. The result is not significant at p <= 0.05.
- global validation: The U-value is 287. The Z-Score is -0.9242. The p-value is 0.35758. The result is not significant at p <= 0.05.

TICTACTOE_DEFAULT x TICTACTOE_REGISTER1
- without extra registers, there are no introns! the programs are more sensitive to mutations!
- cerca de 5150 secs per run x cerca de 6500 secs per run
- best team validation: The U-value is 250.5. The Z-Score is 1.5922. The p-value is 0.11184. The result is not significant at p <= 0.05.
- global validation: The U-value is 265. The Z-Score is 1.3268. The p-value is 0.18352. The result is not significant at p <= 0.05.

TICTACTOE_REGISTER1 x TICTACTOE_PARETOP
- cerca de 5150 secs per run x cerca de 6300 secs per run
- best team validation: The U-value is 315.5. The Z-Score is -0.4026. The p-value is 0.68916. The result is not significant at p <= 0.05.
- global validation: The U-value is 303. The Z-Score is -0.6314. The p-value is 0.5287. The result is not significant at p <= 0.05.
- inconclusive results, it is necessary to evaluate the point population evolution more carefully to draw a conclusion
- vou manter o pareto por enquanto, jah que rpetendo usa-lo no poker

"""

TICTACTOE_DEFAULT = {
    'task': 'reinforcement',
    'reinforcement_parameters': { # only used if 'task' is 'reinforcement'
        'environment': 'tictactoe', # edit _initialize_environment() in SBB and RESTRICTIONS['environment_types'] to add new environments (they must implement DefaultEnvironment)
        'validation_population': 300, # at a validated generation, all the teams with be tested against this population, the best one is the champion
        'champion_population': 1000, # at a validated generation, these are the points the champion team will play against to obtain the metrics
        'opponents_pool': 'only_coded',
        'balanced_opponent_populations': False, # if false, the opponent populations will be swapped instead of mixed
        'hall_of_fame': {
            'enabled': True,
            'diversity': 'normalized_compression_distance', # if False, use the fitness as the criteria to remove teams when the Hall of Fame is full
        },
        'debug_matches': False, # use this option to debug
    },

    'training_parameters': {
        'runs_total': 25,
        'generations_total': 300,
        'validate_after_each_generation': 25,
        'populations': {
            'teams': 100,
            'points': 100,
        },
        'replacement_rate': {
            'teams': 0.5,
            'points': 0.2,
        },
        'mutation': {
            'team': {
                'remove_program': 0.7,
                'add_program': 0.7,
                'mutate_program': 0.2, # is applied to all programs in the team, until at least one program is mutated
            },
            'program': {
                'remove_instruction': 0.5,
                'add_instruction': 0.5,
                'change_instruction': 1.0,
                'swap_instructions': 1.0,
                'change_action': 0.3,
            },
        },
        'team_size': { # the min size is the total number of actions
            'min': 2,
            'max': 18,
        },
        'program_size': {
            'min': 2,
            'max': 10,
        },
    },

    'advanced_training_parameters': {
        'seed': 1, # default = None
        'use_pareto_for_point_population_selection': False, # if False, will select points using uniform probability
        'use_operations': ['+', '-', '*', '/', 'ln', 'exp', 'cos', 'if_lesser_than', 'if_equal_or_higher_than'],
        'extra_registers': 0,
        'diversity': {
            'use_and_show': [], # will be applied to fitness and show in the outputs
            'only_show': [], # will be only show in the outputs
            'k': 10,
        },
        'run_initialization_step2': False,
    },
}
TICTACTOE_DEFAULT_1 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_DEFAULT_1['advanced_training_parameters']['seed'] = 1
TICTACTOE_DEFAULT_1['training_parameters']['runs_total'] = 13

TICTACTOE_DEFAULT_2 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_DEFAULT_2['advanced_training_parameters']['seed'] = 2
TICTACTOE_DEFAULT_2['training_parameters']['runs_total'] = 13

TICTACTOE_PROGRAM20_1 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_PROGRAM20_1['advanced_training_parameters']['seed'] = 1
TICTACTOE_PROGRAM20_1['training_parameters']['runs_total'] = 13
TICTACTOE_PROGRAM20_1['training_parameters']['program_size']['max'] = 20

TICTACTOE_PROGRAM20_2 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_PROGRAM20_2['advanced_training_parameters']['seed'] = 2
TICTACTOE_PROGRAM20_2['training_parameters']['runs_total'] = 13
TICTACTOE_PROGRAM20_2['training_parameters']['program_size']['max'] = 20

TICTACTOE_REGISTERS1_1 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_REGISTERS1_1['advanced_training_parameters']['seed'] = 1
TICTACTOE_REGISTERS1_1['training_parameters']['runs_total'] = 13
TICTACTOE_REGISTERS1_1['advanced_training_parameters']['extra_registers'] = 1

TICTACTOE_REGISTERS1_2 = copy.deepcopy(TICTACTOE_DEFAULT)
TICTACTOE_REGISTERS1_2['advanced_training_parameters']['seed'] = 2
TICTACTOE_REGISTERS1_2['training_parameters']['runs_total'] = 13
TICTACTOE_REGISTERS1_2['advanced_training_parameters']['extra_registers'] = 1

TICTACTOE_PARETOP_1 = copy.deepcopy(TICTACTOE_REGISTERS1_1)
TICTACTOE_PARETOP_1['advanced_training_parameters']['use_pareto_for_point_population_selection'] = True

TICTACTOE_PARETOP_2 = copy.deepcopy(TICTACTOE_REGISTERS1_2)
TICTACTOE_PARETOP_2['advanced_training_parameters']['use_pareto_for_point_population_selection'] = True

TICTACTOE_BALANCED_1 = copy.deepcopy(TICTACTOE_PARETOP_1)
TICTACTOE_BALANCED_1['reinforcement_parameters']['balanced_opponent_populations'] = True

TICTACTOE_BALANCED_2 = copy.deepcopy(TICTACTOE_PARETOP_2)
TICTACTOE_BALANCED_2['reinforcement_parameters']['balanced_opponent_populations'] = True

TICTACTOE_NOFAME_1 = copy.deepcopy(TICTACTOE_PARETOP_1)
TICTACTOE_NOFAME_1['reinforcement_parameters']['hall_of_fame']['enabled'] = False

TICTACTOE_NOFAME_2 = copy.deepcopy(TICTACTOE_PARETOP_2)
TICTACTOE_NOFAME_2['reinforcement_parameters']['hall_of_fame']['enabled'] = False