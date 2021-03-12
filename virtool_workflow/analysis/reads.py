from dataclasses import dataclass
from pathlib import Path

from virtool_workflow.analysis.utils import ReadPaths, make_read_paths
from virtool_workflow.data_model import Sample


@dataclass
class Reads:
    """Dataclass representing prepared reads for an analysis workflow."""
    paired: bool
    min_length: int
    max_length: int
    count: int
    paths: ReadPaths

    @classmethod
    def from_sample(cls, sample: Sample, path: Path):
        min_length, max_length = sample.quality["length"]
        count = sample.quality["count"]
        return cls(sample.paired, min_length, max_length, count, make_read_paths(path, sample.paired))

    @classmethod
    def from_quality(cls, quality: dict, paired: bool, path: Path):
        min_length, max_length = quality["length"]
        count = quality["count"]
        return cls(paired, min_length, max_length, count, make_read_paths(path))
