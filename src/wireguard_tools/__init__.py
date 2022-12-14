#
# Pure Python reimplementation of wireguard-tools
#
# Copyright (c) 2022 Carnegie Mellon University
# SPDX-License-Identifier: MIT
#

__version__ = "0.1.0.post.dev0"

from .wireguard_config import WireguardConfig
from .wireguard_key import WireguardKey

__all__ = [
    "WireguardConfig",
    "WireguardKey",
]
