# LINE-Tech-Fresh-Chatbot
A chatbot for LINE Tech Fresh 2021 preassessment.

## QR Code
![Charbot QRCode](https://i.imgur.com/rCNXSeO.png)
- Or you can use line id `@606jgbyx` to add my chatbot as friend.


## Deploy

1. Install dependencies.

   ```bash
   pip3 install -r requirements.txt
   ```

2. Store chatbot access token and secret to environment variables.

   ```bash
   export LINE_CHANNEL_ACCESS_TOKEN=<LINE_CHANNEL_ACCESS_TOKEN>
   export LINE_CHANNEL_SECRET=<LINE_CHANNEL_SECRET>
   ```

3. (optional) Set port of the web service.

   ```bash
   export PORT=<PORT>
   ```

4. Run it.

   ```bash
   python app.py
   ```

5. Happy chatting!