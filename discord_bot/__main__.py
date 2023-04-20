import argparse
import logging
import json
from core import dotdict

# Set up arguments
parser = argparse.ArgumentParser(
    prog='discord_bot',
    description='A simple discord bot',
    epilog='Arguments will override the corresponding config file settings.'
)

parser.add_argument('-d', '--debuglevel',
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help='Specify the logging level for the bot')

parser.add_argument('-c', '--config',
                    required=True,
                    help='Specify a config file')

parser.add_argument('-l', '--logfile',
                    help='Specify the logfile for the bot')

args = parser.parse_args()

# Load config file and set up variables
try:
    with open(args.config, encoding='utf-8') as config_file:
        # config.bot.channels, config.bot.token, config.debuglevel, config.logfile
        config = dotdict(json.load(config_file))
except FileNotFoundError as err:
    logging.error(err)

if args.logfile:
    config.logfile = args.logfile
if args.debuglevel:
    config.debuglevel = args.debuglevel

# Configure logging
logging.basicConfig(filename=config.logfile, encoding='utf-8', level=config.debuglevel,
                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S%z')

logging.info('Loaded config, configured logging')
print(config)
