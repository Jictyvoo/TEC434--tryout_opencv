from typing import Final

from modules.ground_truth import calculate_gt
from modules.remove_noise import remove_noise

"""A tuple that contains all cli functions for every module"""
MODULES_CLI: Final = [remove_noise, calculate_gt]
