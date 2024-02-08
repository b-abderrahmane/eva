"""Helper function from models defined with a function."""

from typing import Any, Callable, Dict

import jsonargparse
import torch
from torch import nn
from typing_extensions import override


class ModelFromFunction(nn.Module):
    """Wrapper class for models which are initialized from functions.

    This is helpful for initializing models in a `.yaml` configuration file.
    """

    def __init__(
        self,
        path: Callable[..., nn.Module],
        arguments: Dict[str, Any] | None = None,
    ) -> None:
        """Initializes and constructs the model.

        Args:
            path: The path to the callable object (class or function).
            arguments: The extra callable function / class arguments.

        Example:
            >>> import torchvision
            >>> network = ModelFromFunction(
            >>>     path=torchvision.models.resnet18,
            >>>     arguments={
            >>>         "weights": torchvision.models.ResNet18_Weights.DEFAULT,
            >>>     },
            >>> )
        """
        super().__init__()

        self._path = path
        self._arguments = arguments

        self._network = self.build_model()

    def build_model(self) -> nn.Module:
        """Builds and returns the model."""
        class_path = jsonargparse.class_from_function(self._path, func_return=nn.Module)
        return class_path(**self._arguments or {})

    @override
    def forward(self, tensor: torch.Tensor) -> torch.Tensor:
        return self._network(tensor)