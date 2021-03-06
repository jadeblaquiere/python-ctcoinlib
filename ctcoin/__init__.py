# Copyright (C) 2012-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import ctcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.6.1'

class MainParams(ctcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9'
    DEFAULT_PORT = 8333
    RPC_PORT = 8332
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'),
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':0,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}

class TestNetParams(ctcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('bitcoin.petertodd.org', 'testnet-seed.bitcoin.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class RegTestParams(ctcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

class CTRedParams(ctcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xef\xbe\xad\xde'
    DEFAULT_PORT = 17761
    RPC_PORT = 17762
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':0x50,
                       'SCRIPT_ADDR':0x8e,
                       'SECRET_KEY' :0xa3}

class CTIndigoParams(ctcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xef\xbe\xad\xde'
    DEFAULT_PORT = 7764
    RPC_PORT = 7765
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':0x1c,
                       'SCRIPT_ADDR':0x57,
                       'SECRET_KEY' :0xbb}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
ctcoin.core.params correctly too.
"""
#params = ctcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    ctcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = ctcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = ctcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = ctcoin.core.coreparams = RegTestParams()
    elif name == 'ctrednet':
        params = ctcoin.core.coreparams = CTRedParams()
    elif name == 'ctindigonet':
        params = ctcoin.core.coreparams = CTIndigoParams()
    else:
        raise ValueError('Unknown chain %r' % name)
