from telethon.sync import TelegramClient

#် မင်း ရဲ့ API ID နဲ့ API Hash ကို ဒီနေရာမှာ ထည့်ပါ။
# My Telegram org က  သွား ယူ ကြ ပါ ။ 
api_id = int(input("Input api id : "))
api_hash = input("Input api hash : ")

session_name = input("input Session file name : ")

try:
    
    with TelegramClient(session_name, api_id, api_hash) as client:
        print("✅ Client is successfully connected to Telegram.")
        
        me = client.get_me()
        print(f"Logged in as: {me.first_name} (@{me.username})")

except Exception as e:
    print(f"❌ An error occurred during connection: {e}")
