from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9068860"))
API_HASH = getenv("API_HASH", "56d83805b25f0fad70ddedaa4206ac4a")
BOT_TOKEN = getenv("BOT_TOKEN","1917637742:AAF61TOx72pQEap0aHp56t9yQL5VUl-C7R0")
BOT_NAME = getenv("BOT_NAME","NES18Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCdZUPVqWdHudEeVSwMaYj2FoNB7x5LMGmFBTSe603Zo8shg0e_pxyqAJ59lxCvBblBOg-yn3nxNkzleIuv3q4poErGNQLNy2QL11BBjiZv2FK47xWn522ECLgWUg4Tnxhs_gkOZQjWkLkP1NWibeaxy0y5ufTaDS905u7ksMedBw_XBjeZHFkL4kLdRbnerhijU2UP1aJ0QfEN9nrSSDJj6NxxrFpg53nnlT4H9MXyZkGvMa9_CERrgCVlyz4bKcEOqw9RrQk6PhwnawfbkP3ESgFLT3FtBCvmZGFDTY2-1wFQzla9mK00KluI2n_266KZJqFnHLXIbR329-Yyy2ddbAMQnwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2068551800").split()))
