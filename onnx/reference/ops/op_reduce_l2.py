# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunReduceNumpy


class ReduceL2_1(OpRunReduceNumpy):
    def _run(self, data, axes=None, keepdims=None):  # type: ignore
        axes = tuple(axes) if axes is not None else None
        return (
            np.sqrt(np.sum(np.square(data), axis=axes, keepdims=keepdims)).astype(
                dtype=data.dtype
            ),
        )


class ReduceL2_18(OpRunReduceNumpy):
    def _run(self, data, axes=None, keepdims=1, noop_with_empty_axes=0):  # type: ignore
        if self.is_axes_empty(axes) and noop_with_empty_axes:  # type: ignore
            return (data,)

        axes = self.handle_axes(axes)
        keepdims = keepdims != 0  # type: ignore
        return (
            np.sqrt(np.sum(np.square(data), axis=axes, keepdims=keepdims)).astype(
                dtype=data.dtype
            ),
        )
