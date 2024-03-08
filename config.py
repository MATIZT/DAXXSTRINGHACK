# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20006068"
    API_HASH = "346becfc02417e50a2837a8d545b015e"
    TOKEN = os.environ.get("TOKEN", 6821626224:AAFp83mH4nNSo3DVHqehV0B1pf-HuvABEaA)
    MONGO_URL = "mongodb+srv://mdmatinashraf43:gymoW5DpuqoKf9xg@cluster0.s2falsa.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/1f699ca115629afb0e092.jpg"
    SUDOERS = filters.user(["5970997865"])
