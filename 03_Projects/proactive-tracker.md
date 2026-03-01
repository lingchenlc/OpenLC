# Proactive Tracker 🦞

## 🎯 Active Behaviors
- [ ] **Mac Mini Re-pairing**: LC decided to stop for now due to Surge/Gateway complications.
  - *Context*: Last attempt failed due to 127.0.0.1 bind and Surge intercepting loopback.
  - *Next Step*: Wait for LC's signal or a quiet moment to suggest Tailscale/Wireguard as a bypass.
- [ ] **Amazon Ads Skill Refinement**: Intel gathered on 2026-02-28 regarding AMC 2026 features (High-Frequency Audiences) and Amazon Ads MCP Server (Beta).
  - *Context*: Need to build Xnurta-specific MCP wrapper.
  - *Next Step*: Use Codex Researcher to draft the MCP Server implementation.

## 🧠 Pattern Recognition
- **Surge/Proxy Friction**: Repeated connectivity issues when pairing nodes.
  - *Automation Idea*: Create a "Node Doctor" skill that automatically detects proxy settings and suggests `no_proxy` or Surge skip rules.
- **Memory Compression**: Large session history causing Gateway lag.
  - *Action*: Monitor context % and suggest compaction if it stays >60%.

## 📈 Outcome Tracking
- **Decision (2026-02-24)**: Switched Info Hunter focus from Claude Code to OpenClaw + Amazon Ads.
  - *Follow-up (2026-03-03)*: Check if the new intel is more relevant to LC.
