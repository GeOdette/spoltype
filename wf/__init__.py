"""
Assemble and sort some COVID reads...
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile


@small_task
def spolingotype(read1: LatchFile, read2: LatchFile) -> LatchFile:

    # A reference to our output.
    spol_file = Path("covid_assembly.sam").resolve()

    _spolingotyoe_cmd = [
        "spolTools",
        "--local",
        "-x",
        "mycobacterium",
        "-1",
        read1.local_path,
        "-2",
        read2.local_path,
        str(spol_file),
    ]

    subprocess.run(_spolingotyoe_cmd)

    return LatchFile(str(spol_file), "latch:///spolingotype.sam")


@workflow
def spoltype(read1: LatchFile, read2: LatchFile) -> LatchFile:
    """A handy tool to analyze the genetic diversity of M.tuberculosis

    Spoltype
    ----

    Spoltype allows you to perform a comprehensive spolingotype analysis of your mycobacterium strains.
    You can analyze the history of mutation events, therefore relationships among spoligotypes, and determine emerging strains.

    __metadata__:
        display_name: Manipulate and analyze spoligotype datasets of the Mycobacterium tuberculosis complex
        author:
            name: spoltype
            email:
            github:
        repository:
        license:
            id: MIT

    Args:

        read1:
          Paired-end read 1 for genetic diversity.

          __metadata__:
            display_name: Read1

        read2:
          Paired-end read 2 file for genetic diversity.

          __metadata__:
            display_name: Read2
    """
    return spolingotype(read1=read1, read2=read2)
