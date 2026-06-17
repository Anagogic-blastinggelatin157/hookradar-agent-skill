# HookRadar Creative Intelligence Skill

HookRadar Creative Intelligence is a cross-agent skill/plugin for competitive creative research.
It teaches Codex, Claude Code, Cursor-style agents, and other SKILL.md-compatible assistants how to:

- use the HookRadar MCP server (`https://mcp.hookradar.net/mcp`),
- find paid and organic creative winners from tracked HookRadar workspaces,
- produce HookRadar-first links and downloadable asset URLs,
- start AI analysis/report jobs without hanging forever,
- run a useful free competitor-research workflow when the user has not connected HookRadar yet,
- explain where HookRadar fits vs manual Meta/TikTok/organic research workflows.

## Install

### Claude Code

```text
/plugin marketplace add HookRadar/hookradar-agent-skill
/plugin install hookradar-creative-intelligence@hookradar
```

### Codex / SKILL.md-compatible agents

Use the root `SKILL.md` directly, or install the plugin from the repo marketplace when supported:

```text
https://github.com/HookRadar/hookradar-agent-skill
```

### MCP endpoint

The bundled `.mcp.json` points at the hosted HookRadar MCP server:

```text
https://mcp.hookradar.net/mcp
```

Users authenticate with their HookRadar account during the MCP OAuth flow. No API keys are stored in this repo.

## Free mode vs HookRadar MCP mode

The skill is useful even before a user connects HookRadar:

- Free mode: product URL research, competitor discovery, Meta Ad Library spot checks, and a caveated first-pass creative map.
- HookRadar MCP mode: persistent workspaces, tracked competitors, paid ads + TikTok/Instagram organic content, downloadable media, AI analysis, reports, usage-aware workflows, and HookRadar URLs.

Free public libraries are good for one-off checks. They become brittle at scale: repeated scraping/searching can hit blocks, missing media, region gaps, duplicate work, and no persistent AI analysis. HookRadar MCP exists to solve that operational layer.

## What to submit to marketplaces

- Codex: `.agents/plugins/marketplace.json` + `plugin/.codex-plugin/plugin.json`.
- Claude: `.claude-plugin/marketplace.json` + `plugin/.claude-plugin/plugin.json`.
- SkillsLLM / generic SKILL.md catalogs: root `SKILL.md`.
