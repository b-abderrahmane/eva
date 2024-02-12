"""Image classification datasets API."""

from eva.vision.data.datasets.classification.bach import Bach
from eva.vision.data.datasets.classification.patch_camelyon import PatchCamelyon
from eva.vision.data.datasets.classification.total_segmentator import TotalSegmentatorClassification

__all__ = ["Bach", "PatchCamelyon", "TotalSegmentatorClassification"]