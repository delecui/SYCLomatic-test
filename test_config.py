# ====------ test_config.py---------- *- Python -* ----===##
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
#
# ===----------------------------------------------------------------------===#

# The arguments
DPCXX_COM = "dpcpp "     # Default compiler
CT_TOOL = "dpct"         # The migration tool binary name
PYTHON_COM = "python3 "
suite_list_file = "test_suite_list.xml"   # The configuration file lists all the suite to run and corresponding options.

VERBOSE_LEVEL = 0       # Debug verbose level： 0: silent all the debug information. None 0: turn on all the debug information.

current_test = ""  # The name of current test. The test driver will automatically set a name for current test, if the current test is empty.
command_file = ""  # Used to store the execution command.
log_file = ""      # Default: <workspace>/[test name].lf
result_text = ""   # Default: <workspace>/result.md
include_path = ""  # Specify the CUDA header file path.

out_root = ""
command_output = ""
cuda_ver = 0        # CUDA header file version.
test_status = ""    # the test case execution status: MIGFAIL, COMPFAIL, RUNFAIL, SKIPPED or PASS.
test_option = ""    # Ref the option_mapping.json file table.
failed_message = ""
test_driver = ""
suite_cfg = ""      # Parsed from <suite>.xml.
migrate_option = ""
workspace = ""
option_map = ""       # Option mapping table. Ref: option_mapping.json
root_path = ""      # The root path of test repo.
timeout = 300       # The time limit for each test case.

# The default device for the test. Device can be "CPU", "OpenCL:GPU" and "LEVEL_ZERO:GPU".
# For all the devices: https://intel.github.io/llvm-docs/EnvironmentVariables.html#sycl_device_filter
device_filter = "LEVEL_ZERO:GPU"

# Depended libraries
mkl_link_opt_lin = ["-lmkl_intel_ilp64", "-lmkl_sequential", "-lmkl_core",
                    "-lOpenCL", "-lmkl_sycl", "-lpthread", "-ldl"]

mkl_link_opt_win = ["mkl_sycl_dll.lib", "mkl_intel_ilp64_dll.lib", "mkl_sequential_dll.lib", "mkl_core_dll.lib", "sycl.lib", "OpenCL.lib"]

mkl_comp_opt = ["-DMKL_ILP64"]