from pathlib import Path
import platform
import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = int(os.environ["2624913"])
    api_hash = os.environ["a204e6332a52ea40033b8215421bc81d"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = os.environ["index_all": true,"index_private":false,"index_group": false,"index_channel": true,"exclude_chats": [true],"include_chats": [false].strip()
    index_settings = json.loads(index_settings_str)
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["AQAK6U4yD8ZchjZMewiUbAi0VWQpqY7eX32FVCTdB43VLzvuypXkSE0xzj6qo-8bI5PS2-7rRhM4G0XD28u5Zkk7JDOUYwZjazvLKyDJ5Xo0L23XUQARA7Y0Kt-ocn3lpU4F_SBVpf-AklkptquNni3rZRpTib-ewDJiyQRsyDaPWN7QMi8SgelUd2LeOzQCAJj4VOOOuaubk0JDvj1Ikw3DbJMs4Kgo88LoFvTxMbFdnId26p0jclmbdZHzS6Y0oNMxvvENZH-xW9bmi8M41qrhaRvGnPjl3Fci7E4qe2b38fClJFh3Yj-oomvyEKsWM5g0EdJb7UWtMvQ15DbhzvJ1WJFacwA"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path(
    "/Temp/logo/" if platform.system() == 'Windows' else '/tmp/logo'
)
logo_folder.mkdir(exist_ok=True)
