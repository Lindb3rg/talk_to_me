messages = []

while(1):
    text = record_text()
    messages.append({"role":"user","content":text})
    response = send_to_chatGBT(messages)
    SpeakText(response)

    print(response)