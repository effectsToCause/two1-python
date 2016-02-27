"""Utility functions for user wallets."""
import click

import two1
import two1.lib.wallet as wallet
from two1.commands.util import uxstring
from two1.lib.blockchain import twentyone_provider


def get_or_create_wallet(wallet_path):
    """Create a new wallet or return the currently existing one."""
    data_provider = twentyone_provider.TwentyOneProvider(two1.TWO1_PROVIDER_HOST)

    if wallet.Two1Wallet.check_wallet_file(wallet_path):
        return Wallet(wallet_path=wallet_path, data_provider=data_provider)

    # configure wallet with default options
    click.pause(uxstring.UxString.create_wallet)

    wallet_options = dict(data_provider=data_provider, wallet_path=wallet_path)

    if not wallet.Two1Wallet.configure(wallet_options):
        raise click.ClickException(uxstring.UxString.Error.create_wallet_failed)

    # Display the wallet mnemonic and tell user to back it up.
    # Read the wallet JSON file and extract it.
    with open(wallet_path, 'r') as f:
        wallet_config = json.load(f)
        mnemonic = wallet_config['master_seed']

    click.pause(uxstring.UxString.create_wallet_done % (mnemonic))

    # Start the daemon, if:
    # 1. It's not already started
    # 2. It's using the default wallet path
    # 3. We're not in a virtualenv
    try:
        d = daemonizer.get_daemonizer()

        if wallet.Two1Wallet.is_configured() and not os.environ.get("VIRTUAL_ENV") and not d.started():
            d.start()
            if d.started():
                click.echo(uxstring.UxString.wallet_daemon_started)
    except (OSError, DaemonizerError):
        pass