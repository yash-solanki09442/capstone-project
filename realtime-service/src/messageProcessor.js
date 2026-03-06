function buildBroadcastEvent({ rawMessage, clientIp, now = new Date() }) {
  const msg = (rawMessage ?? "").toString();

  return {
    type: "chat.echo",
    from: clientIp,
    payload: msg,
    ts: now.toISOString(),
  };
}

module.exports = { buildBroadcastEvent };