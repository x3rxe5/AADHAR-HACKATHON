# -------------------------
# 
#   TEAM NAME   : GangOfCMPICA
#   TITLE       : ADDRESS FORMATING ISSUE
#   DESCRIPTION : Aadhar hackathon problem statement number 4
#                       
# -------------------------


import uvicorn
from src.main import app

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000,log_level="info")