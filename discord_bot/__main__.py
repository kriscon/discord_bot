import argparse
import logging
import json
import bot
from core import dotdict

# Set up arguments
parser = argparse.ArgumentParser(
    prog='discord_bot',
    description='A simple discord bot'
)

parser.add_argument('-c', '--config',
                    required=True,
                    help='Specify a config file')

parser.add_argument('-d', '--debuglevel',
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help='Override loglevel set in the config file')

parser.add_argument('-l', '--logfile',
                    help='Override log path set in the config file')

args = parser.parse_args()

# Build config variables form config file
try:
    with open(args.config, encoding='utf-8') as config_file:
        # config.bot.channels, config.bot.token, config.debuglevel, config.logfile
        json_data = dotdict(json.load(config_file))
        config = dotdict()
        for item in json_data.items():
            if isinstance(item[1], dict):
                config[item[0]] = dotdict(item[1])
            else:
                config[item[0]] = item[1]

except FileNotFoundError as err:
    logging.error(err)

# Override logfile and debuglevel if specified as argument
if args.logfile:
    config.app.logfile = args.logfile
if args.debuglevel:
    config.app.debuglevel = args.debuglevel

# Configure logging
logging.basicConfig(filename=config.app.logfile, encoding='utf-8', level=config.app.debuglevel,
                    format='%(asctime)s:%(levelname)s:%(lineno)d:%(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S%z')

for setting in config.items():
    logging.info('var config.%s created', setting[0])

# Run the bot
bot.run_bot(config.bot.token)
