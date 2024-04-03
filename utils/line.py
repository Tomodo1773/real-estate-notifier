import requests
import os
import json

def notify_line(args):

    # .env fileから変数を取得
    token = os.environ.get("line_token")

    # LINE Message API
    lineMessageApi = "https://api.line.me/v2/bot/message/broadcast"
    # LINE Flex Message creation
    flexContents = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "NEW",
                    "size": "xs",
                    "color": "#ffffff",
                    "align": "center",
                    "gravity": "center",
                }
            ],
            "paddingAll": "0px",
            "backgroundColor": "#FB4A4A",
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "こんな物件見つけたぽも！",
                    "size": "xs",
                    "color": "#ffffff",
                    "weight": "regular",
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "contents": [],
                                    "size": "xl",
                                    "wrap": True,
                                    "text": args["name"],
                                    "color": "#ffffff",
                                    "weight": "bold",
                                    "margin": "md",
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "販売価格",
                                            "color": "#ffffff",
                                            "style": "normal",
                                            "decoration": "none",
                                            "gravity": "center",
                                            "margin": "lg",
                                            "align": "start",
                                        },
                                        {
                                            "type": "text",
                                            "text": args["price"],
                                            "color": "#FB8989",
                                            "size": "lg",
                                            "weight": "bold",
                                        },
                                    ],
                                    "backgroundColor": "#ffffff1A",
                                    "spacing": "none",
                                    "margin": "md",
                                },
                            ],
                            "spacing": "sm",
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "詳細",
                                    "color": "#ffffff",
                                    "decoration": "underline",
                                    "margin": "none",
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "contents": [],
                                            "size": "sm",
                                            "wrap": True,
                                            "margin": "md",
                                            "color": "#ffffffde",
                                            "text": args["location"],
                                        },
                                        {
                                            "type": "text",
                                            "contents": [],
                                            "size": "sm",
                                            "wrap": True,
                                            "margin": "md",
                                            "color": "#ffffffde",
                                            "text": args["station"],
                                        },
                                        {
                                            "type": "text",
                                            "contents": [],
                                            "size": "sm",
                                            "wrap": True,
                                            "margin": "md",
                                            "color": "#ffffffde",
                                            "text": args["layout"],
                                        },
                                        {
                                            "type": "text",
                                            "contents": [],
                                            "size": "sm",
                                            "wrap": True,
                                            "margin": "md",
                                            "color": "#ffffffde",
                                            "text": args["area"],
                                        },
                                    ],
                                },
                            ],
                            "paddingAll": "13px",
                            "backgroundColor": "#ffffff1A",
                            "cornerRadius": "2px",
                            "margin": "xl",
                        },
                    ],
                },
            ],
            "paddingAll": "20px",
            "backgroundColor": "#464F69",
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "action": {"type": "uri", "label": "詳しくはこっちだぽも！", "uri": args["link"]},
                    "style": "link",
                    "margin": "none",
                    "gravity": "center",
                    "color": "#DCE4FC",
                    "offsetTop": "none",
                    "height": "sm",
                }
            ],
            "spacing": "none",
            "margin": "none",
            "backgroundColor": "#ffffff1A",
        },
        "styles": {"footer": {"backgroundColor": "#666E85"}},
    }
    flexMessage = {"type": "flex", "altText": "新しい不動産情報が出たぽも", "contents": flexContents}
    headers = {"Authorization": "Bearer " + token, "Content-Type": "application/json"}
    data = {"messages": [flexMessage]}
    # Send the request to LINE Message API
    try:
        response = requests.post(lineMessageApi, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # If the response contains an HTTP error status code, this will raise a Python exception
    except requests.exceptions.RequestException as e:
        # Catch any exception that `requests` throws
        print("Error occurred while sending message: ", str(e))
    else:
        # Handling the response. Modify it according to your requirement.
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Failed to send the message. HTTP status code: {response.status_code}")
            print("Response body: ", response.text)
    return
