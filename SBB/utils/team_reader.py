import json
from ..core.program import Program
from ..core.team import Team
from ..core.instruction import Instruction
from ..config import Config

def read_team_from_json(team_descriptor, environment):
    programs = []
    for program_descriptor in team_descriptor['programs']:
        instructions = []
        for instruction_descriptor in program_descriptor['instructions']:
            instruction = Instruction(mode = instruction_descriptor['mode'], 
                target = instruction_descriptor['target'], op = instruction_descriptor['op'], 
                source = instruction_descriptor['source'])
            instructions.append(instruction)
        program = Program(-1, instructions, program_descriptor['action'], 
            program_id = program_descriptor['program_id'])
        programs.append(program)
    return Team(-1, programs, environment, team_id = team_descriptor['team_id'])

def initialize_actions_for_second_layer(path, environment):
        Config.RESTRICTIONS['second_layer']['short_action_mapping'] = {}
        Config.RESTRICTIONS['second_layer']['action_mapping'] = {}
        temp_actions_as_dicts = {}
        with open(path) as data_file:
            data = json.load(data_file)
        for index, team_json in data.iteritems():
            index = int(index)
            team_id = str(team_json['team_id'])+":"+str(team_json['generation'])
            Config.RESTRICTIONS['second_layer']['short_action_mapping'][index] = team_id
            temp_actions_as_dicts[index] = team_json

        for action, team_descriptor in temp_actions_as_dicts.iteritems():
            team = read_team_from_json(team_descriptor, environment)
            Config.RESTRICTIONS['second_layer']['action_mapping'][action] = team