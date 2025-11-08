import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


response = supabase.table("Users").select("username").eq("id","1").execute()
print(response)


# get_user_by_id()
