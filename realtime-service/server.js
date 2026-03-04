const http = require("http");
const WebSocket = require("ws");
const { buildBroadcastEvent } = require("./src/messageProcessor");

const server = http.createServer((req, res) => {
  if (req.url === "/healthz") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ ok: true }));
  }
  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ error: "Not found" }));
});

const wss = new WebSocket.Server({ server });

wss.on("connection", (ws, req) => {
  const clientIp = req.socket.remoteAddress;

  ws.send(
    JSON.stringify({
      type: "server.welcome",
      message: "Connected to realtime-service",
      ts: new Date().toISOString(),
    })
  );

  ws.on("message", (raw) => {
    const event = buildBroadcastEvent({
      rawMessage: raw,
      clientIp,
      now: new Date(),
    });

    for (const client of wss.clients) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify(event));
      }
    }
  });

  ws.on("error", (err) => console.error("[WS] error:", err));
});

const PORT = process.env.PORT || 8080;
server.listen(PORT, () => console.log(`Listening on :${PORT}`));