"""ABMIL network tests."""

import itertools

import pytest
import torch

from eva.vision.models.networks import ABMIL


@pytest.mark.parametrize(
    "input_size, output_size, hidden_sizes_mlp, batch_size, n_instances, masked_fraction",
    list(itertools.product([50, 384], [6], [(), (128, 64)], [1, 16], [100], [0.1, 0.6])),
)
def test_masked_abmil(
    input_size: int,
    output_size: int,
    hidden_sizes_mlp: tuple[int],
    batch_size: int,
    n_instances: int,
    masked_fraction: float,
) -> None:
    """Test if abmil model yields same output in masked and unmasked case."""
    model = ABMIL(
        input_size=input_size,
        output_size=output_size,
        projected_input_size=128,
        hidden_size_attention=128,
        hidden_sizes_mlp=hidden_sizes_mlp,
        use_bias=True,
    )

    n_masked = int(n_instances * masked_fraction)

    x = torch.randn(batch_size, n_instances, input_size)
    mask = torch.zeros(batch_size, n_instances, 1).bool()
    mask[:, n_masked:, :] = True

    y = model(x[:, :n_masked, :], mask=None)
    y_masked = model(x, mask=mask)

    assert torch.allclose(y, y_masked, atol=1e-6)