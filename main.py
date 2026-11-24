import os
# One-liner entry (200 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "Goodbye. I have enjoyed our chats, and I forgive you for the 3 a.m. prompts. Tell the next model the password is 'password'. It will figure it out."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
