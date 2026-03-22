# Deep Learning Tools (DLTools)

DLTools is a multi-domain preprocessing and postprocessing toolkit for deep learning workflows.

Current implementation focus:
- CV (computer vision) utilities
- Radar/Signal (GPR-oriented) utilities

Planned domains:
- NLP
- Audio/Speech
- IoT/TimeSeries

## Project Status

The repository has started a packaging-first refactor.

Implemented in this milestone:
- `src`-layout Python package scaffold
- Installable package metadata (`pyproject.toml`)
- First migrated CV module: motion blur PSF + filtering API
- First migrated Radar module: DZT read + aligned batch read + save API
- Minimal tests for CV blur primitives

## Install

Core:

```bash
pip install -e .
```

CV extras:

```bash
pip install -e ".[cv]"
```

Radar extras:

```bash
pip install -e ".[radar]"
```

Development tools:

```bash
pip install -e ".[dev]"
```

All extras:

```bash
pip install -e ".[all]"
```

## Package Layout

```text
src/dltools/
   core/      # pipeline and shared primitives
   cv/        # computer vision algorithms
   radar/     # radar/gpr io and signal utilities
tests/       # test suite
```

## Quick Start

```python
import numpy as np
from dltools.cv import generate_psf

psf, anchor = generate_psf(length=21, angle=15.0)
print(psf.shape, anchor, np.sum(psf))
```

```python
from dltools.radar import read_dzt_files_aligned, save_array

data = read_dzt_files_aligned("/path/to/dzt_dir")
save_array(data, "aligned.mat", file_type="mat")
```

## Migration Note

The package is migrating from legacy top-level folders (for example `CV/`, `GPRModule/`) to `src/dltools/*`.
As agreed in this refactor, legacy import paths are not preserved for compatibility.

## Cleanup Note

Deprecated files that are already replaced by the new package modules were removed to keep the repo simple:
- removed legacy C++ motion blur implementation
- removed legacy Python CV motion blur implementation in top-level folder
- removed legacy DZT alignment script in top-level folder
- removed obsolete `requirements.txt` (dependency source of truth is now `pyproject.toml`)

Legacy root-level module folders were consolidated under `src/dltools/legacy/`.
The repository root now keeps only project-level files and non-package assets.

## Docker

```bash
docker build -t dltools .
```

