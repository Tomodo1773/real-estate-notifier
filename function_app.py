import logging

import azure.functions as func
from functions.suumo import research_suumo
app = func.FunctionApp()


@app.schedule(schedule="0 0 20 * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def suumo(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("The timer is past due!")

    try:
        research_suumo()
    except Exception as e:
        logging.error(f"research_suumoでエラーが発生しました: {e}")
    logging.info("Python timer trigger function executed.")

    return
