const { buildBroadcastEvent } = require("../src/messageProcessor");

describe("buildBroadcastEvent", () => {
  test("creates a broadcast event with expected shape", () => {
    const fixedDate = new Date("2026-03-02T10:00:00.000Z");

    const event = buildBroadcastEvent({
      rawMessage: "hello",
      clientIp: "127.0.0.1",
      now: fixedDate,
    });

    expect(event).toEqual({
      type: "chat.echo",
      from: "127.0.0.1",
      payload: "hello",
      ts: "2026-03-02T10:00:00.000Z",
    });
  });

  test("handles Buffer-like input by converting to string", () => {
    const fixedDate = new Date("2026-03-02T10:00:00.000Z");

    const event = buildBroadcastEvent({
      rawMessage: Buffer.from("buffer-msg"),
      clientIp: "::1",
      now: fixedDate,
    });

    expect(event.payload).toBe("buffer-msg");
    expect(event.from).toBe("::1");
    expect(event.type).toBe("chat.echo");
  });

  test("handles null/undefined rawMessage safely", () => {
    const fixedDate = new Date("2026-03-02T10:00:00.000Z");

    const event = buildBroadcastEvent({
      rawMessage: undefined,
      clientIp: "x",
      now: fixedDate,
    });

    expect(event.payload).toBe("");
  });
});