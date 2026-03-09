const http = require("http");
const WebSocket = require("ws");

const server = http.createServer(async (req, res) => {
  if (req.method === "GET" && req.url === "/healthz") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ ok: true }));
  }

  if (req.method === "POST" && req.url === "/broadcast") {
    try {
      const body = await readJson(req);

      if (!body || typeof body !== "object" || typeof body.type !== "string") {
        res.writeHead(400, { "Content-Type": "application/json" });
        return res.end(JSON.stringify({ error: "Invalid payload: missing `type`" }));
      }

      broadcastJson(wss, body);

      res.writeHead(200, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ ok: true }));
    } catch (err) {
      res.writeHead(400, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ error: "Invalid JSON body" }));
    }
  }

  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ error: "Not found" }));
});

const wss = new WebSocket.Server({ server });

wss.on("connection", (ws, req) => {
  const clientIp = req.socket.remoteAddress;
  console.log(`[WS] client connected: ${clientIp}`);

  ws.send(
    JSON.stringify({
      type: "server.welcome",
      message: "Connected to realtime-service",
      ts: new Date().toISOString(),
    })
  );

  ws.on("close", () => console.log(`[WS] client disconnected: ${clientIp}`));
  ws.on("error", (err) => console.error(`[WS] error ${clientIp}`, err));
});

function broadcastJson(wss, payload) {
  const msg = JSON.stringify(payload);
  for (const client of wss.clients) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(msg);
    }
  }
}

function readJson(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (chunk) => (data += chunk));
    req.on("end", () => {
      try {
        resolve(JSON.parse(data || "{}"));
      } catch (e) {
        reject(e);
      }
    });
    req.on("error", reject);
  });
}

const PORT = process.env.PORT || 8080;
server.listen(PORT, () => {
  console.log(`[HTTP] http://localhost:${PORT}`);
  console.log(`[WS]   ws://localhost:${PORT}`);
});