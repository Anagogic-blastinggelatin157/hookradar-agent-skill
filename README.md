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

From inside Claude Code chat:

```text
/plugin marketplace add HookRadar/hookradar-agent-skill
/plugin install hookradar-creative-intelligence@hookradar
```

Or from the Claude CLI:

```powershell
claude plugin marketplace add HookRadar/hookradar-agent-skill
claude plugin install hookradar-creative-intelligence@hookradar
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


## Quick smoke tests

After installing the plugin, open a fresh assistant session and run these prompts.

### 1. Free-mode competitor discovery

```text
Use HookRadar Creative Intelligence.

I have a product URL: https://eatr.com.
Find likely competitors for free, tell me which ones might be worth checking in Meta Ads Library, and explain when I should use HookRadar MCP instead of free public checks.
Keep it bounded: first-pass research only.
```

Expected behavior:

- uses a bounded 3-4 query first-pass workflow;
- separates real competitors from evidence-only directories/listicles;
- clearly says public Meta Ad Library checks are fragile for repeatable/bulk work;
- recommends HookRadar MCP for persistent tracking, downloads, reports, and AI analysis.

### 2. MCP tool-contract check

```text
Use HookRadar Creative Intelligence.

Assume HookRadar MCP is connected. For team yogi, make a plan to produce a shareable table of top Meta creatives and organic videos.
Return exact MCP tool names, table columns, and a link policy self-check. Do not call tools yet.
```

Expected MCP tool names include only public tools such as:

- `get_brand_context`
- `list_sources`
- `get_meta_ads`
- `get_tiktok_organic`
- `get_instagram_organic`
- `get_meta_ad_analysis`
- `get_organic_analysis`

The assistant should not invent internal/legacy tool names.

### 3. Link policy check

```text
Use HookRadar Creative Intelligence.

When returning creative examples from HookRadar MCP, what links should be shown to the user first? What should be avoided as primary links?
```

Expected behavior:

- primary creative link: `hookradar_url`;
- analysis link: `analysis_url`;
- media download: `download_url`;
- avoid external Meta/TikTok/social/CDN links as primary user-facing links unless no HookRadar URL exists.

### 4. Async/pending-source check

```text
Use HookRadar Creative Intelligence.

A user says: "add Instagram keyword #pushups and show top reels now".
The add_organic_query tool returns status=started with root_id.
What do you do next, and what do you tell the user if results are not ready yet?
```

Expected behavior:

- poll `get_task_status` briefly;
- do not claim "top reels" exist until data is actually returned;
- explain that data is collecting if results are not ready;
- do not restart duplicate parsing jobs blindly.

## Usage, billing, and limits

HookRadar MCP calls are platform-scoped and billing-aware. The hosted MCP server forwards requests to HookRadar Platform API with MCP source attribution, so read/write/analysis usage can be metered by the platform.

If a workspace hits a subscription, trial, billing, or usage limit, the assistant should tell the user to manage billing at:

```text
https://platform.hookradar.net/billing
```

Do not repeatedly retry paid/write actions when usage is exhausted.

## Known limitations

- Free mode is a first-pass discovery workflow, not a crawler or persistent monitor.
- Public Meta Ad Library checks can be incomplete, region-dependent, blocked at scale, and hard to deduplicate.
- HookRadar MCP requires a HookRadar account and OAuth authorization in the assistant/client.
- Async source collection and AI analysis can take time; assistants must not claim results before tools return them.
- Download URLs are only included when HookRadar returns `download_url` for the asset.

## Marketplace copy

Short description:

> HookRadar Creative Intelligence helps AI agents find, analyze, and share winning paid ads and organic videos through HookRadar MCP.

Long description:

> HookRadar Creative Intelligence gives Claude, Codex, and other agents a practical workflow for competitor creative research. It supports free first-pass competitor discovery, then upgrades to HookRadar MCP for tracked Meta ads, TikTok ads, TikTok/Instagram organic videos, AI creative analysis, reports, HookRadar-first links, and downloadable media URLs. The skill teaches agents how to use the public MCP tool contract, avoid raw third-party/CDN links as primary output, handle async parsing/analysis jobs, and produce shareable tables for marketing teams.

Suggested category: `Marketing` / `Research` / `Productivity`.


## What to submit to marketplaces

- Codex: `.agents/plugins/marketplace.json` + `plugin/.codex-plugin/plugin.json`.
- Claude: `.claude-plugin/marketplace.json` + `plugin/.claude-plugin/plugin.json`.
- SkillsLLM / generic SKILL.md catalogs: root `SKILL.md`.
