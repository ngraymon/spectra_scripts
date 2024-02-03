# system imports
import shutil
import itertools as it
import sys
import os

# third party imports

# local imports
from project_parameters import *

execute_script = "submit_cc.sh"


def submit_multiple_jobs():
    for FC_or_not, coupling_order in it.product(["FC", "vibronic"], ["constant", "linear", "quadratic"]):
        if FC_or_not == "vibronic" and coupling_order == "constant":
            continue

        if coupling_order != "linear":
            continue

        name = "_".join([project_name, FC_or_not, coupling_order])
        for param_list in it.product(*expression_list):
            submit_dir = join(work_root, dir_string.format(name, *param_list))
            shutil.copy("./cc_script.py", submit_dir)
            shutil.copy("./submit_cc.sh", submit_dir)
            command = f"sbatch --mem=5GB --partition=highmem --chdir={submit_dir} {execute_script}"
            print(command)
            # os.system(command)


def submit_single_jobs():
    # FC_or_not = "FC"
    FC_or_not = "vibronic"

    # coupling_order = "constant"
    coupling_order = "linear"
    # coupling_order = "quadratic"

    model_name, A, N = "hexahelicene", 15, 63

    job_name = "_".join([model_name, FC_or_not, coupling_order])

    time = 50.0
    dir_string = f"{job_name:s}_tf{time:.2f}"

    work_root = abspath(f"/work/$USER/projects/2022_tamp_testing/{model_name}/")
    submit_dir = join(work_root, dir_string)
    os.makedirs(submit_dir, exist_ok=True)  # make sure the root directory exists

    # copy scripts to run
    shutil.copy("./cc_script.py", submit_dir)
    shutil.copy("./submit_cc.sh", submit_dir)

    # copy the model files
    shutil.copy(f"../models/{model_name}/{job_name}.op", submit_dir)

    # run the command
    # command = f"sbatch --mem=20GB -c 4 --chdir={submit_dir} {execute_script}"
    # command = f"sbatch --mem=20GB -c 20 --chdir={submit_dir} {execute_script}"
    # command = f"sbatch --mem=35GB -c 16 --chdir={submit_dir} {execute_script}"
    command = f"sbatch --mem=35GB -c 16 --nodelist=cpu16002 --chdir={submit_dir} {execute_script}"
    # command = f"sbatch --mem=30GB --ncpus=8 --partition=highmem --chdir={submit_dir} {execute_script}"

    print(command)
    os.system(command)


if __name__ == "__main__":
    # submit_multiple_jobs()

    submit_single_jobs()
